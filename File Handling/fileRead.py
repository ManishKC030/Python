#We have Demo file in this same folder.
#We will use it to read the data.
#To open the file, we use the built-in open() function.
#It is good practise to close a file after opening.


# Opening the file in Read mode:

file = open("D:\\Python\\File Handling\\demofile.txt", 'r')
print (file.read())
file.close() # Closing the file.

#this doesn't need to specify path as it is in working directory
test = open('test.txt', 'r')
#this reads only 4 first characters
print(test.read(4)) 
test.close()





