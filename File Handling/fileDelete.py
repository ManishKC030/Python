# To delete a file, you must import the OS module, and run its os.remove() function.
# The os.remove() function deletes the specified file.

import os
# Delete a file
os.remove("delete.txt") #this deleted file named delete.txt
# To avoid getting an error, you might want to check if the file exists before you try to delete it.


# Now you can check if file is deleted or not
import os
if os.path.exists('delete.txt'):
    print("file exists")
else:
    print("File doesn't exists")
# output : File doesn't exists as we deleted in above section.
