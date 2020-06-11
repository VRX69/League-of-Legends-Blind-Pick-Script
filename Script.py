import os
import sys
import ctypes
import hashlib
import requests
import pyautogui
import urllib.request
import pygetwindow as gw

urllib.request.urlretrieve("https://i.ibb.co/2MP32k4/champ-select-image.png", "champ_select_image.png")

Lane = input('Enter Lane: ')
Champ = input('Enter Champion: ')

print("Waiting for Champion Select.")

#Waits for Champ Select
while True:
    coords = pyautogui.locateOnScreen('champ_select_image.png')
    if coords is None:
        continue
    else:
        Window = gw.getWindowsWithTitle('League Of Legends')[0]
        Window.activate()
        Window.moveTo(350,200)
        break

#Entering Lane in chat
pyautogui.leftClick(468,881)
pyautogui.write(Lane)
pyautogui.press('enter') 

#Searching Champ
pyautogui.leftClick(1098,301)
pyautogui.write(Champ)
pyautogui.press('enter') 

#SelectsChamp&Locks
pyautogui.leftClick(727,368)
pyautogui.leftClick(727,368)
pyautogui.leftClick(727,368)
pyautogui.leftClick(958,799)
pyautogui.leftClick(958,799)
pyautogui.leftClick(958,799)


input("Done! Press any key to exit.")
