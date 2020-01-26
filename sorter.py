import os
from shutil import move

src = "<PATH TO DIRECTORY>"
musicdest = "<PATH TO DIRECTORY"
docsdest = "<PATH TO DIRECTORY>"
docsext = ["docx", "pdf"] # Add more extensions as per your needs
musicext = ["mp3", "wav"] # Add more extensions as per your needs
filteredList = []
dirList = os.listdir(src)

for z in dirList:
    for i in list(z):
        if i == ".":
            filteredList.append(z)

print("Entering Sorting Stage")


for x in filteredList:
    _, ext = x.split('.')
    for y in docsext:
        if ext == y:
            temp1 = os.path.join(src, x)
            move(temp1, docsdest)

for x in filteredList:
    _, ext = x.split('.')
    for y in musicext:
        if ext == y:
            temp1 = os.path.join(src, x)
            move(temp1, musicdest)
