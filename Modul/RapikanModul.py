#!/usr/bin/env python
import os
import re
import shutil

target_dir = "datamining (ok)"
cwd = os.getcwd()+"\\"+target_dir #folder target
os.chdir(cwd)

def createFolder(fname):
	if not os.path.exists(fname):
		try:
			os.mkdir(fname)
		except OSError:
			print("Gagal membuat folder")

def moveFile():
	pattern = r"(m[0-9]+)"
	folders = []
	
	for file in os.listdir(cwd):
		result = re.search(pattern, file)
		if result is not None:
			folders.append(result.group(0))

	folders = set( folders )
	
	for folder in folders:
		folder = folder.replace("m", "Modul ")
		createFolder(os.getcwd()+"\\"+folder)
	
	#Pindahkan file
	for file in os.listdir(cwd):
		result = re.search(pattern, file)
		if result is not None:
			folder_target = result.group(0)
			folder_target = folder_target.replace("m", "Modul ")
		file_dir = cwd+"\\"+file
		if result is not None and os.path.isfile(file_dir):
			shutil.move(file_dir, cwd+"\\"+folder_target+"\\"+file)
			print(file, "sedang dipindahkan")

moveFile()
	