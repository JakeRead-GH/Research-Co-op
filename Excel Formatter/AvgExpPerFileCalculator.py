def get_bugs_fixed_per_file():
    global different_files, num_diff_files, bugs_fixed_per_file
    
    file = open("ActiveMQBugFixCommitsFiles.txt")
    reading = True

    different_files = ["placeholder"]
    bugs_fixed_per_file = ["placeholder"]
    num_diff_files = 1
    not_in_list = 0

    while reading:
        line = file.readline().rstrip()
        line = line.lstrip()

        if line == "":
            reading = False

        else:
            num_files = line.count(", ") + 1        
            temp_list = line.split(",")
            
            if num_files % 2 == 1:
                    del temp_list[num_files]

            for a in range(num_files):                
                temp_list[a] = temp_list[a].lstrip()
                not_in_list = 0

                for b in range(num_diff_files):
                    if temp_list[a] != different_files[b]:
                        not_in_list = not_in_list + 1

                    else:
                        bugs_fixed_per_file[b] = bugs_fixed_per_file[b] + 1

                if not_in_list == num_diff_files:
                    different_files.append(temp_list[a])
                    bugs_fixed_per_file.append(1)
                    num_diff_files = num_diff_files + 1

    del different_files[0]
    del bugs_fixed_per_file[0]

    #for c in range(num_diff_files - 1):
        #print(different_files[c] + ", " + str(bugs_fixed_per_file[c]) )

    file.close()


def get_authors_for_each_file():
    global different_files, num_diff_files, file_authors

    file = open("ActiveMQBugFixCommitsTestFilesRemoved.txt")
    file_authors = []
    reading = True

    for a in range(100000):
        file_authors.append("")

    while reading:
        line = file.readline().rstrip()

        if line == "":
            reading = False

        else:
            temp_list = line.split(", ")
            author = temp_list[2]

            for b in range(num_diff_files - 1):
                if line.find(different_files[b]) != -1:
                    file_authors[b] = file_authors[b] + ", " + author

    #for c in range(num_diff_files - 1):
        #print(different_files[c] + file_authors[c])

    file.close()


def get_author_experience():
    global names, experience
    
    file = open("ActiveMQAuthorNames.txt", 'r', encoding="utf-16")
    names = []
    experience = []
    authors = 0
    reading = True

    while reading:
        line = file.readline().lstrip()
        line = line.rstrip()

        if line == "":
            reading = False

        else:   
            if line not in names:
                names.append(line)
                experience.append(int(1) )
                authors = authors + 1

            else:
                position = names.index(line)
                experience[position] = experience[position] + 1

    #for a in range(authors):
        #print(names[a] + ", " + str(experience[a]))

    file.close()


def get_avg_experience_per_file():
    global file_authors, names, experience, num_diff_files, avg_experience

    avg_experience = []

    for a in range(num_diff_files - 1):
        temp_list = file_authors[a].split(", ")
        del temp_list[0]
        num_authors = len(temp_list)

        total_experience = 0

        for b in range(num_authors):
            position = names.index(temp_list[b])
            total_experience = total_experience + experience[position]

        avg_experience.append(total_experience/num_authors)


def output():
    global num_diff_files, different_files, bugs_fixed_per_file, avg_experience

    file = open("ActiveMQAvgExpPerFile.txt", 'w')

    for a in range(num_diff_files - 1):
        file.write(different_files[a] + ", " + str(bugs_fixed_per_file[a]) + ", " + str(avg_experience[a]) + '\n')
    

    

##Main Program
get_bugs_fixed_per_file()
get_authors_for_each_file()
get_author_experience()
get_avg_experience_per_file()
output()
