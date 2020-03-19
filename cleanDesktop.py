import os

directory = ".."
print("folders")
for entry in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, entry)):
        print(entry)
print("\n files")
for entry in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, entry)):
        print(entry)
