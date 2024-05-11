# To Do List 

The application i chose to make was a simple to do list running in the python terminal, it will allow the creating of tasks to then complete features can be found below.

# Features:

## Home

The home feature is a simple menu select space that remains open while the user decides exactly they would like to select (Create user, Login to existing user, view the help and controls txt file or exit the application entirely)

### Specific features:

1. Login.
2. Signup (create user).
3. Help and controls.
4. Exit.

## Create User/Login User

The create feature allows the user to create a unique user that will be saved to a database that holds all user created. Following that the user created since its saved will now be accessible via logging in. These features allow the user information and data entered to be stored for later sessions, for example if you make a task on user1 username to be completed that task will be saved to user1 and only accessible to user1, if a user2 is made they will have their information stored under user2, so on so forth.

### Specific features:

1. Create unique user from username/password inputs.
2. Save username/password made by user to user database.
3. Store any information made within the application on specific user to unique user created txt file.


## Main Navigation Menu

This area of the application is simply going to be a navigation hub that accepts inputs from the user to enter different areas of the application as entered by the user, eg typing 1 and pressing enter will place the user in the add task function which will then allow them to access the features of that function, below is more information.

### Specific features:
1. Add task (for logged in user)
2. View tasks made (for logged in user)
3. Complete tasks (for logged in user)
4. Delete tasks (for logged in user)
5. Help and controls (Read only txt file for all users)
6. logout to home (for logged in user)

## Add Task

This function will take the information entered by the logged in user write it then store it in that users database.

### Specific features:

1. Task title
2. Task information (the information stored eg title = shopping list. Task info = eggs - milk - etc.)
3. Task priority (High, medium or low importance)
I added this field with the intention of creating a search and filter functionality to sort tasks by importance and date, however i ran out of time. Regardless i left it in as creating the search functionality later is still viable.
4. Task importance is simply adding a ! to a task of "High" priority, once again this was for easy filtering.
5. Task due date will allow the user to input a date that the task needs to be completed by hence the name. however this can be skipped.

## View All Tasks

View all tasks has no true functionality within it as it is simply to view the tasks made and all the info within them. Although it will allow the view task menu to show until the input of 0 exit or enter is input by the logged in user.

## Complete Tasks

Complete tasks will allow the logged in user view completed and non completed tasks as well as complete and un complete tasks within the menu.
Then once again will allow the user to return to main menu.

## Delete Tasks

Delete tasks will allow the user to completely delete a task created through inputs. There is however no way to re create tasks deleted (an archive).

## Help and Controls

A simple txt doc that will show in the terminal when the user decides to show it, the user will not need to login to view this file. 
The file will also not allow writing to it unless of course its modified at a root folder level.

## Logout of Application 

A simple logout function for the user to input to allow them to be taken back to the HOME page to either login/signup or exit the application entirely.

# Github Link

[To-do list Application in Github](https://github.com/Preedie/T1A3_TerminalApp.git)

# Trelloboard

## Implementation:

I used trelloboard to not only track the tasks i needed to complete but also sort them the way i would like to complete them, i did however realise that due to the way i was writing my code and its modularity that the order of tasks was less important once i had the main menu and selectors within the main menu complete as the way it was designed allowed me to add/remove and adjust alot of the programs functionality without breaking code. I did however stick to the below screenshots mostly with the only deviations from the screen shots being when i went back to patch/change some code already completed as i didn't like the way it functioned logically.

The below screenshots including the submenus within the main tasks are sorted in the order and the day they were done. The main tasks are above the sub menu screenshots simply for layout and design, not to convey any day by day procedure.

### Screenshots of progress

# Day 1/3:

![Day 1](./TrelloboardPics/Trelloboard1.png)

![Day 1](./TrelloboardPics/Trelloboard2%20Login-Create.png)

![Day 2](./TrelloboardPics/Trelloboard3%20mainmenu-selection.png)

![Day 3](./TrelloboardPics/Trelloboard4.png)

## Day 1/3 Done:

# Day 4/7

![Day 4](./TrelloboardPics/Trelloboard5.png)

![Day 4](./TrelloboardPics/Trelloboard6.png)

![Day 4](./TrelloboardPics/Trelloboard7.png)

![Day 5](./TrelloboardPics/Trelloboard8.png)

![Day 6](./TrelloboardPics/Trelloboard9.png) 

## Dat 4/7 Done:

# Day 8:

![Day 8](./TrelloboardPics/Trelloboard10.png)

## Day 8 done:

# Trello Sub Menu Tasks:

![Sub Menu Trello Screenshot](./TrelloboardPics/Trellosubmenu1.png)

![Sub Menu Trello Screenshot](./TrelloboardPics/Trellosubmenu2.png)

![Sub Menu Trello Screenshot](./TrelloboardPics/Trellosubmenu3.png)

![Sub Menu Trello Screenshot](./TrelloboardPics/Trellosubmenu4.png)

![Sub Menu Trello Screenshot](./TrelloboardPics/Trellosubmenu5.png)

# Installation

To run the application follow these steps.

1. Make sure you have pyinstaller first by pasting this code into ubuntu.
~~~ 
pip install pyinstaller
~~~
2. Once pyinstaller is installed, using ubuntu navigated to where the Python file you want to run is located (the directory of the script)

