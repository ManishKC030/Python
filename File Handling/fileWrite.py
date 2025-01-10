# To write in your file, you can either append or write.
# Append will add to the end of the file, while write will overwrite the file.

file = open('test.txt', 'a')
file.write("Now this is an appended line!")
file.close()

#opening file in read mode to see the changes
file = open('test.txt', 'r')
print(file.read())


#Now to overwrite the content
file = open('test.txt', 'w')
file.write("Now this is an overwritten line!")
file.close()
#opening file in read mode to see the changes
file = open('test.txt', 'r')
print(file.read())
#this deletes all previous line and overwrites in it.
