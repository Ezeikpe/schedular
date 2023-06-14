APP VERSION

In this app, I first import the necessary modules and create a new Flask application instance. We also initialize an empty list called `todo_items` to store our Schedular items.

Next, I define two routes:

- `/`: This route will render the index page with the list of to-do items. We pass the `todo_items` list to the template using the `render_template` function.

- `/add`: This route will be called when the user submits a new to-do item using the form on the index page. We get the new item from the form data using `request.form['item']`, add it to the `todo_items` list, and then redirect the user back to the index page.

- `/delete/<int:index>`: This route will be called when the user clicks the "delete" button next to a to-do item on the index page. We get the index of the item to delete from the URL using the `<int:index>` parameter, delete it from the `todo_items` list using `del`, and then redirect the user back to the index page.

Finally, we start the Flask application using `app.run()`.

To render the HTML templates, I create a folder named `templates` in the same directory as the `app.py` file and create an `index.html` file in the `templates` folder.

With this code, you can run the Flask application and navigate to `http://localhost:5000` in your web browser to use the to-do list web application. You can add new items to the list, mark items as completed, and remove completed items from the list.




WINDOW VERSION

**Steps to develop To-do List Project**
Import the Tkinter library
Create to-do list application window
Create application layout
Define to do list functions
1. Import the Tkinter library
#importing packages 
from  tkinter import * 
import tkinter.messagebox
Explanation

In the first line, we are importing Tkinter which is basically a standard GUI library in Python and every possible object of it.
In the second line, we are importing an important widget from the Tkinter library called the message box which is used to display messages in a python to-do list project.
2. Create To-do list application window
window=Tk()
#giving a title
window.title("DataFlair Python To-Do List APP")
window.mainloop()
Explanation

Tk() is a top-level widget which is used to create the main application window in which we will be building python to-do list application.
The title() method is used to give a name to our application which is basically displayed at the top.
The mainloop() method basically runs the Tkinter event loop, it runs and displays everything we have written in our code.
3. Create application layout
4. Explanation

Frame() method is basically a container widget within our main window and it is used to hold different widgets. It takes an argument that is our main window.
pack() method is a geometry manager which organizes the widget properly before placing it in the main window in a level order fashion until explicitly mentioned.
Listbox() widget is going to store all the tasks that we list in python to-do list application. We have given three arguments out of which the first one is where we want our widgets to be placed. If the height and width is not given, it takes the default value. Also it would take the default value as window, if the frame_task is not explicitly mentioned.
Scrollbar() widget is used to place a scroll bar in case the total number of lists exceeds the given dimension of the to-do list window. Like every other widget it takes an argument as to where it should be placed. We pack it to the RIGHT of the frame_task widget then we set it on the listbox_task widget and after that we configure it on the vertical axis given by the command listbox_task.yview.
Button() widget is used to create a button. We want the buttons in our main to-do list window so the input window is given. Then the text which will be displayed on the button is specified and at last in the command input a function is given which will be called when the button is clicked.
