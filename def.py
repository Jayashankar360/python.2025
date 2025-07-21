# def is_even(num):
#     if num%2==0:
#         print(num,"is even")
#     else:
#         print(num,"is odd")
# a=int(input("enter the num"))
# is_even(a)


#######factorialc------------

# def factorial(num):
#     fact=1
#     for k in range(1,num+1):
#         fact=fact*k
#     print("factorial of the number is",fact)
# n=int(input("enetr your num"))
# factorial(n)


##leap year---------------------

# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(year,"is leap year")
#     else:
#         print(year,"is not leap year")
# a=int(input("enter a year"))
# leap_year(a)
        


# def display(name,age):
#     print(f"hello my name is {name} iam {age} years old")
# display("reji",59)



# def display(**a):
#     print(f"hi {a['name']} welome to {a['course']} course")
    
# display(name="reji",course="python")


##pattern-------------------

# n=5
# for i in range(0,n):
#     for j in range(1,i+1):
#         print(j ,end=" ")
#     print()


###pattern abcde--------------


# for r in range(5):
#     n=65
#     for j in range(r+1):
#         print(chr(n),end=" ")
#         n+=1
#     print("")



# a=10
# def fun():
#     global a
#     b=a+25
#     print(b)
# fun()
# def sample():
#     global a
#     c=a-5
#     print(c)
# sample()

# def fact(num):
#     if num==1:
#         return num
#     else:
#         return num*fact(num-1)
# print(fact(5))
    
    
# def fun():
#     print("helO")
#     fun()


