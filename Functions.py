#Functions is block of code which only reuns when it is called.
#Functions are reusable code blocks.

#In python function is defined using 'def' keyword.


#creating a function
def my_function():
    print("Hello World!")
#this wont give any output as function is not called.

#calling a function
my_function()  # Outputs: Hello World!


#Arguments are information that are passed into functions.

def greet(name):
    print("Hello " + name)
    
greet("John") #output is Hello John


#default arguments
def greet(name = "Guest"):
    print("Hello " + name)
    
greet() #output is Hello Guest
greet("John") #output is Hello John


# Return Statement
# The return statement is used to return a value from a function.

def add(Num1 , Num2):
    return Num1 + Num2

result = add(2 , 3)
print(result) #output is 5

