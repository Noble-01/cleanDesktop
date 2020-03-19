import os

directory = ".."
for entry in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, entry)):
        print(entry)
