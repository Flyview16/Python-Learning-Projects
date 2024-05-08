import tkinter
from tkinter import *


# Calculate function
def converter():
    # Check which entry has focus
    focused_widget = window.focus_get()

    # If Miles has focus, calculate kilometers
    if focused_widget == in_miles:
        mile_value = in_miles.get()
        try:
            # If miles value is entered, calculate km
            miles = float(mile_value)
            km = miles * 1.609
            in_km.delete(0, END)
            in_km.insert(0, f"{km:.2f}")
        except ValueError:
            # Handle invalid input
            pass

    # If Km has focus, calculate miles
    elif focused_widget == in_km:
        kilo_value = in_km.get()
        try:
            # If kilometers value is entered, calculate miles
            kilometers = float(kilo_value)
            miles = kilometers / 1.609
            in_miles.delete(0, END)
            in_miles.insert(0, f"{miles:.2f}")
        except ValueError:
            # Handle invalid input
            pass


# Create window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(pady=50, padx=50)

# Labels
miles_label = Label(text="Miles")
km_label = Label(text="Km")
equals = Label(text="=")

# Placement on screen
miles_label.grid(column=0, row=0)
km_label.grid(column=0, row=2)
equals.grid(column=1, row=1)

# Input boxes
in_miles = Entry()
in_km = Entry()
in_km.grid(column=1, row=2)
in_miles.grid(column=1, row=0)

# Calculate button
calculate = Button(text="Calculate", command=converter)
calculate.grid(column=1, row=3)

window.mainloop()
