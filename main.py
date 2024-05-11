import sys
import getpass
from datetime import datetime

# This function will create a new user account 
def create_user(database):

    print('######## CREATE ACCOUNT ########')
    # Checks if the user exists or has had a database file made for it in database.txt
    with open('user-database.txt', 'r') as file:
        existing_usernames = {line.strip().split(',')[0] for line in file}

    username = input("Create Username: ")

    # This will check if the username matches any other usersnames, if it does it will loop and prompt the user to try again.
    if username in existing_usernames:
        print('You were beaten to making that username, please try another one!')
        return

    # Just confirms the passwords match, if they don't prepare to be looped other wise the new user is made
    password = getpass.getpass("Create Password: ")
    password_confirmation = getpass.getpass("Confirm Password: ")

    if password != password_confirmation:
        print("The passwords didn't match, perhaps type slower?")
        return

    with open('user-database.txt', 'a') as file:
        file.write(username + ',' + password + '\n')
        print(f'{username} is created and prepared for action, you can now login.')
    
    # adds the created user to the database
    with open(f'{username}-tasks.txt', 'a'):
        pass

    # Logs in an already existing user, other wise its time to be looped
def login_user(database):
    print('######## LOGIN ########')
    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")

    # This will stop you from being looped to the Home menu as it was annoying to have to re enter login when nothing was entered
    # So instead this will loop you back to username and password input phase
    if not username or not password:
        print("I'm no expert but im pretty sure you need to enter your username and password to login.")
        return login_user(database)
    
    uname = None
    pwd = None

    with open("user-database.txt", "r") as file:
        for line in file:
            user_name_pwd = line.strip().split(",") # Strips and splits the username and password to be stored in the database
            if len(user_name_pwd) == 2: # Ensures there's two parts (username, password) to store
                uname, pwd = user_name_pwd # puts the username and password into one variable to be stored
                # Ensures the users match a user and then logs in, otherwise LOOP back to home to create
            if username == uname and password == pwd:
                print("######## LOGIN SUCCESSFUL ########")
                print("Alright", username,"let's get this party started!")
                return username
        print("Login has failed, take some deep breaths and try again?") 
        return False

# This function handles the create user and login aspects of the application, it displays seletors/inputs for the
# User to input and then acts accordingly. If incorrect inputs error handling is done via LOOP
def home(database):
    print("#### Enter (Login, Signup or Exit) to select desired option ####")
    print('######## HOME ########')
    while True:
        option = input("Login | Signup | Help | Exit: ").strip().lower()
        if option == "login":
            return login_user(database)
        elif option == 'signup':
            create_user(database)
        elif option == 'help':
            help_controls()
        elif option == 'exit':
            sys.exit()
        else:
            print("I think you typed something in wrong, try again?")

# This function is to get the priority of a task from the input of the user and then store and display it later in view tasks
def get_task_priority():

    while True:
        task_priority = input("Enter (High, Medium, Low) to set task importance: ").strip().lower()
        if task_priority in ['high', 'medium','low']:
            return task_priority
        else: 
            print("Invaild input please enter 'high', 'medium', 'low'" )
# This function gets the due date if there is one from the user and then stores it for display later in view tasks
# If a incorrect input for dd/mm/yyyy is used it will prompt the user to try again.
def get_task_due_date():
    while True:
        task_duedate = input("Enter when the big boss wants the task done (DD/MM/YYYY) or press enter to live dangerously: ").strip()
        if not task_duedate:
            return None
        else:
            try:
                datetime.strptime(task_duedate, '%d/%m/%Y')
                return task_duedate
            except ValueError:
                print("You have to enter a valid DD/MM/YYYY then press enter!")
                continue
# This function is the big boy and is in charge of the main purpose of this application, CREATING TASKS
# it will create the task and then store that task for the user that is logged in and NO ONE else. *i hope, i think... only a fool deals in absolutes*
def add_task(username):
    while True:
        print('######## ADD TASK MENU ########')
        task_title = input("Enter task title: ")
        task_info = ''

        print("Enter your task information, when you're done type (0) on a newline:")
        while True:
            line = input('')
            if line.lower() == '0':
                break
            task_info += line + '\n'
        task_priority = get_task_priority()
        task_importance = '!' if task_priority == 'high' else ''
        task_duedate = get_task_due_date()
        
        add_task_data = {
            "task_title": task_title,
            "task_info": task_info,
            "task_priority": task_priority,
            "task_importance": task_importance,
            "task_duedate": task_duedate,
        }

        with open(f"{username}-tasks.txt", "a") as file:
            file.write(str(add_task_data) + "\n")

        print(f"NICE! {task_title} has been added to your To-dos!")

        choice = input("Do you want to create another? enter (Yes/No) or press enter to return to main menu:")
        if choice.lower() != "yes":
            if choice == '0':
                confirmation = input("Would you like to create this task?")
                if confirmation.lower() == 'yes':
                    break
            else:
                break

# This will allow the user to view all the tasks they have made and all the information inside
def view_all_tasks(username):
    while True:
        print('\n########## SAVED TASKS ##########\n')
        with open(f"{username}-tasks.txt", "r") as file: # This ensures the user thats logged in is the only user the information is shown for.
            for line in file:
                if line.strip():
                    task_data = eval(line.strip())
                    print("Title: ", task_data["task_title"])
                    print('Information: ', task_data['task_info'])
                    print("Importance: ", task_data.get("task_priority", "Not set"))
                    print("Due Date: ", task_data.get("task_duedate", "Not set"))
                    completed_status = "Completed" if task_data.get("completed", False) else "Not Completed"
                    print("Complete: ", completed_status, '\n')
                
        choice = input("Enter '0' or type 'exit' or press enter to return to main menu: ").strip()
        if choice.lower() == "exit":
            break
        elif choice == "0":
            return
        break  

