# import Classes.Background_Changer as bgc
import Constants as C
import Classes.popup as pp


# wpc = bgc.WallpaperChanger()
# wpc.change_Wallpaper(C.WALLPAPER_PATH2)

popup = pp.popupGenerator()
popup.start_popups(C.POPUP_COUNT)
popup.closeWindows()
popup.moveMouse()
