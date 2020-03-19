import os
import shutil
import stat

folders = []
files =[]
directory = ".."
checkDir = "../Folders"
if not os.path.exists(checkDir):
    os.mkdir(checkDir)
    print("directory", checkDir , "created")
else:
    print("directory already exists")

for folder in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, folder)):
        if folder == "cleanDesktop":
            pass
        else:
            folders.append(folder)

for file in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, file)):
        files.append(file)

for i in folders:
    shutil.move("../"+i, checkDir)