#!/usr/bin/env python
import os
import re
import shutil

target_dir = "datamining (ok)"		# target folder
cwd = os.getcwd()+"\\"+target_dir 	# direktori "datamining(ok)"
os.chdir(cwd)						# pindah ke direktori target

def createFolder(fname):			# fungsi membuat folder, dengan parameter direktori folder yang akan dibuat
	if not os.path.exists(fname):	# pengujian apakah folder sudah ada
		try:						
			os.mkdir(fname)			# membuat folder
		except OSError:			
			print("Gagal membuat folder")

def moveFile():
	pattern = r"(m[0-9]+)"			# pola regex
	folders = []					# list kosong, nantinya untuk menyimpan folder
	
	for file in os.listdir(cwd):			# perulangan isi direktori sebagai file
		result = re.search(pattern, file)	# mencari nama file yang cocok dengan pola
		if result is not None:				# kondisi jika hasil pencarian ditemukan
			folders.append(result.group(0))	# menyimpan nama file kedalam variable folders

	folders = set( folders )		# membuat isi variable folders bernilai unik
	
	for folder in folders:			# perulangan setiap folder
		folder = folder.replace("m", "Modul ") 	# mengubah karakter m menjadi Modul
		createFolder(os.getcwd()+"\\"+folder)	# membuat folder
	
	#Pindahkan file
	for file in os.listdir(cwd):			# perluangan setiap file di direktori target
		result = re.search(pattern, file)	# mencari nama file yang cocok dengan pola
		if result is not None:				# kondisi jika hasil pencarian ditemukan
			folder_target = result.group(0)	# menyimpan nama file kedalam variable folder_target
			folder_target = folder_target.replace("m", "Modul ") 	# mengubah karakter m menjadi Modul
		file_dir = cwd+"\\"+file			# variable berisi path/ lokasi file
		if result is not None and os.path.isfile(file_dir): 		# kondisi jika hasil pencarian ditemukan dan file yang dicari ada
			shutil.move(file_dir, cwd+"\\"+folder_target+"\\"+file) # memindahkan file dari lokasi asal, ke lokasi tujuan
			print(file, "sedang dipindahkan")

moveFile()	# menjalankan fungsi moveFile
	