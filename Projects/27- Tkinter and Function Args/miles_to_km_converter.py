from tkinter import *

# Create window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)

# Labels
miles = Label(text="Miles")
km = Label(text="Km")
equals = Label(text="=")

# Placement on screen
miles.grid(column=0, row=0)
km.grid(column=0, row=2)
equals.grid(column=1, row=1)

# Input boxes
in_km = Entry()
in_miles = Entry()
in_km.grid(column=1, row=0)
in_miles.grid(column=1, row=2)

# Calculate button
calculate = Button(text="Calculate")
calculate.grid(column=1, row=3)

window.mainloop()