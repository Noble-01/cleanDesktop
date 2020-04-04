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


for i in folders:
   shutil.move("../"+i, checkDirFolder)
for i in files:
    shutil.move("../"+i, checkDirFile)
print(todayDate.strftime("%d-%m-%Y"))