from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        canvas.after(1000, count_down, count - 1)  # Call count down funct after every 1s


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create canvas to set image as background
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Read file to extract image
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))  # Place text on tomato image
canvas.grid(column=1, row=1)
count_down(5)

# Labels
timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
check = Label(text="🗸", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25))
timer.grid(column=1, row=0)
check.grid(column=1, row=3)

# Buttons
start = Button(text="Start")
reset = Button(text="Reset")
start.grid(column=0, row=2)
reset.grid(column=2, row=2)

window.mainloop()
