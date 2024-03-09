from tkinter import *
def buttons():
    # Create five buttons
    button1 = Button(root, text="Customer")
    button2 = Button(root, text="Employee")
    button3 = Button(root, text="Order")
    button4 = Button(root, text="Feedback")
    button5 = Button(root, text="Menu")
    # Pack the buttons horizontally
    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack(side=LEFT)
    button4.pack(side=LEFT)
    button5.pack(side=LEFT)
def create_login_frame():
    # Create labels and entry widgets for username and password
    Label(root, text="Username : ",width=50 , height=2).grid(row=1, column=1)
    username_entry = Entry(root)
    username_entry.grid(row=1, column=2)

    Label(root, text="Password : ",width=50 , height=2).grid(row=2, column=1)
    password_entry = Entry(root, show="*")  # Use show="*" to mask the password
    password_entry.grid(row=2, column=2)

    # Create checkbuttons
    admin_var = IntVar()
    admin_checkbutton = Checkbutton(root, text="Admin",width=50 ,variable=admin_var)
    admin_checkbutton.grid(row=3, column=1)

    user_var = IntVar()
    user_checkbutton = Checkbutton(root, text="User",width=50 , variable=user_var)
    user_checkbutton.grid(row=3, column=2)

    # Function to handle checkbutton selections
    def handle_checkbuttons():
        if admin_var.get() == 1:
            user_checkbutton.deselect()  # Uncheck User checkbutton if Admin is selected
        elif user_var.get() == 1:
            admin_checkbutton.deselect()  # Uncheck Admin checkbutton if User is selected

    # Bind checkbutton selection to the handle_checkbuttons function
    admin_checkbutton.config(command=handle_checkbuttons)
    user_checkbutton.config(command=handle_checkbuttons)

    # Function to handle login
    def login():
        if username_entry.get() == "mohan" and password_entry.get() == "2134":
            print("Login was sucessfull")  # Navigate to root if login is successful
        else:
            print("Invalid credentials")

    # Create login button
    login_button = Button(root, text="Login",width=50 , height=2, command=login)
    login_button.grid(row=4, column=2)
root = Tk()
root.title("Restaurant database")
root.geometry("1500x1080")
buttons()
create_login_frame()
root.mainloop()
