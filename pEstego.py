#liburutegiak
import zipfile
import hashlib
import os

#hash kalkulatzeko funtzioa
def md5Kalkulatu(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # 64k chunk-etan irakurri
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

zip_file_path = '/home/asier/Escritorio/3/segurtasuna/labo1/1 Laborategia -  Zifraketa I-20230925/irudia.zip'
with zipfile.ZipFile(zip_file_path, 'r') as archive:
	for file_info in archive.infolist():
	# file bakoitzaren hash kalkulatu
		file_name = file_info.filename
		file_hash = md5Kalkulatu(archive.extract(file_info))
		if "e5ed313192776744b9b93b1320b5e268" == file_hash:
			print(f'File: {file_name}, MD5: {file_hash}')
			archive.extract(file_info, "/home/asier/Escritorio/3/segurtasuna/labo1/jpgZuzenak")
		
			
