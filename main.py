import Classes.Background_Changer as bgc
import Constants as C
import Classes.popup as pp
import threading

# wpc = bgc.WallpaperChanger()
# wpc.change_Wallpaper(C.WALLPAPER_PATH2)



# for i in range(5):
#     thread = threading.Thread(target=pp.move_window)
#     print('a')
#     thread.start()

popup = pp.popupGenerator()
popup.start_popups(Count=5)
popup.closeWindows()
popup.moveMouse()