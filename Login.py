from tkinter import *
from tkinter import messagebox

# Thi Huong Giang nguyen
# Date: 22/11/2021


class LoginWindow():
    def __init__(self):
        self.win = Tk()
        self.win.geometry("400x800")
        self.win.title("Acme Bank")
        self.labelTitle = Label(self.win, text="ACME BANKING SYSTEM", font="ar 25 bold")
        self.labelTitle.place(x=25, y=25)

        self.login_success = True

        # label
        self.userNameLabel = Label(self.win, text="UserName")
        self.userNameLabel.place(x = 50, y= 100)
        self.passwordLabel = Label(self.win, text="Password")
        self.passwordLabel.place(x = 50, y= 150)

        # textfield
        self.userNameValue = StringVar()
        self.passwordValue = StringVar()

        self.userNameEntry = Entry(self.win, textvariable= self.userNameValue)
        self.passwordEntry = Entry(self.win, textvariable= self.passwordValue, show="*")

        self.userNameEntry.place(x = 150, y= 100)
        self.passwordEntry.place(x = 150, y= 150)


        # button
        self.button1 = Button(self.win, text="1", font="ar 20 bold")
        self.button1.place(x = 50, y= 200, width = 100, height = 100)
        self.button2 = Button(self.win, text="2", font="ar 20 bold")
        self.button2.place(x = 150, y= 200, width = 100, height = 100)
        self.button3 = Button(self.win, text="3", font="ar 20 bold")
        self.button3.place(x = 250, y= 200, width = 100, height = 100)
        self.button4 = Button(self.win, text="4", font="ar 20 bold")
        self.button4.place(x = 50, y= 300, width = 100, height = 100)
        self.button5 = Button(self.win, text="5", font="ar 20 bold")
        self.button5.place(x = 150, y= 300, width = 100, height = 100)
        self.button6 = Button(self.win, text="6", font="ar 20 bold")
        self.button6.place(x = 250, y= 300, width = 100, height = 100)
        self.button7 = Button(self.win, text="7", font="ar 20 bold")
        self.button7.place(x = 50, y= 400, width = 100, height = 100)
        self.button8 = Button(self.win, text="8", font="ar 20 bold")
        self.button8.place(x = 150, y= 400, width = 100, height = 100)
        self.button9 = Button(self.win, text="9", font="ar 20 bold")
        self.button9.place(x = 250, y= 400, width = 100, height = 100)

        self.buttonClear = Button(self.win, text="Clear", font="ar 15 bold", bg="red", command = self.clear)
        self.buttonClear.place(x = 50, y= 500, width = 100, height = 100)
        self.button0 = Button(self.win, text="0", font="ar 20 bold", height=3, width=3)
        self.button0.place(x = 150, y= 500, width = 100, height = 100)
        self.buttonLogin = Button(self.win, text="Login", font="ar 15 bold", bg="#2BF073", command = self.login)
        self.buttonLogin.place(x = 250, y= 500, width = 100, height = 100)

        #bind event
        self.button1.bind('<Button-1>', self.clicked)
        self.button2.bind('<Button-1>', self.clicked)
        self.button3.bind('<Button-1>', self.clicked)
        self.button4.bind('<Button-1>', self.clicked)
        self.button5.bind('<Button-1>', self.clicked)
        self.button6.bind('<Button-1>', self.clicked)
        self.button7.bind('<Button-1>', self.clicked)
        self.button8.bind('<Button-1>', self.clicked)
        self.button9.bind('<Button-1>', self.clicked)
        self.button0.bind('<Button-1>', self.clicked)
        # self.userNameEntry.bind('<Button-1>', self.clearUser)
        
        
    # def clearUser(self, event):
    #      self.userNameEntry.delete(0, 'end')

    def clicked(self, event):
        if self.win.focus_get() == self.userNameEntry:
            self.userNameEntry.insert(END, str(event.widget['text']))
        elif self.win.focus_get() ==self.passwordEntry:
            self.passwordEntry.insert(END, str(event.widget['text']))
        
    #clear btn
    def clear(self):
        self.userNameEntry.delete(0, 'end')
        self.passwordEntry.delete(0, 'end')

    #login btn
    def login(self):
        inputUser = self.userNameEntry.get()
        inputPw = self.passwordEntry.get()

        try: 
            input = []
            file = open('loginDetail.txt', 'r')
            lines = file.readlines()
            for line in lines:
                each_line = line.strip().split(" ")
                input.append(each_line)

            default_username = input[0][1]
            default_password = input[0][2]

            
            if (inputUser == default_username) and (inputPw == default_password):
                messagebox.showinfo("", "Login Success")
                self.win.destroy()
                self.login_success = True
            elif (inputUser != default_username) and (inputPw == default_password):
                messagebox.showinfo("", "username is not correct")
                self.login_success = False
            elif (inputUser == default_username) and (inputPw != default_password):
                messagebox.showinfo("", "password is not correct")
                self.login_success = False
            else:
                messagebox.showinfo("", "Username or password incorrect")
                self.login_success = False
                self.userNameValue.set("")
                self.passwordValue.set("")

            file.close()

        except FileNotFoundError:
            print("File is not found")


        
        
        



myWin = LoginWindow()
myWin.win.mainloop()