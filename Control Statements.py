# Break statement
# The break statement is used to terminate the loop prematurely.
# It is used to exit the loop when a certain condition is met.


#In for loop
for i in range(5):
    if i == 3:
        break
    print(i) #output is 0, 1, 2 as when i = 3 it breaks the loop
    
#While loop
i = 0
while i < 5:
    if i == 2:
        break
    print(i)
    i += 1 #output is 0, 1 as when i = 2 it breaks the loop
    

# Continue statement
# The continue statement is used to skip the current iteration of the loop and move on to the next
# It is used to skip the current iteration when a certain condition is met.

#In for loop
for i in range(5):
    if i == 3:
        continue
    print(i) #output is 0, 1, 2, 4 as when i = 3 it skips it
# its same in while loop too


#else statement
# The else statement is used to execute a block of code when the loop finishes normally 

for i in range(6):
    print(i)
else:
    print("Loop Completed!!")
    
#while Loop
i = 0
while i <= 5:
    print(i)
    i += 1
else:
    print("While loop completed")
    
    
    
    #print commmit


