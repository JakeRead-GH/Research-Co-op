def fill_id_list():
    global issue_id_list
    
    issue_id_list = []
    issue_id_file = open("IssueID.txt", 'r')
    reading = True

    while reading:
        line = issue_id_file.readline()
        
        if line == "":
            reading = False

        else:
            issue_id_list.append(line.strip() )

    issue_id_file.close()


def create_shortened_file():
    global issue_id_list

    formatted_file = open("ActiveMQExcelFormatted.txt", 'r', encoding="utf-16")
    shortened_file = open("ActiveMQBugFixCommits.txt", 'w', encoding="utf-16")
    reading = True

    while reading:
        line = formatted_file.readline()
        
        if line == "":
            reading = False

        else:
            for a in range(980):
                if line.find(issue_id_list[a]) != -1:
                    shortened_file.write(line)

    formatted_file.close()
            
    

##Main Program
fill_id_list()
create_shortened_file()

            
    
