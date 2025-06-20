import PyInstaller.__main__
import PyInstaller.config
import os

print("path:", str(os.getcwd()))

distpath ="--distpath=" + r"C:\Training-Code\Python\Code_Folder\06-20\data\builder"
workpath = "--workpath=" + r"C:\Training-Code\Python\Code_Folder\06-20\data\builder\tempo"
PyInstaller.__main__.run([
    "--onedir",
    # "--onefile",
    r"C:\Training-Code\Python\Code_Folder\06-20\Code\showPopup.py",
    "-nShow_popup",
    "--windowed",
    distpath,
    workpath,
    "--clean",
    "-y"
])
