#img2pdf
#T1
import img2pdf
import os

#dirsname is the file of photo
dirsname = "./Photo"
imgs = []

for fname in os.listdir(dirsname):
    if not fname.endswith(".jpg"):
        continue
    Path = os.path.join(dirsname,fname)
    if os.path.isdir(Path):
        continue
    imgs.append(Path)

with open("Output.pdf","wb") as f:
    f.write(img2pdf.convert(imgs))

