from mantidsimple import *
import SET_env_scripts1
import CRY_ini
import CRY_focus
import CRY_vana
	
expt=CRY_ini.files("hrpd",UnitTest=True)
expt.initialize('Cycle08_2','Calibration',prefFile="mtd_s1_old.pref")
CRY_focus.FocusAll(expt,"39182")
expt.initialize('Cycle08_2','Calibration',prefFile="mtd_s1_new.pref")
CRY_focus.FocusAll(expt,"39182")
