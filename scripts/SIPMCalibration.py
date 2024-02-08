import subprocess as subp
import sys as sys
import time as time
import numpy as np
import os

"""
To use:
    python3 SIPMCalibration.py [ConfigFile] [Threshold] [EventNum] [GroupNum] [Temp] [Voltage] [StoreDir] [MaxEvent(per segment)] [Channels]

"""

try:
    ConfigFile = sys.argv[1]
    Threshold = sys.argv[2]
    EventNum = int(sys.argv[3])
    GroupNum = int(sys.argv[4])
    Temperature = np.round(float(sys.argv[5]))
    Voltage = np.round(float(sys.argv[6]))
    StoreDir = sys.argv[7]
    MaxEvent = int(sys.argv[8])
    Channels = sys.argv[9]

except Exception as e:
    print("Error:",e)
    print("""Missing input. Please use the script in this way:
python3 SIPMCalibration.py [ConfigFile] [Threshold] [EventNum] [GroupNum] [Temperature] [Voltage] [StoreDir] [MaxEvent(per segment)] [Channels]""")

current_folder = f"sipm_{GroupNum}"

full_output_dir = os.path.join(StoreDir,current_folder)
if not os.path.exists(full_output_dir):
    os.mkdir(full_output_dir, mode=0o777)
    print(f"folder {full_output_dir} doesn't exist, just created")
else:
    print(f"folder {full_output_dir} already exists")

tag = f"sipm_group{GroupNum}_threshold{Threshold}_{Temperature}C_{Voltage}V_{MaxEvent}_{Channels}"
print(f"tag is {tag}")
command = f"./../build/zle_exe {ConfigFile} {EventNum} {full_output_dir}/ {tag} {MaxEvent}"
log_file = open(f"{full_output_dir}/log.txt","a")

subp.call(f"{command}",shell=True)

"""
process = subp.Popen(command,shell=True,stdout=subp.PIPE,stderr=subp.STDOUT)
while True:
    # read the information from the process
    line = process.stdout.readline()
    if not line:
        break
    # print the information in terminal
    sys.stdout.write(line.decode())
    sys.stdout.flush()

    # add the information to log_file
    log_file.write(line.decode())
    log_file.flush()
log_file.close()
"""

time.sleep(2)

