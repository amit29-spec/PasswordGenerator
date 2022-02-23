from tkinter import *
from tkinter import messagebox
import random
import json

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
new_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=new_img)
canvas.grid(column=1, row=0)
winput = None
uinput = None
pinput = None
new_data = None


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letter
    random.shuffle(password_list)

    password = "".join(password_list)
    pwrite.insert(0, password)


text = Label(text="Website :")
text.grid(column=0, row=1)

write = Entry(width=35)
write.grid(column=1, row=1, columnspan=2)

ntext = Label(text="")
ntext.grid(column=0, row=2)

user = Label(text="Email/Username :")
user.grid(column=0, row=3)

nwrite = Entry(width=35)
nwrite.grid(column=1, row=3, columnspan=2)

ztext = Label(text="")
ztext.grid(column=0, row=4)

passw = Label(text="Password :")
passw.grid(column=0, row=5)

pwrite = Entry(width=21)
pwrite.grid(column=1, row=5)

pbutton = Button(text="Generate Password", command=generate_password)
pbutton.grid(column=2, row=5)

qtext = Label(text="")
qtext.grid(column=0, row=6)


def get_every():
    global winput
    winput = write.get()
    global uinput
    uinput = nwrite.get()
    global pinput
    pinput = pwrite.get()
    global new_data
    new_data = {
        winput: {
            "email": uinput,
            "password": pinput
        }
    }

    if winput == "" or uinput == "" or pinput == "":
        messagebox.showerror(title="Error", message="Field is empty")

    else:
        try:
            with open("password.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except:
            with open("password.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("password.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)


def search_butt():
    try:
        new_winput = write.get()
        if new_winput == "":
            messagebox.showerror(title="Error", message="Field is empty")
        else:

            with open("password.json") as data_file:
                data = json.load(data_file)
                if new_winput in data:
                    new_uinput = data[new_winput]["email"]
                    new_pinput = data[new_winput]["password"]
                    messagebox.askokcancel(title="Info", message=f"email:{new_uinput}\n password:{new_pinput}")
                else:
                    messagebox.showerror(title="Error", message="No such field")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="First Create an email and password ")


abutton = Button(text="ADD", width=36, command=get_every)
abutton.grid(column=1, row=7, columnspan=2)

sbutton = Button(text="Search", command=search_butt)
sbutton.grid(column=3, row=1)

window.mainloop()
