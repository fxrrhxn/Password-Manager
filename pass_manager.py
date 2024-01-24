from tkinter import *
from tkinter import messagebox
import pass_generator, view_pass

def generate():
    # Function to generate a password using pass_generator module
    password_box.delete(0, END)
    generated_password = pass_generator.generate_password()
    password_box.insert(0, generated_password)

def save():
    # Function to save the entered username and password to 'passwords.txt'
    username = username_box.get()
    password = password_box.get()

    if username and password:

        with open('passwords.txt', 'a') as file:
            file.write(f"Username: '{username}' | Password: '{password}'\n")

        messagebox.showinfo(title="Successful", message="Password Saved Successfully!")
        username_box.delete(0, END)
        password_box.delete(0, END)

    elif password and not username:
        messagebox.showwarning(title="No details found.", message='Username cannot be empty!')

    elif username and not password:
        messagebox.showwarning(title="No details found.", message='Password cannot be empty!')

    else:
        messagebox.showwarning(title="No details found.", message='Username & Password cannot be empty!')

def view():
    # Function to view saved passwords using the view_pass module
    view_pass.passwords_screen()

window = Tk()

# Main window and its attributes:
window.geometry('800x650')
window.configure(background='white')
window.title("Password Manager & Generator")

# Set window icon:
icon = PhotoImage(file='pass_icon.png')
window.iconphoto(True, icon)
app_icon = PhotoImage(file='app_icon.png')

# Icon label:
icon_label = Label(window,
                   image=app_icon,
                   bg='white')
icon_label.place(x=325, y=30)

# Welcome text, title:
title_label = Label(window,
                    text="Password Manager\nand Generator",
                    font=("SF Pro", 25, 'bold'),
                    bg='white',
                    fg='#1D1D1D')
title_label.place(x=282, y=165)

# Attribution label:
attribution_label = Label(window,
                          text='Designed by Farhan Bhat',
                          font=('SF Pro', 10),
                          bg='white',
                          fg='#1D1D1D')
attribution_label.place(x=325, y=620)

# Username prompt label:
username_label = Label(window,
                       text="Enter Your Username",
                       font=('SF Pro', 15, 'bold'),
                       borderwidth=3,
                       bg='white',
                       fg='#1D1D1D',
                       relief='solid',
                       bd=3,
                       padx=10,
                       pady=5)
username_label.place(x=300, y=250)

# Username entry box:
username_box = Entry(window,
                     background='#bec2bf',
                     fg='#1D1D1D',
                     bg='white',
                     borderwidth=3,
                     relief='solid',
                     bd=0.5,
                     font=("SF Pro", 13, 'bold'))
username_box.place(x=296, y=295)

# Password prompt label:
password_label = Label(window,
                       text="Enter Your Password or Generate a Strong One",
                       font=('SF Pro', 15, 'bold'),
                       borderwidth=3,
                       bg='white',
                       fg='#1D1D1D',
                       relief='solid',
                       padx=10,
                       pady=5)
password_label.place(x=215, y=350)

# Password entry/generation box:
password_box = Entry(window,
                     background='#bec2bf',
                     fg='#1D1D1D',
                     bg='white',
                     borderwidth=3,
                     relief='solid',
                     bd=0.5,
                     font=("SF Pro", 13, 'bold'))
password_box.place(x=296, y=395)

# Password generation button:
generate_button = Button(window,
                         text="Generate Password",
                         font=('SF Pro', 15, 'bold'),
                         fg='#1D1D1D',
                         bg='#F7D302',
                         relief='solid',
                         borderwidth=2,
                         command=generate)
generate_button.place(x=300, y=430)

# Save button:
save_button = Button(window,
                     text="Save Password",
                     font=('SF Pro', 15, 'bold'),
                     fg='#1D1D1D',
                     bg='#6CB505',
                     relief='solid',
                     borderwidth=2,
                     activeforeground='#1D1D1D',
                     activebackground='#6CB505',
                     command=save)
save_button.place(x=320, y=475)

# View passwords button:
view_button = Button(window,
                     text="View Passwords",
                     font=('SF Pro', 15, 'bold'),
                     bg='white',
                     fg='#1D1D1D',
                     padx=10,
                     pady=5,
                     command=view)
view_button.place(x=304, y=535)

window.mainloop()
