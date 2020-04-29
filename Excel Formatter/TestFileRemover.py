bug_fix_commits_file = open("ActiveMQBugFixCommits.txt", 'r', encoding="utf-16")
file_names = open("ActiveMQBugFixFileNames.txt")
new_file = open("ActiveMQBugFixCommitsTestFilesRemoved.txt", 'w')
reading = True
blank_lines = 0

while reading:
    commit = bug_fix_commits_file.readline()
    line = file_names.readline().rstrip()
    line = line.lstrip()

    if line == "":
        blank_lines = blank_lines + 1

        if blank_lines == 3:
            reading = False

    else:
        blank_lines = 0
        
        if line.find("test") == -1 and line.find("Test") == -1:
            new_file.write(commit)

file_names.close()
bug_fix_commits_file.close
new_file.close()
