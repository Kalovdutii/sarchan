import os
import random
import sys
import shutil

def pytooshop(f,cycles):
	fsize = os.path.getsize(f)
	f = open(f,"rb+")
	for i in range(cycles):
		ss = random.randint(1,3)
		f.seek(random.randint(100,fsize-ss-1))
		buf = f.read(ss)
		
		f.seek(random.randint(100,fsize-ss-1))
		f.write(buf)
	
	f.close()

