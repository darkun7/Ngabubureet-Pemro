#!/usr/bin/env python
import os
import shutil
import glob
import PIL
from PIL import Image

target_dir = "compress"
root = os.getcwd()

cwd = os.getcwd()+"\\"+target_dir #folder target
os.chdir(cwd)

images = [file for file in os.listdir() if file.endswith(('jpg', 'png', 'jfif'))]

def createFolder(fname):
	if not os.path.exists(fname):
		try:
			os.mkdir(fname)
		except OSError:
			print("Gagal membuat folder")

def compressImage():
	compressed_file = []
	for img in images:
		fname = img.split('.')[0]
		ext   = img.split('.')[1]
		file_name = fname+'-compressed.'+ext
		
		print("Compressing file", file_name,"...")
		
		image = Image.open(img)
		image.save(file_name,
				optimize = True,
				quality = 20)
				
		compressed_file.append(file_name)
	moveFile(compressed_file)

def moveFile(files):
	target_dir = root+"\\Compress Result"
	createFolder(target_dir)
	for file in files:
		file_dir = cwd+"\\"+file
		shutil.move (file_dir, target_dir+"\\"+file)
		print("Moving file", file,"...")

	pass

compressImage()