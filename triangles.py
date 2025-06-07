def lower_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

def upper_triangle(n):
    for i in range(n):
        for j in range(n):
            if j < i:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()

def pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for k in range(2 * i + 1):
            print("*", end=" ")
        print()


flag=0
while(flag==0):
    try:
        rows = int(input("Enter number of rows "))
        if rows <= 0:
            print("Please enter a positive number ")
        else:
            flag=1
            print()
            print("Lower Triangle")
            print()
            lower_triangle(rows)

            print()
            print("Upper Triangle")
            print()
            upper_triangle(rows)

            print()
            print("Pyramid")
            print()
            pyramid(rows)
        
    except:
        print("Please enter a valid number")
