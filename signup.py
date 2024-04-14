import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import customtkinter
import os

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

def validate_username(username):
    return username.isalnum()

def validate_password(password):
    return len(password) >= 6

def username_exists(username, cursor):
    cursor.execute("SELECT * FROM customers WHERE username=?", (username,))
    customer = cursor.fetchone()

    cursor.execute("SELECT * FROM admins WHERE username=?", (username,))
    admin = cursor.fetchone()

    return customer or admin

def register(user_type):
    entry_username = username_entry.get()
    entry_password = password_entry.get()

    if not entry_username or not entry_password:
        messagebox.showerror("Registration", "Please enter both username and password")
        return

    if not validate_username(entry_username):
        messagebox.showerror("Registration", "Invalid username. Please use alphanumeric characters only.")
        return

    if not validate_password(entry_password):
        messagebox.showerror("Registration", "Password should be at least 6 characters long")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        if username_exists(entry_username, cursor):
            messagebox.showerror("Registration", "Username already exists. Please choose another.")
            return

        if user_type == "customer":
            cursor.execute("INSERT INTO customers VALUES (?, ?)", (entry_username, entry_password))
        elif user_type == "admin":
            cursor.execute("INSERT INTO admins VALUES (?, ?)", (entry_username, entry_password))

        conn.commit()
        conn.close()

        messagebox.showinfo("Registration", "Registration successful!")

        # Clear input boxes after successful registration
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    except sqlite3.Error as e:
        messagebox.showerror("Registration", f"Database error: {e}")

    finally:
        conn.close()

def open_login_page():
    signup_window.destroy()
    os.system("python mainproject.py")

signup_window = customtkinter.CTk()
signup_window.title("Signup Page")

img1_signup = ImageTk.PhotoImage(Image.open("pattern.png"))
l1_signup = customtkinter.CTkLabel(master=signup_window, image=img1_signup)
l1_signup.pack()

frame_signup = customtkinter.CTkFrame(master=l1_signup, width=320, height=360, corner_radius=15)
frame_signup.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l2_signup = customtkinter.CTkLabel(master=frame_signup, text="Create your Account", font=('Century Gothic', 20))
l2_signup.place(x=50, y=45)

username_entry = customtkinter.CTkEntry(master=frame_signup, width=220, placeholder_text='Username')
username_entry.place(x=50, y=110)

password_entry = customtkinter.CTkEntry(master=frame_signup, width=220, placeholder_text='Password', show="*")
password_entry.place(x=50, y=165)

login_button = customtkinter.CTkButton(master=frame_signup, text="Already have an account? Login", command=open_login_page)
login_button.place(x=60, y=300)

signup_button1 = customtkinter.CTkButton(master=frame_signup, text="Register (Customer)", command=lambda: register("customer"))
signup_button1.place(x=85, y=210)

signup_button2 = customtkinter.CTkButton(master=frame_signup, text="Register (Admin)", command=lambda: register("admin"))
signup_button2.place(x=85, y=250)

signup_window.mainloop()
