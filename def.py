# def is_even(num):
#     if num%2==0:
#         print(num,"is even")
#     else:
#         print(num,"is odd")
# a=int(input("enter the num"))
# is_even(a)


#######factorialc

# def factorial(num):
#     fact=1
#     for k in range(1,num+1):
#         fact=fact*k
#     print("factorial of the number is",fact)
# n=int(input("enetr your num"))
# factorial(n)


##leap year

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year,"is leap year")
    else:
        print(year,"is not leap year")
a=int(input("enter a year"))
leap_year(a)
        
