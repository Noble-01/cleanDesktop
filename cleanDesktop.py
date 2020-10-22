import os
import shutil
import stat
from datetime import date
todayDate = date.today()
folders = []
files =[]
safeFolders = ["cleanDesktop", "Folders", "Files"]
directory = ".."
checkDirFolder = "../Folders"
checkDirFile = "../Files"
if not os.path.exists(checkDirFolder):
    os.mkdir(checkDirFolder)
if not os.path.exists(checkDirFile):
    os.mkdir(checkDirFile)

for folder in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, folder)):
        if folder in safeFolders:
            pass
        else:
            folders.append(folder)

for file in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, file)):
        files.append(file)

try:
    for i in folders:
        if(os.path.isdir(checkDirFolder +"/"+i)):
            print("folder exists in folder already")
        else:
            shutil.move("../"+i, checkDirFolder)

    for i in files:
        if(os.path.isfile(checkDirFile +"/"+i)):
             print("file exists in folder already")
        else:
            shutil.move("../"+i, checkDirFile)
    pass
except:
    print("error")
    pass

print(todayDate.strftime("%d-%m-%Y"))