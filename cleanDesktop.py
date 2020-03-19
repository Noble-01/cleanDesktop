import os
folders = []
files =[]

directory = ".."
for folder in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, folder)):
        folders.append(folder)

for file in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, file)):
        files.append(file)