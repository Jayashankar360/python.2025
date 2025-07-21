def display(v):
    print(v)
    
    
def addition(a,b):
    ans=a+b
    display(f"sum of {a} and {b} is {ans}")
def substraction(a,b):
    ans=a-b
    display(f"substarction of {a} and {b} is {ans}")

def multtiplication(a,b):
    ans=a*b
    display(f"multtiplication of {a} and {b} is {ans}")
def division(a,b):
    ans=a/b
    display(f"division of {a} and {b} is {ans}")

while True:
    print("1 . ADDITION")
    print("2 . substraction")
    print("3 . multtiplication")
    print("4 . division")
    print("5.exit")
    choice =int(input("enter your choice :"))
    if (choice == 1):
        a=int(input("enter a number"))
        b=int(input("enter the second num"))
        addition(a,b)
        
    elif(choice == 2):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        substraction(a,b)
    elif(choice == 3):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        multtiplication(a,b)
    elif(choice == 4):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        if(b!=0):
           division(a,b)
        else:
            print("undefined")
    elif choice==5:
        print("exiting ......")
        break
        
        
        
        
        
    