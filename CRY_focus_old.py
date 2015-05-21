from mantid.simpleapi import *
import CRY_utils
import CRY_load
import CRY_sample
import CRY_vana

#===========
# Focussing
# ==========
def FocusAll(expt, samplelistTexte, scale=0, NoVabs=False, NoSAC=False, Eff=True, Norm=True):
	if scale == 0:
		scale=float(expt.scale)
	# === Norm boolean flag used to Optionally correct to a Vana ===
	if Norm:
		# SAC/EFF corrections loads the Vana
		LoadSacEff(expt, NoSAC=NoSAC, Eff=Eff)
		newCalFile=expt.user+expt.GrpFile
		MaskDetectorsIf(InputWorkspace="Corr",InputCalFile=expt.Path2GrpFile,OutputCalFile=newCalFile,Mode="DeselectIf",Operator="Equal",Value=0)	
		expt.Path2GrpFile=newCalFile
		errReadFiles=CRY_vana.CorrectOrLoadVana(expt,NoAbs=NoVabs)
		if errReadFiles:
			print 'No Required Vanadium data available, skip this treatement'
			print 'Maybe, Vruns form a Wrong Cycle?'
			return
	else:
		LoadSacEff(expt, NoSAC=True)	
	# === Construct a list of runs, sum of runs
	sampleSumLists=CRY_utils.getSampleList(expt.basefile,samplelistTexte,expt.RawDir)
	# to loop over
	for sample2Add in sampleSumLists:
		print '--------------------------'
		print '         Start focus here        '
		print '--------------------------'
		print " ---> " + Focus(expt,sample2Add, scale, Norm)

def LoadSacEff(expt, NoSAC=False, Eff=True):
# Loads SAC/Efficiency correction in wkspc "Corr" or sets it to "1"
	if NoSAC:
		CreateSingleValuedWorkspace(OutputWorkspace="Corr",DataValue= str(1))
		print " => No SAC/Eff applied "
		return
	else:
		# First try to load the vana (this won't crash if no vana run  is set)....
		(dum,uampstotal)=CRY_sample.getDataSum(expt.VanFile,"Vanadium",expt)
		uampstotal = mtd["Vanadium"].getRun().getProtonCharge()
		if uampstotal<1e-6:
			print " => Van NOT found : No SAC/eff correction will be applied"
			CreateSingleValuedWorkspace(OutputWorkspace="Corr",DataValue= str(1))
		else:
			print ' => Pre-calculate SAC from Vana '
			SolidAngle(InputWorkspace="Vanadium",OutputWorkspace="Corr")                                                                          
			CreateSingleValuedWorkspace(OutputWorkspace="Sc",DataValue= str(100))
			Multiply(LHSWorkspace="Corr",RHSWorkspace="Sc",OutputWorkspace="Corr")
			if Eff:
				Divide(LHSWorkspace="Vanadium",RHSWorkspace="Corr",OutputWorkspace="Vanadium")
				print ' => Pre-calculate Efficiency correction from Vana '
				ConvertUnits(InputWorkspace="Vanadium", OutputWorkspace="Vanadium", Target="Wavelength")
				Integration(InputWorkspace="Vanadium",OutputWorkspace="Vanadium", \
						RangeLower=expt.LowerLambda,RangeUpper=expt.UpperLambda)
				Multiply(LHSWorkspace="Corr",RHSWorkspace="Vanadium",OutputWorkspace="Corr")
				CreateSingleValuedWorkspace(OutputWorkspace="Sc",DataValue= str(100000))
				Divide(LHSWorkspace="Corr",RHSWorkspace="Sc",OutputWorkspace="Corr")
				mtd.remove("Sc")  
#			mtd.remove("Vanadium")  

def Focus(expt, sampleAdd, scale, Norm):
	(outname,uampstotal)=CRY_sample.getDataSum(sampleAdd,"sample",expt)
	if uampstotal<1e-6:
		return "No usable data, Raw files probably not found: cannot create "+outname+"\n"
	if expt.SEmptyFile[0] <> "none":
	# === Optionally loads Sample Empty ===
		(dum1,uamps)=CRY_sample.getDataSum(expt.SEmptyFile,"Sempty",expt)
		Minus(LHSWorkspace="sample",RHSWorkspace="Sempty",OutputWorkspace="sample")
		mtd.remove("Sempty")  
	CRY_load.Align("sample",expt)
	Divide(LHSWorkspace="sample",RHSWorkspace="Corr",OutputWorkspace="sample")	
	CRY_load.ScaleWspc("sample",scale)
	if expt.CorrectSampleAbs=="yes":
		if expt.SampleAbsCorrected==False:
			CRY_utils.CorrectAbs(InputWkspc= "sample", outputWkspc="SampleTrans", \
				TheCylinderSampleHeight=     expt.SampleHeight,                     \
				TheCylinderSampleRadius=      expt.SampleRadius,                     \
				TheAttenuationXSection=      expt.SampleAttenuationXSection,         \
				TheScatteringXSection=       expt.SampleScatteringXSection,          \
				TheSampleNumberDensity=      expt.SampleNumberDensity,               \
				TheNumberOfSlices =          expt.SampleNumberOfSlices,              \
				TheNumberOfAnnuli=           expt.SampleNumberOfAnnuli,              \
				TheNumberOfWavelengthPoints= expt.SampleNumberOfWavelengthPoints,    \
				TheExpMethod=                expt.SampleExpMethod               )
			expt.SampleAbsCorrected=True
		else:
				ConvertUnits(InputWorkspace="sample", OutputWorkspace="sample", Target="Wavelength")
				Divide(LHSWorkspace="sample",RHSWorkspace= "SampleTrans",OutputWorkspace= "sample")
				ConvertUnits(InputWorkspace="sample", OutputWorkspace="sample", Target="dSpacing")
	DiffractionFocussing(InputWorkspace="sample",OutputWorkspace="sample",GroupingFileName=expt.Path2GrpFile)	
	print " => SAMPLE FOCUSED"
	if not expt.dataRangeSet:
		CRY_load.setsDrange("sample",expt)
	CRY_load.SplitBank("sample",expt.bankList, Del=False)
