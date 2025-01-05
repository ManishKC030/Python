#for loop is used to iterate over the sequence

#syntax:
# for iems in sequence:
     #code to be executed
     
fruits = ["apple", "banana", "cherry", "berry"]
for x in fruits:
    print(x)
    

for i in range (0, 10):
    print (i) #output will be 0 to 9
    
#in range function range() you can specify 
# range(start, stop, step_size)

#example
for i in range (0, 10, 2):  #loop steps 2 sizes
    print (i) #output will be 0, 2, 4, 6, 8
