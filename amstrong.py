#amstrong
i=int(input("Enter a number: "))
a=i
j=0
while (i>0):
    b=i%10
    j=j+b**3
    i=i//10
if (a==j):
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
        