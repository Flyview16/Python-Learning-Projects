import tkinter

# Creating a window
window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)


# Creating a label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack()






# Keep Screen on
window.mainloop()