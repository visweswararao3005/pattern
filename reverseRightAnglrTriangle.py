n = int(input("Enter Size : "))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
for i in range(1, n+1):
    for j in range(1, ((n+1)-i)+1):
        print("*", end=" ")
    print()
for i in range(1, n+1):
    for j in range(1, ((n+1)-i)+1):
        print(i, end=" ")
    print()
for i in range(1, n+1):
    for j in range(1, ((n+1)-i)+1):
        print(j, end=" ")
    print()
