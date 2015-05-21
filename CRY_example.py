import CRY_ini
import CRY_focus

from mantid.simpleapi import config
config['datasearch.searcharchive'] = 'On'
print config['datasearch.searcharchive']
	
expt=CRY_ini.files("hrpd",Analysisdir='test')
#expt.RawDir="C:/AZIZWORK/BigData/HRPD/Bigg"
expt.initialize('cycle_09_2',user = 'tester',prefFile='mtd.pref')
expt.tell()
#------------------------------------
# 1) process single runs, given as 
#     a list of mubers OR ranges (raw):
# eg: "1000 1005 1250-1260" 
#    AND/OR process a range of runs merging data every n runs 
#    (checks for 0 uamps data)
# eg: "1300-1200-5"
# The two options can be used together
# 3) XOR: process several instermediate saves
# eg: s42356 1-3 5
#------------------------------------
#CRY_focus.FocusAll(expt,"43022-43025 43028-43045-3")
CRY_focus.FocusAll(expt,"43022")
# Optional : 
# Skip Normalization & user-defined scale, e.g:
#CRY_focus.FocusAll(expt,"1000 1005 1250-1260" , scale=100, Norm=False)
