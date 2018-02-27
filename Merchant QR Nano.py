import sys
import os
import pyqrcode
from PyQt5.QtWidgets import QMainWindow,QLabel, QApplication, QPushButton, QLineEdit, QMessageBox, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from shutil import copyfile
from coinmarketcap import Market
import datetime

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
        #self.tab2 = QWidget()
        #self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.resize(300,200) 
 
# Add tabs
        self.tabs.addTab(self.tab1,"Nano")
        #self.tabs.addTab(self.tab2,"Lumens")
        #self.tabs.addTab(self.tab3,"Bitcoin")
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
        nano_value = self.textbox1.text()
        nano_discount = self.textboxdis.text()

    #Convert NANO amount to AUD
        audprice = float(nano_value)/float(price)
        nano_aud = ("%.7f" % round(audprice,7))

    #Write transaction details to file for HTML readfile
        file = open("Logs/Tx.txt", "w")
        file.write("You are sending $" + nano_value + " (" + nano_aud + " NANO) to " + nano_address + "\n\n--PENDING--")
        file.close()

    #Generate QR Code Image
        qr = pyqrcode.create(nano_address)
        qr.png('Images/GUI_test_QR.png', scale=20)

    #Create Confirmation popup
        buttonReply = QMessageBox.question(self, 'Waiting Confirmation', " QR Code generated! \n\nNANO Recieved? ",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

        if buttonReply == QMessageBox.Yes:

        #If yes selected:
            print('Transaction Confirmed')

        #replace image with successful image
            os.remove('Images/GUI_test_QR.png')
            copyfile('Images/Success.png', 'Images/GUI_test_QR.png')

        #Log successful transaction to file
            print("You received " + nano_value + " NANO at [time]")
            tx_log = open("Logs/Transaction_Log.csv", "a")
            tx_log.write(nano_value + "," + nano_address + ",SUCCESSFUL," + nano_aud + "," + now.strftime("%Y-%m-%d %H:%M") + "\n")

        #Write Successful transaction to HTML readfile
            file = open("Logs/Tx.txt", "w")
            file.write("You have sent $" + nano_value + " (" + nano_aud + " NANO) " + " to " + nano_address + "\n\n--PENDING--" + "\n\n--TRANSACTION SUCCESSFUL--")
            file.close()

        #set textbox back to default
            self.textbox1.setText("")

        
        else:

    #if selected no
            print('Transaction Failed')

        #Replace image with failed transaction
            copyfile('Images/Failed.png', 'Images/GUI_test_QR.png')

        #Write failed transaction to HTML readfile
            file = open("Logs/Tx.txt", "w")
            file.write("You attempted to send $" + nano_value + " (" + nano_aud + " NANO) " + " to " + nano_address + "\n\n--PENDING--" + "\n\n--TRANSACTION FAILED--")
            file.close()

        #Log failed transaction
            tx_log = open("Logs/Transaction_Log.csv", "a")
            #tx_log.write("Requested: $" + nano_value + "\nReceiving Address: " + nano_address + "\nStatus: FAILED" + "\nNANO Value: " + nano_aud + "\nTime: " + now.strftime("%Y-%m-%d %H:%M") + "\n\n")
            tx_log.write(nano_value + "," + nano_address + ",FAILED," + nano_aud + "," + now.strftime("%Y-%m-%d %H:%M") + "\n")



    #Address change events
    #save new nano address
    @pyqtSlot()
    def on_click_nano_change(self):
        nano_address = self.textbox4.text()
        QMessageBox.question(self, 'Confirm Amount', "Address Changed", QMessageBox.Ok, QMessageBox.Ok)
        file = open("NANO_ADDRESS.txt", "w")
        file.write(nano_address)

    @pyqtSlot()
    def on_click_nano_change_dis(self):
        nano_discount = self.textboxdis.text()
        QMessageBox.question(self, 'Confirm Amount', "Discount Changed", QMessageBox.Ok, QMessageBox.Ok)
        filedis = open("NANO_DISCOUNT.txt", "w")
        filedis.write(nano_discount)


    @pyqtSlot()
    def on_click_AUD(self):
        amount = self.textboxaud.text()

        
        nano_data = coinmarketcap.ticker("NANO", convert="AUD")
        nano_price = nano_data[0]['price_aud']
        
        nano_conversion = float(amount)/float(nano_price)
        
        print(nano_conversion)
        nano_AUD = ("%.7f" % round(nano_conversion,7))
        
                
        self.labelnano.setText("NANO Value: " + nano_AUD)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ret = app.exec_()
    file = open("Logs/Tx.txt", "w").close()
    copyfile('Images/Logo.png', 'Images/GUI_test_QR.png')
    sys.exit(ret)
