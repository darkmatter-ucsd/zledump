# ZLE Dump

A modification of wavedump using ZLE for the x720. This will still work without ZLE when not using the x720, but allows for ZLE to work when using the x720. There are modifications to the config file which programs for the ZLE enabling, ZLE thresholds per channel, and ZLE look forward and look back.

## Usage:

```
./zle_exe [config] [number of events] [output directory (JUST the directory)] [tag (the type of data you are taking)] [events per segment]
```

Here, a `run` is a timestamp of [YYYY][MM][DD]T[HH][mm][SS] and is a folder containing `number of events` events. These are broken up into segments for processing, so that way a whole file of several GB does not have to be loaded at once.

`ZLEAutoTakeData.py` takes data with a config file and stores the data files into a folder called a "run mode", which is the type of data that is being taken. For example, a run mode can be "cf252_4500V" to incidate that the data is taken with a Cf-252 source with an anode voltage of 4500V. `ZLEAutoTakeData.py` is ran with the following command:

```
python3 ZLEAutoTakeData.py --config [config file] --events_per_run [events per run] --run_mode [run mode] --rawdata_dir [raw data directory] --events_per_segment [events per segment] --acquisition_time [Time that this program will run for in s]
```

The program runs for the acquisition time plus the time it takes to finish the current run.


## Changes from WaveDump

The zledump software works nearly the same as the default CAEN WaveDump with the following exceptions:
  * Plotting is disabled
  * The data is not split up per channel. I don't know why the default WaveDump does this.
  * The config file has the following new features:
    * ZLE_ENABLED: Whether to enable or disable ZLE. Options are ENABLE or DISABLE
    * ZLE_LFW: Number of samples to save after the pulse has gone below the ZLE threshold
    * ZLE_LBK: Number of samples to save before the pulse has gone above the ZLE threshold
    * ZLE_THRESHOLD: The ZLE threshold configurable for each channel. This is in terms of the absolute threshold in ADC, ranging from 0 to 4095
