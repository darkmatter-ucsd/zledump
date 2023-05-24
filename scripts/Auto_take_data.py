import subprocess as sp
import time
import os
from datetime import datetime
import argparse


#def main():val
parser = argparse.ArgumentParser(description="Auto take data for SanDix")
parser.add_argument('--config', help="what's the config file you want to use?", type=str, default=None)
parser.add_argument('--path', help="what's the path of raw data?", type=str, default=None)
parser.add_argument('--files', help='how many files to take at each run', type=int, default=None)
parser.add_argument('--nevents', help='number of events to take in each file', type=int, default=None)
parser.add_argument('--time', help='how long to take one run (in seconds)', type=float, default=None)
parser.add_argument('--voltage', help='anode/cathode voltage', type=str, default=None)


template = """mkdir {path}
cp {config} {path}
python /home/daqtest/DAQ/Python/RunAcquisition.py {config} {n_events} {file_each_run} {path} >> {log}
"""

args = parser.parse_args()

config = args.config
basic_path = args.path
file_each_run = args.files
n_events = args.nevents
wait_time = args.time
voltage_info = args.voltage


folder = datetime.now().strftime('%Y%m%d') + datetime.now().strftime('%H%M') + '_' + voltage_info
path = os.path.join(basic_path, folder)
log = os.path.join(path, 'log.txt')

command = template.format(template, path=path, file_each_run=file_each_run, config=config, log=log, n_events = n_events)
process = sp.Popen(command, shell=True, stdout=sp.PIPE)
process.wait()

time.sleep(wait_time)

#if __name__ == '__main__':
#    main()
