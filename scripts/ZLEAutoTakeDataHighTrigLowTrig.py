import subprocess
import os
import argparse
import time
from datetime import datetime


def RunZLE(config, num_events, outdir, tag, events_per_segment):
    with open(f"{outdir}log.txt", 'w') as f:
        subprocess.run(["./../build/zle_exe",
        config,
        str(num_events),
        outdir,
        tag,
        str(events_per_segment)], stdout = f)

    return f"Finished run"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="For taking data in runs using ZLE")
    parser.add_argument('--low_config',
        help = "Low-trigger configuration file for data taking",
        dest = 'low_config', action = 'store', required = True, type = str, default = None)
    parser.add_argument('--high_config',
        help = "High-trigger configuration file for data taking",
        dest = 'high_config', action = 'store', required = True, type = str, default = None)
    parser.add_argument('--events_per_run',
        help = "Number of events per run",
        dest = 'events_per_run', action = 'store', required = True, type = int, default = 1000000)
    parser.add_argument('--run_mode_low',
        help = "Run mode for the low trigger",
        dest = 'run_mode_low', action = 'store', required = True, type = str, default = None)
    parser.add_argument('--run_mode_high',
        help = "Run mode for the high trigger",
        dest = 'run_mode_high', action = 'store', required = True, type = str, default = None)
    parser.add_argument('--rawdata_dir',
        help = "Raw data directory",
        dest = 'rawdata_dir', action = 'store', required = True, type = str, default = None)
    parser.add_argument('--events_per_segment',
        help = "Events per segment",
        dest = 'events_per_segment', action = 'store', required = True, type = int, default = 10000)
    parser.add_argument('--acquisition_time_low',
        help = "Time that the low trigger data taking will run for",
        dest = 'acquisition_time_low', action = 'store', required = True, type = int, default = 3600)
    parser.add_argument('--acquisition_time_high',
        help = "Time that the high trigger data taking will run for",
        dest = 'acquisition_time_high', action = 'store', required = True, type = int, default = 3600)
    parser.add_argument('--n_cycles',
        help = "Number of cycles for high and low data taking",
        dest = 'n_cycles', action = 'store', required = True, type = int, default = 1)
    
    args = parser.parse_args()

    if (args.rawdata_dir[-1]!='/'):
        args.rawdata_dir += '/'

    lowtrig_run_date_output_dir = f"{args.rawdata_dir}{args.run_mode_low}/"
    hightrig_run_date_output_dir = f"{args.rawdata_dir}{args.run_mode_high}/"

    for i in range(args.n_cycles):
        start_time = time.time()
        while (time.time()-start_time < args.acquisition_time_low):
            #Take the low trigger data
            run_id = datetime.now().strftime('%Y%m%d') + "T"+datetime.now().strftime('%H%M%S')
            full_output_dir = lowtrig_run_date_output_dir + run_id + "/"

            if not os.path.exists(full_output_dir):
                os.mkdir(full_output_dir, mode = 0o777)

            RunZLE(args.low_config, args.events_per_run, full_output_dir, args.run_mode_low, args.events_per_segment)
            time.sleep(2)
        
        start_time = time.time()
        while (time.time()-start_time < args.acquisition_time_high):
            #Take the low trigger data
            run_id = datetime.now().strftime('%Y%m%d') + "T"+datetime.now().strftime('%H%M%S')
            full_output_dir = hightrig_run_date_output_dir + run_id + "/"

            if not os.path.exists(full_output_dir):
                os.mkdir(full_output_dir, mode = 0o777)

            RunZLE(args.high_config, args.events_per_run, full_output_dir, args.run_mode_high, args.events_per_segment)
            time.sleep(2)