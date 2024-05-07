from tkinter import *


def button_clicked():
    my_label["text"] = user_input.get()


# Creating a window
window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)


# Creating a label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.pack()

# Taking input using entry component
user_input = Entry()
user_input.pack()

# Creating a button
button = Button(text="Change label", command=button_clicked)
button.pack()

# Keep Screen on
window.mainloop()
