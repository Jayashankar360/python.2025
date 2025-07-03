num1=int(input("enter 1st number"))
num2=int(input("enter 2st number"))
if(num1>num2):
    print("num1 is greater")
    num1 += 10
    print("updated num is",num1)
else:
    print("num2 is greater")
    num2 -= 5
    print("upadted num is",num2)