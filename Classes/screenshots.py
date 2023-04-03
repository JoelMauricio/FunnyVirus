import pyautogui
import schedule
from datetime import datetime
import os
import time

class ScreenShots():
    def __init__(self) -> None:
        self.screenShotter = schedule.every(60).seconds.do(self.capture_screen)

    def capture_screen(self):
        home_dir = os.path.expanduser("~")

        # Create a screenshots directory if it doesn't exist
        if not os.path.exists(home_dir+ "\\screenshots"):
            os.mkdir(home_dir+"\\screenshots")
            
        # Construct the screenshot path using the current date and time
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        screenshot_name = f"sc-{os.getlogin()}-{timestamp}.png"
        screenshot_path = os.path.join(home_dir,"screenshots", screenshot_name)
        
        # Capture the screenshot and save it to the specified path
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)

    def Run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def Stop(self):
        self.screenShotter.cancel_after.now()

 