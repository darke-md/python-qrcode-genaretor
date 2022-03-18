import pyqrcode
import png
from pyqrcode import QRCode

s = input("Url: ")
url = pyqrcode.create(s)
url.svg("code.svg", scale = 8)
url.png("code.png" , scale = 6)
print("images is saved as 'code.png' and 'code.svg'")
print("Thanks For uaing this tool :)")
