file = open("log.txt")
names = []
commits = []
blank_lines = 0
authors = 0
still_reading = True

while still_reading:
    line = file.readline().strip()

    if (line.find("Author:") != -1):
        before_keyword, keyword, name = line.partition("Author:")
        name = name.lstrip()
        if name not in names:
            names.append(name)
            commits.append(int(1) )
            authors = authors + 1

        else:
            position = names.index(name)
            commits[position] = commits[position] + 1

    elif line == "":
        blank_lines = blank_lines + 1
        
        if blank_lines == 3:
            still_reading = False

    else:
        blank_lines = 0

for a in range(authors):
    print("Author: " + names[a])
    print("Commits: " + str(commits[a]) )
    print("")

file.close()



## Code for removing email if required

#name = ' '.join(after_keyword.split()[:2])
#        print(name)
