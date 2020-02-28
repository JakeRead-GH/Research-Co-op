t = int(input() )

num = int(input() )

for a in range(num):
    if a > 1:
        for i in range(2, a):
            print(a, i)
            if (a % i) == 0:
                print(a,"is not a prime number")

            else:
                print(a,"is a prime number")
