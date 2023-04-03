import cv2
import time
import schedule
from datetime import datetime
import threading as th
import os

import time

date = datetime.now()
now = date.strftime('%d-%m-%Y %H:%M:%S')

cam= cv2.VideoCapture(0)
while True:

    ret,frame=cam.read()
    cv2.imshow ('nanocam' , frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

def sendPhoto():
    pass

def camera():
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    if result:
        photopath = os.path.expanduser('~') + str(date).replace(":", ".")+".png"
        cv2.imwrite(photopath, image)
        try:
            # TB.sendPhoto(photopath)
            pass
        except:
            print(Exception)
        else:
            print("ERROR")



# th.Timer(10, ransom).start()
# wallpapersch()
# run()