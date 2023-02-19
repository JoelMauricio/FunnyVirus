import ctypes as cty
from tkinter import *
from tkinter import messagebox as msg
import random as rnd

user32 = cty.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pos_X = rnd.randint(0, screensize[0])
pos_Y = rnd.randint(0, screensize[1])


def click():

    msg.showwarning(title='WARNING!!!!!!!',
                        message='Estás infectado por un virus divertido hahahah')


window = Tk()
button = Button(window, command=click, text='Click me')
button.pack()

window.mainloop()
