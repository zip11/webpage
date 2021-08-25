import qrcode
from PIL import Image
import os

def get_desk_p():
    return os.path.join(os.path.expanduser('~'),"Desktop")



def gen_qrcode(link):
    qr = qrcode.QRCode(
         version = 2,
         error_correction = qrcode.constants.ERROR_CORRECT_L,
         box_size=10,
         border=10,)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image()
    img.show()
 
    photopath = os.path.join(get_desk_p(), "test")
    if not os.path.exists(photopath):
        os.makedirs(photopath)
    path = os.path.join(photopath, 'create.jpg')
    img.save(path)
    return path

while 1:
    
    text = input("输入文字或URL：") 
    gen_qrcode(text)
