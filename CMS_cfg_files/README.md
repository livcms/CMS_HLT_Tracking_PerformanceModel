# CMS_cfg_files

These files are based on those by Dr. Shane Breeze, with small alterations, described below. 
<https://github.com/shane-breeze/CMS_HLT_Phase2_Tracking> 


## DQM Fast Timer Service 
The DQM Fast Timer Service is defined in step3_tracking/modules/extras_cff.py

enableDQMbyModule should be set to true for module timings. Values for dqmModuleTimeResolution and dqmTimeRange should be set. 

## Defining pileup in MC event generation

To set a constant, or poisson distributed pileup, something like this can be set: 
```
if options.nopileup==1:
    process.load('SimGeneral.MixingModule.mixNoPU_cfi')
elif options.nopileup==0:
    process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
    process.mix.input.type = cms.string('fixed')
else:
    process.load('SimGeneral.MixingModule.mix_FIX_average_cfi')
```


## Copy of Dr. Breeze's README

A collection of [CMSSW](https://github.com/cms-sw/cmssw) configuration files
and modules to generate and run the HLT phase II tracking algorithm. Currently
setup to generate 14 TeV tt MC with (optionally) 200 average pileup vertices.
The configuration files are split into 4 steps: `gen`, `raw`, `tracking` and
`harvest`. Each step is detailed below. To setup this repository with the
relevent CMSSW environment run

```
git clone https://github.com/shane-breeze/CMS_HLT_Phase2_Tracking
cd CMS_HLT_Phase2_Tracking
sh setup.sh
```

### General configuration

The general configuration for each step includes:

* conditions: `110X_mcRun4_realistic_v3`
* beamspot: `HLLHC14TeV`
* geometry: `Extended2026D49`
* era: `Phase2C9`

### `gen`

The GEN step calculates the matrix element for the process and passes this to
a parton shower to generate a full set of MC events. The response of the
detector to these events is simulated. Execute this step with

```
cmsRun step1_gen/cfg.py maxEvents=10 nThreads=4 outputFile=file:gen.root
```

### `raw`

This step involves the overlay of pileup vertices, digitisation of the detector
output, L1 trigger, conversion to RAW event format and the HLT trigger. The
overlay of pileup vertices (known as pileup mixing) uses a reference MC dataset
(e.g. minimum bias) as a set of pregenerated pileup vertices. The number of
pileup vertices per event is taken as a random sampling of a poission
distribution centered on a desired number (default is 200). The pileup mixing
may be turned off. This step is executed with

```
cmsRun step2_raw/cfg.py maxEvents=10 nThreads=4 inputFiles=file:gen_numEvent10.root outputFile=file:raw.root mixnpu=200
```

### `tracking`

This step involves the unpacking of the RAW event format followed by a custom
set of modules defined in `step3_tracking/modules/` to perform the tracking,
validation and DQM. There are three versions of the tracking algorithm to choose
from. By default the reconstruction output is not written. This step is executed
with

```
cmsRun step3_tracking/cfg.py maxEvents=10 nThreads=4 inputFiles=file:raw_numEvent10.root outputFile=file:tracking.root
```

Some pre-exisiting `GEN-SIM-DIGI-RAW` files may be used in place of steps 1 and
2. These can be found with

```
dasgoclient --query "dataset=/*14TeV*/Phase2HLT*/GEN-SIM-DIGI-RAW"
dasgoclient --query "file dataset=/TT_TuneCP5_14TeV-powheg-pythia8/Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2/GEN-SIM-DIGI-RAW" # replace with the desired dataset
```

and use the resulting files as the `inputFiles` option for the above `cmsRun` command.

### `harvest`

The harvesting stage collects information on the tracking steps, such as timing
and performance. A DQM output file is generated containing all the relevent
information. This step is executed with

```
cmsRun step4_harvest/cfg.py maxEvents=10 nThreads=4 inputFiles=file:tracking.root
```

### References

* <https://twiki.cern.ch/twiki/bin/viewauth/CMS/HighLevelTriggerPhase2>
* <https://github.com/hevjinyarar/CMS_HLT_Phase2_Tracking>
* <https://twiki.cern.ch/twiki/bin/viewauth/CMS/FastTimerService>
* <https://twiki.cern.ch/twiki/bin/viewauth/CMS/TriggerStudiesTiming>
