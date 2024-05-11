import qrcode


data = 'https://alpachi.com'

img = qrcode.make(data)

img.save('F:/Coding/Python/QR Code Generator/QR/myqrcode.png')
