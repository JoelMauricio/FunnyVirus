import os
import win32com.client as win32

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # Get path to the desktop
icon_path = "../Media/Icon.ico"  # Path to the new icon file

shell = win32.Dispatch("WScript.Shell")  # Create an instance of the Windows Shell

def change_icons():
    for file_name in os.listdir(desktop_path):  # Loop through all files on the desktop
        file_path = os.path.join(desktop_path, file_name, '.lnk')  # Get the full path to the file

        if file_path.endswith('test'): # Only change the icon for files with a .txt extension
            print(file_name)
            shortcut = shell.CreateShortcut(file_path)  # Create a shortcut object for the file
            shortcut.IconLocation = icon_path  # Set the new icon location for the shortcut
            shortcut.Save()  # Save the shortcut to apply the new icon

change_icons()