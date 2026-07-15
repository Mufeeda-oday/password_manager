from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
import json
FONT_NAME = "san-serif"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # list_variable = [new item for item in range()]
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    # below code replaces with above join method.
    # for char in password_list:
    #   password += char

    password_entry.insert(0, string=f"{password}")
    pyperclip.copy(password)

#   copy and paste clipboard function using pyperclip
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please dont leave any field empty!")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                #json.dump(new_data,f,indent=4)
                    # f.write(f"{website} | {email} | {password}\n")
        except FileNotFoundError:
            with open("data.json", "w") as f:
                 json.dump(new_data, f, indent=4)
        else:
            # print(data)
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data,f, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- SEARCH ------------------------------- #
def search_password():
    website = web_entry.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message = "No data file found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"There are no details for {website} exist ")



# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

# Labels
web_label = Label(text= "Website:",font = (FONT_NAME,12))
web_label.grid(column=0,row=1)
email_label = Label(text= "Email/Username:",font = (FONT_NAME,12))
email_label.grid(column=0,row=2)
password_label = Label(text= "Password:",font = (FONT_NAME,12))
password_label.grid(column=0,row=3)

# Entries
web_entry = Entry(width=21)
web_entry.grid(column=1,row=1)
web_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(END,string="my_email@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)
# web_entry.insert(END,string="")

# Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2,row=3)
save_button = Button(text="Add", width= 36, command=save)
save_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text="Search",width = 13, command= search_password)
search_button.grid(column=2,row=1)
window.mainloop()