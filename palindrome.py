#palindrome
i=int(input("Enter a number: "))
j=0
b=i
while (b>0):
    a=b%10
    j=j*10+a
    b=b//10
if (i==j):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")