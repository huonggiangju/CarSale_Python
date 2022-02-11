from tkinter import * 
import sqlite3 
from tkinter import messagebox
from openpyxl import Workbook

# Thi Huong Giang nguyen
# Date: 22/11/2021


class CarSaleWindow():
    def __init__(self):
        self.win = Tk()
        self.win.geometry("1100x700")
        self.win.title("Car Sales")
        self.win.configure(bg="#F5F5DC")


        self.labelTitle = Label(self.win,text = "Dodge Brothers Motor Manager", font = "ar 20 bold")
        self.labelTitle.place(x = 200, y = 0)

        #customer detail
        self.custDetail = Label(self.win, text = "Customer details:", font="ar 15 bold")
        self.custName = Label(self.win, text = "Customer name *")
        self.custPhone = Label(self.win, text = "Customer phone *")
        self.vehiclePrice = Label(self.win, text = "Vehicle Price *")
        self.lessTradeIn = Label(self.win, text = "Less Trade In")

        self.custDetail.place(x = 50, y = 50)
        self.custName.place(x = 50, y = 100)
        self.custPhone.place(x = 50, y = 150)
        self.vehiclePrice.place(x = 50, y = 200)
        self.lessTradeIn.place(x = 50, y = 250)

        #textfield
        self.name = StringVar()
        self.phone = StringVar()
        self.price = StringVar()
        self.tradeIn = StringVar()
        self.subAmount = StringVar()
        self.gstAmount = StringVar()
        self.finalAmount = StringVar()

        self.custNameEntry = Entry(self.win, textvariable = self.name)
        self.custPhoneEntry = Entry(self.win, textvariable = self.phone)
        self.vehiclePriceEntry = Entry(self.win, textvariable = self.price)
        self.lessTradeInEntry = Entry(self.win, textvariable = self.tradeIn)

        self.custNameEntry.place(x = 200, y = 100)
        self.custPhoneEntry.place(x = 200, y = 150)
        self.vehiclePriceEntry.place(x = 200, y = 200)
        self.lessTradeInEntry.place(x = 200, y = 250)

        # =========calculated frame ============
        self.calculationLb = Label(self.win, text = "Calculation: ", font="ar 15 bold")
        self.subAmountLb = Label(self.win, text = "Sub Amount")
        self.gstAmountLb = Label(self.win, text = "GST amount")
        self.finalAmountLb = Label(self.win, text = "Final Amount")

        self.calculationLb.place(x = 50, y = 300)
        self.subAmountLb.place(x = 50, y = 350)
        self.gstAmountLb.place(x = 50, y = 400)
        self.finalAmountLb.place(x = 50, y = 450)

        #textfield
        self.subAmountEntry = Entry(self.win, textvariable = self.subAmount)
        self.gstAmountEntry = Entry(self.win, textvariable = self.gstAmount)
        self.finalAmountEntry = Entry(self.win, textvariable = self.finalAmount)

        self.subAmountEntry.place(x = 200, y = 350)
        self.gstAmountEntry.place(x = 200, y = 400)
        self.finalAmountEntry.place(x = 200, y = 450)

        #btn frame
        self.saveBtn = Button(self.win, text="Save", command = self.save)
        self.saveBtn.place(x = 600, y = 100, width = 120, height = 50)
        self.resetBtn = Button(self.win, text="Reset", command = self.reset)
        self.resetBtn.place(x = 600, y = 160, width = 120, height = 50)
        self.summaryBtn = Button(self.win, text="Summary", command = self.summary)
        self.summaryBtn.place(x = 600, y = 220, width = 120, height = 50)
        
        #picture frame
        self.picTitle = Label(self.win, text = "Programmed by TAFESA ITWorkd Team", font="ar 15 bold")
        self.picTitle.place(x = 500, y = 300)
        
        self.image = PhotoImage(file = 'car1.png')
        self.picture = Label(self.win, image=self.image)
       
        self.picture.place(x = 550, y = 350)


    def reset(self):
        self.name.set("")
        self.phone.set("")
        self.price.set("")
        self.tradeIn.set("")
        self.subAmount.set("")
        self.gstAmount.set("")
        self.finalAmount.set("")

    #connect DB
    def connect(self):
        try: 
            conn =sqlite3.connect("data.db")
            return conn
        except Exception as e:
            print("error is: ", e)

        #create tables
    def create_table(self, conn):
        with conn:
            command1 = """CREATE TABLE IF NOT EXISTS customer_detail(cus_id INTERGER PRIMARY KEY,
                            customerName TEXT, customerPhone TEXT, GSTAmount DOUBLE, FinalAmount DOUBLE );""" 
            conn.execute(command1)

    #insert value 
    def insert_data( self,conn):
        with conn:        
            insert = """INSERT INTO customer_detail(customerName, customerPhone, GSTAmount, FinalAmount)
                        VALUES (?, ?, ?, ?); """

            conn.execute(insert, (self.name.get(), self.phone.get(), self.gstAmount.get(), self.finalAmount.get()))
            conn.commit()
            messagebox.showinfo("", "Data was save successfully")

    #get all data
    def get_all_data(self, conn):
        with conn:
            results = conn.execute("SELECT * FROM customer_detail").fetchall()
            return results
            
            
    #validate blank field
    def isRequired(self):
        if (self.name.get() == ""):
            messagebox.showinfo("", "name is not blank")
            return False
        elif (self.phone.get() == ""):
            messagebox.showinfo("", "Phone is not blank")
            return False
        elif (self.price.get() == ""):
            messagebox.showinfo("", "Price is not blank")
            return False
        return True

    #validate number
    def isNumber(self):
        if self.phone.get().isnumeric() == False:
            messagebox.showinfo("", "Phone must be numbers only")
        elif self.price.get().isnumeric() == False:
            messagebox.showinfo("", "Price must be numbers only")
        elif self.tradeIn.get().isnumeric() == False:
            messagebox.showinfo("", "Trade In must be numbers only")      
        return True

    def save(self):      
        if (self.isRequired() ==  True) and (self.isNumber()==True):
            vehiclePriceValue = float(self.price.get())  #convert from string to float
           
            if self.tradeIn.get() != "":
                lessTradeInValue = float(self.tradeIn.get())
            else:
                lessTradeInValue = 0
            subAmountValue = float(vehiclePriceValue - lessTradeInValue)
            gstAmountValue = float(subAmountValue * 0.1)
            finalAmountValue = float(subAmountValue + gstAmountValue)
            # set value in textfield
            sub_Amount =  str("$" '%.2f' % (subAmountValue))
            self.subAmount.set(sub_Amount)

            gstAmount_Value = str("$" '%.2f' % gstAmountValue)
            self.gstAmount.set(gstAmount_Value)

            finalAmount_Value = str("$" '%.2f' % finalAmountValue)
            self.finalAmount.set(finalAmount_Value)

            conn = self.connect()
            self.create_table(conn)
            self.insert_data(conn)
            database = self.get_all_data(conn)
            #print data row in console
            for i in database:
                print(i)

            conn.close()


    def summary(self):
        workbook = Workbook()
        sheet = workbook.active

        conn = self.connect()
        datalist = self.get_all_data(conn)
        
        for row in datalist:
            sheet.append([row[0], row[1], row[2], row[3], row[4]])

        workbook.save(filename="saleDetail.xlsx")








myWin = CarSaleWindow()
myWin.win.mainloop()