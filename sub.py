from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3
import home_page
from tkinter import messagebox
import re
from datetime import datetime
import customtkinter


def add():
    
    root = Tk()
    root.title("subscribers")
    root.geometry("1920x1200")
    img = Image.open("dojo.png")
    img_tk = ImageTk.PhotoImage(img)
    imglbl = tkinter.Label(root, image=img_tk)
    imglbl.place(x=0, y=0, relwidth=1, relheight=1)
    # -----------------------------------------------------------------------
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    # ----------------------------------------------------------------------

    conn = sqlite3.connect('app.db')
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS subscribers (id INTEGER, name TEXT, age INTEGER, joindate DATE, subtype TEXT, fees REAL, months INTEGER, packagesub INTEGER)")

    conn.commit()
    # conn.close()

    def exit():
        root.destroy()
        home_page.display_home()

    def update_fees():
        try:
            selected_package_value = selected_package.get()
            fees_dict = {
                "Muay Thai": 7000,
                "Taekwondo": 1000,
                "Kung Fu": 1500,
                "Kickboxing": 3000,
                "Karate": 1000,
                "Judo": 500,
                "Boxing": 4000
            }
            fees = fees_dict.get(selected_package_value, 0)
            months_val = float(en5.get())
            total_fees = fees * months_val
            en7.delete(0, END)
            en7.insert(0, total_fees)
        except ValueError:
            messagebox.showerror("Error", "Invalid data type for Months. Please enter a floating-point number.")


    def update_package_num(*args):
        selected_package_value = selected_package.get()
        package_dict = {
            "Muay Thai": 1,
            "Taekwondo": 2,
            "Kung Fu": 3,
            "Kickboxing": 4,
            "Karate": 5,
            "Judo": 6,
            "Boxing": 7
        }
        package_var.set(package_dict.get(selected_package_value, ''))

    def update_selected_package(*args):
        selected_package_value = selected_package.get()
        package_dict = {
            1: "Muay Thai",
            2: "Taekwondo",
            3: "Kung Fu",
            4: "Kickboxing",
            5: "Karate",
            6: "Judo",
            7: "Boxing"
        }
        selected_package.set(package_dict.get(package_var.get(), ''))

    def submit():
        try:
            id_val = int(en1.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid data type for ID. Please enter an integer.")
            return

        # Check if ID already exists
        conn = sqlite3.connect('app.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM subscribers WHERE id=?", (id_val,))
        existing_record = cur.fetchone()
        conn.close()

        if existing_record:
            messagebox.showerror("Error", f"ID {id_val} already exists. Please use a different ID.")
            return

        name_val = en2.get()
        if not re.match("^[A-Za-z]+$", name_val):
            messagebox.showerror("Error", "Invalid characters in the name. Please use only A-Z and a-z.")
            return

        try:
            age_val = int(en3.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid data type for Age. Please enter an integer.")
            return

        joindate_val = en4.get()
        # Validate joindate using the datetime module
        try:
            datetime.strptime(joindate_val, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format for Join Date. Please use YYYY-MM-DD.")
            return

        try:
            fees_val = float(en7.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid data type for Fees. Please enter a floating-point number.")
            return

        try:
            months_val = float(en5.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid data type for months. Please enter a floating-point number.")
            return

        total_fees=fees_val*months_val
        conn = sqlite3.connect('app.db')
        cur = conn.cursor()

        cur.execute("create table if not exists subscribers (id integer, name text, age integer, joindate date, subtype text, fees float, months integer,packagesub integer)")
        cur.execute("INSERT INTO subscribers VALUES(:id, :name, :age, :joindate, :subtype, :fees, :months,:packagesub)",
                    {
                        'id': id_val,
                        'name': name_val,
                        'age': age_val,
                        'joindate': joindate_val,
                        'subtype': selected_package.get(),
                        'fees': total_fees,
                        'months': months_val,
                        'packagesub': package_var.get()
                    })

        conn.commit()
        conn.close()

        en1.delete(0, END)
        en2.delete(0, END)
        en3.delete(0, END)
        en4.delete(0, END)
        en5.delete(0, END)
        en7.delete(0, END)       

    # ----------------------------------------------------------------------

    # -----------------------------------------------------------------------
    frame1 = tkinter.Frame(root, width=320, height=300, bg="#986B4B")
    frame1.place(x=200, y=200)

    frame2 = tkinter.Frame(root, width=350, height=300, bg="#986B4B")
    frame2.place(x=900, y=200)
    # -----------------------------------------------------------------------

    lb1 = customtkinter.CTkLabel(master=frame1, text='ID:', font=('arial', 12, 'bold'))
    lb2 = customtkinter.CTkLabel(master=frame1, text='Name:', font=('arial', 12, 'bold'))
    lb3 = customtkinter.CTkLabel(master=frame1, text='Age:', font=('arial', 12, 'bold'))
    lb4 = customtkinter.CTkLabel(master=frame1, text='Join date:', font=('arial', 12, 'bold'))
    lb5 = customtkinter.CTkLabel(master=frame2, text='Fees:', font=('arial', 12, 'bold'))
    lb6 = customtkinter.CTkLabel(master=frame2, text='Package type:', font=('arial', 12, 'bold'))
    lb7 = customtkinter.CTkLabel(master=frame2, text='Package num:', font=('arial', 12, 'bold'))
    lb8 = customtkinter.CTkLabel(master=frame2, text='Months:', font=('arial', 12, 'bold'))

    en1 = Entry(master=frame1)
    en2 = Entry(master=frame1)
    en3 = Entry(master=frame1)
    en4 = Entry(master=frame1)
    en5 = Entry(master=frame2)
    en7 = Entry(master=frame2)

    btn2 = tkinter.Button(root, text='Add', font=('arial', 20, 'bold'), bg="#F4CB6E", fg="black", padx=150, pady=20,
                          command=submit)
    btn2.place(x=400, y=600)
    btn3 = tkinter.Button(root, text='Exit', font=('arial', 20, 'bold'), bg="#F4CB6E", fg="black", padx=150, pady=20,
                          command=exit)
    btn3.place(x=800, y=600)

    lb1.place(x=40, y=50)
    lb2.place(x=40, y=100)
    lb3.place(x=40, y=150)
    lb4.place(x=40, y=200)
    en1.place(x=140, y=50)
    en2.place(x=140, y=100)
    en3.place(x=140, y=150)
    en4.place(x=140, y=200)

    lb5.place(x=40, y=50)
    lb6.place(x=40, y=100)
    lb7.place(x=40, y=150)
    lb8.place(x=40, y=200)

    en5.place(x=150, y=200)
    en7.place(x=150, y=50)

    v2_rbtn = IntVar()
    v2_rbtn.set(1)

    package_type = ["", "Muay Thai", "Taekwondo", "Kung Fu", "Kickboxing", "Karate", "Judo", "Boxing"]
    selected_package = StringVar()
    selected_package.set('')
    # combo3 = OptionMenu(root, selected_package, *package_type, command=update_package_num)
    # combo3.place(x=1050, y=300)
    combo3 = OptionMenu(root, selected_package, *package_type)
    combo3.place(x=1050, y=300)
    combo3.bind("<Configure>", update_package_num)


    package_num = [1, 2, 3, 4, 5, 6, 7]
    package_var = IntVar()
    package_var.set('')
    # combo3 = Combobox(root, values=package_num, state='readonly', textvariable=package_var, command=update_selected_package)
    # combo3.place(x=1050, y=350)
    combo3 = Combobox(root, values=package_num, state='readonly', textvariable=package_var)
    combo3.place(x=1050, y=350)
    combo3.bind("<<ComboboxSelected>>", update_selected_package)


    update_fees_btn = tkinter.Button(root, text='Update Fees', font=('arial', 12, 'bold'), bg="#F4CB6E", fg="black",
                                     command=update_fees)
    update_fees_btn.place(x=1050, y=450)

    conn.commit()
    conn.close()
    root.mainloop()


if __name__ == "__main__":
    add()
