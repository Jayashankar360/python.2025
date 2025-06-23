# name=(input("Enter the string:"))
# reverse=""
# for i in range name:
#     reverse=i+reverse 
#     #reverse =text[::-1] without builtin
# print("reversed string:",reverse)


text = input("Enter the string:")
reverse = ""
for i in text:
    reverse = i + reverse  # Adds each character to the front
print("reversed string:", reverse)