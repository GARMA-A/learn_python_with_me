from tkinter import *
from tkinter import messagebox
import json

# --------SAVE THE DATA ----------------------


def create_data_obj():
    my_data = {}
    my_data["website_name"] = website_entry.get()
    my_data["password"] = password_entry.get()
    my_data["email"] = email_entry.get() 
    if my_data["website_name"]=="" or my_data["password"]=="" or my_data["email"] =="":
       messagebox.showinfo(message="Please enter your all your entries")
    else:
        website_entry.delete(0,END)
        password_entry.delete(0,END)
        email_entry.delete(0,END)
        return my_data  

def save_to_txt_file():
       the_data = create_data_obj()
       with open("data.txt",'a')as data_file:
              data_file.write(the_data['website_name']+'\n')
              data_file.write(the_data['password']+'\n')
              data_file.write(the_data['email']+'\n')
              
              
def save_to_json():
       old_obj = create_data_obj()
       old_obj['website_name'] =  old_obj['website_name']
       ok = messagebox.askokcancel(title="Warning!" , message=f"your about to save \n Email : {old_obj['email']}\n Password : {old_obj['password']} \n WebsiteName: {old_obj['website_name']}")
       if ok:   
        with open("pass.json" , 'r') as json_file:
              content = json.load(json_file)
              content[str(old_obj['website_name']).lower()] = {"email":old_obj['email'],"password":old_obj['password']}       
        with open("pass.json" , 'w') as json_file:
              json.dump(content,json_file,indent=4)
      
       
def delete_all_data():
       with open("pass.json" , 'w') as json_file:
              json.dump({},json_file,indent=4)
       with open("data.txt",'w')as data_file:
              data_file.write("")
              
              
def search():
       content = None
       website_entery_data = website_entry.get().lower()
       with open("pass.json" , 'r') as json_file:
              content = json.load(json_file)
       messagebox.showinfo(title="Search",message=f"Email:{content[website_entery_data]['email']}\n Password:{content[website_entery_data]['password']}\n")
       
            
           
       



# --------------------------------------------

window = Tk()

window.title("Password manager")
window.config(padx=40 , pady=40)


canvas = Canvas(width=300,height=250)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(150,100,image=lock_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website", font=('Arial',16,"normal"))
website_label.grid(row=1,column=0)
# --------------------------------------------
website_entry = Entry(text="Website", font=('Arial',16,"normal") , width=21)
website_entry.grid(row=1,column=1 )
website_entry.focus()
# --------------------------------------------
search_btn = Button(text="Search", font=('Arial',16,"normal") , width=14 , command=search)
search_btn .grid(row=1,column=2 , )
# --------------------------------------------

email_label = Label(text="Email/Username", font=('Arial',16,"normal"))
email_label.grid(row=2,column=0)
# --------------------------------------------
email_entry = Entry(text="Email" , font=('Arial',16,"normal") , width=35)
email_entry.insert(0,"girgisemad74@gmail.com")
email_entry.grid(row=2 ,column=1 , columnspan=2)
# --------------------------------------------
password_label = Label(text="Password", font=('Arial',16,"normal"))
password_label.grid(row=3,column=0)
# --------------------------------------------

password_entry = Entry(text="Password", font=('Arial',16,"normal"),width=21 )
password_entry.grid(row=3,column=1)
# --------------------------------------------
generate_pasword = Button(text="Generate pasword" , font=('Arial',16,"normal"),width=14)
generate_pasword.grid(row=3,column=2)


add_btn = Button(text="Add" , font=('Arial',20,"normal") , width=21 , command=save_to_json)
add_btn.grid(row=4,column=1 )

delete_btn = Button(text="Delete" , font=('Arial',20,"normal") , width=14 , command=delete_all_data)
delete_btn.grid(row=4,column=2)









window.mainloop()
