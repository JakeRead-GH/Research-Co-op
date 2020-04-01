changed_files = []
reading = True

general_log = open("ActiveMQBasicLog.txt")
file_names_file = open("ActiveMQFileNames.txt")

while reading:
    line = general_log.readline().strip()

    if line.find("Author:") != -1:
        before_keyword, keyword, name = line.partition("Author:")
        name = name.lstrip()
        reading = False

reading = True

while reading:
    line = file_names_file.readline()

    if line == "":
        reading = False

    else:
        changed_files.append(line)

file_names_file.close()
general_log.close()

print(name, changed_files[0])

    
