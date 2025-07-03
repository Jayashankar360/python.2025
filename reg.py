while True:
    print("1 . registration")
    print("2 . login")
    print("3.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        name=(input("enter your name"))
        age=int(input("enter your age"))
        if(age>18):
            print("you are eligible")
        else:
            print("you are not eligible")
        phone=int(input("enter your phine num"))
        if(phone<10 and phone>10):
            print("valid num")
        else:
            print("invalid")
            
        address=int(input("enter your address"))
        uname=int(input("enter your username"))
        password=int(input("enter your password"))
    elif choice == 2:
        userid=int(input("enter your username"))
        userpass=int(input("enter your password"))
    elif choice==3:
        print("exiting ......")
        break
        
        
        
    