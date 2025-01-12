# Inheritance allows a class to inherit attributes and methods from another class.
# The child class inherits all the attributes and methods from the parent class.

# Single Inheritance: A child class inherits from one parent class.
# Multiple Inheritance: A child class inherits from multiple parent classes.
# Multilevel Inheritance: A class inherits from a derived class.

class Animal:   #Parent Class
    def sound(self):
      return "I am an Animal"
        
class Dog(Animal):  #CHild Class
    def sound(self):
       return "Dog Barks. Woof!!"
        
dog = Dog()
print(dog.sound())