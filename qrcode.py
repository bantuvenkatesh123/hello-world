import pyqrcode
def qr_code():
    s='This is POWER python class'
    d=pyqrcode.create(s)
    d.png('my_img.png',scale=6)
    print('execute code properly')
if __name__=='__main__':
    qr_code()
