n = int(input("Enter Size : "))
count = int(input("Enter Starting number : "))
for i in range(n):
    for j in range(n):
        if count < 10:
            print(count, end="  ")
        else:
            print(count, end=" ")
        count = count + 1
    print()
