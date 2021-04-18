#!/usr/bin/env python
import os
import shutil
import glob
import PIL
from PIL import Image

root = os.getcwd()					# folder utama

target_dir = "kompres"				# target folder
cwd = os.getcwd()+"\\"+target_dir 	# folder target
os.chdir(cwd)						# pindah ke direktori target

images = [file for file in os.listdir() if file.endswith(('jpg', 'png', 'jfif'))]	# Memperoleh file yang berekstensi tertentu untuk disimpan kedalam variable

def createFolder(fname):			# fungsi membuat folder, dengan parameter direktori folder yang akan dibuat
	if not os.path.exists(fname):	# pengujian apakah folder sudah ada
		try:						
			os.mkdir(fname)			# membuat folder
		except OSError:			
			print("Gagal membuat folder")

def compressImage():
	compressed_file = []			# list kosong, nantinya untuk menyimpan nama file
	for img in images:				# perulangan setiap file
		fname = img.split('.')[0]	# memperoleh nama file, disimpan ke dalam variable
		ext   = img.split('.')[1]	# memperoleh ekstensi file, disimpan ke dalam variable
		file_name = fname+'-compressed.'+ext # nama file baru yang akan disimpan
		print("Compressing file", file_name,"...")
		
		image = Image.open(img)		# stream gambar yang akan diproses
		image.save(file_name,		# menyimpan gambar dengan pengaturan kompresi tertentu
				optimize = True,
				quality = 20)
				
		compressed_file.append(file_name)	# menyimpan nama file kedalam variable compressed_file
	moveFile(compressed_file)		# menjalankan fungsi moveFile dengan parameter list dari seluruh nama file

def moveFile(files):				
	target_dir = root+"\\hasil"		# folder target
	createFolder(target_dir)		# membuat folder
	for file in files:				# perulangan setiap file
		file_dir = cwd+"\\"+file	# variable berisi path/ lokasi file
		shutil.move (file_dir, target_dir+"\\"+file) # memindahkan file dari lokasi asal, ke lokasi tujuan
		print("Moving file", file,"...")

compressImage()