#!/usr/bin/env python
import os
import glob
from PIL import Image
import PIL
import shutil

target_dir = 'compress'
root = os.getcwd()
cwd = root+"\\"+target_dir
os.chdir( cwd )

images = [file for file in os.listdir() if file.endswith(('jpg', 'png','jfif'))]

def createFolder(dirname):
	if not os.path.exists(dirname):
		try:
			os.mkdir(dirname)
		except OSError:
			print("Fail to create directory")

def compressImage():
	compressed_file = []
	for img in images:
		fname = img.split('.')[0]
		ext   = img.split('.')[1]
		file_name = fname+"-compressed."+ext
		
		print("Compressing",fname+"...")
		image = Image.open(img)
		image.save(file_name,
				 optimize=True,
				 quality=30) #upto 65
		compressed_file.append(file_name)
	moveFile(compressed_file)

def moveFile(files):
	target_dir = root+'\\compressed_result'
	createFolder(target_dir)
	for file in files:
		file_dir = cwd+'\\'+file
		shutil.move(file_dir, target_dir+'\\'+file)
		print("Migrating",file+"...")

compressImage()