from tkinter import *

def mile_to_km():
       value = float(entry_for_miles.get())
       value*=1.609
      
       label_km_value.config(text=round(value,2)) 
       


window = Tk()
window.minsize(width=250,height=75)
window.config(padx=25,pady=25)

entry_for_miles = Entry(text="0")
entry_for_miles.grid(column=1 , row=0)

label_miles= Label(text="Miles")
label_miles.grid(column=2,row=0)


label_is_equal = Label(text="is equal to")
label_is_equal.grid(column=0,row=1)

label_km_value = Label(text="0")
label_km_value.grid(column=1,row=1)

label_km = Label(text="Km")
label_km.grid(column=2,row=1)

btn=Button(text="Calculate" , command=mile_to_km)
btn.grid(column=1,row=2)





window.mainloop()

