#Walrus Operator is faeture introduced in python 3.8
#Walrus operator is denoted by (:=) in python
 
 #without Walrus
Number = int(input("Enter a Number"))
if Number == 0:
    print("Number is 0")
else:
    print("Not a Zero")
    
# After Using Walrus
if(number := int(input("Enter a number"))) == 0:
    print("Number is 0")
else:
    print("Number is Not a zero")    

manaia