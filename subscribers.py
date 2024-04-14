from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3
from tkinter import simpledialog
from PIL import ImageTk,Image
import home_page
import customtkinter
from customtkinter import *
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
def subs():
    # setting up the connection
    Mydb = sqlite3.connect("app.db")
    cursor = Mydb.cursor()

    def update_func(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('', 'end', values=i)


    # this function made to search the Data base based on the name

    def search_func():
        q2 = q.get()
         # Check if the search query is empty
        if not q2:
            messagebox.showerror("Error", "Search query cannot be empty.")
            return

        query = "SELECT id, name, age, joindate, subtype, fees, months, packagesub FROM subscribers WHERE name LIKE ?"
        cursor.execute(query, ('%' + q2 + '%',))
        rows = cursor.fetchall()
        update_func(rows)

    # this function made to refresh the tabel afte every update, search or delete


    def clear_func():
        query = "SELECT id , name, age, joindate, subtype, fees, months, packagesub FROM subscribers"
        cursor.execute(query)
        rows = cursor.fetchall()
        update_func(rows)


    # this function is event driven <double click> to present data in the entry box for modification
    def getrow(event):
        rowid = trv.identify_row(event.y)
        item = trv.item(trv.focus())
        t1.set(item['values'][0])
        t2.set(item['values'][1])
        t3.set(item['values'][7])
        t4.set(item['values'][6])

    # this function is made for updating the remaining months of the subscribers
    def update_customer():
        months = t4.get()
        

    # Check if 'months' field is empty
        if not months:
            messagebox.showerror("Error", "Please select a record first.")
            return
        
        id = t1.get()
        Mydb = sqlite3.connect("app.db")
        cursor = Mydb.cursor()
        if messagebox.askyesno(" Confirm update", "Are you sure you want to update the months?"):
            query = "update subscribers SET months = ? where id = ?"
            cursor.execute(query, (months, id))
            Mydb.commit()
            clear_func()
            messagebox.showinfo("Success", "Changes successfully applied.")

        else:
            return True

    # this function is made to cancel the subscribtion


    def delete_customer():
        id = t1.get()
        package_number = t3.get()
        months = t4.get()
        Mydb = sqlite3.connect("app.db")
        cursor = Mydb.cursor()
        if messagebox.askyesno(" Confirm Deletion", "Are you sure you want to delete this user?"):
            query = "delete from subscribers where id = ?"
            cursor.execute(query,(id,))
            Mydb.commit()
            clear_func()
        else:
            return True

    # this function is made to reward a certain package subscribers with additonal months


    def reward():
        increase_months = simpledialog.askinteger("Reward months", "Enter the number of months to reward")
        package_num = simpledialog.askinteger("Reward package", "Enter the number of the package rewarded")
        
        if increase_months is not None and package_num is not None:
            Mydb = sqlite3.connect("app.db")
            cursor = Mydb.cursor()
            
            if messagebox.askyesno("Confirm update", "Are you sure you want to increase the months?"):
                query = "UPDATE subscribers SET months = months + ? WHERE packagesub = ?"
                cursor.execute(query, (increase_months, package_num))
                Mydb.commit()
                clear_func()
                messagebox.showinfo("Success", f"months increased for Package {package_num}")
            else:
                return True
        else:
            messagebox.showwarning("Input Error", "Please enter valid values for months and package number")


    # exit to home page function
    def exit_func():
        subscribers.destroy()
        home_page.display_home()
    

    subscribers = Tk()  # the form
    q = StringVar()  # made for use in search function
    t1, t2, t3, t4= StringVar(), StringVar(), StringVar(), StringVar()

    subscribers.title('Subscribers Modifications')
    screenwidth = subscribers.winfo_screenwidth()
    screenheight = subscribers.winfo_screenheight()
    subscribers.geometry(f'{screenwidth}x{screenheight}+0+0')
    #-----------------------------------------------------------------------------

    img=Image.open("gatilo.jpg")
    img=img.resize((screenwidth,screenheight))
    img_tk=ImageTk.PhotoImage(img)
    imglbl=Label(subscribers,image=img_tk)
    imglbl.place(x=0,y=0,relwidth=1,relheight=1)

    f1=customtkinter.CTkFrame(subscribers,fg_color="#797979",width=350,height=100)
    f2=customtkinter.CTkFrame(subscribers,fg_color="#797979",width=700,height=100)

   # tree view for traversing the database
    trv = Treeview(subscribers, columns=(1, 2, 3, 4, 5, 6, 7,8), show="headings", height="10", selectmode='browse')
    trv.pack(side=LEFT)
    trv.place(x=0, y=0)

    trv.heading(1, text="ID")
    trv.heading(2, text="Name")
    trv.heading(3, text="Age")
    trv.heading(4, text="Join Date")
    trv.heading(5, text="Subscribtion Type")
    trv.heading(6, text="Subscribtion Fees")
    trv.heading(7, text="Months")
    trv.heading(8, text="package number")


    trv.column(1, width=100, anchor='center')
    trv.column(2, width=400)
    trv.column(3, width=100, anchor='center')
    trv.column(4, width=250)
    trv.column(5, width=150, anchor='center')
    trv.column(6, width=150, anchor='center')
    trv.column(7, width=100, anchor='center')
    trv.column(8, width=150, anchor='center')

    style = Style()
    style.configure('Treeview', font=('arial', 11),
                    foreground='#100720', background='#797979')
    style.configure('Treeview.Heading', font=('tahoma', 12))

    # traverse data on the tree view section
    cursor.execute(
        "select id , name, age, joindate, subtype , fees, months, packagesub from subscribers")
    rows = cursor.fetchall()
    update_func(rows)

    # search section
    a=customtkinter.CTkLabel(f1,text="Enter Name")
    a.place(x=20,y=10)
    ent = customtkinter.CTkEntry(f1, textvariable=q)
    ent.place(x=120,y=10)
    btn = customtkinter.CTkButton(f1, text="Search", command=search_func,fg_color="#ffa200",width=60)
    btn.place(x=120,y=50)
    Cbtn = customtkinter.CTkButton(f1, text='Clear',command=clear_func,fg_color="#ffa200",width=60)
    Cbtn.place(x=200,y=50)
 # User Data Section
    trv.bind('<Double 1>', getrow)

    # 4 data entry
    lbl1 = customtkinter.CTkLabel(f2, text="Customer ID",bg_color="#797979")
    lbl1.grid(row=0, column=0, padx=5, pady=3)
    ent1 = customtkinter.CTkEntry(f2, textvariable=t1)
    ent1.grid(row=0, column=1, padx=5, pady=3)
    ent1.configure(state=DISABLED)

    lbl2 = customtkinter.CTkLabel(f2, text="Name",bg_color="#797979")
    lbl2.grid(row=1, column=0, padx=5, pady=3)
    ent2 = customtkinter.CTkEntry(f2, textvariable=t2)
    ent2.grid(row=1, column=1, padx=5, pady=3)
    ent2.configure(state=DISABLED)

    lbl3 = customtkinter.CTkLabel(f2, text="Package",bg_color="#797979")
    lbl3.grid(row=2, column=0, padx=5, pady=3)
    ent3 = customtkinter.CTkEntry(f2, textvariable=t3)
    ent3.grid(row=2, column=1, padx=5, pady=3)
    ent3.configure(state=DISABLED)

    lbl4 = customtkinter.CTkLabel(f2, text="Months",bg_color="#797979")
    lbl4.grid(row=3, column=0, padx=5, pady=3)
    ent4 = customtkinter.CTkEntry(f2, textvariable=t4)
    ent4.grid(row=3, column=1, padx=5, pady=3)

    # 3 Buttons for modifications
    up_btn = customtkinter.CTkButton(f2, text="Update months",command=update_customer,fg_color="#ffa200")
    add_btn =customtkinter.CTkButton(f2, text="Reward months",command=reward,fg_color="#ffa200")
    delete_btn = customtkinter.CTkButton(f2, text="Cancel subscription",command=delete_customer,fg_color="#ffa200")
    # add fuction here to return to main page
    Exit =customtkinter.CTkButton(f2, text="EXIT to main menu", command=exit_func,fg_color="#ffa200")

    add_btn.grid(row=0, column=5,padx=10,pady=10)
    up_btn.grid(row=1, column=5, padx=10, pady=10)
    delete_btn.grid(row=2, column=5, padx=10, pady=10)
    Exit.grid(row=3, column=5, padx=10, pady=10)


    f1.place(x=1052,y=228)
    f2.place(x=0,y=220)

    subscribers.mainloop()
if __name__ == "__main__":
        subs()