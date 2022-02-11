from Login import LoginWindow
from CarSale import CarSaleWindow

# Thi Huong Giang nguyen
# Date: 22/11/2021

def main():
    myLogin = LoginWindow()
    myLogin.win.mainloop()
    myCarSale = CarSaleWindow()

    if myLogin.login_success == True:
        myCarSale.win.mainloop()
    