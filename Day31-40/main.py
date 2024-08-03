from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"


# ---------------Buttons Functions ---------------
my_df = pandas.read_csv('data/french_words.csv')
to_learn = my_df.to_dict(orient="records")
english_word=""


def next_card():
       global flip_timer
       window.after_cancel(flip_timer)
       current_card_data = random.choice(to_learn)
       french_word = current_card_data["French"]
       global english_word
       english_word = current_card_data["English"]
       
       canvas.itemconfig(title_text , text="French")
       canvas.itemconfig(french_text, text=french_word )
       flip_timer = window.after(3000 , flip_card)
      



def flip_card():
       canvas.itemconfig(title_text,text="English")
       canvas.itemconfig(french_text, text=english_word )
       
       















# ---------------Buttons Functions ---------------



window = Tk()
flip_timer = window.after(3000,func=flip_card)

window.title("Flashy")
window.config(width=900 , height=900 ,background=BACKGROUND_COLOR ,padx=50,pady=50)
 

canvas = Canvas(width=800,height=526)
front_card = PhotoImage(file="images/card_back.png")
canvas.create_image(400,263,image =front_card )
canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)
title_text = canvas.create_text(400,150,text="Title" , font=("Arial" , 40 , "italic"))
french_text = canvas.create_text(400,263,text="Word",font=("Arial" , 60 , "bold"))
canvas.grid(column=0,row=0 , columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image , highlightthickness=0 , command=next_card)
wrong_button.grid(row=1,column=0)


check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image , highlightthickness=0, command=next_card)
right_button.grid(row=1,column=1)

next_card()


















window.mainloop()