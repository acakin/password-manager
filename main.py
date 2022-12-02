from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    generate_password = random.choices(letters, weights=None, cum_weights=None, k = random.randint(8,10))\
                    + random.choices(symbols, weights=None, cum_weights=None, k = random.randint(2,4))\
                    + random.choices(numbers, weights=None, cum_weights=None, k = random.randint(2,4))
    random.shuffle(generate_password)
    generate_password += (str(generate_password[i]) for i in range(0,len(generate_password)))
    password_entry.insert(0, "".join(generate_password))
    pyperclip.copy(generate_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty.")
    else:
        ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                           f"Email: {username}\n"
                                                           f"Password: {password}\n"
                                                           f"Is it OK to save?")
        if ok:
            with open("data_of_users.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)


website_text = Label(text="Website:")
website_text.grid(row=1, column=0)
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_text = Label(text="Email/Username:")
username_text.grid(row=2, column=0)
username_entry = Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "xyz@gmail.com")

password_text = Label(text="Password:")
password_text.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate", width=13, command=generate)
generate_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
