from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import os
from Assistant import greet, awaken, user




Assistant=Tk()
Assistant.title("Natasha")
width=700
height=630
Assistant_Width = Assistant.winfo_screenwidth() # width of the screen
Assistant_Height = Assistant.winfo_screenheight() # height of the screen
Assistant.resizable(False,False)


Assistant.config(background='#85a9d6')

Assistant.config
x = (Assistant_Width /2) - (width /2)
y = (Assistant_Height /2) - (height /2)

Assistant.geometry('%dx%d+%d+%d' % (width, height, x,y))

Exit_Button_Imng = PhotoImage(file="Src\Exit.png")
Listen_Button_Imng = PhotoImage(file="Src\Listen.png")

datasheet = 'https://www.youtube.com/watch?v=eBGIQ7ZuuiU&ab_channel=YouGotRickRolled'

global Login_Check
Login_Check=0

global Config_Check
Config_Check=0
#Buttons used in order to move around

def Config():
    
    Menu_Natasha.select(1)
    

def Close():
    
    Assistant.destroy()

def Listen_WA():
    if Login_Check==1:
        awaken()
        
        
    else:
        messagebox.showerror("Error","Login/Setup in order to use the program!")

def How_To_Use():
    webbrowser.open_new(datasheet)

def GoBack():
    Menu_Natasha.select(0)

def GoLogin():
        global Login_Check #Used in order to be able to modify the global variable inside the subprogram
        if Login_Check == 0:
            Menu_Natasha.select(2)
        else:
            messagebox.showerror("Error","Already logged!")
def VA_Data():
     global Config_Check
     if Username.get()=="" or Password1.get()=="" or Password2.get()=="" or City.get()=="" or Email.get()=="" or Phone.get()=="":
        messagebox.showerror("Error","All fields are required!")
     elif Password1.get()!=Password2.get():
        messagebox.showerror("Error","Passwords do not match")
     else:
        username=Username.get()
        print(username)
        password1=Password1.get()
        print(password1)
        password2=Password2.get()
        print(password2)
        city=City.get()
        print(city)
        email=Email.get()
        print(email)
        phone=Phone.get()
        print(phone)
        Config_Check=1
        
        Lists_of_Users = os.listdir()
        if username in Lists_of_Users:
                messagebox.showerror("Error","User already exists!")
                User_TextBox.delete(0, END)
                Password_TextBox.delete(0, END)
                Password2_TextBox.delete(0, END)
                City_TextBox.delete(0, END)
                Email_TextBox.delete(0, END)
                Phone_TextBox.delete(0, END)
        else:

            file = open(username, "w")
            file.write(username +"\n")
            file.write(password1 + "\n")
            file.write(city + "\n")
            file.write(email + "\n")
            file.write(phone + "\n")
            file.close()

            User_TextBox.delete(0, END)
            Password_TextBox.delete(0, END)
            Password2_TextBox.delete(0, END)
            City_TextBox.delete(0, END)
            Email_TextBox.delete(0, END)
            Phone_TextBox.delete(0, END)
            messagebox.showerror("Congrats!","User Added!")
            Menu_Natasha.select(0)
       
def Login_C():
            global Login_Check
            if Login_Username.get()=="" or Login_Password.get()=="":
                messagebox.showerror("Error","All fields are required in order to login!")
            else:

                user_login=Login_Username.get()
                password_login=Login_Password.get()
                print(user_login)   
                print(password_login)
                
                
                Lists_of_Users = os.listdir()
                if user_login in Lists_of_Users:
                    Current_file=open(user_login,"r")
                    Check=Current_file.read().splitlines()
                    print(Check)
                    if password_login in Check:
                        messagebox.showinfo("Congrats!","Welcome "+ user_login + "!")
                        Menu_Natasha.select(0)
                        Login_Check=1
                        user=user_login
                        User_TextBox_Login.delete(0, END)
                        Password_TextBox_Login.delete(0, END)
                        greet()
                    else:
                        messagebox.showerror("Error","Wrong Password!")
                        Password_TextBox_Login.delete(0, END)
                else:
                    messagebox.showerror("Error","User Not Found!")





Menu_Natasha=ttk.Notebook(Assistant)
Menu_Natasha.pack()

Page1=Frame(Menu_Natasha,width=700,height=630,background='#85a9d6' )
Page2=Frame(Menu_Natasha,width=700,height=630,background='#85a9d6',)
Page3=Frame(Menu_Natasha,width=700,height=630,background='#85a9d6',)

Page1.pack(fill="both",expand=0)

Page2.pack(fill="both",expand=0)

Page3.pack(fill="both",expand=0)

Menu_Natasha.add(Page1,text="Menu")
Menu_Natasha.add(Page2,text="Setup")
Menu_Natasha.add(Page3,text="Login")

#Buttons used for the Main Menu

Titlu=Label(Page1,text="Natasha Assistant", fg="black", font=('Arial 30 bold'),bg="#85a9d6")
Titlu.place(x=350, y=80, anchor="center")    


Listen=Button(Page1,command=Listen_WA,text="Listen!",image=Listen_Button_Imng,bg="#85a9d6",fg="black" ,height = 100, width = 100,highlightthickness = 0, bd = 0,font=('Arial  25'))
Listen.place(x=350, y=175, anchor="center")

