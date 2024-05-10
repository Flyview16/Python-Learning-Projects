from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle


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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_user_info():
    website_name = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()

    if website_name == "" or user_email == "" or user_password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any field(s) empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"These are the details of entered:\nEmail:{user_email}\n"
                                               f"Password:{user_password}\nIs it okay to save?")

        if is_ok:
            # write data to file, open in append mode
            with open(file="data.txt", mode="a") as file:
                file.write(f"{website_name} | {user_email} | {user_password}\n")
                # Clear Text from entry box
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


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
website_entry = Entry(width=52)
email_entry = Entry(width=52)
password_entry = Entry(width=33)

website_entry.focus()

website_entry.grid(column=1, row=1, columnspan=2)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
password_generator = Button(text="Generate Password",command=generate_password)
add_button = Button(text="Add", width=44, command=save_user_info)

password_generator.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
