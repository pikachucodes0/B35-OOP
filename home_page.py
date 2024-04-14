from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os



def display_home():
    import subscribers
    def tosubs(): 
        root.destroy()
        subscribers.subs()
    import sub
    def tosub():
        root.destroy()
        sub.add()
    
    def tologin():
        root.destroy()
        os.system("python mainproject.py")
    def toabout():
        root.destroy()
        os.system("python about.py")

    root=Tk()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    root.geometry(f'{screenwidth}x{screenheight}+0+0')
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
    btnlogo=Label(root,compound='right',image=logoimg_tk,bd=0,bg='#A97653')#,width=150,height=150
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
    nav=LabelFrame(root,text='Navigator',font=20,bg='#A97653',fg='white',bd=2,width=300,height=1200,relief='groove')
    nav.place(x=0,y=0)

    #create buttons
    home_img=PhotoImage(file='imgs/home.png')
    home_nav=Label(root,text='Home',compound='left',highlightcolor='black',image=home_img,fg='#43380D',bg='#A97653',font=('',"13", "bold"),bd=0,padx=8,pady=8)
    home_nav.place(x=50,y=33)

    img1=PhotoImage(file='imgs/buy.png')
    btn1_nav=Button(root,text='Subscribers',compound='left',highlightcolor='black',image=img1,fg='white',bg='#A97653',font=('',"13", "bold"),bd=0,padx=8,pady=8,command=tosubs)
    btn1_nav.place(x=50,y=250)

    img2=PhotoImage(file='imgs/add.png')
    btn2_nav=Button(root,text='Add a new package',compound='left',image=img2,fg='white',bg='#A97653',font=('',"13", "bold"),bd=0,padx=3,pady=8,command=tosub)
    btn2_nav.place(x=52,y=150)

    img3=PhotoImage(file='imgs/about.png')
    btn4_nav=Button(root,text='About',compound='left',image=img3,fg='white',bg='#A97653',font=('',"13", "bold"),bd=0,padx=8,pady=8,command=toabout)
    btn4_nav.place(x=50,y=350)

    img4=PhotoImage(file='logout.png')
    btn5_nav=Button(root,text='Logout',compound='left',image=img4,fg='white',bg='#A97653',font=('',"13", "bold"),bd=0,padx=8,pady=8,command=tologin)
    btn5_nav.place(x=1200,y=30)


    info=Label(root,text="For more information\n\n981100222, 01-42086",fg='white',bg='#A97653',font=('',"13", "bold"))
    info.place(x=60,y=600)



    root.mainloop()

if __name__ == "__main__":
    display_home()