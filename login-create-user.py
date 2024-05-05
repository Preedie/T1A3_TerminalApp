def create_user():
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
        create_user()
    else:
        if len(password) <= 7:
            print('Password must be at least 7 characters')
            create_user()
        elif username in username_store:
            print('Username already exists, try again')
            create_user()
        else:
            database = open('user-database.txt','a')
            database.write(username + ',' + password + '\n')
            print(f'Welcome {username}, enjoy.')

create_user()
    
def login_user():
    username = input('Enter Username: ') 
    password = input('Enter Password: ')
    
    if not len(username or password)<1:
        username_store = []
        password_store = []
        for  i in database:
            a, b = i.split(',')
            b = b.strip()
            username_store.append(a)
            password_store.append(b)
        data = dict(zip(username_store, password_store))
    
        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print('Login successful')
                        print('Hi, ', username)
                    else:
                        print('Login failed Username or Password incorrect')
                except:
                    print('Login failed Username or Password incorrect')
            else:
                    print('Username doesnt Exist')
        except:
            print('Login Error')

def home(option=None):
    option = input('Login | Signup: ')
    if option == 'login':
        login_user()
    elif:
        option == 'Signup'
        create_user()
    else:
        print('Please enter an option')
home()       
        
        
        
        