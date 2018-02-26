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

file = open("Tx.txt", "w").close()
copyfile('Logo.png', 'GUI_test_QR.png')

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'BTR CryptoQR Generator'
        self.left = 700
        self.top = 400
        self.width = 400
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.setWindowIcon(QIcon('Icon.png'))
 
        self.show()
 
class MyTableWidget(QWidget):        
 
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        
# Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()	
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.resize(300,200) 
 
# Add tabs
        self.tabs.addTab(self.tab1,"Nano")
        self.tabs.addTab(self.tab2,"Lumens")
        self.tabs.addTab(self.tab3,"Bitcoin")
        self.tabs.addTab(self.tab5,"FIAT Conversion")
        self.tabs.addTab(self.tab4,"Settings")


        
# Create first tab
        self.tab1.layout = QVBoxLayout(self)
    #Set Tab Label
        self.label1 = QLabel(self)
        self.tab1.layout.addWidget(self.label1)
        self.label1.setText("Enter Nano Amount:")
    #set tab textbox
        self.textbox1 = QLineEdit(self)
        self.tab1.layout.addWidget(self.textbox1)
    #set tab QR code generator button
        self.pushButton1 = QPushButton("Generate QR Code")
        self.tab1.layout.addWidget(self.pushButton1)
    #Set tab image
        self.label = QLabel(self)
        self.tab1.layout.addWidget(self.label)
        pixmap = QPixmap('Nano.png')
        self.label.setPixmap(pixmap)
        self.tab1.setLayout(self.tab1.layout)

    #If button is clicked
        self.pushButton1.clicked.connect(self.on_click_nano)
        self.show()



# Create second tab
        self.tab2.layout = QVBoxLayout(self)
        self.label2 = QLabel(self)
        self.tab2.layout.addWidget(self.label2)
        self.label2.setText("Enter Lumens Amount:")
        self.textbox2 = QLineEdit(self)
        self.tab2.layout.addWidget(self.textbox2)
        self.pushButton2 = QPushButton("Generate QR Code")
        self.tab2.layout.addWidget(self.pushButton2)
        self.tab2.setLayout(self.tab2.layout)

        self.label = QLabel(self)
        
        self.tab2.layout.addWidget(self.label)
        pixmap = QPixmap('Lumens.png')
        self.label.setPixmap(pixmap)

        self.pushButton2.clicked.connect(self.on_click_xlm)
        self.show()

# Create third tab
        self.tab3.layout = QVBoxLayout(self)
        self.label3 = QLabel(self)
        self.tab3.layout.addWidget(self.label3)
        self.label3.setText("Enter Bitcoin Amount:")
        self.textbox3 = QLineEdit(self)
        self.tab3.layout.addWidget(self.textbox3)
        self.pushButton3 = QPushButton("Generate QR Code")
        self.tab3.layout.addWidget(self.pushButton3)
        self.tab3.setLayout(self.tab3.layout)

        self.label = QLabel(self)
        
        self.tab3.layout.addWidget(self.label)
        pixmap = QPixmap('Bitcoin.png')
        self.label.setPixmap(pixmap)

        self.pushButton3.clicked.connect(self.on_click_btc)
        self.show()

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
    #Set Tab Label XLM
        self.labelxlm = QLabel(self)
        self.tab5.layout.addWidget(self.labelxlm)
        self.labelxlm.setText("XLM Value: ")
    #Set Tab Label BTC
        self.labelbtc = QLabel(self)
        self.tab5.layout.addWidget(self.labelbtc)
        self.labelbtc.setText("BTC Value: ")
    #Set tab image
        self.label = QLabel(self)
        self.tab5.layout.addWidget(self.label)
        pixmap = QPixmap('Exchange.png')
        self.label.setPixmap(pixmap)
        self.tab5.setLayout(self.tab5.layout)

    #If button is clicked
        self.pushButton5.clicked.connect(self.on_click_AUD)
        self.show()

# Create settings tab
    #Nano address change
        file = open("NANO_ADDRESS.txt", "r")
        nano_address = file.read()
        
        self.tab4.layout = QVBoxLayout(self)
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
        self.show()

