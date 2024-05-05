# To Do List Application
import json

CREATED_USER_STORAGE = 'created-user.json'
logged_in_user = None # Stores the currenly logged in user.
def load_user():
    try:
        with open(CREATED_USER_STORAGE, 'r') as storage:
            return json.load(storage)
    except FileNotFoundError:
        return {} 
    
def save_user(data):
    with open(CREATED_USER_STORAGE, 'w') as storage:
        json.dump(data, storage)

def create_user():
    username = input('Create Username: ')
    password = input('Create Password: ')
    user_info = load_user()
    user_info[username] = password
    save_user(user_info)22
    print('Welcome')
    login_user()
    
    # This function prompts the user to create their own user by entering their desired username and password.    
    
def login_user():
    global logged_in_user
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    user_info = load_user()
    if username in user_info and user_info[username] == password:
        print('Login Successful, Welcome')
        logged_in_user = username
        main_menu()
    else:
        print('Login Failed, Try Again')
        
def logout_user():
    global logged_in_user
    logged_in_user = None
    print('Logged Out')
    # This function logs the user out and sends them to the login screen.
        
def add_task(): 
    print('Add task Function')
    #This function is used to add the task.
    
def created_task_info():
    input('Enter Task Information: ')
    # This function is used to enter created tasks information.
        
def view_all_tasks():
    print('View all tasks Function')
    # This function is used to view all the tasks created.
    
def completed_tasts():
    print('Mark a task as complete Function')
    # This function is used to mark a task as complete.
    
def delete_task():
    print('Delete a task Function')
    # This function is used to delete tasks and send them to the ARCHIVED function

    
def help_controls():
    print('Add decription of how to display and navigate menus create/del tasks')
    # This function will show the user how to use the application
    
def archived_tasks():
    print('Archived tasks Function')
    # This function is used to view all the archived tasks and allow the user to un archive.

def logout_application():
    print('Logging out of user')
    exit()   
    # This function logs the user out and sends them to the login screen.

def main_menu():

        options = {
            '1': add_task,
            '2': view_all_tasks,
            '3': completed_tasts,
            '4': delete_task,
            '5': help_controls,
            '6': archived_tasks,
            '7': logout_application 
        }
    
        while True:
            print('Welcome to To Do List')
            print('1. Add a tasks')
            print('2. View all tasks')
            print('3. Completed tasks')
            print('4. Delete tasks')
            print('5. Help and Controls')
            print('6. Archived tasks')
            print('7. Logout of application')
            choice = input('Enter Menu number: ')
            
            if choice in options:
                options[choice]()
            else:
                print('Please enter a valid menu number')
        
main_menu()
            
    # I created this dictionary to hold the options for the main menu, i went with
    # a dictionary because it is easier to read and understand, and also allows the application
    # to be more modular if i feel asif i need to add or remove anything.
    # I used a while loop to keep the menu open until the user chooses to log out.
            
 
