import os, sys
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

src_dir = sys.argv[1] if len(sys.argv) >= 2 else '../html'

dirpath = os.getcwd()
log_files = dirpath+"/small_files_result.txt"

count = 0
fw = open(log_files, "w")
print(src_dir)
for root, dirs, files in os.walk(src_dir):
	count += len(files)
	for file in files:
		filepath = os.path.join(root, file)
		f = open(filepath, 'r')
		if os.path.getsize(filepath)<300:
			fw.write(filepath+"\n")
			print(filepath)

print("Total number of files: "+str(count))
print("Finished!")
