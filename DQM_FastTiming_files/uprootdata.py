import uproot
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import re

#DQMFilename = raw_input("Please enter filename (must have PU followed by pileup number:")
DQMFilename = raw_input("Please enter filename (must have PU followed by pileup number:")
file = uproot.open(DQMFilename)["DQMData;1"]["Run 1;1"]["DQM;1"]["Run summary;1"]["TimerService;1"]
numevent= re.compile("numEvent([0-9]*)")
numevents = int(numevent.findall(DQMFilename)[0])
#there are two directories in the Timerservice. Find the names in the first directory
plotnames = file.keys()
#we are only interested in the time plots, and not by the ones by ls
time_plotnames = [name for name in plotnames if ("time_real" in name) & ("byls" not in name)]


#find names in the second directory, which contains by module info    
timebymodule = file["process RECO modules;1"]
plotnames_bymodule = timebymodule.keys()
time_plotnames_bymodule = [name for name in plotnames_bymodule if ("time_real" in name) & ("byls" not in name)]


#the data is in histograms, so binned. Function to find midpoint of bin. If the upper limit is infinite, set midpoint as the left edge of the bin
def midpoint(bins): 
    if np.isinf(bins.right): 
        x = bins.left
    else: 
        x = bins.mid
    return x



times =[]
stds =[]
#come back and generalise


#iterate through each plot and append the average time and standard deviation to lists 
def read_hists_from_folder(directory, plotnamelist):
    for name in plotnamelist: 
    
            timehist = directory[name]
            timehistpd = timehist.pandas()
	     
	    
            #uproot reads all the zeros from the histogram. Read only non_zero values. Bins are an index, reset so they become a column
            nonzero_timehist = timehistpd[timehistpd["count"]>0].reset_index()	    
            nonzero_timehist["bin_centres"] = nonzero_timehist.iloc[:,0].apply(lambda x:  midpoint(x))
            if name=="event time_real;1": 
                print(nonzero_timehist["bin_centres"])
            #count times bin centre
            count_times =nonzero_timehist["count"]*nonzero_timehist["bin_centres"]
            avtime =sum(count_times)/numevents
            times.append(round(avtime,2))
            stds.append(round(np.std(count_times),2))
            #numevents = sum(nonzero_timehist["count"])  


read_hists_from_folder(file, time_plotnames)

read_hists_from_folder(timebymodule, time_plotnames_bymodule)


res = pd.DataFrame({
    #print module names so the string stops where "time" begins
    "Module":  [name[:name.rfind("time")] for name in time_plotnames+time_plotnames_bymodule], 
    "Average time/event (ms) at " + str(int(numevents)) +" events": times, 
      "Std (ms) at " +str(int(numevents)) + " events" : stds
})
#pd.set_option("display.max_rows", None, "display.max_columns", None)
cols = list(res)
#since the average time column name is so long, it is displayed first, reshuffle so module comes first 
cols.insert(0, cols.pop(cols.index("Module")))
reordered_res = (res.ix[:, cols])
outputname = raw_input("Please enter output file name")
print(sum(reordered_res.iloc[5:, 1]))
reordered_res.to_csv(outputname+".csv")