Login=Button(Page1,command=GoLogin,text="Login",bg="#85a9d6",fg="black" ,height = 1, width = 10,highlightthickness = 0, bd = 0,font=('Arial  30'))
Login.place(x=350, y=275, anchor="center")

Setup=Button(Page1,command=Config,text="Setup",bg="#85a9d6",fg="black" ,height = 1, width = 10,highlightthickness = 0, bd = 0,font=('Arial  30'))
Setup.place(x=350, y=350, anchor="center")

Instructions=Button(Page1,command=How_To_Use,text="Instructions",bg="#85a9d6",fg="black" ,height = 1, width = 10,highlightthickness = 0, bd = 0,font=('Arial  30'))
Instructions.place(x=350, y=425, anchor="center")

Exit=Button(Page1,command=Close,text="Exit",image=Exit_Button_Imng,bg="#85a9d6",fg="black" ,height = 100, width = 150,highlightthickness = 0, bd = 0,font=('Arial  25'))
Exit.place(x=350, y=525, anchor="center")

#Configurate menu
Username=StringVar()
Password1=StringVar()
Password2=StringVar()
City=StringVar()
Email=StringVar()
Phone=StringVar()

Configurate=Label(Page2,text="Configure", fg="black", font=('Arial 30 bold'),bg="#85a9d6")
Configurate.place(x=345, y=50, anchor="center")

user_label=Label(Page2,text="Username:", fg="black", font=('Arial 14 bold'),bg="#85a9d6")
user_label.place(x=140, y=150, anchor="center")

User_TextBox=Entry(Page2,textvariable=Username,fg="black", font=('Arial 14'),bg="white")
User_TextBox.place(x=350, y=150, anchor="center")


password_label1=Label(Page2,text="Password:", fg="black", font=('Arial 14 bold'),bg="#85a9d6")
password_label1.place(x=140, y=210, anchor="center")

Password_TextBox=Entry(Page2,show='*',textvariable=Password1,fg="black", font=('Arial 14'),bg="white")
Password_TextBox.place(x=350, y=210, anchor="center")

password_label2=Label(Page2,text="Confirm Password:",fg="black", font=('Arial 14 bold'),bg="#85a9d6")
password_label2.place(x=100, y=270, anchor="center")

Password2_TextBox=Entry(Page2,show='*',textvariable=Password2,fg="black", font=('Arial 14'),bg="white")
Password2_TextBox.place(x=350, y=270, anchor="center")

City_label=Label(Page2,text="City:", fg="black", font=('Arial 14 bold'),bg="#85a9d6")
City_label.place(x=165, y=330, anchor="center")

City_TextBox=Entry(Page2,textvariable=City,fg="black", font=('Arial 14'),bg="white")
City_TextBox.place(x=350, y=330, anchor="center")

email_label=Label(Page2,text="Email:", fg="black", font=('Arial 14 bold'),bg="#85a9d6")
email_label.place(x=155, y=390, anchor="center")

Email_TextBox=Entry(Page2,textvariable=Email,fg="black", font=('Arial 14'),bg="white")
Email_TextBox.place(x=350, y=390, anchor="center")

phone_label=Label(Page2,text="Phone Number:", fg="black", font=('Arial 14 bold'),bg="#85a9d6")
phone_label.place(x=115, y=450, anchor="center")

Phone_TextBox=Entry(Page2,textvariable=Phone,fg="black", font=('Arial 14'),bg="white")
Phone_TextBox.place(x=350, y=450, anchor="center")

Config=Button(Page2,command=VA_Data,text="Config!",bg="#85a9d6",fg="black",highlightthickness = 0, bd = 0,font=('Arial  25'))
Config.place(x=250, y=530, anchor="center")   

Back=Button(Page2,command=GoBack,text="Back",bg="#85a9d6",fg="black",highlightthickness = 0, bd = 0,font=('Arial  25'))
Back.place(x=450, y=530, anchor="center")   


#Login
Login_Username=StringVar()
Login_Password=StringVar()

Configurate=Label(Page3,text="Login", fg="black", font=('Arial 40 bold'),bg="#85a9d6")
Configurate.place(x=345, y=75, anchor="center")

user_login=Label(Page3,text="Username:", fg="black", font=('Arial 14 bold'),bg="#85a9d6")
user_login.place(x=140, y=150, anchor="center")

User_TextBox_Login=Entry(Page3,textvariable=Login_Username,fg="black", font=('Arial 14'),bg="white")
User_TextBox_Login.place(x=350, y=150, anchor="center")

password_login=Label(Page3,text="Password:", fg="black", font=('Arial 14 bold'),bg="#85a9d6")
password_login.place(x=140, y=210, anchor="center")

Password_TextBox_Login=Entry(Page3,show='*',textvariable=Login_Password,fg="black", font=('Arial 14'),bg="white")
Password_TextBox_Login.place(x=350, y=210, anchor="center")

Login=Button(Page3,command=Login_C,text="Login!",bg="#85a9d6",fg="black",highlightthickness = 0, bd = 0,font=('Arial  25'))
Login.place(x=250, y=280, anchor="center")   

Fall_Back=Button(Page3,command=GoBack,text="Back",bg="#85a9d6",fg="black",highlightthickness = 0, bd = 0,font=('Arial  25'))
Fall_Back.place(x=450, y=280, anchor="center")  



Assistant.mainloop()
