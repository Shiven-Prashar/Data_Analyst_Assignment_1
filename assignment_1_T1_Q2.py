x = 2000
while x >= 2000 and x <= 3200:
    if x % 7 == 0:
        if x % 5 != 0:
            print(x,end =', ')
    x += 1