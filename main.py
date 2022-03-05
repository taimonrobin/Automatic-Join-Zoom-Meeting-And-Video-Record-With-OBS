import os
from re import search
import schedule
import time as t
import webbrowser
import pyautogui
from datetime import datetime
import sys

TIME_TO_START_DT = datetime.strptime('00:34',"%H:%M").time()
MINUTES_TO_RUN = 1

def open_link(link):
    #Start Obs and record
    # os.system('cmd /k start /d "C:\\Program Files\\obs-studio\\bin\\64bit\\" obs64.exe --startrecording --minimize-to-tray & exit')
    #Open OBS
    pyautogui.press('win')
    search_bar = pyautogui.locateCenterOnScreen('clickable/search_bar.png')
    pyautogui.moveTo(search_bar)
    pyautogui.write("OBS Studio (64bit)")
    t.sleep(1)
    pyautogui.press('enter')
    t.sleep(3)

    #start recording
    start_recording_button = pyautogui.locateCenterOnScreen('clickable/start_recording_button.png')
    pyautogui.moveTo(start_recording_button)
    pyautogui.click()
    t.sleep(1)

    #Minimize OBS
    minimize_button = pyautogui.locateCenterOnScreen('clickable/minimize_button.png')
    pyautogui.moveTo(minimize_button)
    pyautogui.click()
    t.sleep(1)

    #Open Zoom Meeting 
    webbrowser.open(link)
    t.sleep(3)

    #clicks the python join button
    launch_button_center = pyautogui.locateCenterOnScreen('clickable/launch_meeting.png')
    pyautogui.moveTo(launch_button_center)
    pyautogui.click()

    t.sleep(MINUTES_TO_RUN * 60)


    os.system('cmd /k taskkill /F /IM obs64.exe')


def start_meeting():
    open_link('https://us05web.zoom.us/j/9894370645?pwd=aVczOEgzdGwwUGg1Rno5NjJIUDkyZz09')
print(datetime.now())
#schedule.every().saturday.at(TIME_TO_START_DT.strftime("%H:%M")).do(start_meeting)
start_meeting()

while 1:
    schedule.run_pending()
    t.sleep(1)