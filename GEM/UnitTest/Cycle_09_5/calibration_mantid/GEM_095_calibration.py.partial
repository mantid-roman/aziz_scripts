from SET_env_scripts1 import *
#CRY_ini.EnvAnalysisdir='B:/MantidPowderFocus/scripts1/GEM/UnitTest/'
#print sys.path
# RAW file setup
expt=CRY_ini.files("gem", UnitTest=True)
#expt=CRY_ini.files("gem")
expt.initialize('Cycle_09_5','calibration_mantid','GEM_095_calibration.pref')
#------------------------------------
# 1) process single runs, given as a list of numbers OR ranges (raw):
#    eg: "1000 1005 1250-1260" 
# 2)   AND/OR process a range of runs merging data every n runs 
#    (checks for 0 uamps data)
# eg: "1300-1200-5"
# The two options can be used together
# 3) XOR: process several intermediate saves
# eg: s42356 1-3 5
#------------------------------------
#CRY_focus.FocusAll(expt,"43022-43025 43028-43045-3")
#CRY_focus.FocusAll(expt,"48560", NoVabs=False)
CRY_focus.FocusAll(expt,"48560")
#
