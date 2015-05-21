######################################################################
#Python Script Generated by Algorithm History Display 
######################################################################
LoadRaw(Filename="B:\MantidPowderFocus\scripts2/hrpd/UnitTest/RAW/hrp39191.raw",OutputWorkspace="Vanadium",LoadLogFiles="0")
MaskBins(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",XMin="19970",XMax="20140")
MaskBins(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",XMin="39970",XMax="40140")
MaskBins(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",XMin="59970",XMax="60140")
MaskBins(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",XMin="79970",XMax="80140")
MaskBins(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",XMin="99970",XMax="100140")
NormaliseByCurrent(InputWorkspace="Vanadium",OutputWorkspace="Vanadium")
SolidAngle(InputWorkspace="Vanadium",OutputWorkspace="Corr")
CreateSingleValuedWorkspace(OutputWorkspace="Sc",DataValue="100")
Multiply(LHSWorkspace="Corr",RHSWorkspace="Sc",OutputWorkspace="Corr")
Divide(LHSWorkspace="Vanadium",RHSWorkspace="Corr",OutputWorkspace="Vanadium")
ConvertUnits(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",Target="Wavelength")
Integration(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",RangeLower="1.3999999999999999",RangeUpper="3")
Multiply(LHSWorkspace="Corr",RHSWorkspace="Vanadium",OutputWorkspace="Corr")
CreateSingleValuedWorkspace(OutputWorkspace="Sc",DataValue="100000")
Divide(LHSWorkspace="Corr",RHSWorkspace="Sc",OutputWorkspace="Corr")
LoadRaw(Filename="B:\MantidPowderFocus\scripts2/hrpd/UnitTest/RAW/hrp39191.raw",OutputWorkspace="Vanadium",LoadLogFiles="0")
MaskBins(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",XMin="19970",XMax="20140")
MaskBins(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",XMin="39970",XMax="40140")
MaskBins(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",XMin="59970",XMax="60140")
MaskBins(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",XMin="79970",XMax="80140")
MaskBins(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",XMin="99970",XMax="100140")
NormaliseByCurrent(InputWorkspace="Vanadium",OutputWorkspace="Vanadium")
LoadRaw(Filename="B:\MantidPowderFocus\scripts2/hrpd/UnitTest/RAW/hrp39187.raw",OutputWorkspace="Empty",LoadLogFiles="0")
MaskBins(InputWorkspace="Empty",OutputWorkspace="Empty",XMin="19970",XMax="20140")
MaskBins(InputWorkspace="Empty",OutputWorkspace="Empty",XMin="39970",XMax="40140")
MaskBins(InputWorkspace="Empty",OutputWorkspace="Empty",XMin="59970",XMax="60140")
MaskBins(InputWorkspace="Empty",OutputWorkspace="Empty",XMin="79970",XMax="80140")
MaskBins(InputWorkspace="Empty",OutputWorkspace="Empty",XMin="99970",XMax="100140")
NormaliseByCurrent(InputWorkspace="Empty",OutputWorkspace="Empty")
Minus(LHSWorkspace="Vanadium",RHSWorkspace="Empty",OutputWorkspace="Vanadium")
AlignDetectors(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",CalibrationFile="B:\MantidPowderFocus\scripts2/hrpd/UnitTest//GrpOff//hrpd_new_072_01_corr.cal")
Divide(LHSWorkspace="Vanadium",RHSWorkspace="Corr",OutputWorkspace="Vanadium")
ConvertUnits(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",Target="Wavelength")
CylinderAbsorption(InputWorkspace="Vanadium",OutputWorkspace="Transmission",AttenuationXSection="5.0999999999999996",ScatteringXSection="5.0800000000000001",SampleNumberDensity="0.071999999999999995",NumberOfWavelengthPoints="100",CylinderSampleHeight="2",CylinderSampleRadius="0.40000000000000002",NumberOfSlices="10",NumberOfAnnuli="10")
Divide(LHSWorkspace="Vanadium",RHSWorkspace="Transmission",OutputWorkspace="Vanadium")
ConvertUnits(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",Target="dSpacing")
DiffractionFocussing(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",GroupingFileName="B:\MantidPowderFocus\scripts2/hrpd/UnitTest/Cycle08_2/Si/hrpd_new_072_01_corr.cal")
ReplaceSpecialValues(InputWorkspace="Vanadium",OutputWorkspace="Vanadium",NaNValue="0",InfinityValue="0",BigNumberThreshold="99999999.999999985")
CropWorkspace(InputWorkspace="Vanadium",OutputWorkspace="Vanadium-1",EndWorkspaceIndex="0")
SmoothData(InputWorkspace="Vanadium-1",OutputWorkspace="Vanadium-1",NPoints="100")
RemoveBins(InputWorkspace="Vanadium-1",OutputWorkspace="Vanadium-1",XMin="2.1240000000000001",XMax="2.1680000000000001",Interpolation="Linear",WorkspaceIndex="0")
RemoveBins(InputWorkspace="Vanadium-1",OutputWorkspace="Vanadium-1",XMin="1.502",XMax="1.5329999999999999",Interpolation="Linear",WorkspaceIndex="0")
RemoveBins(InputWorkspace="Vanadium-1",OutputWorkspace="Vanadium-1",XMin="1.2250000000000001",XMax="1.254",Interpolation="Linear",WorkspaceIndex="0")
RemoveBins(InputWorkspace="Vanadium-1",OutputWorkspace="Vanadium-1",XMin="1.0609999999999999",XMax="1.0840000000000001",Interpolation="Linear",WorkspaceIndex="0")
RemoveBins(InputWorkspace="Vanadium-1",OutputWorkspace="Vanadium-1",XMin="0.94999999999999996",XMax="0.96999999999999997",Interpolation="Linear",WorkspaceIndex="0")
RemoveBins(InputWorkspace="Vanadium-1",OutputWorkspace="Vanadium-1",XMin="0.86799999999999999",XMax="0.88300000000000001",Interpolation="Linear",WorkspaceIndex="0")
RemoveBins(InputWorkspace="Vanadium-1",OutputWorkspace="Vanadium-1",XMin="0.80300000000000005",XMax="0.81999999999999995",Interpolation="Linear",WorkspaceIndex="0")
RemoveBins(InputWorkspace="Vanadium-1",OutputWorkspace="Vanadium-1",XMin="0.70299999999999996",XMax="0.72199999999999998",Interpolation="Linear",WorkspaceIndex="0")
RemoveBins(InputWorkspace="Vanadium-1",OutputWorkspace="Vanadium-1",XMin="0.64400000000000002",XMax="0.64800000000000002",Interpolation="Linear",WorkspaceIndex="0")
RemoveBins(InputWorkspace="Vanadium-1",OutputWorkspace="Vanadium-1",XMin="0.59199999999999997",XMax="0.59799999999999998",Interpolation="Linear",WorkspaceIndex="0")
LoadRaw(Filename="B:\MantidPowderFocus\scripts2/hrpd/UnitTest/RAW/hrp39182.raw",OutputWorkspace="sample",LoadLogFiles="0")
MaskBins(InputWorkspace="sample",OutputWorkspace="sample",XMin="19970",XMax="20140")
MaskBins(InputWorkspace="sample",OutputWorkspace="sample",XMin="39970",XMax="40140")
MaskBins(InputWorkspace="sample",OutputWorkspace="sample",XMin="59970",XMax="60140")
MaskBins(InputWorkspace="sample",OutputWorkspace="sample",XMin="79970",XMax="80140")
MaskBins(InputWorkspace="sample",OutputWorkspace="sample",XMin="99970",XMax="100140")
NormaliseByCurrent(InputWorkspace="sample",OutputWorkspace="sample")
AlignDetectors(InputWorkspace="sample",OutputWorkspace="sample",CalibrationFile="B:\MantidPowderFocus\scripts2/hrpd/UnitTest//GrpOff//hrpd_new_072_01_corr.cal")
Divide(LHSWorkspace="sample",RHSWorkspace="Corr",OutputWorkspace="sample")
CreateSingleValuedWorkspace(OutputWorkspace="scale",DataValue="1")
Multiply(LHSWorkspace="sample",RHSWorkspace="scale",OutputWorkspace="sample")
DiffractionFocussing(InputWorkspace="sample",OutputWorkspace="sample",GroupingFileName="B:\MantidPowderFocus\scripts2/hrpd/UnitTest/Cycle08_2/Si/hrpd_new_072_01_corr.cal")
CropWorkspace(InputWorkspace="sample",OutputWorkspace="sample-1",EndWorkspaceIndex="0")
Divide(LHSWorkspace="sample-1",RHSWorkspace="Vanadium-1",OutputWorkspace="ResultD-1")
Rebin(InputWorkspace="ResultD-1",OutputWorkspace="ResultD-1",Params="0.216746,-0.00010066,2.19305")
ConvertUnits(InputWorkspace="ResultD-1",OutputWorkspace="ResultTOF-1",Target="TOF")
ReplaceSpecialValues(InputWorkspace="ResultTOF-1",OutputWorkspace="ResultTOF-1",NaNValue="0",InfinityValue="0",BigNumberThreshold="99999999.999999985")
GroupWorkspaces(InputWorkspaces="ResultTOF-1,ResultTOF-2,ResultTOF-3",OutputWorkspace="ResultTOFgrp")
