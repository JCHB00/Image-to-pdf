#img2pdf
#T1
import img2pdf
import os
from PyPDF2 import PdfWriter
# image file
img = '1'
pdf_n = img + '.pdf'
jpg_n = img + '.jpg'
with open(pdf_n,"wb") as f:
	f.write(img2pdf.convert(jpg_n))

img_list = []
pdf_list = []
for i in range(1,20):
    print('Please input the name of the image, not need the .jpg /.png, input quit can stop the loop.')
    a = input('请输入图片名称,不需要输入.jpg/.png, 输入quit可以结束,最多可输入20次')
    if a  == 'quit':
        break
    else:
        img_list.append(a)
for i in img_list:
    pdf_n = i + '.pdf'
    pdf_list.append(pdf_n)
    jpg_n = i + '.jpg'
    with open(pdf_n,"wb") as f:
        f.write(img2pdf.convert(jpg_n))

#合拼
merger = PdfWriter()
for pdf in pdf_list:
    merger.append(pdf)
merger.write('merged-pdf.pdf')
merger.close()
