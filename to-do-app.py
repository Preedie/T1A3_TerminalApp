import sys

def create_user(database):
    database = open("user-database.txt", "a")
    # Database will link to the user-database.txt file and will allow the user to write login information to it. (creating their account and saving it for future sessions to login to)
    username = input("Create Username: ")
    # This is where the username that is entered/created will be input.
    password = input("Create Password: ")
    # This is where the password that is entered/created will be input.
    password_confirmation = input("Confirm Password: ")
    # This will prompt the user to confirm their password to ensure they match.

    if password != password_confirmation:
        print("Passwords do not match, try again")
        create_user(database)
        return
        # Simple code reading the input from the user from password variable making sure password_confirmation matches and then
        # storing the password in a list within the txtfile using password_store.
    
    with open('user-database.txt', 'r') as file:
        for line in file:
            if ',' in line:  # Check if the line contains a comma
                user_info = line.strip().split(', ')
                if len(user_info) == 2:  # Ensure there are two parts (username and password)
                    uname, _ = user_info
                    if username == uname:
                        print('Please pick another username!')
                        create_user(database)
                        return
    
    with open('user-database.txt', 'a') as file:
        file.write(username + ',' + password + '\n')
        print(f'Welcome {username}, enjoy making your tasks!')

def login_user(database):
    username = input("Enter Username: ") # Username and Password Enteries 
    password = input("Enter Password: ")

    if not username or not password: # If the username and/or password do not match a created user in user-database it will return user to login 
        print("Username or Password cannot be empty")
        return login_user(database)

    with open("user-database.txt", "r") as file: # Here the application is opening and reading the user-datatxt to check the uname and pwd exist
        for line in file:
            user_name_pwd = line.strip().split(",") # Ensuring uname and pwd are split 
            if len(user_name_pwd) == 2: # Ensuring there are two parts (which split took care of) in the form of uname and pwd
                uname, pwd = user_name_pwd
            if username == uname and password == pwd: # if the uname and pwd are saved in userdata txt this code outputs
                print("Login successful")
                print("Hi,", username)
                return True
        print("Login failed: Username or Password incorrect or account does not exist") 
        # if uname and pwd dont match any created users 
        # user is returned to login
        return False

def home(database):
    while True: # While there has been no valid input from the user the "option" menu will continue to show to allow the user to either
        #login create an account or to exit the application.
        option = input("Login | Signup | Exit: ").strip().lower() # I used the strip and lower method so that whatever input the user uses for login
        #create or exit, the application will accept it and perform what the user specifies 
        if option == "login":
            return login_user(database)
        elif option == 'signup':
            create_user(database)
        elif option == 'exit':
            sys.exit()
        else:
            print("Please enter an option")
            # A very simple and straight forward if loop that takes the users input and checks it against the options.
            # If an invalid input is used it will perform the else print statement and loop until a valid option is used ending the while loop.

def get_task_priority():
    while True:
        task_priority = input("Enter (High, Medium, Low) to set task importance or press enter to skip: ").strip().lower() # Enters the priority of the task and stores in txt
        if task_priority in ['high', 'medium','low']:
            return task_priority
        else: 
            print("Invaild input please enter 'high', 'medium', 'low', or leave it empty and press enter" )
            
def get_task_due_date():
    while True:
        task_duedate = input("Enter task due date (DD/MM/YYYY) or press enter to skip: ").lower().strip()
        if task_duedate in ['high', 'medium','low']:
            return task_duedate
        else: 
            print("Invaild input please enter 'high', 'medium', 'low', or leave it empty and press enter" )

def add_task():
    while True:
        task_title = input("Enter task title: ") # Enter the task title and store in txt
        task_info = input("Enter task information: ") # Enter the task info and store it in txt
        task_priority = get_task_priority()
        task_importance = '!' if task_priority == 'High' else ''
        task_duedate = input("Enter task due date (DD/MM/YYYY) or press enter to skip: ")
        

        add_task_data = {
            "task_title": task_title,
            "task_info": task_info,
            "task_priority": task_priority,
            "task_importance": task_importance,
            "task_duedate": task_duedate,
        }

        with open("add-task.txt", "a") as file:
            file.write(str(add_task_data) + "\n")

        print(f"NICE! {task_title} has been added to your To-dos!")

        choice = input("Do you want to create another task? (Yes/No) or press enter to return to main menu: ")
        if choice.lower() != "yes":
            break
        # This function is used to add the task.

def view_all_tasks():
    while True:
        print('########## Saved Tasks ##########')
        with open("add-task.txt", "r") as file:
            for line in file:
                task_data = eval(line.strip())
                print("Title: ", task_data["task_title"])
                print("Importance: ", task_data.get("task_priority", "Not set"))  # Handle missing priority
                print("Due Date: ", task_data.get("task_duedate", "Not set"))  # Handle missing due date
                completed_status = "Completed" if task_data.get("completed", False) else "Not Completed" # This is going to add a 'Completed' Status to the view tasks if the task is completed in completed tasks def
                print("Complete: ", completed_status) # Prints the code above but in a user friendly manner.
                print()  # Add a newline between tasks

        choice = input("Enter '0' or type 'exit' to return to main menu: ").strip()
        if choice.lower() == "exit":
             break
        elif choice == "0":
            return
        break  # Break out of the loop to return to the main menu

