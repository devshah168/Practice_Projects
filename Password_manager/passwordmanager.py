from tkinter import *
from random import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    pass_letters=[choice(letters) for _ in range(randint(8,10))]
    pass_numbers=[choice(numbers) for _ in range(randint(2,14))]
    pass_symbols=[choice(symbols) for _ in range(randint(2,14))]
    pass_list=pass_letters+pass_numbers+pass_symbols
    shuffle(pass_list)
    password="".join(pass_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("C:/PROJECTS/100 days of python/day29/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists."
            )


# ---------------------------- SAVE PASSWORD ------------------------------- #
def sav_data():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    
    new_data={
        website:{
            "email":email,
            "password":password,
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showerror(title="Oops",message="Please don't leave any fields empty!")
    else:
        try:
            with open("C:/PROJECTS/100 days of python/day29/data.json",'r') as file:
                data=json.load(file)
        except FileNotFoundError:
            with open("C:/PROJECTS/100 days of python/day29/data.json",'w') as file:
                json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)
            with open("C:/PROJECTS/100 days of python/day29/data.json",'w') as file:
                json.dump(data,file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200,highlightthickness=0)
pass_image = PhotoImage(file="C:/PROJECTS/100 days of python/day29/logo.png")
canvas.create_image(100,100,image=pass_image)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry=Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"dev@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)


search_but=Button(text="Search",width=14,command=find_password)
search_but.grid(column=2,row=1)
gen_button=Button(text="Generate Password",width=14,command=generate_password)
gen_button.grid(column=2,row=3)
add_button=Button(text="Add",width=36,command=sav_data)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()
