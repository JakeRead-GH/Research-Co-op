changed_files = []
reading = True

general_log = open("ActiveMQBasicLog.txt", 'r', encoding="utf-16")
file_names_file = open("ActiveMQFileNames.txt", 'r', encoding="utf-16")

while reading:
    line = general_log.readline().strip()

    if line.find("commit") != -1:
        before_keyword, keyword, commit_id = line.partition("commit")
        commit_id = commit_id.strip()
        commit_id.replace(",", "")
        reading = False

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

reading = True

while reading:
    line = general_log.readline().strip()

    if line.find("Date:") != -1:
        before_keyword, keyword, date = line.partition("Date:")
        date = date.lstrip()
        date = date.rstrip()
        date.replace(",", "")
        reading = False

reading = True

while reading:
    line = file_names_file.readline()

    if line == "":
        reading = False

    else:
        line.replace(",", "")
        changed_files.append(line)

file_names_file.close()
general_log.close()

print(commit_id, date, name, changed_files[0])

    