# This function handles completing the task of, once again, a specific user.
def completed_tasks(username):
    print("######### COMPLETED TASKS #########")
    tasks_to_store = []
    with open(f'{username}-tasks.txt', 'r') as file: # User the task is being completed for.
        for line in file:
            task_data = eval(line.strip())
            tasks_to_store.append(task_data)

    if not tasks_to_store:
        print('\n'+ "There's nothing in here to mark complete, we should make a task!" + '\n')
        return
    
    print("Choose a task you would like to add to 'Completed': ")
    for i, task in enumerate(tasks_to_store, 1):
        print(f'{i}. {task["task_title"]} - {"Complete" if task.get("completed", False) else "Not Completed"}')

    while True:
        try:
            choice = int(input("Enter the task number starting from '1' to mark task as complete or to reverse completion, or enter '0' to exit: "))
            if choice == 0:
                return
            elif 1 <= choice <= len(tasks_to_store):
                task = tasks_to_store[choice - 1]
                if task.get('completed', False):
                    # This will un-complete the completed task
                    task['completed'] = False
                    print('Task completion reversed!')
                else:
                    task['completed'] = True
                    # This will mark the task as complete
                    print('Another day, another task complete!')
                with open(f'{username}-tasks.txt', 'w') as file:
                   for updated_task in tasks_to_store:
                       file.write(str(updated_task) + '\n')  
                return
            else:
                print("It doesn't look like there's a task to delete with that number!")
        except ValueError:
            print('You have no power here hacker, enter a valid task number or pay the fine!')

# This function handles task deletion, it will completely remove a task created in the logged in user.
def delete_task(username):
    print('######## DELETE TASK MENU ########')
    tasks_to_store = []
    with open(f'{username}-tasks.txt', 'r') as file:
        for line in file:
            task_data = eval(line.strip())
            tasks_to_store.append(task_data)

    if not tasks_to_store:
        print('THIS IS EMPTY, MPTY, MPT, MT!!! Create a task to Delete it!')
        return
    
    print('Please choose a task you would like to delete: ')
    for i, task in enumerate(tasks_to_store, 1):
        print(f'{i}. {task["task_title"]}')

    while True:
        try:
            choice = int(input('Enter the task number to delete it, or enter 0 to exit: '))
            if choice == 0:
                return
            elif 1 <= choice <= len(tasks_to_store):
                # Removes the selected task
                del tasks_to_store[choice - 1]
                # updates the database once the deletion has happened
                with open(f'{username}-tasks.txt', 'w') as file:
                    for task in tasks_to_store:
                        file.write(str(task) + '\n')
                print('Task deleted successfully.')
                return
            else:
                print("So I had a quick look and there's no task with that corresponding number, let's try inputting the number again.")
        except ValueError:
            print('You have no power here hacker, enter a valid task number or pay the fine!')
      
def help_controls():
    print('######## Help and Controls ########')
    try:
        with open('help-controls.txt', 'r') as file:
            for line in file:
                print(line.rstrip())
    except FileNotFoundError:
        print("Someone has deleted the help file, if you weren't panicking you should be.")
    return

# Handles logging the logged in user out specifics of the handling located in (def main)
def logout_application():
    print('Adios comrade, until we meet again!')
    return False

# So there was Mr meat earlier that adds the task, but this. This is the mothership.
# Within this function is the main menu, the navigation hub that will take the user to wherever they desire within the application
# I made it a dict menu navigating through keys and values becase it was super modular!
def main_menu(username, user_logged_in, database):
    options = {
        "1": lambda: add_task(username), # Lambdas have been added to the options that require the username arg so data is saved uniquely to each user.
        "2": lambda: view_all_tasks(username),
        "3": lambda: completed_tasks(username),
        "4": lambda: delete_task(username),
        "5": help_controls,
        "6": logout_application
    }

# Main menu display to user loops aslong as the user is TRUE for being logged in
    while True:
        print("######## WELCOME TO THE MAIN MENU #########")
        if user_logged_in:
            print("1. Add a tasks")
            print("2. View all tasks")
            print("3. Complete tasks")
            print("4. Delete tasks")
            print("5. Help and Controls")
            print("6. Logout of application")
            choice = input("Enter Menu number: ")

            if choice in options:
                if choice == '6':
                    user_logged_in = not options[choice]()
                    break
                else:
                    options[choice]()
            else:
                print("Not trying to tell you what to do, but you might want to try entering a number between 1-6.")
        else:
            print("How did you even get here? why are you even reading this? Honestly well done getting here... Anyway, you need to login first")
            if home(database):
                user_logged_in = True
    return

# This starts the application and sends you to home to get the party started!
def main():
    # Loops until the program is manually closed/exited
    while True: 
        # Opens the userdata txt to read
        with open("user-database.txt", "r") as file:
            user_logged_in = False
            # This will keep asking to run asking for a login
            while not user_logged_in:
                username = home(file)
                # if the user is logged in successfully it will change to true and execute the main menu function
                if username:
                    user_logged_in = True
                    main_menu(username, user_logged_in, file)

# This makes sure the program/script/application is being run by python interpreter
if __name__ == "__main__":
    # Then it will call main if it is
    main()