from mantidsimple import *
from SET_env_scripts1 import *	
expt=CRY_ini.files("hrpd",UnitTest=True)
expt.initialize('Cycle08_2','Calibration',prefFile="mtd_s1_new.pref")
CRY_focus.FocusAll(expt,"39182")
