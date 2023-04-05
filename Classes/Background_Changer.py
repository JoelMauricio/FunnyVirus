import ctypes as cty
import os
import getpass
import datetime

# # get the current time
# now = datetime.datetime.now()

# # subtract one day from the current time
# one_day_ago = now - datetime.timedelta(days=1)

# # set the local time using the SYSTEMTIME structure
# cty.windll.kernel32.SetLocalTime(cty.byref(one_day_ago.fromtimestamp()))
    
# USER_NAME = getpass.getuser()

# def add_to_startup(file_path=""):
#     if file_path == "":
#         file_path = os.path.dirname(os.path.realpath(__file__))
#     bat_path = r'C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup' % USER_NAME
#     with open(bat_path + '//' + "open.bat", "w+") as bat_file:
#         bat_file.write(r'start "" "%s"' % file_path)

def change_Wallpaper():
    # file_path = os.path.join(current_directory, 'Media/wp.jpg')
    # print(wp_path)
    wp_path = 'C:/Users/mauri/AlgoritmosMaliciosos/Classes/Media/wp.jpg'
    cty.windll.user32.SystemParametersInfoW(20, 0, wp_path, 3)

