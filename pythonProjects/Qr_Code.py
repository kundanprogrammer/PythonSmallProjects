# import pyqrcode

# print("Welcome to QR Code Generator")
# msg =input("Type Your Secret Message")
# code = pyqrcode.create(msg)
# code.png('QRCODEIMG.png',scale=4)
# print("QR sucessfully created to")


import pyqrcode
import sys
url = pyqrcode.create('http://uca.edu')
url.svg(sys.stdout, scale=1)
url.svg('uca.svg', scale=4)
number = pyqrcode.create(123456789012345)
number.png('big-number.png')