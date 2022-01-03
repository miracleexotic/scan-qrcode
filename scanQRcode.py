# import cv2
from pyzbar import pyzbar
from PIL import Image
from win10toast_click import ToastNotifier
import pyperclip
import argparse

my_parser = argparse.ArgumentParser(description='image file')
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to file name')
args = my_parser.parse_args()
input_path = args.Path

data = ""

def callback_copy():
    pyperclip.copy(data)

def callback_open():
    image = Image.open(input_path)
    image.show()

def scanQRcode():
    global data
    toaster = ToastNotifier()
    try:

        decodedText = pyzbar.decode(Image.open(input_path))

        data = str(decodedText[0].data).strip("b'")
        toaster.show_toast(
            "QR code", # title
            f'>> {data} \n🖱️ click to copy', # message 
            icon_path=None, # 'icon_path' 
            duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
            callback_on_click=callback_copy # click notification to run function 
        ) 
        
    except:
        toaster.show_toast(
            "QR code", # title
            f'❗ Not detected \n🖱️ click to open', # message 
            icon_path=None, # 'icon_path' 
            duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
            callback_on_click=callback_open # click notification to run function 
        ) 

if __name__ == '__main__':
    scanQRcode()




