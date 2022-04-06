from tkinter import *
import time
import beepy

# ---- Constants ----
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---- Globals ----
reps = 0
timer_on = False
timer = None
pomodoros = 0


# ---- Timer reset ----
def timer_reset():
    global timer
    global timer_on
    global pomodoros
    global reps

    window.after_cancel(timer)
    title_label.config(text="Timer\n", fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    check.config(text='')
    pomodoros = 0
    reps = 0
    timer_on = False
    pass


# ---- Timer mechanism ----
def timer_start():
    global reps
    global timer_on
    global pomodoros

    if not timer_on:
        reps += 1
        if reps % 8 == 0:
            count_down(LONG_BREAK_MIN * 60)
            # count_down(10)
            title_label.config(text='Loooong\nbreak', fg=RED)
            check.config(text=(pomodoros*'☑︎'))
        elif reps % 2 == 0:
            count_down(SHORT_BREAK_MIN * 60)
            # count_down(1)
            title_label.config(text='Short\nbreak', fg=PINK)
            check.config(text=(pomodoros*'☑︎'))
        else:
            if pomodoros < 4:
                pomodoros += 1
            else:
                pomodoros = 0
                check.config(text=(pomodoros * '☑︎'))
            count_down(WORK_MIN * 60)
            # count_down(5)
            title_label.config(text=('Time to \nwork' + pomodoros * '!'), fg=GREEN)
        window.focus_force()
        beepy.beep(sound=1)

        timer_on = True


# ---- Countdown mechanism ----
def count_down(count):
    global timer
    global timer_on

    canvas.itemconfig(timer_text, text=time.strftime('%M:%S', time.gmtime(count)))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_on = False
        timer_start()


# ---- UI setup ----

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

check = Label(text='')
check.config(font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text='00:00', fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer\n")
title_label.config(font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", command=timer_start, font=(FONT_NAME, 15, "bold"),
                      bg=YELLOW, fg=RED, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=timer_reset, font=(FONT_NAME, 15, "bold"),
                      bg=YELLOW, fg=RED, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2, columnspan=2) # expand to 2 columns


mainloop()
