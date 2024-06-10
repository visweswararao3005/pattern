n = int(input("Enter size : "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
a = int(input("Enter starting number : "))
for i in range(1, n+1):
    for j in range(1, i+1):
        if a < 10:
            print(a, end="  ")
        else:
            print(a, end=" ")
        a += 1
    print()
