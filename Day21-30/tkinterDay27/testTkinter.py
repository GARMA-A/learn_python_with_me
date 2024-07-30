import tkinter
# create a window
window = tkinter.Tk()
# # change the title of the window
# window.title('my first use for Tkinter')
# # change the size of the window
window.minsize(width=600, height=600)
# # create a label
# my_label = tkinter.Label(text="i'm the label" ,font=('Arial',24,'bold'))
# # you need to tell tkinter how and where to display it (packer) 
# # my_label.pack() # you have side=right left center ->up by default bottom also
# # you can config the label all properties by passing them 
# # direct to your label on insilization or config it after that
# my_label.config(text="new text by config")
# # buttons
# def button_clicked():
#        my_label.config(text=input.get())


# button = tkinter.Button(text="click me",command=button_clicked)
# # button.pack()

# # entry 

# input = tkinter.Entry(width=10)
# # input.pack()
# print(input.get())

# # now you know how to take data from entry and display it 
# # on the screen go to BasicTKinter and return here

# #How to Position your elements
# # you know pack and know you will know place (better)

# my_label.place(x=20,y=200)

# # but the best is the Grid 

# new_label = tkinter.Label(text="the newest lable")
# new_label.grid(column=2,row=2)


# Chalange one #1

lable1 = tkinter.Label(text="Label1")
lable1.grid(column=0,row=0)
lable1.config(padx=10,pady=10)


btn1 = tkinter.Button(text="click me")
btn1.grid(column=1,row=1)
btn1.config(padx=10,pady=10)


btn2 = tkinter.Button(text="click me")
btn2.grid(column=2,row=0)
btn2.config(padx=10,pady=10)




entry = tkinter.Entry(text="entry")
entry.grid(column=3,row=3)






window.mainloop()