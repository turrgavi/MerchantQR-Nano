import sys
import os
import pyqrcode
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow,QLabel, QApplication, QPushButton, QLineEdit, QMessageBox, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from shutil import copyfile
from coinmarketcap import Market
import datetime
import nano

rpc = nano.rpc.Client('http://localhost:7076')
process = QtCore.QProcess()
coinmarketcap = Market()
now = datetime.datetime.now()

file = open("Logs/Tx.txt", "w").close()
copyfile('Images/Logo.png', 'Images/GUI_test_QR.png')
    
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Merchant NANO QR Generator'
        self.left = 700
        self.top = 400
        self.width = 400
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.setWindowIcon(QIcon('Images/Icon.png'))
 
        self.show()
 
class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)


        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.resize(300,200)

        # Add tabs
        self.tabs.addTab(self.tab1,"Nano")
        self.tabs.addTab(self.tab5,"FIAT Conversion")
        self.tabs.addTab(self.tab4,"Settings")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        #Set Tab Label
        self.label1 = QLabel(self)
        self.tab1.layout.addWidget(self.label1)
        self.label1.setText("Enter AUD Amount:")
        #set tab textbox
        self.textbox1 = QLineEdit(self)
        self.tab1.layout.addWidget(self.textbox1)
        #set tab QR code generator button
        self.pushButton1 = QPushButton("Generate QR Code")
        self.tab1.layout.addWidget(self.pushButton1)
        #Set tab image
        self.label = QLabel(self)
        self.tab1.layout.addWidget(self.label)
        pixmap = QPixmap('Images/Nano.png')
        self.label.setPixmap(pixmap)
        self.tab1.setLayout(self.tab1.layout)

        #If button is clicked
        self.pushButton1.clicked.connect(self.on_click_nano)
        self.show()

        #BTC and XLM tabs removed for easier dev

        # Create Exchange tab
        self.tab5.layout = QVBoxLayout(self)
        #Set Tab Label
        self.label5 = QLabel(self)
        self.tab5.layout.addWidget(self.label5)
        self.label5.setText("Enter AUD Amount:")
        #set tab textbox
        self.textboxaud = QLineEdit(self)
        self.tab5.layout.addWidget(self.textboxaud)
        #set tab QR code generator button
        self.pushButton5 = QPushButton("Fetch Latest Prices")
        self.tab5.layout.addWidget(self.pushButton5)
        #Set Tab Label NANO
        self.labelnano = QLabel(self)
        self.tab5.layout.addWidget(self.labelnano)
        self.labelnano.setText("NANO Value: ")

        #Set tab image
        self.label = QLabel(self)
        self.tab5.layout.addWidget(self.label)
        pixmap = QPixmap('Images/Exchange.png')
        self.label.setPixmap(pixmap)
        self.tab5.setLayout(self.tab5.layout)

        #If button is clicked
        self.pushButton5.clicked.connect(self.on_click_AUD)
        self.show()

        # Create settings tab
        #Nano address change
        file = open("NANO_ADDRESS.txt", "r")
        nano_address = file.read()

        filedis = open("NANO_DISCOUNT.txt", "r")
        nano_discount = filedis.read()

        self.tab4.layout = QVBoxLayout(self)

        self.pushButtonreset = QPushButton("RESET DISPLAY")
        self.tab4.layout.addWidget(self.pushButtonreset)
        self.tab4.setLayout(self.tab4.layout)

        self.labeldis = QLabel(self)
        self.tab4.layout.addWidget(self.labeldis)
        self.labeldis.setText("Percentage Discount for NANO:")
        self.textboxdis = QLineEdit(self)
        self.textboxdis.setText(nano_discount)
        self.tab4.layout.addWidget(self.textboxdis)
        self.pushButtondis = QPushButton("Save")
        self.tab4.layout.addWidget(self.pushButtondis)


        self.label4 = QLabel(self)
        self.tab4.layout.addWidget(self.label4)
        self.label4.setText("Enter Updated Nano Address:")
        self.textbox4 = QLineEdit(self)
        self.textbox4.setText(nano_address)
        self.tab4.layout.addWidget(self.textbox4)
        self.pushButton4 = QPushButton("Save Address")
        self.tab4.layout.addWidget(self.pushButton4)
        self.tab4.setLayout(self.tab4.layout)

        self.pushButtonreset.clicked.connect(self.on_click_display_reset)
        self.pushButton4.clicked.connect(self.on_click_nano_change)
        self.pushButtondis.clicked.connect(self.on_click_nano_change_dis)
        self.show()


        #Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    #QR generation events
    #generate nano qr code
    @pyqtSlot()
    def on_click_nano(self):

        #Ftech NANO CMC price AUD
        data = coinmarketcap.ticker("NANO", limit=3, convert="AUD")
        price = data[0]['price_aud']

        #Fetch NANO Address and amount
        filea = open("NANO_ADDRESS.txt", "r")
        nano_address = filea.read()
        filedis = open("NANO_DISCOUNT.txt", "r")
        nano_discount = filedis.read()
        nano_discount_float = float(nano_discount)
        nano_value = float(self.textbox1.text())*((100-nano_discount_float)/100)
        balance = str(nano_address)
        current_balance = float(nano.conversion.convert(rpc.account_balance(balance)["balance"], "raw", "Mrai"))
        print(current_balance)
        print(nano_value)

        #Convert NANO amount to AUD
        new_balance=float(0)
        audprice = nano_value/float(price)
        nano_aud = ("%.6f" % round(audprice,6))
        nano_aud_float = float(nano_aud)

        #Write transaction details to file for HTML readfile
        file = open("Logs/Tx.txt", "w")
        file.write("You are sending $" + str(nano_value) + " (" + nano_aud + " NANO) to " + nano_address + "\n\n--PENDING--")
        file.close()

        #Generate QR Code Image
        qr = pyqrcode.create("xrb:"+nano_address+"?amount="+str(nano_aud_float))
        qr.png('Images/GUI_test_QR.png', scale=20)
        print("[TRANSACTION GENERATED]")
        #Create Confirmation popup
        buttonReply = QMessageBox.question(self, 'Waiting Confirmation', " QR Code generated! \n\nWait for confirmation? ", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

        if (buttonReply==QMessageBox.Cancel):
            print("[TRANSACTION CANCELLED]")

        if (buttonReply==QMessageBox.No):
            print('Transaction Confirmed')
            print(new_balance)
            os.remove('Images/GUI_test_QR.png')
            copyfile('Images/Success.png', 'Images/GUI_test_QR.png')

            # Log successful transaction to file
            tx_log = open("Logs/Transaction_Log.csv", "a")
            tx_log.write(str(nano_value) + "," + nano_address + ",SUCCESSFUL," + nano_aud + "," + now.strftime("%Y-%m-%d %H:%M") + "\n")

            # Write Successful transaction to HTML readfile
            file = open("Logs/Tx.txt", "w")
            file.write("You have sent $" + str(nano_value) + " (" + nano_aud + " NANO) " + " to " + nano_address + "\n\n--PENDING--" + "\n\n--TRANSACTION SUCCESSFUL--")
            file.close()

            # set textbox back to default
            self.textbox1.setText("")
            QMessageBox.question(self, 'SUCCESS', "TRANSACTION SUCCESSFUL", QMessageBox.Ok)
            file = open("Logs/Tx.txt", "w").close()
            copyfile('Images/Logo.png', 'Images/GUI_test_QR.png')


        if (buttonReply==QMessageBox.Yes):

            while (1==1):
                new_total = ("%.6f" % round(current_balance+nano_aud_float,6))
                new_balance_round = ("%.6f" % round(new_balance,6))

                print(nano_aud_float)
                print(current_balance)
                print(new_balance)
                print(new_total)

                if (new_total == new_balance_round):
                    #If yes selected:
                    print('Transaction Confirmed')
                    print(new_balance)
                    break
                    os.remove('Images/GUI_test_QR.png')
                    copyfile('Images/Success.png', 'Images/GUI_test_QR.png')

                    #Log successful transaction to file
                    print("You received " + str(nano_value) + " NANO at [time]")
                    tx_log = open("Logs/Transaction_Log.csv", "a")
                    tx_log.write(str(nano_value) + "," + nano_address + ",SUCCESSFUL," + nano_aud + "," + now.strftime("%Y-%m-%d %H:%M") + "\n")

                    #Write Successful transaction to HTML readfile
                    file = open("Logs/Tx.txt", "w")
                    file.write("You have sent $" + str(nano_value) + " (" + nano_aud + " NANO) " + " to " + nano_address + "\n\n--PENDING--" + "\n\n--TRANSACTION SUCCESSFUL--")
                    file.close()

                    #set textbox back to default
                    self.textbox1.setText("")
                    QMessageBox.question(self, 'SUCCESS', "TRANSACTION CONFIRMED", QMessageBox.Ok)
                    file = open("Logs/Tx.txt", "w").close()
                    copyfile('Images/Logo.png', 'Images/GUI_test_QR.png')


                new_balance = float(nano.conversion.convert(rpc.account_balance(balance)["balance"], "raw", "Mrai"))
                QtCore.QCoreApplication.processEvents()

    #Address change events
    #save new nano address
    @pyqtSlot()
    def on_click_nano_change(self):
        nano_address = self.textbox4.text()
        QMessageBox.question(self, 'Confirm Amount', "Address Changed", QMessageBox.Ok, QMessageBox.Ok)
        file = open("NANO_ADDRESS.txt", "w")
        file.write(nano_address)
        print("[NANO RECEIVE ADDRESS SET]")

    @pyqtSlot()
    def on_click_nano_change_dis(self):
        nano_discount = self.textboxdis.text()
        QMessageBox.question(self, 'Confirm Amount', "Discount Changed", QMessageBox.Ok, QMessageBox.Ok)
        filedis = open("NANO_DISCOUNT.txt", "w")
        filedis.write(nano_discount)
        print("[NANO DISCOUNT SET]")

    @pyqtSlot()
    def on_click_AUD(self):
        amount = self.textboxaud.text()
        nano_data = coinmarketcap.ticker("NANO", convert="AUD")
        nano_price = nano_data[0]['price_aud']
        nano_conversion = float(amount)/float(nano_price)
        print("[FIAT TO NANO CONVERSION]")
        print(nano_conversion)
        nano_AUD = ("%.7f" % round(nano_conversion,7))
        self.labelnano.setText("NANO Value: " + nano_AUD)

    @pyqtSlot()
    def on_click_display_reset(self):
        QMessageBox.question(self, 'Confirm Amount', "Display Reset", QMessageBox.Ok, QMessageBox.Ok)
        file = open("Logs/Tx.txt", "w").close()
        copyfile('Images/Logo.png', 'Images/GUI_test_QR.png')
         
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ret = app.exec_()
    file = open("Logs/Tx.txt", "w").close()
    copyfile('Images/Logo.png', 'Images/GUI_test_QR.png')
    sys.exit(ret)
    
