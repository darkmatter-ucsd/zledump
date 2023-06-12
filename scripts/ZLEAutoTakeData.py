import subprocess
import os
import argparse
import time
from datetime import datetime


def RunZLE(config, num_events, outdir, tag, events_per_segment):

    """./zle_exe ~/DAQ/WavedumpConfig/sandix_zle_test.txt 2000000 /media/daqtest/Samsung4T/Run29/rawdata/xe_act_zle_4000V/ xe_act_zle_4000V 10000"""

    with open(f"{outdir}log.txt", 'w') as f:
        subprocess.run(["./../build/zle_exe",
        config,
        str(num_events),
        outdir,
        tag,
        str(events_per_segment)], stdout = f)
    # subprocess.run(["./../build/zle_exe",
    #     config,
    #     str(num_events),
    #     outdir,
    #     tag,
    #     str(events_per_segment)])

    return f"Finished run"

if __name__ == "__main__":
    start_time = time.time()

    parser = argparse.ArgumentParser(description="For taking data in runs using ZLE")
    parser.add_argument('--config',
        help = "Configuration file for data taking",
        dest = 'config', action = 'store', required = True, type = str, default = None)
    parser.add_argument('--events_per_run',
        help = "Number of events per run",
        dest = 'events_per_run', action = 'store', required = True, type = int, default = 1000000)
    parser.add_argument('--run_mode',
        help = "Run mode",
        dest = 'run_mode', action = 'store', required = True, type = str, default = None)
    parser.add_argument('--rawdata_dir',
        help = "Raw data directory",
        dest = 'rawdata_dir', action = 'store', required = True, type = str, default = None)
    parser.add_argument('--events_per_segment',
        help = "Events per segment",
        dest = 'events_per_segment', action = 'store', required = True, type = int, default = 10000)
    parser.add_argument('--acquisition_time',
        help = "Time that this program will run for",
        dest = 'acquisition_time', action = 'store', required = True, type = int, default = 3600)
    
    args = parser.parse_args()

    if (args.rawdata_dir[-1]!='/'):
        args.rawdata_dir += '/'

    run_date_output_dir = f"{args.rawdata_dir}{args.run_mode}/"




    while (time.time()-start_time < args.acquisition_time):
        run_id = datetime.now().strftime('%Y%m%d') + "T"+datetime.now().strftime('%H%M%S')
        full_output_dir = run_date_output_dir + run_id + "/"

        if not os.path.exists(full_output_dir):
            os.mkdir(full_output_dir, mode = 0o777)

        RunZLE(args.config, args.events_per_run, full_output_dir, args.run_mode, args.events_per_segment)
        time.sleep(2)