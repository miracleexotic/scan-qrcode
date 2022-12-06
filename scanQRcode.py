# import cv2
from pyzbar import pyzbar
from PIL import Image
from win10toast_click import ToastNotifier
import pyperclip
import sys

input_path = sys.argv[1]
print(sys.argv[1])

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
        # image = cv2.imread(input_path)

        # qrCodeDetector = cv2.QRCodeDetector()
        # decodedText, points, _ = qrCodeDetector.detectAndDecode(image)

        decodedText = pyzbar.decode(Image.open(input_path))

        data = str(decodedText[0].data).strip("b'")
        # print(data) 
        toaster.show_toast(
            "QR code", # title
            f'>> {data} \n🖱️ click to copy', # message 
            icon_path=None, # 'icon_path' 
            duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
            callback_on_click=callback_copy # click notification to run function 
        ) 
        
    except:
        # print(e)
        # print("QR code not detected")
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




