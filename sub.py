from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3
import home_page
from tkinter import messagebox
import re
from datetime import datetime

def add():
    
    root=Tk()
    root.title("subscribers")
    root.geometry("1920x1200")
    img=Image.open("dojo.png")
    img_tk=ImageTk.PhotoImage(img)
    imglbl=tkinter.Label(root,image=img_tk)
    imglbl.place(x=0,y=0,relwidth=1,relheight=1)
    #-----------------------------------------------------------------------
    conn=sqlite3.connect('app.db')
    cur=conn.cursor()
    #----------------------------------------------------------------------
    def exit():
        root.destroy()
        home_page.display_home()


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
            days_val = float(en5.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid data type for Days. Please enter a floating-point number.")
            return


        conn = sqlite3.connect('app.db')
        cur = conn.cursor()

        cur.execute("create table if not exists subscribers (id integer, name text, age integer, joindate date, subtype text, fees float, days integer,packagesub integer)")
        cur.execute("INSERT INTO subscribers VALUES(:id, :name, :age, :joindate, :subtype, :fees, :days,:packagesub)",
                    {
                        'id': id_val,
                        'name': name_val,
                        'age': age_val,
                        'joindate': joindate_val,
                        'subtype': selected_package.get(),
                        'fees': fees_val,
                        'days': days_val,
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



    #----------------------------------------------------------------------

    #-----------------------------------------------------------------------
    f1 = tkinter.Frame(root, bg="#986B4B", bd=8, relief=tkinter.GROOVE)
    f2 = tkinter.Frame(root, bg="#986B4B", bd=8, relief=tkinter.GROOVE)
    
    f3=tkinter.Frame(root)

    #-----------------------------------------------------------------------

    lb1=Label(f1,text='ID:',font=('arial',12,'bold'),background="#986B4B")
    lb2=Label(f1,text='Name:',font=('arial',12,'bold'),background="#986B4B")
    lb3=Label(f1,text='Age:',font=('arial',12,'bold'),background="#986B4B")
    lb4=Label(f1,text='Join date:',font=('arial',12,'bold'),background="#986B4B")
    lb5=Label(f2,text='Fees:',font=('arial',12,'bold'),background="#986B4B")
    lb6=Label(f2,text='Package type:',font=('arial',12,'bold'),background="#986B4B")
    lb7=Label(f2,text='Package num:',font=('arial',12,'bold'),background="#986B4B")
    lb8=Label(f2,text='Days:',font=('arial',12,'bold'),background="#986B4B")

    en1=Entry(f1)
    en2=Entry(f1)
    en3=Entry(f1)
    en4=Entry(f1)
    en5=Entry(f2)
    en7=Entry(f2)
    #btn1=tkinter.Button(f3,text='View',font=('arial',12,'bold'),padx=150,pady=20,command=view_subscribers)
    #btn1.grid(row=0,column=4)

    btn2=tkinter.Button(f3,text='Add',font=('arial',20,'bold'),bg="#F4CB6E",fg="black",padx=150,pady=20,command=submit)
    btn2.grid(row=0,column=4)  
    btn3=tkinter.Button(f3,text='Exit',font=('arial',20,'bold'),bg="#F4CB6E",fg="black",padx=150,pady=20,command=exit)
    btn3.grid(row=0,column=5)

    lb1.grid(row=0,column=1)
    lb2.grid(row=1,column=1)
    lb3.grid(row=2,column=1)
    lb4.grid(row=3,column=1)
    #v1_rbtn=IntVar()
    #v1_rbtn.set(1)
    #rbtn1=Radiobutton(root,text='male',value=1,variable=v1_rbtn)
    #rbtn2=Radiobutton(root,text='female',value=2,variable=v1_rbtn)
    en1.grid(row=0,column=2,padx=70,pady=20)
    en2.grid(row=1,column=2,padx=70,pady=20)
    en3.grid(row=2,column=2,padx=70,pady=20)
    en4.grid(row=3,column=2,padx=70 ,pady=20)

    #f1.grid(row=5,column=2,pady=100)
    f1.place(anchor='e',relx=0.8,rely=0.35)


    #f3.place(anchor='s',relx=0.5,rely=0.5)

    f3.pack(side='bottom',padx=80,pady=40)

    lb5.grid(row=4,column=6,padx=40,pady=20)
    lb6.grid(row=1,column=6,padx=40,pady=20)
    lb7.grid(row=2,column=6,padx=40,pady=20)
    lb8.grid(row=3,column=6,padx=40,pady=20)

    en5.grid(row=3,column=7,padx=40,pady=20)
    en7.grid(row=4,column=7,padx=40,pady=20)
    
    v2_rbtn=IntVar()
    v2_rbtn.set(1)

    package_type=["Muay Thai","Taekwondo","Kung Fu","Kickboxing","Karate","Judo"]
    # Use StringVar to store the selected option
    selected_package = StringVar()
    selected_package.set(package_type[0])  # Set the default value

    # Create the OptionMenu
    combo3 = OptionMenu(f2, selected_package, *package_type)
    combo3.grid(row=1, column=7, padx=50, pady=80)

    #package number
    package_num=[1,2,3]
    package_var=IntVar()
    package_var.set(package_num[0])
    combo3=Combobox(f2,values=package_num,state='readonly',textvariable=package_var)
    combo3.grid(row=2,column=7,padx=50,pady=80)
    #------------------------------------------------------------------------
    # f2.grid(row=5,column=7,pady=100)
    f2.place(anchor='w',relx=0.1,rely=0.5)

    

    #-------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    conn.commit()
    conn.close()
    root.mainloop()
if __name__ == "__main__":
    add()