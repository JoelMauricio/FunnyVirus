from tkinter import *
import tkinter as tk

import threading
import time
import random
import sys

def disable_event():
    pass

def move_window():
    root = Tk()
    root.title("Haz sido infectado por el virus de TEAMHAWKS")
    root.attributes('-toolwindow',True)
    root.attributes('-disabled',True)

    x = random.randint(0, root.winfo_screenwidth())
    y = random.randint(0,root.winfo_screenheight())
    root.resizable(0,0)
    root.geometry(f'300x50+{x}+{y}')
    root.configure(background='white')

    root.protocol("WM_DELETE_WINDOW", disable_event)
    
    root.mainloop()

if __name__ == '__main__':
    for i in range(3):
        thread = threading.Thread(target=move_window)
        thread.start()