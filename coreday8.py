i=int(input("enter your mark:"))
if(i>=95 and i<=100):
    print(" congratulation  your are grauated with high distiniction")
elif(i>=85 and i<95):
    print("Grade a+")
elif(i>=75 and i<85):
    print("Grade a")
elif(i>=65 and i<75):
    print("Grade b")
elif(i>=55 and i<65):
    print("Grade c")
elif(i>=45 and i<55):
    print("Grade d")
elif(i<0 or i>100):
    print("Invalid Marks")

else:
    print("Fail")