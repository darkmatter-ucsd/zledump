##########################
#written by Qing Lin @ 2012-11-05
###################################

import subprocess as subp
import sys as sys
import time as time

ConfigFile = sys.argv[1]
EventNum = int(sys.argv[2])
FileNum = int(sys.argv[3])
Path = sys.argv[4]

for i in range(FileNum):
	subp.call(f"./../zledump/build/zle_exe {ConfigFile} {EventNum} {Path}/", shell=True)
	#print i
	time.sleep(2)
	
	
