# Vtune 

Intel's Vtune 2020.1 was used here. 

## Recompiling CMSSW code 
To see the source code, one must recompile [CMSSW](https://github.com/cms-sw/cmssw)  with debug info. This is done by 
```
scram b clean; scram b USER_CXXFLAGS="-g"
``` 
Scram builds by default in its current directory. Building all of CMSSW with debug info takes about 12-24hrs.

To be able to stop and start vtune, ittnotify must be used. In the relevant Buildfile, add
```
<use   name="itt_notify"/> 
```
and in the relevant file add 
```
#include<ittnotify.h> 
``` 
and around the code that needs to be timed, add 
```
__itt_resume();
__itt_pause(); 
``` 

Itt may need to be set up with CMSSW, in which case, run 
```
scram setup ittnotify
``` 


## Running vtune 
Two different approaches were used. To find hotspots in the relevant code, something like the following command was used: 
```
vtune -collect hotspots -start-paused -quiet  -knob sampling-mode=hw -knob enable-stack-collection=true -knob stack-size=0  -data-limit=0 cmsRun step3_tracking/cfg.py maxEvents=100 nThreads=1 inputFiles=file:raw/raw8_PU200_numEvent500.root outputFile=file:tracking.root
```
It is started paused so it only collects where specified. Hardware mode ensures reliable timings, and by default samples every 1ms. Setting stack-size and data-limit to 0 means they are unlimited. 

To analyze loops, something like the following was used; 
```
vtune -collect-with runsa -start-paused -quiet -knob enable-stack-collection=true -knob stack-size=0 -knob analyze-loops=true -knob enable-trip-counts=true cmsRun step3_tracking/cfg.py maxEvents=100 nThreads=1 inputFiles=file:raw/raw8_PU200_numEvent500.root outputFile=file:tracking.root
``` 
Run vtune gui with 
```
vtune-gui
``` 

NB: the files here are only the result files. In vtune, one can open the corresponding source code, for which the source files are needed.  
