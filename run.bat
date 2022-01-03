@echo off
setlocal

CALL :ARG-PARSER %*

call C:\tools\miniconda3\Scripts\activate C:\tools\miniconda3\envs\ssQrcode && python C:\Users\IAMMAI\Desktop\test\extra\screenScanQrcode\scanQRcode.py %1