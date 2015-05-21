from SET_env_scripts1 import *
expt=CRY_ini.files("INS", UnitTest=True)
expt.initialize('Cycle_10_1','test',prefFile="mtd.pref")
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
# Optional : 
# Skip Normalization & user-defined scale, e.g:
#CRY_focus.FocusAll(expt,"1000 1005 1250-1260" , scale=100, Norm=False)
#------------------------------------
CRY_focus.FocusAll(expt,"05957")
#CRY_focus.FocusAll(expt,"05957")
#CRY_focus.FocusAll(expt,"s45601 1")
