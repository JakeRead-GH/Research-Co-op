swifts_total = 0
sema_total = 0

not_valid = True

while not_valid:
    n = input()

    try:
        n = int(n)

        if n >= 1 and n <= 100000:
            not_valid = False

    except:
        print("Invalid Input")
        

not_valid = True

while not_valid:
    swifts = [swifts for swifts in input().split()]
    not_failed = True

    for a in range(n):
        if not_failed:
            try:
                swifts[a] = int(swifts[a])

                if swifts[a] < 0 or swifts[a] > 20:
                    not_failed = False

            except:
                print("Invalid Input")
                not_failed = False

    if len(swifts) == n and not_failed:
        not_valid = False

not_valid = True

while not_valid:
    sema = [sema for sema in input().split()]
    not_failed = True

    for a in range(n):
        if not_failed:
            try:
                sema[a] = int(sema[a])
                
                if sema[a] < 0 or sema[a] > 20:
                    not_failed = False

            except:
                print("Invalid Input")
                not_failed = False

    if len(sema) == n and not_failed:
        not_valid = False

equal = False

for c in range(n):
    swifts_total = swifts_total + swifts[c]
    sema_total = sema_total + sema[c]

    if swifts_total == sema_total:
        k = c + 1
        equal = True

if equal == False:
    print("0")

else:
    print(k)


        
