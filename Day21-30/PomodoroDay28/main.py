from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps=0
check_mark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
       global check_mark
       check_mark=""
       window.after_cancel(timer)
       canvas.itemconfig(timer_txt,text ="00:00")
       timer_label.config(text="Timer")
       global reps
       reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
       global reps
       global check_mark 
       
       reps+=1
       work_sec = WORK_MIN*60
       short_break_sec = SHORT_BREAK_MIN*60
       long_break_sec = LONG_BREAK_MIN*60  
       if reps%8==0:
              count_down(long_break_sec)
              timer_label.config(text="Long break" ,fg=RED)
              
       elif reps%2==0:
              count_down(short_break_sec)
              timer_label.config(text="Short break" ,fg=PINK)
       else:
              count_down(work_sec)
              timer_label.config(text="Work" , fg=GREEN)
              check_mark+="✔️"
              check_label.config(text=check_mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count=70):
       min = int(count/60)
       sec = int(count%60)
       if(min<=9):
        min = f"0{min}"
       if(sec<=9):
              sec = f"0{sec}"
       canvas.itemconfig(timer_txt ,text=f"{min}:{sec}")
       if count>0:
         global timer
         timer= window.after(1000,count_down,count-1)
       else :
        start_timer()
              


       
# ---------------------------- UI SETUP ------------------------------- #

window  = Tk()
window.title("Pomodoro")

window.config(padx=100,pady=50 ,bg=YELLOW,highlightthickness=0,border=0)







canvas = Canvas(width=200 , height=224 , bg=YELLOW)
tomato_img = PhotoImage(file="PomodoroDay28/tomato.png")
canvas.create_image(102,112,image=tomato_img)
timer_txt = canvas.create_text(103,130,text="00:00" , fill="white" , font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

timer_label = Label(text="Timer" , font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)


start_btn = Button(text="Start" , font=(FONT_NAME,12,"bold"),padx=5,pady=5 , command=start_timer)
start_btn.grid(row=2,column=0)

check_label = Label(text=check_mark,fg=GREEN,bg=YELLOW)
check_label.grid(row=2,column=1)


reset_btn = Button(text="Reset" , font=(FONT_NAME,12,"bold"),padx=5,pady=5 , command=reset)
reset_btn.grid(row=2,column=2)











window.mainloop()



