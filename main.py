# import Classes.Background_Changer as bgc
import Constants as C
import Classes.popup as pp
import concurrent.futures

# wpc = bgc.WallpaperChanger()
# wpc.change_Wallpaper(C.WALLPAPER_PATH2)

popup = pp.popupGenerator()
with concurrent.futures.ProcessPoolExecutor() as executor:
    popup.start_popups(Count=C.POPUP_COUNT)
    popup.closeWindows(infinite=C.ACTUALVIRUS)
    popup.moveMouse()