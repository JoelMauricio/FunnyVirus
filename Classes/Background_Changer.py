import Constants as C
import ctypes as cty


def change_Wallpaper(path):
    cty.windll.user32.SystemParametersInfoW(20, 0, path, 3)


if __name__ != '__main__':
    change_Wallpaper(C.WALLPAPER_PATH2)
