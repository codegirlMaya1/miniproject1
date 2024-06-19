print(" Welcome to the To-Do List App!")
def add_task(tasks):
    
    # ask for task to add
    add = input("\nWhat tasks do you want to add? ")

    # if tasks not already in list, add task
    tasks.append(add) if not add in tasks else print("\nTask already in list.")

def show_task(tasks):
    
    # show all tasks
    print("\nThese are your tasks: ", tasks)
    
    

def delete_task(tasks):
    
    # ask for tasks to delete
    delete = input("\nPlease enter task to delete: ")

    # if tasks is in list, delete tasks
    tasks.remove(delete) if delete in tasks else print("\nTask not found.")
    
def remove_task(tasks):
    
    # ask for which tasks were completed
    delete = input("\nPlease enter completed tasks: ")

    # if tasks is in list, remove completed tasks
    tasks.remove(delete) if delete in tasks else print("\nTask not found.")


def main():
    
    # initialise list of sample tasks
    tasks = ["sweep","mop","sanitize"]

    # loop action cycle
    while 1:
        try:
            # ask user for selection
            selection = int(input("\nMENU: \n(1) Add task\n(2) Show all task\n(3) Complete a task\n(4) Delete a task\n(5) Quit\n"))

            # call associated function
            if selection == 1:
                add_task(tasks)
            elif selection == 2:
                show_task(tasks)
            elif selection == 3:
                remove_task(tasks)
            elif selection == 4:
                delete_task(tasks)    
            elif selection == 5:
                break
            else:
                raise ValueError

        except ValueError:
            print("\nNot a viable option. Please pick 1, 2 or 3.")



if __name__ == "__main__":
    main()