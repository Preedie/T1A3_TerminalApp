def create_user(database):
    database = open("user-database.txt", "r")
    # Database will link to the user-database.txt file and will allow the user to write login information to it. (creating their account and saving it for future sessions to login to)
    username = input("Create Username: ")
    # This is where the username that is entered/created will be input.
    password = input("Create Password: ")
    # This is where the password that is entered/created will be input.
    password_confirmation = input("Confirm Password: ")
    # This will prompt the user to confirm their password to ensure they match.
    username_store = []
    # This will store the username input, into a list
    password_store = []
    # This will store the password input, into a list
    for i in database:
        a, b = i.split(",")
        b = b.strip()
        username_store.append(a)
        password_store.append(b)
    data = dict(zip(username_store, password_store))
    # the data variable was made so i could print the usernames and passwords in dict form, it is
    # slightly reduntant as the usernames and passwords are being stored
    # implicitly due to them being stored in a seperate txt file however i found it easier to call
    # the list in dict form so i could read/see what was happening to ensure it was what i wanted. (Writing and reading the inputs by the user)

    # The for loop used here will take the username and password strip them of their white space
    # and store them into a (list) in a seperate txt file.
    # This will allow the user to input their username and password into the dictionary.

    if password != password_confirmation:
        print("Passwords do not match, try again")
        create_user(database)
        # Simple code reading the input from the user from password variable making sure password_confirmation matches and then
        # storing the password in a list within the txtfile using password_store.
    else:
        if len(password) <= 7:
            print("Password must be at least 7 characters")
            create_user(database)
            # If the password created is shorter than 7 characters this code will as you to rewrite your password with atleast 7 characters.
        elif username in username_store:
            print("Username already exists, try again")
            create_user(database)
        else:
            database = open("user-database.txt", "a")
            database.write(username + "," + password + "\n")
            print(f"Welcome {username}, enjoy.")


def login_user(database):
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if not username or not password:
        print("Username or Password cannot be empty")
        return login_user(database)

    with open("user-database.txt", "r") as file:

        for line in file:
            uname, pwd = line.strip().split(",")
            if username == uname and password == pwd:
                print("Login successful")
                print("Hi,", username)
                return True
        print("Login failed: Username or Password incorrect or account does not exist")
        return False


def home(database):
    option = input("Login | Signup: ")
    if option == "Login":
        return login_user(database)
    elif option == "Signup":
        return create_user(database)
    else:
        print("Please enter an option")
        return False


################################################################################################################################################ ABOVE DONE


def add_task():
    while True:
        task_title = input("Enter task title: ")
        task_info = input("Enter task information: ")
        task_priority = input(
            "Enter (High, Medium, Low) to set task importance or press enter to skip: "
        )
        task_importance = (
            "!" if task_priority.lower() == "High" else "" if task_priority else ""
        )
        task_duedate = input(
            "Enter task due date (DD/MM/YYYY) or press enter to skip: "
        )

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

        choice = input("Do you want to create another task? (Yes/No): ")
        if choice.lower() != "yes":
            break
        # This function is used to add the task.


def view_all_tasks():
    while True:
        with open("add-task.txt", "r") as file:
            for line in file:
                task_data = eval(line.strip())
                print("Title: ", task_data["task_title"])
                print("Importance: ", task_data.get("task_priority", "Not set"))  # Handle missing priority
                print("Due Date: ", task_data.get("task_duedate", "Not set"))  # Handle missing due date
                print()  # Add a newline between tasks

        choice = input("Press Enter to continue or type 'exit' to return to main menu: ").strip()
        if choice.lower() == "exit":
            break  # Break out of the loop to return to the main menu


def completed_tasts():
    print("Mark a task as complete Function")
    # This function is used to mark a task as complete.


def delete_task():
    print("Delete a task Function")
    # This function is used to delete tasks and send them to the ARCHIVED function


def help_controls():
    print("-------Welcome to my To-Do List/Task Application!--------")
    # This function will show the user how to use the application
    return


def archived_tasks():
    print("Archived tasks Function")
    # This function is used to view all the archived tasks and allow the user to un archive.


def logout_application():
    print('Logging out of user')
    return True
 
    # This function logs the user out and sends them to the login screen.


def main_menu(user_logged_in, database):

    options = {
        "1": add_task,
        "2": view_all_tasks,
        "3": completed_tasts,
        "4": delete_task,
        "5": help_controls,
        "6": archived_tasks,
        "7": logout_application,
    }

    while True:
        print("Welcome to To Do List")
        if user_logged_in:
            print("1. Add a tasks")
            print("2. View all tasks")
            print("3. Completed tasks")
            print("4. Delete tasks")
            print("5. Help and Controls")
            print("6. Archived tasks")
            print("7. Logout of application")
            choice = input("Enter Menu number: ")

            if choice in options:
                if choice == '7':
                    user_logged_in = not options[choice]() # if the user inputs 7 they log out which will update the user_logged_in to false returning them to signup/create
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
    with open("user-database.txt", "r") as file:
        user_logged_in = False
        while not user_logged_in:
            user_logged_in = home(file)
            if user_logged_in:
                main_menu(user_logged_in, file)


if __name__ == "__main__":
    main()

