##n to 1 prinnt
# def rec(num):
#     if num==1:
#         return num
#     else:
#         return f"{num},{rec(num-1)}"
# n=int(input("eneter your number"))
# print(rec(n))


##some of n natural numbers********
# def sum(num):
#     if num==0:
#         return num
#     else:
#         return num+(sum(num-1))
# n=int(input("eneter your number"))
# print(sum(n))

#*****summ of dighit******
# def sum(num):
#     if num<10:
#         return num
#     else:
#         return (num % 10) +sum(num//10)
# n=int(input("eneter your number"))
# print(f"sum of digihits of {n} is {sum(n)}")

#******reverse of a letter***********
def reverse(s):
    if len(s)<= 0:  
        return s
    else:
        return reverse(s[1:]) + s[0]  
string = input("Enter a string: ")
print(f"Reversed string: {reverse(string)}")