from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_SEC = 25*60          # Simulated 25 min
SHORT_BREAK_SEC = 5*60   # Simulated 5 min
LONG_BREAK_SEC = 20*20    # Simulated 20 min

def setup_timer_logic():
    sets = [0]  # Mutable container to keep track of state

    def start_timer():
        if sets[0] < 3:
            count_down(WORK_SEC, short_break)
        elif sets[0] == 3:
            count_down(WORK_SEC, long_break)
        else:
            canvas.itemconfig(timer, text="DONE")
            checkmark.config(text="✔️✔️✔️✔️")

    def short_break():
        sets[0] += 1
        checkmark.config(text="✔️" * sets[0])
        count_down(SHORT_BREAK_SEC, start_timer)

    def long_break():
        sets[0] += 1
        checkmark.config(text="✔️" * sets[0])
        count_down(LONG_BREAK_SEC)

    StartBTN.config(command=start_timer)

    def reset():
        sets[0] = 0
        canvas.itemconfig(timer, text="00:00")
        checkmark.config(text="")

    ResetBTN.config(command=reset)

    return start_timer

# ---------------------------- COUNTDOWN ------------------------------- #
def count_down(count, callback=None):
    count_min = floor(count / 60)
    count_sec = count % 60
    time_str = f"{count_min:02d}:{count_sec:02d}"
    canvas.itemconfig(timer, text=time_str)

    if count > 0:
        window.after(1000, count_down, count - 1, callback)
    elif callback:
        callback()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

TimerLabel = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
TimerLabel.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="Pomodoro/tomato.png")
canvas.create_image(100, 112, image=img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

StartBTN = Button(text="Start")
StartBTN.grid(row=2, column=0)

ResetBTN = Button(text="Reset")
ResetBTN.grid(row=2, column=2)

checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark.grid(row=3, column=1)

# Hook up logic
setup_timer_logic()

window.mainloop()
