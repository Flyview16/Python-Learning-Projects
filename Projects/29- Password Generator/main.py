from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_user_info():
    website_name = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()

    # write data to file, open in append mode
    with open(file="data.txt", mode="a") as file:
        file.write(f"{website_name} | {user_email} | {user_password}")

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
website = Label(text="Website:")
email_username = Label(text="Email/Username:")
password = Label(text="Password:")

website.grid(column=0, row=1)
email_username.grid(column=0, row=2)
password.grid(column=0, row=3)

# Text input fields
website_entry = Entry(width=52)
email_entry = Entry(width=52)
password_entry = Entry(width=33)

website_entry.focus()

website_entry.grid(column=1, row=1, columnspan=2)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
password_generator = Button(text="Generate Password")
add_button = Button(text="Add", width=44, command=save_user_info)

password_generator.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
