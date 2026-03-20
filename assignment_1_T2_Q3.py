x = input("Enter word: ")
i = len(x) - 1

while i < len(x) and i >= 0:
    print(x[i], end="")
    i -= 1