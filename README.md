# Scan QR code
**Note** : use miniconda env to run script and pyzbar to scan QRcode

### Install
Use **python pip** with **miniconda**
- gti clone
    ```console
    $ git clone https://github.com/miracleexotic/scan-qrcode.git
    $ cd scan-qrcode
    ```
- create env
    ```console
    $ conda create --name ssQrcode python=3.9
    ```
- activate env
    ```console
    $ conda activate ssQrcode
    ```
- install dependencies requirements
    ```console
    $ pip install -r requirements.txt
    ```

### Used
Use **python**
```console
$ python /path/to/scan-qrcode/scanQRcode.py /path/to/test/01.png
```
![scan QR-code](/assets/images/decode_cli.png "scan")
![scan result](/assets/images/win10_notification.png "result")

### Integrating with greenshot
&darr; [Download Greenshot](https://getgreenshot.org/ "Greenshot")
1. **right click** in greenshot icon (bottom right in screen)
2. choose **Configure external commands**
3. **click New** in External command settings pane
4. fill in 
**Name** : ```QRcode```
**Command** : ```C:\Windows\System32\wscript.exe```
**Arguments** : ```\path\to\scan-qrcode\invisible.vbs "\path\to\scan-qrcode\run.bat {0}"```

**Note** : Edit run.bat with correct path

##### Use greenshot
1. press **prtsc button**
2. crop QRcode
3. select **QRcode** in menu pane
4. click notification to copy message
