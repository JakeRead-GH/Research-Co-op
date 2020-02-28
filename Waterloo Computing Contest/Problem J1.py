not_valid = True
possibilities = 0

while not_valid:
    n = input()

    try:
        n = int(n)

        if n >= 1 and n <= 10:
            not_valid = False

    except:
        print("Invalid Input")

for a in range(6):
    for b in range(6):
        if a + b == n and a >= b:
            possibilities = possibilities + 1

print(possibilities)
