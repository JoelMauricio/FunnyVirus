import ctypes as cty
import Constants as C


class WallpaperChanger:
    """
        Agrega la clase de la funcionalidad del cambiar el wallpaper del computador.
    """

    def __init__(self):
        pass

    def change_Wallpaper(self, path: str):
        """_summary_

        Args:
            path (string): Ubicación del archivo imagen para el cambio de fondo de pantalla.
        """
        if path.split('.')[-1] in C.IMAGES_TYPES and __name__ == '__main__':

            cty.windll.user32.SystemParametersInfoW(20, 0, path, 3)
