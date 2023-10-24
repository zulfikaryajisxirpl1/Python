# 1.) install library qrcode = pip install qrcode
# 2.) install library image = pip install image
# 3.) code . untuk membuka vscode lewat terminal
# 4.) install python 3.12 di msstore yang eror di php

import qrcode  # import library yang akan dipakai
import image

qr = qrcode.QRCode(
    version=15,  # untuk versi qr code nya
    box_size=10,  # untuk ukuran qr code nya
    border=5,  # untuk ukuran putih2 nya qr code
)

data = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # link qr code

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")  # setting warna qrcode
img.save("qrcode.png")  # untuk build qr ke gambar png
