# if condition
#example
a=5;
b=10;
if a<b:
  print("a is smaller than b") #this will bw printed cause condition is true

#in python you have to make sure of indentation otherwise it thows you an error.


#elif is just like "if else/ else if "

elif a == b:
  print("a is equal to b") #this will not be printed cause condition is false
  
  
#else. if both condition fails then this is printed

else:
  print("a is greater than b") 
  

#conditional expression or ternary operator or short hand if..else

x=20
y=30
print("x is greater than y") if x>y else print("x is smaller than y")
