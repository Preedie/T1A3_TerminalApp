def create_user(database):
    database = open('user-database.txt','r') 
    # Database will link to the user-database.txt file and will allow the user to write login information to it. (creating their account and saving it for future sessions to login to)
    username = input('Create Username: ') 
    # This is where the username that is entered/created will be input.
    password = input('Create Password: ')
    # This is where the password that is entered/created will be input.
    password_confirmation = input('Confirm Password: ')
    # This will prompt the user to confirm their password to ensure they match.
    username_store = []
    # This will store the username input, into a list
    password_store = []
    # This will store the password input, into a list
    for  i in database:
        a, b = i.split(',')
        b = b.strip()
        username_store.append(a)
        password_store.append(b)
    data = dict(zip(username_store, password_store))
    # the data variable was made so i could print the usernames and passwords in dict form, it is 
    # slightly reduntant as the usernames and passwords are being stored
    # implicitly due to them being stored in a seperate txt file however i found it easier to call 
    # the list in dict form so i could read/see what was happening to ensure it was what i wanted.
    
    
    # The for loop used here will take the username and password strip them of their white space
    # and store them into a (list) in a seperate txt file.
    # This will allow the user to input their username and password into the dictionary.
        
        
    if password!= password_confirmation:
        print('Passwords do not match, try again')
        create_user(database)
    else:
        if len(password) <= 7:
            print('Password must be at least 7 characters')
            create_user(database)
        elif username in username_store:
            print('Username already exists, try again')
            create_user(database)
        else:
            database = open('user-database.txt','a')
            database.write(username + ',' + password + '\n')
            print(f'Welcome {username}, enjoy.')
    
def login_user(database):
    username = input('Enter Username: ') 
    password = input('Enter Password: ')
    
    if not username or not password:
        print('Username or Password cannot be empty')
        return login_user(database)
    
    for line in database:
        uname, pwd = line.strip().split(',')
        if username == uname and password == pwd:
            print('Login successful')
            print('Hi,', username)
            return
    print('Login failed: Username or Password incorrect')
    

def home(database):
    option = input('Login | Signup: ')
    if option == 'Login':
        login_user(database)
    elif option == 'Signup':
        create_user(database)
    else:
        print('Please enter an option')
      
        





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


def main_menu():

    options = {
    '1': add_task,
    '2': view_all_tasks,
    '3': completed_tasts,
    '4': delete_task,
    '5': help_controls,
    '6': archived_tasks, 
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
    
def main():
    with open('user-database.txt', 'r') as file:
        home(file)

if __name__ == "__main__":
    main()  

main_menu() 
        
        