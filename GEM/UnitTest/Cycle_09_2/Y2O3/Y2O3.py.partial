from SET_env_scripts1 import *
expt=CRY_ini.files("gem",UnitTest=True)
expt.initialize('Cycle_09_2','Y2O3')
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
#
# e.g: CRY_focus.FocusAll(expt,"43022-43025 43028-43045-3")
#------------------------------------
#CRY_vana.correctOrLoadVana(expt, NoAbs=True)
# Optional arguments
# CRY_focus,FocusAll(expt, samplelistTexte, scale=0, NoVabs=False, NoSAC=False, Eff=True, Norm=True)
# By default:
# Norm is set to normalize to a vana, in such case:
#   NoVabs is set to DO the Vana Abs correction
#   NoSAC is set to DO a  Solid angle correction
#   Eff is set to DO the efficiency correction using the wavelenght integration of each spectrum
# If norm only the Sample focussing is done, without any corrections
#
CRY_focus.FocusAll(expt,"46489")
