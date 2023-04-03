import ctypes as cty
import Constants as C

def change_Wallpaper():
    path = C.WALLPAPER_PATH
    if path.split('.')[-1] in C.IMAGES_TYPES and __name__ == '__main__':
        cty.windll.user32.SystemParametersInfoW(20, 0, path, 3)


