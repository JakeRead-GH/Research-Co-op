flips = input()
flips = flips.upper()

hor_flips = flips.count('H')
ver_flips = flips.count('V')

if hor_flips % 2 == 0 and ver_flips % 2 == 0:
    print("1 2" + '\n' + "3 4")

elif hor_flips % 2 == 1 and ver_flips % 2 == 0:
    print("3 4" + '\n' + "1 2")

elif hor_flips % 2 == 0 and ver_flips % 2 == 1:
    print("2 1" + '\n' + "4 3")

elif hor_flips % 2 == 1 and ver_flips % 2 == 1:
    print("4 3" + '\n' + "2 1")

