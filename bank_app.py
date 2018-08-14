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
        self.master.configure(background='#666666')
        self.menu_forget = False
        self.upd_pass=False
        self.upd_name=False

    def run(self):
        self.main_frame()

    def menu(self):

        self.menu = tk.Frame(self.master,bg="#777777")

        self.m_l1 = Label(self.menu,text='Welcome {}'.format(Bank.data[1]),bg="#777777",font=('Times','20','bold'),fg="#ffffff")
        self.m_l1.grid(row=0,column=0,padx=60,pady=10)

        self.m_b1 = tk.Button(self.menu,text='DEBIT',bg="#777777",width=10,font=('Times','20','bold'),command=self.debframe,fg="#003b8b")
        self.m_b1.grid(row=1,column=0,padx=60,pady=10)

        self.m_b2 = tk.Button(self.menu,text='CREDIT',width=10,bg="#777777",font=('Times','20','bold'),command=self.credframe,fg="#003b8b")
        self.m_b2.grid(row=2,column=0,padx=76,pady=20)

        self.m_b3 = tk.Button(self.menu,text='Profile',bd=0,bg="#777777",font=('Times','20','bold'),command=self.show_profile,fg="#aadcba")
        self.m_b3.grid(row=0,column=1,padx=76,pady=25)


        self.m_b4 = tk.Button(self.menu,text='LOGOUT',width=10,bg="#777777",font=('Times','18','bold'),command=self.show_f,fg="#ff0000")

        self.m_b4.grid(row=3,column=1,padx=76,pady=15)
        self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)

    def credframe(self):

        self.credframe = tk.Frame(self.menu,bg="#777777")

        self.up_amnt_lbl = Label(self.credframe,text='Enter amount to credit',bg="gray",font=('Times','30','bold'),fg="#00ff00")
        self.up_amnt_lbl.grid(row=0,column=0,pady=10)

        self.up_amnt = Entry(self.credframe,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.up_amnt.grid(row=1,column=0,pady=10)

        self.up_amnt_btn = tk.Button(self.credframe,text='update balance',bg="#777777",font=('Times','20','bold'),command=self.credit,fg="#aadcba")
        self.up_amnt_btn.grid(row=2,column=0,pady=10)


        self.credframe.grid(row=4,column=0,padx=76,pady=25)

    def debframe(self):

        self.debframe = tk.Frame(self.menu,bg="#777777")

        self.up_amnt_lbl = Label(self.debframe,text='Enter amount to debit ',bg="gray",font=('Times','30','bold'),fg="#00ff00")
        self.up_amnt_lbl.grid(row=0,column=0,pady=10)

        self.up_amnt = Entry(self.debframe,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.up_amnt.grid(row=1,column=0,pady=10)

        self.up_amnt_btn = tk.Button(self.debframe,text='update balance',bg="#777777",font=('Times','20','bold'),command=self.debit,fg="#aadcba")
        self.up_amnt_btn.grid(row=2,column=0,pady=10)


        self.debframe.grid(row=4,column=0,padx=76,pady=25)



    def credit(self):
        acc=Bank.data[0]
        amnt=self.up_amnt.get()

        cmd="update user SET balance=balance+{} where acc='{}'".format(amnt,acc)
        Bank.c.execute(cmd)
        Bank.db.commit()

        s='\n'+str(amnt)+' credited to the account  {} '.format(acc)

        messagebox.showinfo("CREDIT",s)

    def debit(self):
        acc=Bank.data[0]
        amnt=float(self.up_amnt.get())
        print('amnt:',amnt)
        print('balance',Bank.data[3])


        if amnt <= Bank.data[3]:
            cmd="update user SET balance=balance-{} where acc='{}'".format(amnt,acc)
            Bank.c.execute(cmd)
            Bank.db.commit()

            s='\n'+str(amnt)+' debited from the account {} '.format(acc)

        else:
            s='\nInsufficient balance for the account {}\n'.format(acc)

        messagebox.showinfo("Debit",s)


    def show_f(self):
        self.menu.grid_forget()
        self.menu_forget = True
        self.f.grid(padx=self.ws*.3,pady=self.hs*.2)

    def show_m(self):
        self.profframe.grid_forget()
        self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)


    def show_profile(self):

        self.menu.grid_forget()
        self.profframe = tk.Frame(self.master,bg="gray")
        #print(Bank.data)
        self.p_l1 = Label(self.profframe,text='Account No:{}'.format(Bank.data[0]),bg="#777777",font=('Times','18','bold'),fg="#ffffff")
        self.p_l1.grid(row=0,column=0,columnspan=2,padx=64)

        self.p_l2 = Label(self.profframe,text='User Name:{}'.format(Bank.data[1]),bg="#777777",font=('Times','18','bold'),fg="#ffffff")
        self.p_l2.grid(row=1,column=0,columnspan=2,padx=64)

        #print(Bank.data)
        self.p_l3 = Label(self.profframe,text='Balance:{}'.format(Bank.data[3]),bg="#777777",font=('Times','18','bold'),fg="#ffffff")
        self.p_l3.grid(row=2,column=0,columnspan=2,padx=64)


        self.p_b1 = tk.Button(self.profframe,text='Change Name',bg="#777777",font=('Times','20','bold'),width=13,command=self.showupdnameframe,fg="#003b8b")
        self.p_b1.grid(row=3,column=0,padx=64,pady=19)

        self.p_b2 = tk.Button(self.profframe,text='Change Password',bg="#777777",font=('Times','20','bold'),width=13,command=self.showupdpassframe,fg="#003b8b")
        self.p_b2.grid(row=4,column=0,padx=64,pady=10)

        self.p_b3 = tk.Button(self.profframe,text='<<Back',width=10,bg="#777777",font=('Times','18','bold'),command=self.show_m,fg="#000000")
        self.p_b3.grid(row=5,column=1,padx=64,pady=18)

        self.profframe.grid(padx=self.ws*.3,pady=self.hs*.2)

    def cmdupd(self):
        acc=Bank.data[0]
        cmd="update user SET name='{}' where acc='{}'".format(self.up_name.get(),acc)
        print(cmd)
        try:
            Bank.c.execute(cmd)
            Bank.db.commit()

            s='\nName updated successfully for account {} '.format(acc)
        except Exception as e:
            s='Error in updating name{}'.format(e)

        messagebox.showinfo("Information",s)

    def cmdupdpass(self):
        acc=Bank.data[0]

        if(Bank.data[2]==self.up_opass.get()):
            npasswd=self.up_npass.get()

            cmd="update user SET password='{}' where acc='{}'".format(npasswd,acc)
            print(cmd)

            try:
                Bank.c.execute(cmd)
                Bank.db.commit()

                s='\nPassword updated successfully for account {}'.format(acc)
            except Exception as e:
                s='Some error occured{}'.format(e)
        else:
            s='\nPassword mismatch!Try again  for account {}'.format(acc)

        messagebox.showinfo("Information",s)



    def updpass(self):

        self.passupdate = tk.Frame(self.profframe,bg="gray")

        self.up_opass_lbl = Label(self.passupdate,text='Old password:',bg="gray",font=('Times','30','bold'),fg="#00ff00")
        self.up_opass_lbl.grid(row=0,column=0)

        self.up_opass = Entry(self.passupdate,bg='#123456',show="*",width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.up_opass.grid(row=0,column=1)

        self.up_npass_lbl = Label(self.passupdate,text='New password:',bg="gray",font=('Times','30','bold'),fg="#00ff00")
        self.up_npass_lbl.grid(row=1,column=0)

        self.up_npass = Entry(self.passupdate,bg='#123456',width=20,show="*",font=('Times','20','bold'),fg='#FFFFFF')
        self.up_npass.grid(row=1,column=1)

        self.pass_b1=tk.Button(self.passupdate,text="Update",bg="gray",font=('Times','20','bold'),command=self.cmdupdpass,fg="#000000")
        self.pass_b1.grid(row=1,column=2,padx=30,pady=10)

        self.passupdate.grid(row=6,column=0)

    def showupdnameframe(self):

        if self.upd_pass :
            self.passupdate.destroy()
            self.upd_pass=False
            self.updname()

        else :
            self.updname()

        self.upd_name=True

    def showupdpassframe(self):

        if self.upd_name :
            self.nameupdate.destroy()
            self.upd_name=False
            self.updpass()

        else :
            self.updpass()

        self.upd_pass=True


    def updname(self):


        acc=Bank.data[0]
        self.nameupdate = tk.Frame(self.profframe,bg="gray")


        self.up_name_lbl = Label( self.nameupdate,text='New name:',bg="gray",font=('Times','30','bold'),fg="#00ff00")
        self.up_name_lbl.grid(row=0,column=0)

        self.up_name = Entry( self.nameupdate,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.up_name.grid(row=0,column=1)

        self.name_b1=tk.Button( self.nameupdate,text="Update",bg="gray",font=('Times','20','bold'),command=self.cmdupd,fg="#000000")
        self.name_b1.grid(row=0,column=2,padx=30,pady=10)

        self.nameupdate.grid(row=6,column=0)


    def main_frame(self):

        self.f = Frame(self.master,bg='#777777')
        Bank.username = StringVar()
        Bank.password = StringVar()

        self.l0 = Label(self.f,text="Welcome To PYTHON Banking Services",bg='#777777',font=('Times','20','bold'),fg='#abcdef')
        self.l0.grid(row=0,column=0,columnspan=3)

        self.l1 = Label(self.f,text='UserName : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
        self.l1.grid(row=1,column=0,ipadx=40,pady=30)

        self.e1 = Entry(self.f,textvariable=Bank.username,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.e1.grid(row=1,column=1)

        self.l2 = Label(self.f,text='Password : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
        self.l2.grid(row=2,column=0)



        self.e2 = Entry(self.f,textvariable=Bank.password,show='*',bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.e2.grid(row=2,column=1,padx=20)

        self.b3 = Button(self.f,bg='#777777',text='forget forward ?',font=('Times','12','bold'),command=self.login,fg='red',width=30,bd=0)
        self.b3.grid(row=3,column=1)

        self.b1 = Button(self.f,bg='#777777',text='LOGIN',font=('Times','20','bold'),command=self.login,fg='#123456')
        self.b1.grid(row=4,column=0,columnspan=4,padx=19,pady=31)

        self.b2 = Button(self.f,bg='#777777',text='SIGNUP',font=('Times','20','bold'),command=self.signup,fg='#123456')
        self.b2.grid(row=4,column=1,columnspan=4)

        self.master.bind('<Return>',self.login)

        self.f.grid(padx=self.ws*.3,pady=self.hs*.2)
        #self.f.grid_propagate(False)

    def show_sf(self):
            self.sp.grid_forget()
            self.menu_forget = True
            self.f.grid(padx=self.ws*.3,pady=self.hs*.2)




    def signup(self):

            self.bal = StringVar()
            self.uname = StringVar()
            self.creds = StringVar()

            self.f.grid_forget()
            self.sp = Frame(self.master,bg='#777777')

            self.sl1 = Label(self.sp,text='UserName : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
            self.sl1.grid(row=0,column=0,ipadx=40,pady=28)

            self.se1 = Entry(self.sp,textvariable=self.uname,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
            self.se1.grid(row=0,column=1)

            self.sl2 = Label(self.sp,text='Password : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
            self.sl2.grid(row=1,column=0)

            self.se2 = Entry(self.sp,textvariable=self.creds,show='*',bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
            self.se2.grid(row=1,column=1,padx=20)

            self.sl3 = Label(self.sp,text='Balance : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
            self.sl3.grid(row=2,column=0,ipadx=42,pady=27)

            self.se3 = Entry(self.sp,textvariable=self.bal,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
            self.se3.grid(row=2,column=1)


            self.sb2 = Button(self.sp,bg='#777777',text='SIGNUP',font=('Times','20','bold'),command=self.mksignup,fg='#123456')
            self.sb2.grid(row=3,column=1,columnspan=4)

            self.sb3 = tk.Button(self.sp,text='<<Back',width=10,bg="#777777",font=('Times','18','bold'),command=self.show_sf,fg="#000000")
            self.sb3.grid(row=3,column=0,padx=66,pady=17)
            #self.master.bind('<Return>',self.login)
            self.sp.grid(padx=self.ws*.3,pady=self.hs*.2)

    def mksignup(self):

        uname = self.uname.get()
        password  = self.creds.get()
        balance = self.bal.get()
        # print("User ",uname)
        # print("Password ",password)
        # print("Balance ",balance)
        try :
            db = sql.connect('localhost','bank','bank','bank')
            c = db.cursor()
            c.execute('select * from user where name="{}"'.format(uname))
            d = c.fetchone()
            if d :
                messagebox.showerror("UserExist","User with this name is already exists.\n Please Login if you are already a user \nelse choose another name")
            else :
                cmd = "insert into user(name,password,balance) values('{}','{}',{})".format(uname,password,balance)
                c.execute(cmd)
                db.commit()
            messagebox.showinfo("Account Created","Congratulations!! Your Account is Successfully Created\nPlease LOGIN to Enjoy your services")
            self.sp.grid_forget()
            self.f.grid(padx=self.ws*.3,pady=self.hs*.2)


        except Exception as e :
            print("Error!!",e)

    def login(self,event=None):

        UserName = self.e1.get()
        Password = self.e2.get()

        #print(UserName)
        #print(Password)

        try :

            Bank.db = sql.connect('localhost','bank','bank','bank')
            Bank.c = Bank.db.cursor()
            cmd = "select * from user where name = '{}'".format(UserName)

            Bank.c.execute(cmd)
            Bank.data = Bank.c.fetchone()


           # c.execute(cmd)

            #Bank.data = c.fetchone()

            self.password.set('')

            if Bank.data :

                if Password == Bank.data[2] :

                    self.f.grid_forget()
                    #messagebox.showinfo("Information","!!Khud bhi kuch karo sara main hi karoo yaha")
                    if self.menu_forget :
                        self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)

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
