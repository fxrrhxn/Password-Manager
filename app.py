# Password Manager GUI
import tkinter as tk, sys
from tkinter import ttk, messagebox
import ttkbootstrap as ttk
import pass_generator

access_key = "12345"

# main screen
window = ttk.Window(themename='cyborg')

# configuring the height and width of the window
window.configure(height=600, width=800)

# setting the minimum and maximum height of the window
window.minsize(height=600, width=800)
window.maxsize(height=600, width=800)

# setting the title of the window
window.title("Password Manager")

# creating a photo image for the window icon:
iconPhoto = tk.PhotoImage(name='App Icon', file='pass_icon.png')

# setting the app icon
window.iconphoto(True, iconPhoto)

# configuring the rows and columns for the grid:

# columns:
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_columnconfigure(4, weight=1)
window.grid_columnconfigure(5, weight=1)
window.grid_columnconfigure(6, weight=1)

# rows:
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)
window.grid_rowconfigure(6, weight=1)
window.grid_rowconfigure(7, weight=1)
window.grid_rowconfigure(8, weight=1)

# setting up the main interface:
main_frame = ttk.Frame(window)

# title label:
title_label = ttk.Label(main_frame, 
                        text='Password Manager', 
                        font=('Lota Grotesque', 30, 'bold'))
title_label.pack(side='top', expand=True)

# acces_key label:
access_key_label = ttk.Label(main_frame, 
                        text='Please enter your access key:', 
                        font=('Lota Grotesque', 12))
access_key_label.pack(side='top')

# access_key entry:
access_key_var = ttk.StringVar()
access_key_entry = ttk.Entry(main_frame, 
                             font=('Lota Grotesque', 14),
                             textvariable=access_key_var)
access_key_entry.pack(side='top', expand=True, fill='x')

# Incorrect pin label:
wrong_key_label = ttk.Label(main_frame, 
                           text="Please enter the correct access key!", 
                           foreground='red',
                           font=('Lota Grotesque', 12))

# functions:

# function to destroy the onscreen widgets on the initial page:
def destroy_login():
    title_label.pack_forget()
    access_key_label.pack_forget()
    access_key_entry.pack_forget()
    login.pack_forget()

