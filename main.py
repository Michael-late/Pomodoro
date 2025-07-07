from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(REPS):
    count_down(6,REPS)

def short_break(REPS):
    count_down(3,REPS)

def long_break(REPS):
    count_down(5, REPS)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count, REPS):
    if count == 0 and REPS < 5:
        checkmark.config(text="✓"*REPS)
        REPS += 1
        if REPS == 4:
            long_break(REPS)
        else:
            short_break(REPS)
            start_timer(REPS)

    count_min = floor(count / 60)
    count_second = count % 60
    if (count_second < 10):
        count_second = "0" + str(count_second)
    
    if (count_min < 10):
        count_min =  "0" + str(count_min)

    canvas.itemconfig(timer, text=f"{count_min}:{count_second}")
    if count > 0:
        window.after(1000, count_down, count-1, REPS)
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

TimerLabel = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
TimerLabel.grid(row=0,column=1)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="Pomodoro/tomato.png")
canvas.create_image(100, 112, image = img)
timer = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column= 1)

StartBTN = Button(text="Start", command=lambda: start_timer(REPS))
StartBTN.grid(row=2,column=0)

ResetBTN = Button(text="Reset")
ResetBTN.grid(row=2,column=2)

checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark.grid(row=3,column=1)

window.mainloop()