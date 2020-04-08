def initialize_files():
    global general_log, file_names_log, hash_log, comment_log, formatted_file
    
    general_log = open("ActiveMQBasicLog.txt", 'r', encoding="utf-16")
    file_names_log = open("ActiveMQFileNames.txt", 'r', encoding="utf-16")
    hash_log = open("ActiveMQHashLog.txt", 'r', encoding="utf-16")
    comment_log = open("ActiveMQCommitComments.txt", 'r', encoding="utf-16")
    formatted_file = open("ActiveMQExcelFormatted.txt", 'w', encoding="utf-16")


def get_hash():
    global hash_log, commit_id
    
    line = hash_log.readline().strip()
    before_keyword, keyword, commit_id = line.partition("Commit Hash:")
    commit_id = commit_id.strip()
    commit_id.replace(",", "")


def get_author():
    global general_log, name
    
    reading = True

    while reading:
        line = general_log.readline().strip()

        if line.find("Author:") != -1:
            before_keyword, keyword, name_and_email = line.partition("Author:")
            name_and_email = name_and_email.lstrip()
            name = name_and_email.split("<")[0]
            name = name.rstrip()
            name.replace(",", "")
            reading = False


def get_date():
    global general_log, date
    
    reading = True

    while reading:
        line = general_log.readline().strip()

        if line.find("Date:") != -1:
            before_keyword, keyword, date = line.partition("Date:")
            date = date.lstrip()
            date = date.rstrip()
            date.replace(",", "")
            reading = False


def get_comment():
    global comment_log, comment
    
    reading = True
    same_comment = True
    comment_lines = []

    while reading:
        line = comment_log.readline().strip()
        
        if line.find("Comment:") != -1:
            before_keyword, keyword, comment_line = line.partition("Comment:")
            comment_lines.append(comment_line)
            
            while same_comment:
                last_pos = comment_log.tell()
                if line.find("Comment:") != -1:
                    line = comment_log.readline().strip()

                    if line != "":
                        comment_lines.append(line)

                else:
                    same_comment = False
                    reading = False
                    comment_log.seek(last_pos)
                    comment = "".join(comment_lines)
                    comment = comment.lstrip()
                    comment.replace(",", "")


def get_changed_files():
    global file_names_log, changed_files, num_files
    
    reading = True
    changed_files = []
    num_files = 0

    while reading:
        line = file_names_log.readline().strip()

        if line == "":
            reading = False

        else:
            line.replace(",", "")
            changed_files.append(line)
            num_files = num_files + 1


def write_info_to_file():
    global formatted_file, commit_id, date, name, comment, changed_files, num_files
    
    formatted_file.write(commit_id + ", " + date + ", " + name + ", " + comment)
    
    for a in range(num_files):
        formatted_file.write(", " + changed_files[a])

    formatted_file.write('\n')


def check_if_finished():
    global general_log, finished
    
    last_pos = general_log.tell()
    line_one = general_log.readline()
    line_two = general_log.readline()
    line_three = general_log.readline()
    general_log.seek(last_pos)

    if line_one == "" and line_two == "" and line_three == "":
        finished = True


def close_files():
    global file_names_log, general_log, hash_log, comment_log
    
    file_names_log.close()
    general_log.close()
    hash_log.close()
    comment_log.close()


##Main Program
finished = False
initialize_files()

while finished == False:
    get_hash()
    get_author()
    get_date()
    get_comment()
    get_changed_files()
    write_info_to_file()
    check_if_finished()

close_files()