#	CRY_load.BinBank("sample",expt.bankList,expt.Drange)
	if Norm:
		# === Optional normalization ===
#		CRY_load.BinBank("Vanadium",expt.bankList,expt.Drange)
		for i in expt.bankList:
			Divide(LHSWorkspace="sample-"+str(i),RHSWorkspace= "Vanadium-"+str(i),OutputWorkspace= "ResultD-"+str(i))
	else:
		for i in expt.bankList:
			RenameWorkspace(InputWorkspace="sample-"+str(i),OutputWorkspace="ResultD-"+str(i))
	# === Cleans results in D and TOF before outputing bank by bank ===
	CRY_load.BinBank("ResultD",expt.bankList,expt.Drange)
	for i in expt.bankList:
		ConvertUnits(InputWorkspace="ResultD-"+str(i), OutputWorkspace="ResultTOF-"+str(i), Target="TOF")		
		ReplaceSpecialValues(InputWorkspace="ResultD-"+str(i),OutputWorkspace="ResultD-"+str(i),NaNValue="0",InfinityValue="0",BigNumberThreshold="99999999.99999999")
		ReplaceSpecialValues(InputWorkspace="ResultTOF-"+str(i),OutputWorkspace="ResultTOF-"+str(i),NaNValue="0",InfinityValue="0",BigNumberThreshold="99999999.99999999")
	# === Output===
	# GSS
	GrpList="ResultTOF-"+str(expt.bankList[0])
	for i in expt.bankList[1:]:	
		GrpList=GrpList+",ResultTOF-"+str(i)
	GroupWorkspaces(OutputWorkspace="ResultTOFgrp",InputWorkspaces=GrpList)		
	if expt.OutSuf=="":
		OutputFile=expt.user+outname
	else:
		OutputFile=expt.user+outname+"_"+expt.OutSuf	
	# Gss 
	rearrang4GSS(OutputFile,expt)
	# Nexus 
	rearrang4Nex(OutputFile,expt)
	# XYE 
	OutputFile=OutputFile+"_"
	rearrange4XYE(OutputFile,expt,units="TOF")
	rearrange4XYE(OutputFile,expt,units="D")
	return outname+"  focused with uampstotal="+str(uampstotal)

#===========
# Output in XYE, GSS...
# ==========
def rearrange4XYE(OutputFile,expt,units="TOF"):
	if (units=="D" and expt.saveXYEd) or (units=="TOF" and expt.saveXYEtof):
		for i in expt.bankList:		
			inwkpsc="Result"+units+"-"+str(i)
			SaveFocusedXYE(InputWorkspace=inwkpsc, Filename=OutputFile+"b"+str(i)+"_"+units+".dat", SplitFiles="False")
	
def rearrang4GSS(OutputFile,expt):
	if expt.GSS == "no":
		return
	SaveGSS(InputWorkspace="ResultTOFgrp", Filename=OutputFile+".gss", SplitFiles="False", Append=False )

def rearrang4Nex(OutputFile,expt):
	if expt.Nex == "no":
		return
	#SaveNexusProcessed(Filename=OutputFile+".nxs", InputWorkspace="ResultTOFgrp")
	groupList = mtd["ResultTOFgrp"].getNames()
	for name in groupList[1:]:
		SaveNexusProcessed(InputWorkspace=name,Filename=OutputFile+'.nxs', Append=True) 
			
if __name__ == '__main__':
	rearrange4XYE("ResultTOFtmp",0,"11200,-0.0003,104000","tst1.dat",units="TOF")	
	rearrange4XYE("ResultTOFtmp",1,"11200,-0.0008,104000","tst2.dat",units="TOF")	
	rearrange4XYE("ResultTOFtmp",2,"11200,-0.0012,104000","tst3.dat",units="TOF")	
	#CorrectVana(VanFile,EmptyFile,AcalibFile,1)
	#normalizeall(SampleDatFile,AcalibFile)
	#rearrangeallbanks(OutputFile,"")
