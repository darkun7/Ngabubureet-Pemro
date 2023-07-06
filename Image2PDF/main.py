#!/usr/bin/env python
import os
import re
import shutil
import aspose.words as aw
from PIL import Image
from fpdf import FPDF

target_dir = "images"
cwd = os.getcwd()+"\\"+target_dir
os.chdir(cwd)

def createFolder(fname):
	if not os.path.exists(fname):
		try:						
			os.mkdir(fname)
		except OSError:			
			print("Gagal membuat folder")

def convertToPDF():
    images = [file for file in os.listdir() if file.endswith(('jpg', 'png','jfif'))]
    # doc = aw.Document()
    # builder = aw.DocumentBuilder(doc)

    # for fileName in images:
    #     builder.insert_image(fileName)
    #     builder.writeln()

    # doc.save("Output.pdf")
    # print('finish')

    pdf = FPDF()
    w,h = 0,0
    for fileName in images:
        if fileName == images[0]:
            cover = Image.open(fileName)
            w,h = cover.size
            pdf = FPDF(unit = "pt", format = [w,h])
        image = fileName
        pdf.add_page()
        pdf.image(image,0,0,w,h)
    pdf.output("result.pdf", "F")
    print('Finished')

    # for i in range(1, 100):
    #     fname = sdir + "IMG%.3d.png" % i
    #     if os.path.exists(fname):
    #         if i == 1:
    #             cover = Image.open(fname)
    #             w,h = cover.size
    #             pdf = FPDF(unit = "pt", format = [w,h])
    #         image = fname
    #         pdf.add_page()
    #         pdf.image(image,0,0,w,h)
    #     else:
    #         print("File not found:", fname)
    #     print("processed %d" % i)
    # pdf.output("output.pdf", "F")
    # print("done")

convertToPDF()



	