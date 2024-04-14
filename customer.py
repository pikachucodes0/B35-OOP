from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import sqlite3
import customtkinter


def show_profiles(entered_username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM subscribers WHERE Name=?", (entered_username,))
        profiles = cursor.fetchall()

        if profiles:
            row_position = 200
            for profile in profiles:
                x_position = 250
                for item in profile:
                    label1 = Label(text=item, font=('arial',11),bg='#986B4B',fg="white")
                    label1.place(x=x_position, y=row_position)
                    row_position += 40
                row_position += 20

        else:
            messagebox.showinfo("Info", "No user profiles found.")

    except sqlite3.OperationalError as e:
        messagebox.showerror("Error", f"Error accessing the database: {e}")
    conn.close()

def on_show_profile():
    entered_username = en1.get()
    if not entered_username:
        messagebox.showwarning("Warning", "Please enter a username to show the profile.")
        return

    # Clear existing labels before showing new profiles
    for widget in frame1.winfo_children():
        if isinstance(widget, Label):
            widget.destroy()

    # Call the show_profiles function
    en1.delete(0,END)
    show_profiles(entered_username)


#customer
def display_home():
    import subscribers
    
root=Tk()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
a=root.geometry(f'{screenwidth}x{screenheight}+0+0')
root.title("Home")
#insert main picture
mainimg=Image.open('dojo.png')
mainimg_tk=ImageTk.PhotoImage(mainimg)
btn=Label(root,image=mainimg_tk)
btn.pack()  
    

    #right side
lblri=Label(root,bg='#A97653',height=776,width=146)
lblri.place(x=1200,y=0)
lblri1=Label(root,text='Super Martial Arts',font=("Times", "24", "bold italic"),fg='white',bd=0,bg='#A97653')
lblri1.place(x=1215,y=140)

#insert logo img
logoimg=Image.open('kick.png')
logoimg_tk=ImageTk.PhotoImage(logoimg)
btnlogo=Label(root,compound='right',image=logoimg_tk,bd=0,bg='#A97653')
btnlogo.place(x=1225,y=250) 

    #features
lblfea=Label(root,text='Muay Thai',bg='#A97653',fg='white',font=('',"13", "bold"))
lblfea.place(x=1225,y=400)

lblfea1=Label(root,text='Taekwondo',bg='#A97653',fg='white',font=('',"13", "bold"))
lblfea1.place(x=1225,y=440)

lblfea2=Label(root,text='Kung Fu',bg='#A97653',fg='white',font=('',"13", "bold"))
lblfea2.place(x=1225,y=480)

lblfea3=Label(root,text='Kickboxing',bg='#A97653',fg='white',font=('',"13", "bold"))
lblfea3.place(x=1225,y=520)

lblfea3=Label(root,text='Karate',bg='#A97653',fg='white',font=('',"13", "bold"))
lblfea3.place(x=1225,y=560)

lblfea3=Label(root,text='Judo',bg='#A97653',fg='white',font=('',"13", "bold"))
lblfea3.place(x=1225,y=600)

lblfea3=Label(root,text='Boxing',bg='#A97653',fg='white',font=('',"13", "bold"))
lblfea3.place(x=1225,y=640)


    #create navigator
nav=Frame(root,text='Navigator',font=20,bg='#A97653',fg='white',bd=2,width=500,height=1200,relief='groove')
nav.place(x=0,y=0)
    

    #client info
frame1 = Frame(root, width=400, height=400,bg="#986B4B")
frame1.place(x=50,y=150)

    #-----------------------------------------------------------------------

lb1=customtkinter.CTkLabel(master=frame1,text='ID:',font=('arial',14,'bold'))
lb2=customtkinter.CTkLabel(master=frame1,text='Name:',font=('arial',14,'bold'))
lb3=customtkinter.CTkLabel(master=frame1,text='Age:',font=('arial',14,'bold'))
lb4=customtkinter.CTkLabel(master=frame1,text='Join date:',font=('arial',14,'bold'))
lb5=customtkinter.CTkLabel(master=frame1,text='Package type:',font=('arial',14,'bold'))
lb6=customtkinter.CTkLabel(master=frame1,text='Fees:',font=('arial',14,'bold'))
lb7=customtkinter.CTkLabel(master=frame1,text='Months:',font=('arial',14,'bold'))
lb8=customtkinter.CTkLabel(master=frame1,text='Package num:',font=('arial',14,'bold'))


lb1.place(x=40,y=50)
lb2.place(x=40,y=90)
lb3.place(x=40,y=130)
lb4.place(x=40,y=170)
lb5.place(x=40,y=210)
lb6.place(x=40,y=250)
lb7.place(x=40,y=290)
lb8.place(x=40,y=330)
    

en1 = customtkinter.CTkEntry(master=frame1,height=30,fg_color=("#A97653"),border_color="white",placeholder_text='Enter Name')
en1.place(x=35, y=12)
# en1 = Entry(root)
# en1.place(x=100, y=164)


def tologin():
    root.destroy()
    os.system("python mainproject.py")
def about():
    root.destroy()
    os.system("python aboutCustomer.py")


show_profile_btn = customtkinter.CTkButton(master=frame1, text="Show Profile", compound='left',fg_color=("snow4"),
                                            command=on_show_profile)
show_profile_btn.place(x=220, y=12)


    #create buttons
home_img=PhotoImage(file='imgs/home.png')
home_nav=Label(root,text='Home',compound='left',highlightcolor='black',image=home_img,fg='#43380D',bg='#A97653',font=('',"13", "bold"),bd=0,padx=8,pady=8)
home_nav.place(x=50,y=33)



img3=PhotoImage(file='imgs/about.png')
btn4_nav=Button(root,text='About',compound='left',image=img3,fg='white',bg='#A97653',font=('',"13", "bold"),bd=0,padx=8,pady=8,command=about)
btn4_nav.place(x=50,y=600)

img4=PhotoImage(file='logout.png')
btn5_nav=Button(root,text='Logout',compound='left',image=img4,fg='white',bg='#A97653',font=('',"13", "bold"),bd=0,padx=8,pady=8,command=tologin)
btn5_nav.place(x=1200,y=30)

info=Label(root,text="For more information\n\n981100222, 01-42086",fg='white',bg='#A97653',font=('',"13", "bold"))
info.place(x=60,y=700)


root.mainloop()


if __name__ == "__main__":
    display_home()