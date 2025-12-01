
number = int(input("Insert a number: "))

for n in range(1,number+1):
    for i in range(number-n):
        print(" ", end="")
    
    for j in range(2*n-1):
        print("*", end="")
    print()

for n in range(number-1, 0 , -1):
    for i in range (number-n):
        print(" ", end="")

    for i in range(2*n-1):
        print("*", end="")

    print()