# function to load the landing page:
def land():

    # setting up the landing page:

    # functions:

    # function to destroy the onscreen widgets on the functions page:
    def destroy_land():
        action_choice_label.pack_forget()
        add_pass_button.pack_forget()
        view_pass_button.pack_forget()
        exit_button.pack_forget()

    # function to load the password add ui:
    def add():

        # function to load the destroy_add and land functions into the button:
        def back_for_add():
            destroy_add()
            land()

        # function to destroy the elements in the add pass section:
        def destroy_add():
            username_label.pack_forget()
            username_box.pack_forget()
            password_label.pack_forget()
            password_box.pack_forget()
            generate_pass_button.pack_forget()
            website_label.pack_forget()
            website_title_box.pack_forget()
            clear_details_button.pack_forget()
            save_button.pack_forget()
            back_button.pack_forget()


        # calling the destroy_land() function to remove elements from the screen:
        destroy_land()

        # setting up the interface for the password add section:

        # text frames:
        username_frame = ttk.Frame(window)
        password_frame = ttk.Frame(window)
        save_frame = ttk.Frame(window)

        # username section:

        # username label:
        username_label = ttk.Label(username_frame, 
                                text='Enter your Username:', 
                                font=('Lota Grotesque', 12))
        username_label.pack(anchor='center', side='top', expand=True)

        # username entry box:
        username_var = ttk.StringVar()
        username_box = ttk.Entry(username_frame,
                                font=('Lota Grotesque', 14),
                                textvariable=username_var,)
        username_box.pack(anchor='center', fill='x', side='bottom')

        # placing the username elements:
        username_frame.grid(row= 2, column=2, columnspan=3, sticky='ns')

        # password section:

        # password label:
        password_label = ttk.Label(password_frame, 
                                text='Enter or Generate a Strong Password:', 
                                font=('Lota Grotesque', 12),
                                justify='center')
        password_label.pack(anchor='center', side='top', expand=True, fill='y')

        # password entry box:
        password_var = ttk.StringVar()
        password_box = ttk.Entry(password_frame,
                                font=('Lota Grotesque', 14),
                                textvariable=password_var)
        password_box.pack(anchor='center', fill='x', side='top')

        def generate_pass():

            # The password_box.delete can also be used, like this:
            # password_box.delete(first=0, last=-1)

            password_var.set('')
            generated_pass = pass_generator.generate_password()
            password_var.set(generated_pass)

        # generate password button:
        generate_pass_button = ttk.Button(password_frame,
                                        bootstyle='danger', 
                                        text= 'Generate Password', 
                                        command= generate_pass)
        generate_pass_button.pack(anchor='center', side='top', expand=True)

        # placing the password elements:
        password_frame.grid(row= 3, rowspan=2, column=2, columnspan=3, sticky='ns')

        # SAVE section:
        def save_pass():

            if username_var.get() and not password_var.get():
                messagebox.showerror(title="Details Missing", message="Please enter your details!", icon='warning')

            elif password_var.get() and not username_var.get():
                messagebox.showerror(title="Details Missing""Please enter your details!", message="Please enter your details!", icon='warning')

            elif username_var.get() and password_var.get() and not website_var.get():
                messagebox.showerror(title="Details Missing""Please enter your details!", message="Please enter your details!", icon='warning')

            elif website_var and not username_var.get() and not password_var.get():
                messagebox.showerror(title="Details Missing""Please enter your details!", message="Please enter your details!", icon='warning')

            elif not password_var.get() and not username_var.get() and not website_var.get():
                messagebox.showerror(title="Details Missing""Please enter your details!", message="Please enter your details!", icon='warning')

            else:
                with open('passwords.txt', 'a') as f:
                    entered_username = username_var.get()
                    entered_pass = password_var.get()
                    website_name = website_var.get()
                    f.writelines(f"Website: {website_name} | Username: {entered_username} | Password: {entered_pass}\n")

                messagebox.showinfo(title='Save Successful', message='Your Password was saved successfully!', icon='info')
                clear_details()

        # app/website title label:
        website_label = ttk.Label(save_frame, 
                                text='Enter Website:',
                                font=('Lota Grotesque', 12))
        website_label.pack(anchor='center', side='top', expand=True)

        # app/website title entry:
        website_var = ttk.StringVar()
        website_title_box = ttk.Entry(save_frame,
                                font=('Lota Grotesque', 14),
                                textvariable=website_var)
        website_title_box.pack(anchor='center', expand=True, fill='x', side='top')

        # save button:
        save_button = ttk.Button(save_frame, 
                                text='Save Password',
                                command=save_pass,
                                bootstyle='danger')
        save_button.pack(anchor='center', side='top', expand=True)

        # clear button & function:
        def clear_details():
            password_var.set('')
            username_var.set('')
            website_var.set('')

        # clear details button:
        clear_details_button = ttk.Button(save_frame, 
                                        text= 'Clear Details', 
                                        command= clear_details,
                                        bootstyle='dark')
        clear_details_button.pack(anchor='center', side='top', expand=True)

        # back button:
        back_button = ttk.Button(save_frame, 
                                 text="< Back",
                                 style='outline danger',
                                 command=back_for_add)
        back_button.pack(anchor='center', side='bottom', expand=True)

        # placing the save section elements:
        save_frame.grid(row= 5, rowspan=2, column=2, columnspan=3, sticky='ns')

    # function to load the view pass ui:
    def view():

        # function to load the destroy_view1() and land() functions into the button:
        def back_for_view1():
            destroy_view1()
            land()

        # function to load the destroy_view2() and land() functions into the button:
        def back_for_view2():
            destroy_view2()
            land()

        # function to destroy the elements in the view pass section if there are any passwords:
        def destroy_view1():
            label1.pack_forget()
            pass_box.pack_forget()
            back_button.grid_forget()


        # function to destroy the elements in the view pass section if there are no passwords:
        def destroy_view2():
            label2.grid_forget
            back_button.grid_forget()


        # calling the destroy_land() function to destroy the elements on the landing page:
        destroy_land()

        # setting up the main interface for the view pass section:

        # password reading and display section:
        with open('passwords.txt', 'r') as file:
            passwords = file.readlines()

            # check if there are any passwords in the file
            if passwords:

                # display the label if there are any passwords saved:
                # title Frame:
                intro_frame = ttk.Frame(window)

                # title label:
                label1 = ttk.Label(intro_frame,
                                text='Your saved passwords are:',
                                font=('Lota Grotesque', 20, 'bold'),
                                justify='center')
                label1.pack(expand=True, side='top')

                # placing the intro frame on the display
                intro_frame.grid(row=2, column=2, columnspan=3, sticky='ns')

                # get the number of passwords in the text file using the len() function
                num_passwords = len(passwords)

                # using list comprehension get the max length of any password in the file
                max_password_length = max(len(password.strip()) for password in passwords)

                # based on the above numbers, determine the height and width of the scrollable text box:
                dynamic_height = min(25, num_passwords)
                dynamic_width = max(50, max_password_length +5)

                # password frame:
                pass_frame = ttk.Frame(window)

                # pass box:
                pass_box = ttk.ScrolledText(pass_frame, 
                                            font=('Lota Grotesque', 12), 
                                            height=dynamic_height, 
                                            width=dynamic_width)
                
                # using a for loop, enumerate the passwords and insert them into the scrollable text bar
                for index, line in enumerate(passwords, start=1):
                    pass_box.insert(tk.END, f"{index}. {line.strip()}\n")

                # disable the ability to modify the scroll text bar:
                pass_box.configure(state='disabled')

                # place the pass box on the display:
                pass_box.pack(side='bottom')

                # placing the password box frame on the display:
                pass_frame.grid(row=4, column=1, columnspan=5, sticky='nsew')

                # back button:
                back_button = ttk.Button(window, 
                                        text="< Back",
                                        style='danger',
                                        command=back_for_view1)
                back_button.grid(row=5, column=2, columnspan=3)
            
            else:
                # label if there are no passwords in the file:
                label2 = ttk.Label(window,
                                text='There are no saved passwords currently. \nPlease add a password first.',
                                font=('Lota Grotesque', 20, 'bold'),
                                justify='center')
                label2.grid(row=4, column=2, columnspan=3, sticky='ns')

                # back button:
                back_button = ttk.Button(window, 
                                        text="< Back",
                                        style='danger',
                                        command=back_for_view2)
                back_button.grid(row=5, column=2, columnspan=3)

    # first label:
    action_choice_frame = ttk.Frame(window)
    action_choice_label = ttk.Label(action_choice_frame, 
                                    text="Please Choose an Action from the Following:", 
                                    font=('Lota Grotesque', 18, 'bold'),
                                    justify='center')
    action_choice_label.pack(expand=True, side='top')

    # packing the action choice frame:
    action_choice_frame.grid(row=3, column=2, columnspan=3, sticky='ns')

    # button frames:
    button_frame = ttk.Frame(window)
    exit_button_frame = ttk.Frame(window)

    # buttons:

    # button for adding a new password:
    add_pass_button = ttk.Button(button_frame, 
                                text="Add Password",
                                style='outline danger',
                                command=add)
    add_pass_button.pack(expand=True, fill='both', side='left')

    # button for viewing added passwords:
    view_pass_button = ttk.Button(button_frame, 
                                text="View Passwords",
                                style='outline danger',
                                command=view)
    view_pass_button.pack(expand=True, fill='both', side='left')

    # button for exiting the program:
    exit_button = ttk.Button(exit_button_frame, 
                                text="Quit",
                                bootstyle='danger', 
                                command= lambda: sys.exit())
    exit_button.pack(expand=True, side='bottom', fill='x')

    # packing the button frame:
    button_frame.grid(row=4, column=3, columnspan=1, sticky='nsew')
    exit_button_frame.grid(row=5, column=2, columnspan=3, sticky='ns')

