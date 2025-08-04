def squareroot():
    num = int(input("Enter a number: "))
    if num < 0:
        print("Cannot compute square root of a negative number.")
    else:     
        root = num ** 0.5
    print("Square root of", num, "is", root)
squareroot()
