import os
import time
#this has to run all the time, seperate the saving files from climate control since if internet goes down I want to be able to keep climate control on 
while True:
	try: 
		os.system("git add . ")
		os.system("git commit -a -m  'auto update' ")
		os.system("git push origin main ")
	except: 
		print("git not pushing right")
		
	time.sleep(60)
