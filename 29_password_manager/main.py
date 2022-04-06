from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- SEARCH THE WEBSITE ------------------------------- #

def search():
    website = website_entry.get()
    if website:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title='Error', message='No data file found')
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(message=f'Email: {email}\nPassword: {password}')
                pyperclip.copy(password)
            else:
                messagebox.showerror(title='Error', message='There is no entry for this website')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)

    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website and email and password:
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }

        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except Exception as exception:
            print(exception)
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)  # if there something wrong with file, we rewrite it
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)  # if all works as intended, we update the info
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    else:
        messagebox.showinfo(message='Please fill out all fields.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(bg='white', padx=20, pady=50)

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)

img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website", bg='white', fg='black', highlightthickness=0)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username", bg='white', fg='black', highlightthickness=0)
email_label.grid(column=0, row=2)
password_label = Label(text="Password", bg='white', fg='black', highlightthickness=0)
password_label.grid(column=0, row=3)

# buttons
generate_button = Button(width=12, text='Generate Password', command=generate_password, highlightbackground='white',
                         fg='black')
generate_button.grid(column=2, row=3, sticky='w')
add_button = Button(width=34, text='Add', command=save_password, highlightbackground='white', fg='black')
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(width=12, text='search', command=search, highlightbackground='white', fg='black')
search_button.grid(column=2, row=1, sticky='w')

# entry
website_entry = Entry(width=20, highlightbackground='white', highlightthickness=0, bg='white', fg='black',
                      insertbackground='black')
website_entry.grid(column=1, row=1, sticky='w', pady=2)
website_entry.focus()
email_entry = Entry(width=37, highlightbackground='white', highlightthickness=0, bg='white', fg='black',
                    insertbackground='black')
email_entry.grid(column=1, row=2, columnspan=2, sticky='w', pady=2)
email_entry.insert(0, "meinlp@ya.ru")
password_entry = Entry(width=20, highlightbackground='white', highlightthickness=0, bg='white', fg='black',
                       insertbackground='black')
password_entry.grid(column=1, row=3, sticky='w', pady=2)

window.mainloop()
