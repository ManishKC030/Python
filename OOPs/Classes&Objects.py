# OOP stands fot Object Oriented Programming.
# It is a programming paradigm that uses objects and classes to design applications and programs.

# Classes and Objects
    # Class:
    #   - A blueprint or a template for creating objects is called class.
    #Class is always written in PascalCase.

#To create a 'class', use the keyword "class".

class MyClass :
    x=5   #we created class MyClass with Property named X.

#Now we can use class to create objects.
#Object is an instance of a class.
#Object is created using the class name.
#Object is always written in camelCase.

obj = MyClass()  #we created object obj from class MyClass.
print(obj.x)  #we printed the value of property X of object obj.


#__init__() Function
#The __init__() function is a special function in Python classes, which is always executed when class is being initiated.
#It is used to assign initial values to variables or other resources during object creation.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #Now we can create objects from class Person and print their properties.

obj1 = Person("John", 30)
print(obj1.name)  # prints: John
print(obj1.age)   # prints: 30
