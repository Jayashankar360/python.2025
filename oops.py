##***********class object******************
# class Employee:
#     id=10
#     name="john"
#     def display(self):#invoking
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()#obejct
# emp.display()
# #delete 
# del emp.id
# del emp.name
# emp.display()##its make error

#***obeject ,constructor
# class Car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year)
# c1=Car("toyota",2016)
# # c1.display()

# #***parametrs constructor************
# class Employee:
#     def __init__(self,name,id):
#         self.id=id
#         self.name=name
#     def display(self):
#         print("ID:%d\n Name:%s"%(self.id,self.name))
# emp1=Employee("john",101)
# emp2=Employee("david",102)
# emp1.display()
# emp2.display()


#****non parmetrsz constrcur*******
# class Student:
#     def __init__(self):
#         print("this is non parametrized constructor")
#     def show(self,name):
#         print("Hello",name)
# Student=Student()
# Student.show("john")
        
class student:
    def __init__(self,name,id,age):
     self.name=name
     self.id=id
     self.age=age
s=student("john",101,22)
#print the attribute nameof the obj
print(getattr(s,'name'))
#reset the value to 23
setattr(s,"age",23)
#print the modified value
print(getattr(s,'age'))
##print true if the student cobatin the attribute name id
print(hasattr(s,'id'))
#3delete the attribute age
delattr(s,'age')
#this will be given an errror since the attribute age has been deleted
# print(s.age)        