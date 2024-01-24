# Password Viewer for GUI Password Manager
from tkinter import *
from tkinter import messagebox
import sys

def passwords_screen():
    # Create a new Tkinter window
    screen = Tk()

    # Set window size and background color
    screen.geometry('800x650')
    screen.configure(background='white')
    screen.title("Saved Passwords")

    # Title label for the saved passwords screen
    title_label = Label(screen,
                        text="Your saved Passwords are:",
                        font=("SF Pro", 25, 'bold'),
                        bg='white',
                        fg='#1D1D1D')
    title_label.place(relx=0.5, y=95, anchor=CENTER)

    # Attribution label for the designer
    attribution_label = Label(screen,
                            text='Designed by Farhan Bhat',
                            font=('SF Pro', 10),
                            bg='white',
                            fg='#1D1D1D')
    attribution_label.place(x=325, y=620)

    # Read the passwords from 'passwords.txt'
    with open('passwords.txt', 'r') as file:
        passwords = file.readlines()

        # Check if there are any saved passwords
        if passwords:
            num_passwords = len(passwords)
            max_password_length = max(len(password.strip()) for password in passwords)

            # Determine the height and width for the Text widget dynamically
            dynamic_height = min(25, num_passwords)
            dynamic_width = max(50, max_password_length +5)

            # Create a Text widget to display passwords
            password_text = Text(screen,
                                 font=('SF Pro', 12, 'bold'),
                                 bg='white',
                                 fg='black',
                                 height=dynamic_height,
                                 width=dynamic_width)
            password_text.insert(END, '\n'.join(f"{index}. {line.strip()}" for index, line in enumerate(passwords, start=1)))
            
            # Disable the ability to edit the Text widget
            password_text.configure(state='disabled')
            
            # Place the Text widget in the center of the screen
            password_text.place(relx=0.5, rely=0.5, anchor=CENTER)

        else:
            # Show a warning message if there are no saved passwords and exit the program
            messagebox.showwarning(title='Empty!',
                                   message='There are no saved passwords currently!')
            sys.exit()

    # Start the Tkinter main loop
    screen.mainloop()

# Run the passwords_screen function if this script is executed directly
if __name__ == '__main__':
    passwords_screen()