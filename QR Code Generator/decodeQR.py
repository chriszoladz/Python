from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('F:\Coding\Python\QR Code Generator\QR\myqrcode.png')

result = decode(img)

print(result)