def completed_tasks():
    print("######### COMPLETED TASKS #########")
    tasks_to_store = []
    with open('add-task.txt', 'r') as file:
        for line in file:
            task_data = eval(line.strip()) # Identifies the information in task data as a dict
            tasks_to_store.append(task_data)

    if not tasks_to_store: # this is just checking if theres any tasks to store 
        print('\n'+ 'There are no tasks to mark as completed' + '\n')
        return
    
    print("Choose a task you would like to add to 'Completed': ")
    for i, task in enumerate(tasks_to_store, 1):
        print(f'{i}. {task["task_title"]} - {"Completed" if task.get("completed", False) else "Not Completed"}')

    while True:
        try:
            choice = int(input("Enter the task number starting from '1' to mark task as complete or to reverse completion, or enter '0' to exit: "))
            if choice == 0:
                return
            elif 1 <= choice <= len(tasks_to_store):
                task = tasks_to_store[choice - 1]
                if task.get('completed', False):
                    task['completed'] = False # This will hopefully reverse the completed task, it's late and as i write this comment ive not yet tested it
                    # i may just have a mental breakdown if it doesn't work, will update with an edit.
                    # This function is used to mark a task as in-complete. *edit* thank you lord it works 
                    print('Task completion reversed!')
                else:
                    task['completed'] = True #This will make the task complete "fingers crossed"
                    print('Task completed successfully!')
                with open('add-task.txt', 'w') as file: # this will update the txt file if there's a task changed to complete.
                   for updated_task in tasks_to_store:
                       file.write(str(updated_task) + '\n')  
                return
            else:
                print('There are no tasks with that number, please enter a valid number.')
        except ValueError:
            print('You have no power here hacker, enter a valid task number!')

def delete_task():
    tasks_to_store = []
    with open('add-task.txt', 'r') as file:
        for line in file:
            task_data = eval(line.strip()) # Identifies each line in task_data as a dictionary
            tasks_to_store.append(task_data)

    if not tasks_to_store: # This will check if there are no tasks
        print('There are no tasks to delete.')
        return
    
    print('Please choose a task you would like to delete: ')
    for i, task in enumerate(tasks_to_store, 1): # This will enumerate a list of tasks that have been created from the txt file starting at 1.
        print(f'{i}. {task["task_title"]}')

    while True:
        try:
            choice = int(input('Enter the task number to delete it, or enter 0 to exit: '))
            if choice == 0:
                return
            elif 1 <= choice <= len(tasks_to_store):
                del tasks_to_store[choice - 1] # This will delete the selected class if its above 0 otherwise the user will exit delete task
                with open('add-task.txt', 'w') as file: # This will update the txt file taht stores the tasks if a task is deleted
                    for task in tasks_to_store:
                        file.write(str(task) + '\n')
                print('Task deleted successfully.')
                return
            else:
                print("There's no task with that number! Try again.")
        except ValueError:
            print('You have no power here hacker, enter a valid task number!')
      
def help_controls():
    print("-------Welcome to my To-Do List/Task Application!--------")
    # This function will show the user how to use the application
    return

def archived_tasks():
    print("Archived tasks Function")
    # This function is used to view all the archived tasks and allow the user to un archive.

def logout_application():
    print('Logging out of user')
    return False
 
    # This function logs the user out and sends them to the login screen.

def main_menu(user_logged_in, database):

    options = {
        "1": add_task,
        "2": view_all_tasks,
        "3": completed_tasks,
        "4": delete_task,
        "5": help_controls,
        "6": archived_tasks,
        "7": logout_application,
    }
    # This is a dictionary to select/add functions to create the to do list. I chose a dictionary as it's SUPER easy to add and take away whatever i would like without effecting
    # or BREAKING all the other code in the program.

    while True:
        print("Welcome to To Do List")
        if user_logged_in:
            print("1. Add a tasks")
            print("2. View all tasks")
            print("3. Complete tasks")
            print("4. Delete tasks")
            print("5. Help and Controls")
            print("6. Archived tasks")
            print("7. Logout of application")
            choice = input("Enter Menu number: ")

            if choice in options:
                if choice == '7':
                    user_logged_in = not options[choice]() # if the user inputs 7 they log out which will update the user_logged_in to false returning them to signup/create
                    break
                else:
                    options[choice]()
            else:
                print("Please enter a valid menu number")
        else:
            print("You need to login first")
            if home(database): # This will call the home function and update the user_logged_in to True if the user indeed passes the login requirements
                user_logged_in = True
            
    return

def main():
    while True: 
        with open("user-database.txt", "r") as file:
            user_logged_in = False
            while not user_logged_in:
                user_logged_in = home(file)
                if user_logged_in:
                    main_menu(user_logged_in, file)

if __name__ == "__main__":
    main()

