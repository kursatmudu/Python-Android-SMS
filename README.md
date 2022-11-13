
# Python Android SMS

This project sends sms from Android device to server. It works with Qpython 3S. **Qpython 3L is incompatible because it does not have permission to read sms. Do not install from Google Play.**


## Installation

- First install Qpython 3S.

```bash
  Install Qpython 3S.
```

- Install Python Requests Library

```bash
  * Open Qpython
  * Click Programs
  * Click Left Up Button(More button)
  * Select PIP Console
  * pip install requests 
  if not working pip install requests; try pip3 install requests.
```
- Move Files To /sdcard/qpython/*
- If you want to do this with adb(write commandline):
- First PC file location. Secound phone file location
```bash
  adb push file_location /sdcard/qpython/
```
- Open Qpython
- Click Programs
- Find This Project Click And Run
## Components

Download Components

- [Qpython 3S](https://github.com/qpython-android/qpython3/releases)
- [ADB Driver](https://forum.xda-developers.com/attachment.php?attachmentid=4623157&d=1540039037)

  
## Used Technologies

**Client:** Python, Python Requests Module, Qpython3S

**Server:** Python, Python Requests Module

  
## Authors

- [@kursatmudu](https://github.com/kursatmudu) development.

  
## Feedback

You can send your feedback at mic.crackogy@gmai.com.

  