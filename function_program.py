# def palindrome(num):
#     temp=num
#     rev=0
#     while num>0:
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     if temp==rev:
#         print("The number is palindrome")
#     else:
#         print("The number is not palindrome")
# a=int(input("enter the number:"))
# palindrome(a)

#************reverse of a string**********
# def reverse(s):
#     if len(s)<= 0:  
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
# string = input("Enter a string: ")
# print(f"Reversed string: {reverse(string)}")    

######Write a function that takes a string and counts the number of vowels.**************
# def vowels(c):
    
#     count = 0
#     for i in c:
#         if i.lower() in 'aeiou':
#             count += 1
#     return count
# string = input("Enter a string: ")
# print(f"Number of vowels in '{string}': {vowels(string)}")

###**power of number***
# def power(b,e):
#     result=1
#     for i in range(0,e):
#         result=result*b
# b=int(input("Enter the base:"))
# e=int(input("Enter the exponent:"))
# print(f"{b} raised to the power{e} is {power(b,e)}")
    