#XLM Address change

        file = open("XLM_ADDRESS.txt", "r")
        xlm_address = file.read()
        
        self.label5 = QLabel(self)
        self.tab4.layout.addWidget(self.label5)
        self.label5.setText("Enter Updated Stellar Lumens Address:")
        self.textbox5 = QLineEdit(self)
        self.textbox5.setText(xlm_address)
        self.tab4.layout.addWidget(self.textbox5)
        self.pushButton5 = QPushButton("Save Address")
        self.tab4.layout.addWidget(self.pushButton5)
        self.tab4.setLayout(self.tab4.layout)

        self.pushButton5.clicked.connect(self.on_click_xlm_change)
        self.show()

#BTC Address change

        file = open("BTC_ADDRESS.txt", "r")
        btc_address = file.read()
        
        self.label6 = QLabel(self)
        self.tab4.layout.addWidget(self.label6)
        self.label6.setText("Enter Updated Bitcoin Address:")
        self.textbox6 = QLineEdit(self)
        self.textbox6.setText(btc_address)
        self.tab4.layout.addWidget(self.textbox6)
        self.pushButton6 = QPushButton("Save Address")
        self.tab4.layout.addWidget(self.pushButton6)
        self.tab4.setLayout(self.tab4.layout)

        self.pushButton6.clicked.connect(self.on_click_btc_change)
        self.show()

        self.label = QLabel(self)
        self.tab4.layout.addWidget(self.label)
        pixmap = QPixmap('Update.png')
        self.label.setPixmap(pixmap)
        self.tab4.setLayout(self.tab4.layout)
 
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

    #Convert NANO amount to AUD
        audprice = float(nano_value)*float(price)
        nano_aud = ("%.2f" % round(audprice,2))

    #Write transaction details to file for HTML readfile
        file = open("Tx.txt", "w")
        file.write("You are sending " + nano_value + " NANO ($" + nano_aud + ") to " + nano_address + "\n\n--PENDING--")
        file.close()

    #Generate QR Code Image
        qr = pyqrcode.create(nano_address)
        qr.png('GUI_test_QR.png', scale=20)

    #Create Confirmation popup
        buttonReply = QMessageBox.question(self, 'Waiting Confirmation', " QR Code generated! \n\nNANO Recieved? ",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

        if buttonReply == QMessageBox.Yes:

        #If yes selected:
            print('Transaction Confirmed')

        #replace image with successful image
            os.remove('GUI_test_QR.png')
            copyfile('Success.png', 'GUI_test_QR.png')

        #Log successful transaction to file
            print("You received " + nano_value + " NANO at [time]")
            tx_log = open("Transaction_Log.txt", "a")
            tx_log.write("Requested: " + nano_value + " NANO" + "\nReceiving Address: " + nano_address + "\nStatus: SUCCESSFUL" + "\nAUD Value: $" + nano_aud + "\nTime: " + now.strftime("%Y-%m-%d %H:%M") + "\n\n")

        #Write Successful transaction to HTML readfile
            file = open("Tx.txt", "w")
            file.write("You have sent " + nano_value + " NANO ($" + nano_aud + ") " + " NANO to " + nano_address + "\n\n--PENDING--" + "\n\n--TRANSACTION SUCCESSFUL--")
            file.close()

        #set textbox back to default
            self.textbox1.setText("")

        
        else:

    #if selected no
            print('Transaction Failed')

        #Replace image with failed transaction
            copyfile('Failed.png', 'GUI_test_QR.png')

        #Write failed transaction to HTML readfile
            file = open("Tx.txt", "w")
            file.write("You attempted to send " + nano_value + " NANO ($" + nano_aud + ") " + " NANO to " + nano_address + "\n\n--PENDING--" + "\n\n--TRANSACTION FAILED--")
            file.close()

        #Log failed transaction
            tx_log = open("Transaction_Log.txt", "a")
            tx_log.write("Requested: " + nano_value + " NANO" + "\nReceiving Address: " + nano_address + "\nStatus: FAILED" + "\nAUD Value: $" + nano_aud + "\nTime: " + now.strftime("%Y-%m-%d %H:%M") + "\n\n")
             

    #generate xlm qr code
    @pyqtSlot()
    def on_click_xlm(self):

        
        xlm_value = self.textbox2.text()
        file = open("XLM_ADDRESS.txt", "r")
        xlm_address = file.read()

        open("Tx.txt", "w").close()
        file = open("Tx.txt", "w")

        file.write("You are sending " + xlm_value + " XLM to " + xlm_address)

        file.close()
        
        qr = pyqrcode.create(xlm_address)
        qr.png('GUI_test_QR.png', scale=20)
        QMessageBox.question(self, 'Confirm Amount', "QR Code Generated ", QMessageBox.Ok, QMessageBox.Ok)
        file = open("Tx.txt", "w").close()
        copyfile('Logo.png', 'GUI_test_QR.png')
        self.textbox2.setText("")
        

        

        tx_log = open("Transaction_Log.txt", "a")
        tx_log.write("Requested: " + xlm_value + " XLM" + "\nReceiving Address: " + xlm_address + "\nTime: " + now.strftime("%Y-%m-%d %H:%M") + "\n\n")


    #generate btc qr code
    @pyqtSlot()
    def on_click_btc(self):
        btc_value = self.textbox3.text()
        QMessageBox.question(self, 'Confirm Amount', "QR Code Generated ", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox3.setText("")
        file = open("BTC_ADDRESS.txt", "r")
        btc_address = file.read()

        open("Tx.txt", "w").close()
        file = open("Tx.txt", "w")

        file.write("You are sending " + btc_value + " BTC to " + btc_address)
        
        qr = pyqrcode.create(btc_address)
        qr.png('GUI_test_QR.png', scale=20)

        tx_log = open("Transaction_Log.txt", "a")
        tx_log.write("Requested: " + btc_value + " BTC" + "\nReceiving Address: " + btc_address + "\nTime: " + now.strftime("%Y-%m-%d %H:%M") + "\n\n")



    #Address change events
    #save new nano address
    @pyqtSlot()
    def on_click_nano_change(self):
        nano_address = self.textbox4.text()
        QMessageBox.question(self, 'Confirm Amount', "Address Changed", QMessageBox.Ok, QMessageBox.Ok)
        file = open("NANO_ADDRESS.txt", "w")
        file.write(nano_address)

    #save new xlm address
    @pyqtSlot()
    def on_click_xlm_change(self):
        xlm_address = self.textbox5.text()
        QMessageBox.question(self, 'Confirm Amount', "Address Changed", QMessageBox.Ok, QMessageBox.Ok)
        file = open("XLM_ADDRESS.txt", "w")
        file.write(xlm_address)

    #save new btc address
    @pyqtSlot()
    def on_click_btc_change(self):
        btc_address = self.textbox6.text()
        QMessageBox.question(self, 'Confirm Amount', "Address Changed", QMessageBox.Ok, QMessageBox.Ok)
        file = open("BTC_ADDRESS.txt", "w")
        file.write(btc_address)

    @pyqtSlot()
    def on_click_AUD(self):
        amount = self.textboxaud.text()

        xlm_data = coinmarketcap.ticker("STELLAR", convert="AUD")
        xlm_price = xlm_data[0]['price_aud']
        btc_data = coinmarketcap.ticker("BITCOIN", convert="AUD")
        btc_price = btc_data[0]['price_aud']
        nano_data = coinmarketcap.ticker("NANO", convert="AUD")
        nano_price = nano_data[0]['price_aud']
        
        nano_conversion = float(amount)/float(nano_price)
        xlm_conversion = float(amount)/float(xlm_price)
        btc_conversion = float(amount)/float(btc_price)

        nano_AUD = ("%.2f" % round(nano_conversion,2))
        xlm_AUD = ("%.2f" % round(xlm_conversion,2))
        btc_AUD = ("%.2f" % round(btc_conversion,2))
                
        self.labelnano.setText("NANO Value: " + nano_AUD)
        self.labelxlm.setText("XLM Value: " + xlm_AUD)
        self.labelbtc.setText("BTC Value: " + btc_AUD)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ret = app.exec_()
    file = open("Tx.txt", "w").close()
    copyfile('Logo.png', 'GUI_test_QR.png')
    sys.exit(ret)
