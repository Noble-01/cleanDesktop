import os
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
        folders.append(folder)

for file in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, file)):
        files.append(file)