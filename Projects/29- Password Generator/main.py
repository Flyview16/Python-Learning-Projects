from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    # Automatically copy password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_user_info():
    website_name = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()
    user_data = {website_name: {
        "email": user_email,
        "password": user_password
    }}

    if website_name == "" or user_email == "" or user_password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any field(s) empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"These are the details of entered:\nEmail: {user_email}\n"
                                               f"Password: {user_password}\nIs it okay to save?")
        if is_ok:
            # Saving data to json file
            try:
                with open(file="data.json", mode="r") as file:
                    # Read old data
                    data = json.load(file)
            except FileNotFoundError:
                with open(file="data.json", mode="w") as file:
                    json.dump(user_data, file, indent=4)
            else:
                # Update old data with new
                data.update(user_data)
                with open(file="data.json", mode="w") as file:
                    # Saving update data
                    json.dump(data, file, indent=4)
            finally:
                # Clear Text from entry box
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website_name = website_entry.get()
    try:
        with open(file="data.json", mode="r") as file:
            # Read data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name,
                                message=f"Email/Username: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_name} found.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas for logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
email_username = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(column=0, row=1)
email_username.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Text input fields
website_entry = Entry(width=33)
email_entry = Entry(width=52)
email_entry.insert(0, "herbert@gmail.com")
password_entry = Entry(width=33)

website_entry.focus()

website_entry.grid(column=1, row=1)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
password_generator = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=44, command=save_user_info)
search_button = Button(text="Search", width=14, command=find_password)

password_generator.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1)

window.mainloop()
