n = 0
for i in range(9):
    
    for j in range(5):
        if j <= n:
            print("*", end="")
    print("\n")

    if i < 4:
       n += 1
    else:
        n -= 1