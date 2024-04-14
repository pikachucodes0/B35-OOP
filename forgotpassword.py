from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import customtkinter
import os
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
win3 = customtkinter.CTk()

screenwidth = win3.winfo_screenwidth()
screenheight = win3.winfo_screenheight()
win3.geometry(f'{screenwidth}x{screenheight}+0+0')
# win3.geometry("1920x1080")
win3.resizable(0,0)

win3.title("Password Reset")

# BACKGROUND IMAGE
# img = Image.open("pattern.png")
# bg = ImageTk.PhotoImage(img)

# photoLabel = Label(win3, image=bg)
# photoLabel.place(x=0, y=0)
img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
l1 = customtkinter.CTkLabel(master=win3, image=img1)
l1.pack()
frame = customtkinter.CTkFrame(master=l1, width=320, height=440, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)



# frame.place(x=350, y=130)

"""-----FUNCTIONS-----"""


# show password function
def showPassword():
    if newPasswordEntry.cget("show") == "*":
        newPasswordEntry.config(show="")
    else:
        newPasswordEntry.config(show="*")


# show password function2
def showPassword2():
    if confirmPasswordEntry.cget("show") == "*":
        confirmPasswordEntry.config(show="")
    else:
        confirmPasswordEntry.config(show="*")


# back to login page
def backLogin():
    win3.destroy()
    os.system("python mainproject.py")


# password reset function
def resetPassword():
    username = usernameEntry.get()
    newPassword = newPasswordEntry.get()
    confirmPassword = confirmPasswordEntry.get()
    if usernameEntry != "" and newPassword != "" and confirmPassword != "":
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        if newPassword == confirmPassword:
            selectusername = """SELECT * FROM users WHERE username=?"""
            cursor.execute(selectusername, [(username)])
            if cursor.fetchall():
                passwordUpdate = """UPDATE users SET password=? WHERE username=?"""
                cursor.execute(passwordUpdate, [(newPassword), (username)])
                messagebox.showinfo(
                    title="info", message="Password succcessfully updated."
                )
                usernameEntry.delete(0, END)
                newPasswordEntry.delete(0, END)
                confirmPasswordEntry.delete(0, END)
            else:
                messagebox.showerror(title="error", message="invalid credentials")
                usernameEntry.delete(0, END)
                newPasswordEntry.delete(0, END)
                confirmPasswordEntry.delete(0, END)
        else:
            messagebox.showerror(title="error", message="Passwords do not match")
            usernameEntry.delete(0, END)
            newPasswordEntry.delete(0, END)
            confirmPasswordEntry.delete(0, END)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror(title="error", message="invalid credentials")
        usernameEntry.delete(0, END)
        newPasswordEntry.delete(0, END)
        confirmPasswordEntry.delete(0, END)


# LABEL

# login
resetPasswordLabel = customtkinter.CTkLabel(master= frame, text="RESET PASSWORD", font=("ariel", 20, "bold"))
resetPasswordLabel.place(x=50, y=20)

# username
usernamelabel =customtkinter.CTkLabel(master=frame, text="Username", font=("ariel", 18))
usernamelabel.place(x=30, y=80)


# create password
newPasswordLabel = customtkinter.CTkLabel(master=frame, text="New Password", font=("ariel", 18))
newPasswordLabel.place(x=30, y=140)

# confirm password
confirmPasswordLabel = customtkinter.CTkLabel(
    master=frame, text="Confirm Password", font=("ariel", 18)
)
confirmPasswordLabel.place(x=30, y=250)

# ENTRY
# username
usernameEntry = Entry(win3, width=24, font=("ariel", 15), relief=SUNKEN)
usernameEntry.place(x=800, y=400)

# create password
newPasswordEntry = Entry(win3, width=24, font=("ariel", 15), show="*", relief=SUNKEN)
newPasswordEntry.place(x=800, y=490)

# confirm password
confirmPasswordEntry = Entry(
    win3, width=24, font=("ariel", 15), show="*", relief=SUNKEN
)
confirmPasswordEntry.place(x=800, y=630)


# BUTTONS
# back button
backBtn = customtkinter.CTkButton(
    master=win3,
    text="BACK",
    # font=("ariel", 10),
    # # fg="white",
    # # bg="#ACA9AB",
    # width=15,
    # height=2,
    # borderwidth=1,
    command=backLogin,
   
)
backBtn.place(x=780, y=600)

# reset button
resetBtn = customtkinter.CTkButton(
    master=win3,
    text="RESET",
    # font=("ariel", 10),
    # fg="white",
    # bg="#ACA9AB",
    # width=15,
    # height=2,
    # borderwidth=1,
    command=resetPassword,

)
resetBtn.place(x=620, y=600)






# CHECKBUTTON
# show password
var = IntVar()
checkbtn1 = Checkbutton(
    win3,
    text="Show Password",
    variable=var,
    command=showPassword,
    bg="#2b2b2b",
    font=("ariel", 10),
    fg="white",

)
checkbtn1.place(x=800, y=540)

var2 = IntVar()
checkbtn2 = Checkbutton(
    win3,
    text="Show Password",
    variable=var2,
    command=showPassword2,
    bg="#2b2b2b",
    font=("ariel", 10),
    fg="white",
)
checkbtn2.place(x=800, y=690)

win3.mainloop()