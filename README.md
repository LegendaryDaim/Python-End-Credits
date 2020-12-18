# Python-End-Credits
Google sheets to video

First coding project and first git push. 

Purpose of this code is to create video file from Google Sheets for use as end credits.

It works but a bit junkie. 

Installation:
* Check libraries file for module list. and install modules.
* This code uses gspread to fetch data from Google Sheets. You need to create your own Auth token.
Go to https://console.developers.google.com/ to create and download json file.
You will need to put that file into %APPDATA%\gspread\ if on windows.
Follow this tutorial if unsure https://www.youtube.com/watch?v=T1vqS1NL89E
* Now you can copy any google sheets link and turn it into end credits.
Right now it's set up like this: Collum 1,2 is the left side. Collum 3 is middle and Collum 4,5 is right side.    
     
     
I used PyQt5 module for UI but I could not find how to extract font directory for fonts.
So I didn't find an easy way of inserting absolute path into Pillow module.    

Changing fonts will be done from config.py file. 

Here is how end result might look like: https://youtu.be/TU3L0_slsEE

Python Version Python 3.6.2   
gspread         # gspread-3.6.0   
pillow          # pillow-8.0.1   
ffmpeg-python   # ffmpeg-python-0.2.0 future-0.18.2   
PyQt5           # PyQt5-5.15.1 PyQt5-sip-12.8.1   
