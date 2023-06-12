# ZLE Dump

A modification of wavedump using ZLE for the V1720. This will still work without ZLE, but allows for ZLE to work. There are modifications to the config file which programs for the ZLE enabling, ZLE thresholds per channel, and ZLE look forward and look back.

## Usage:

```
./zle_exe [config] [number of events] [output directory (JUST the directory)] [tag (the type of data you are taking)] [events per segment]
```

Here, a `run` is a timestamp of [YYYY][MM][DD]T[HH][mm][SS] and is a folder containing `number of events` events. These are broken up into segments for processing, so that way a whole file of several GB does not have to be loaded at once.
