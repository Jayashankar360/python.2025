# ##**********protect member*********

# class Base: 
# 	def __init__(self): 
# 		# Protected member 
# 		self._a = 2
# # Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 
# 		# Calling constructor of 
# 		# Base class 
# 		Base.__init__(self) 
# 		print("Calling protected member of base class: ", self._a) 
# 		# Modify the protected variable: 
# 		self._a = 3
# 		print("Calling modified protected member outside class: ", self._a) 
# obj1 = Derived() 

# obj2 = Base() 

# # Calling protected member 
# # Can be accessed but should not be done due to convention 
# print("Accessing protected member of obj1: ", obj1._a) 

# # Accessing the protected variable outside 
# print("Accessing protected member of obj2: ", obj2._a) 

#****private meber*********8
# class Base: 
#  def __init__(self): 
#    self.a = "Hello"
#    self.__c = "World"

# # Creating a derived class 
# class Derived(Base): 
#     def __init__(self): 

# # Calling constructor of 
# # Base class 
#         Base.__init__(self) 
#         print("Calling private member of base class: ") 
#         print(self.__c)
#         obj1 = Base() 
#         print(obj1.a) 

##abstarction***********
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method

class Dog(Animal):  # Concrete class
    def make_sound(self):
        return "Woof!"

class Cat(Animal):  # Concrete class
    def make_sound(self):
        return "Meow!"

    # Client code
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound()) # Output: Meow!