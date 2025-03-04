#Add task
#Changing status of task
#add and delete tasks, etc

def display_task():
    print("this display all the tasks")
    
def add_task():
    print("This adds the function")
    
def toggle_task():
    print("this functions toggles task")
    
def delete_task():
    print("this function deletes the task")
    
def main():
     while True:   
        print("\n .............Welcome to my ToDo List.............")
        print("\n1. Display task")
        print("2. Add Task")
        print("3.change task status")
        print("4. Delete Task")
        print("5. Quit \n") 
        
        choice = input("Select your option(1-5):")
        if choice == '1':
            display_task()
        elif choice == '2':
            add_task()
        elif choice == '3':
            toggle_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print ("you are quiting now")
        break
     else:
         print("Not valid choice")
    
if __name__ == "__main__":
    main()