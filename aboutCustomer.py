from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os

root=Tk()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.geometry(f'{screenwidth}x{screenheight}+0+0')
root.title("About")
 
def back():
        root.destroy()
        os.system("python customer.py")
        

nav=LabelFrame(root,text='Super Martial Arts',font=("Times", "26", "bold"),bg='#75543B',fg='white',bd=2,width=10000,height=100,relief='groove')
nav.place(x=0,y=0)
quote=Label(root,text='If you wish to control others',bg='#75543B',fg='white',font=('',"18", "bold"))
quote.place(x=625,y=62)
quote2=Label(root,text='you must first control yourself',fg='#75543B',font=('',"18", "bold"))
quote2.place(x=610,y=100)
artist=Label(root,text='-Miyamoto Musashi',fg='#75543B',font=('',"12", "italic"))
artist.place(x=988,y=105)

img1=PhotoImage(file='amita.png')
img_amit=Label(root,highlightcolor='#43380D',image=img1)
img_amit.place(x=100,y=250)

img2=PhotoImage(file='hero.png')
img_hero=Label(root,highlightcolor='#43380D',image=img2)
img_hero.place(x=500,y=250)

img3=PhotoImage(file='udh.png')
img_udh=Label(root,highlightcolor='#43380D',image=img3)
img_udh.place(x=900,y=250)

img4=PhotoImage(file='kale.png')
img_kale=Label(root,highlightcolor='#43380D',image=img4)
img_kale.place(x=1250,y=250)

amit=Label(root,text="Amit Khayargoli",font=("Arial", "14", "bold"))
amit.place(x=130,y=520)
art1=Label(root,text="Taekwondo/Karate",font=("Arial","12")).place(x=135,y=550)

aryan=Label(root,text="Aryan Nakarmi",font=("Arial", "14", "bold"))
aryan.place(x=535,y=520)
art2=Label(root,text="Muay Thai/Kickboxing",font=("Arial","12")).place(x=525,y=550)

asrim=Label(root,text="Asrim Suwal",font=("Arial", "14", "bold"))
asrim.place(x=940,y=520)
art3=Label(root,text="Kung Fu",font=("Arial","12")).place(x=970,y=550)

ishan=Label(root,text="Ishan Raj Dhami",font=("Arial", "14", "bold"))
ishan.place(x=1280,y=520)
art4=Label(root,text="Judo/Boxing",font=("Arial","12")).place(x=1300,y=550)

mison=Label(root,text="Our Mission",font=("Arial","14","bold")).place(x=750,y=650)

exp=Label(root,text="We're a small group of people who love the art of fighting. We're introducing the different forms of this art.\n\nwww.supermartialarts.org").place(x=540,y=700)

backimg=PhotoImage(file='back.png')
btn=Button(root,text="BACK",compound="left",image=backimg,fg='white',bg='#75543B',font=('',"14", "bold"),bd=0,padx=8,pady=8,command=back)
btn.place(x=1360,y=40)


root.mainloop()