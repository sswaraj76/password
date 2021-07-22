from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    input3.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = input1.get()
    password = input3.get()
    email = input2.get()
    user_detail = {
        web: {
            'email': email,
            'password': password
        }
    }
    if len(password) == 0 or len(web) == 0 or len(email) == 0:
        messagebox.showwarning(title="Warning", message="Don't leave any field empty")
    else:
        with open("User_data.json", mode="r") as data:
            loaded_data = json.load(data)
            loaded_data.update(user_detail)
        with open("User_data.json", mode="w") as data:
            json.dump(loaded_data, data, indent=4)
            input1.delete(0, END)
            input2.delete(0, END)
            input3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Saver")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
bg_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=1, row=0)

label = Label(text="Website:")
label.grid(column=0, row=1)
label.focus()
label1 = Label(text="Email/Username:")
label1.grid(column=0, row=2)

label2 = Label(text="Password:")
label2.grid(column=0, row=3)

input1 = Entry(width=40)

input1.grid(column=1, row=1, columnspan=2)

input2 = Entry(width=40)
input2.grid(column=1, row=2, columnspan=2)
input2.insert(0, "eg: swaraj413@gmail.com")

input3 = Entry(width=20)
input3.grid(column=1, row=3, columnspan=1)

button1 = Button(text="Generate Password", width=15, command=generator)
button1.grid(column=2, row=3)

button2 = Button(text="Add", width=33, command=save)
button2.grid(column=1, row=4, columnspan=2)

window.mainloop()
