n = int(input("Enter Size : "))
for i in range(n):
    for j in range((n-i)-1):
        print("", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range((n - i) - 1):
        print("", end=" ")
    for j in range(i + 1):
        print(i, end=" ")
    print()
for i in range(n):
    for j in range((n - i) - 1):
        print("", end=" ")
    for j in range(i + 1):
        print(j, end=" ")
    print()
a = int(input("Enter starting number : "))
for i in range(n):
    for j in range((n - i) - 1):
        print("", end=" ")
    for j in range(i + 1):
        if a < 10:
            print(a, end="  ")
        else:
            print(a, end=" ")
        a += 1
    print()