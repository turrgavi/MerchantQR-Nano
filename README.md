# NANO Merchant QR Code Generator

This project allows an easier way for merchants to generate their public address for customers to scan. This program will generate a QR 
from your address, and display it on any device capable of connecting to the shared folder. This program also fetch the latest coin prices
from CoinMarketCap.com. 

This aims to provide a more customer friendly way to accept your cryptocurrency payments.

## Getting Started

Ideally the program would run on the merchant's computer and they would then generate a QR code that will be displayed on a smaller screen
that the customers can then use to view the amount requested, in both FIAT and Crypto values. The screen will also display whether the 
transaction was successful or not.

Using a raspberry pi with a small display with a simple browser proccessing the HTML file would be suitable for this.

New version now supports automatic transaction confirmations. Requires desktop wallet with RPC enabled.

### Prerequisites

In order to run this program, you will need a few things:

* Python 3.4+
* CoinMarketCap API
* PyQRCode
* PyQt5
* Nano Desktop Wallet with RPC enabled
* Nano-Python
* PyPNG

### Installing

A step by step series of examples that tell you have to get a development env running

1) Install Python 3.6 for your specific OS:

* https://www.python.org/downloads

2) Download and install pip.

* https://bootstrap.pypa.io/get-pip.py

Right click, download file to python directory, then cd to python directory and run it.

Example:
```
cd C:\Users\[YOURUSERNAME]\AppData\Local\Programs\Python\Python36-32

python get-pip.py
```
This will install pip and put it into your python/scripts folder.

3) Install pre-requesites. (PyQt5, Coinmarketcap, PyQRCode)

```
cd C:\Users\[YOURUSERNAME]\AppData\Local\Programs\Python\Python36-32\Scripts

pip3 install python-qt5 coinmarketcap pyqrcode pypng pyqt5
```
You should now be able to run the Merchant QR Nano.py

## Deployment

From here you can share your folder to read the HTML file from another device and display it in a browser window.

* Simply:
1. Open the desktop wallet
2. Open the "QR Display.html" file in a browser window
3. Run "Merchant QR Nano.py" file
4. Generate QR Codes to your heart's content
5. Watch the browser window as you generate and approve/disapprove/cancel transactions

## Built With

* [Python](https://www.python.org)
* [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5)
* [PyQRCode](https://pypi.python.org/pypi/PyQRCode)
* [CoinMarketCap API](https://pypi.python.org/pypi/coinmarketcap/)
* [Nano Wallet](https://github.com/nanocurrency/raiblocks/releases)
* [Nano Python](https://github.com/dourvaris/nano-python)

## Supported Currencies

* NANO
* More currencies can be added easily

## Authors

* **Gavin Michael Turrell** - *Noob Developer* - [turrgavi](https://github.com/turrgavi)

## License

Feel free to use this code and develop your own version to better suit you or better yet help me improve this! 

## Acknowledgments

* I am by no means a developer, I am just doing this as a hobby at the moment and appreciate suggestions.
* I encourage all to develop and push for adoption.

## Donations

I will be doing this in my own time and will be pitching it to nearby merchants at my own expense for the first store. 
Obviously I don't expect donations but anything would be appreciated.
* xrb_3nijkoe98ctgup4g3xq1jyn7nonbshir15z9xymgfyj3apcdiicfpa7y9kgo