# login button functions:
attempts = 0
def key_check():

    global wrong_key_label
    global attempts
    
    if access_key_var.get() == access_key:
        destroy_login()
        land()
    
    elif attempts < 3 and access_key_var.get()!= access_key:
        attempts += 1

        if attempts == 3:
            sys.exit(messagebox.showerror(title='Program Termination', message='You have exceeded the maximum number of attempts. The app will now terminate.', icon=messagebox.WARNING))

        else:
            wrong_key_label.pack(side='top', expand=True)
            if access_key_entry:
                access_key_entry.delete(0, 'end')

# keyboard binding function:
def key_check_keyboard(event):

    global wrong_key_label
    global attempts
    
    if access_key_var.get() == access_key:
        destroy_login()
        land()
    
    elif attempts < 3 and access_key_var.get()!= access_key:
        attempts += 1

        if attempts == 3:
            sys.exit(messagebox.showerror(title='Program Termination', message='You have exceeded the maximum number of attempts. The app will now terminate.', icon=messagebox.WARNING))

        else:
            wrong_key_label.pack(side='top', expand=True)
            if access_key_entry:
                access_key_entry.delete(0, 'end')

# login button:
login = ttk.Button(main_frame, 
                       text='Login',
                       bootstyle='danger',
                       command=key_check)
login.pack(side='bottom')

# access key entry bind functionality:
def remove_wrong_key_label(event):
    if wrong_key_label.winfo_ismapped():
        wrong_key_label.pack_forget()

# binding the function to the entry box for the access key:
access_key_entry.bind('<FocusIn>', remove_wrong_key_label)
access_key_entry.bind('<Return>', key_check_keyboard)

# placing the frame:
main_frame.grid(row=4, column=2, columnspan=3, sticky='ns')

# run the mainloop:
window.mainloop()