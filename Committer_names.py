file = open("log.txt")
still_reading = True
print("hello")

#while still_reading:
for a in range(10):
    line = file.readline()
    print(line)

    if line.find("Author:") != -1:
        print("y")
        still_reading = False
    else:
        print("n")

file.close()
