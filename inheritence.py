#***********single inheritnece***********
# class Animal:
#     def speak(self):
#         print("animaln speaking")
#     #child class dog inhert base class animal
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# d=Dog()
# d.bark()
# d.speak()



###**********multi level inheritance**************
# class Animal:
#     def speak(self):
#         print("animaln speaking")
#     #child class dog inhert base class animal
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
#the vchild claaas  dog child ihertit childd class of dog
# class DogChild(Dog):
#     def eat(self):
#         print("Eating bread...")
# d=DogChild()
# d.bark()
# d.speak()
# d.eat()
 
# ##mlttipplle inhertince
# class Calculation1:
#     def summation(self,a,b):
#         return(a+b)
# class Calculation2:
#     def multtiplication(self,a,b):
# #         return(a*b)
# # class Derived(Calculation1,Calculation2):
# #     def divide(self,a,b):
# #         return(a/b)
# # d=Derived()
# # print(d.summation(10,20))
# # print(d.multtiplication(10,20))
# # print(d.divide(30,5))
    
    
# #hierchial imnherotince
# class Parent:
#     def func1(self):
#         print("the function is parent class")
# class Child1(Parent):
#     def func2(self):
#         print("this function in child  one")

# class child2(Parent):
#     def func3(self):
#         print("this func in child 1")
# d=Child1()
# d.func1()
# d.func2()

# a=child2()
# a.func1()
# a.func3()
    
    
    ##hybrid***********
# class Person:
#     def display(self):
#         print("This is the person class")
# class Student(Person):
#     def student_info(self):
#         print("This is the stucent class")
# class Sports:
#     def sports_info(self):
#         print("This is the sports class")
# class SchoolStudent(Student,Sports):
#     def school_student_info(self):
#         print("This is the SchoolStudent")
# s=SchoolStudent()
# s.display()
# s.student_info()
# s.sports_info()
# s.school_student_info()
