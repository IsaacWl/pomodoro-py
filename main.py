from tkinter import *
import os
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
PATH = os.path.dirname(os.path.realpath(__file__))
reps = 0
time = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, time
    window.after_cancel(time)
    canvas.itemconfig(timer, text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    timer_session = 0

    if reps % 2 == 0:
        timer_session = SHORT_BREAK_MIN * 60
        title.config(text="Break", fg=PINK)
    if reps % 8 == 0:
        timer_session = LONG_BREAK_MIN * 60
        title.config(text="Break", fg=RED)
    if reps % 2 == 1:
        timer_session = WORK_MIN * 60
        title.config(text="Work", fg=GREEN)

    counter(timer_session)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def counter(count):
    global time
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        time = window.after(1000, counter, count - 1)
    else:
        start_timer()
        checks = ""

        for _ in range(math.floor(reps/2)):
            checks += "✔️"

        check_marks.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file=f"{PATH}/tomato.png")


canvas.create_image(100, 112, image=tomato_image)

timer = canvas.create_text(100, 130, text="00:00", fill="#eeeeee",
                           font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)

window.mainloop()
