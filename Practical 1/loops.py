for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
 print(i, end=' ')
print()

star = int(input("Please enter a number: "))

for i in range(star):
    for j in range(i+1):
        print("*",end=' ')
    print()
