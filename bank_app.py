from tkinter import * 
import tkinter as tk
import pymysql as sql
from tkinter import messagebox


class Bank:
    def __init__(self,master):
        self.master = master()
        self.master.title('BANK Application')
        self.ws=self.master.winfo_screenwidth()
        self.hs=self.master.winfo_screenheight()

        self.master.wm_minsize(self.ws,self.hs)

        self.menu_forget = False
    def run(self):
        self.main_frame()
    def menu(self):

        self.menu = tk.Frame(self.master,bg="gray")
        
        self.m_b1 = tk.Button(self.menu,text='Debit',bg="gray",font=('Times','30','bold'),command=self.show_f,fg="#003b8b")
        self.m_b1.grid(row=1,column=0,padx=30,pady=10)

        self.m_b2 = tk.Button(self.menu,text='Credit',bg="gray",font=('Times','30','bold'),command=self.show_f,fg="#003b8b")
        self.m_b2.grid(row=2,column=0,padx=30,pady=20)
        
        self.m_b3 = tk.Button(self.menu,text='Update Profile',bg="gray",font=('Times','30','bold'),command=self.show_f,fg="#003b8b")
        self.m_b3.grid(row=3,column=0,padx=30,pady=30)


        self.m_b4 = tk.Button(self.menu,text='Log Out',bg="gray",font=('Times','30','bold'),command=self.show_f,fg="#ff0000")
        self.m_b4.grid(row=4,column=0,padx=30,pady=40)
        
        self.menu.grid(padx=self.ws*.4,pady=self.hs*.2)

    def show_f(self):
        self.menu.grid_forget()
        self.menu_forget = True
        self.f.grid()
    
    def main_frame(self):

        self.f = Frame(self.master,bg='gray')
        Bank.username = StringVar()
        Bank.password = StringVar()

        self.l1 = Label(self.f,text='UserName : ',bg='gray',font=('Times','30','bold'),fg='#123456')
        self.l1.grid(row=0,column=0,ipadx=50,pady=50)
        self.e1 = Entry(self.f,textvariable=Bank.username,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.e1.grid(row=0,column=1,padx=30,pady=50)

        self.l2 = Label(self.f,text='Password : ',bg='gray',font=('Times','30','bold'),fg='#123456')
        self.l2.grid(row=1,column=0,ipadx=50)
        
        
        self.e2 = Entry(self.f,textvariable=Bank.password,show='*',bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.e2.grid(row=1,column=1,padx=30)
        
        self.b3 = Button(self.f,bg='gray',text='forget forward ?',font=('Times','12','bold'),command=self.login,fg='red',activeforeground='#123456',width=30,bd=0)
        self.b3.grid(row=2,column=1)



        self.b1 = Button(self.f,bg='gray',text='LOGIN',font=('Times','20','bold'),command=self.login,fg='#123456')
        self.b1.grid(row=3,column=0,columnspan=4,padx=20,pady=50)
        
        self.b2 = Button(self.f,bg='gray',text='SIGNUP',font=('Times','20','bold'),command=self.login,fg='#123456')
        self.b2.grid(row=3,column=1,columnspan=4)
        
        self.master.bind('<Return>',self.login)
        self.f.grid(padx=self.ws*.3,pady=self.hs*.2)



    def login(self,event=None):
        UserName = self.e1.get()
        Password = self.e2.get()
        print(UserName)
        print(Password)
        try :

            db = sql.connect('localhost','bank','bank','bank')
            c = db.cursor()
            cmd = "select * from user where name = '{}'".format(UserName)
            c.execute(cmd)
            data = c.fetchone()
            self.password.set('')
            if data : 
                if Password == data[2] : 
                    self.f.grid_forget()
                    #messagebox.showinfo("Information","!!Khud bhi kuch karo sara main hi karoo yaha")
                    if self.menu_forget : 
                        self.menu.grid()
                    else :

                        self.menu()
                
                else : 
                    messagebox.showerror("Error","!!Invalid Password")

            else : 
                messagebox.showerror("Error","!!No such user exists")
                Bank.username.set('')
        except Exception as e : 
            print("Errorr something is wrong",e)
            messagebox.showerror("Error","!!Check Data BAse Connectivity {}".format(e))




root = Bank(Tk)
root.run()
mainloop()

