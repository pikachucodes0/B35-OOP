import tkinter as tk
import customtkinter
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import os
from hashlib import sha256

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
# app.geometry("1920x1080")
screenwidth = app.winfo_screenwidth()
screenheight = app.winfo_screenheight()
app.geometry(f'{screenwidth}x{screenheight}+0+0')
app.title('Login')

# Database initialization
def create_tables():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Create customers table
    cursor.execute("CREATE TABLE IF NOT EXISTS customers (username TEXT, password TEXT)")
    
    # Create admins table
    cursor.execute("CREATE TABLE IF NOT EXISTS admins (username TEXT, password TEXT)")
    user=cursor.fetchone()
    conn.commit()
    conn.close()
create_tables()

# def login(user_type, home_page_func):
#     username = username.get()
#     password = password.get()

#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()

#     if user_type == "customer":
#         cursor.execute("SELECT * FROM customers WHERE username=? AND password=?", (username, password))
#     elif user_type == "admin":
#         cursor.execute("SELECT * FROM admins WHERE username=? AND password=?", (username, password))

#     user = cursor.fetchone()
#     conn.close()

#     if user:
#         messagebox.showinfo("Login", "Login successful!")
#         home_page_func()
#     else:
#         messagebox.showerror("Login", "Invalid username or password")

def login(user_type, home_page_func):
    entered_username = entry1.get()  # Use a different name for Entry widget
    entered_password = entry2.get()  # Use a different name for Entry widget

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    if user_type == "customer":
        cursor.execute("SELECT * FROM customers WHERE username=? AND password=?", (entered_username, entered_password))
    elif user_type == "admin":
        cursor.execute("SELECT * FROM admins WHERE username=? AND password=?", (entered_username, entered_password))

    user = cursor.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Login", "Login successful!")
        home_page_func()
    else:
        messagebox.showerror("Login", "Invalid username or password")



def admin_home_page():
    os.system("python home_page.py")
def open_signup_page():
    app.destroy()
    os.system("python signup.py")
def forgot_password():
    app.destroy()
    os.system("python forgotpassword.py")

# Functions for home pages
def customer_home_page():
    # Implement customer home page functionality here
    messagebox.showinfo("Customer Home Page", "Welcome to the Customer Home Page!")


img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

button1 = customtkinter.CTkButton(master=frame,text="Login (Customer)", command=lambda: login("customer", customer_home_page), corner_radius=6)
button1.place(x=80, y=200)
button2 = customtkinter.CTkButton(master=frame,text="Login (Admin)", command=lambda: login("admin", admin_home_page),corner_radius=6)
button2.place(x=80, y=240)


l3 = customtkinter.CTkButton(master=frame, text="Don't have an account? Sign Up", command=open_signup_page)
l3.place(x=60, y=320)
l3 = customtkinter.CTkButton(master=frame, text="Forgot password?", command=forgot_password)
l3.place(x=85, y=280)


app.mainloop()
