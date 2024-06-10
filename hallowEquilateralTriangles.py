n = int(input("Enter Size : "))
for i in range(n):
    for j in range((n-i)-1):
        print("", end=" ")
    for j in range(i+1):
        if j == 0 or i == n-1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n):
    for j in range((n-i)-1):
        print("", end=" ")
    for j in range(i+1):
        if j == 0 or i == n-1 or j == i:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n):
    for j in range((n-i)-1):
        print("", end=" ")
    for j in range(i+1):
        if j == 0 or i == n-1 or j == i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
