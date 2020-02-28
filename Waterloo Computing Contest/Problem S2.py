not_valid = True

while not_valid:
    n = input()

    try:
        n = int(n)

        if n >= 2 and n <= 2000000:
            not_valid = False

        else:
            print("Invalid Input")

    except:
        print("Invalid Input")

r = []
possible = []
for b in range(n):
    r.append(0)

a = 0
p = -1
most_frequent = 0

while a != n:
    r[a] = input()

    try:
        r[a] = int(r[a])

        if r[a] >= 1 and r[a] <= 1000:
            a = a + 1
            if r[a] not in possible:
                possible.append(r[a])
                p = p + 1

        else:
            print("Invalid Input1")
            

    except:
        print("Invalid Input2")

##for e in range(n):
##    print(r[e], possible[e], p)


for c in range(p):
    for d in range(n):
        if r.count(possible[c]) > most_frequent:
            most_frequent = possible[c]
            print(most_frequent)

