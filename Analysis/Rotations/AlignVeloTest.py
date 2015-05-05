##############################################################################
# File for running Velo alignment on FEST data
#
# Syntax is:
#
# gaudirun.py $ESCHEROPTS/VeloMill2HalfAlign_Boff.py
# gaudirun.py $ESCHEROPTS/VeloMillepedeAlignModuleBoff.py $ESCHEROPTS/2009-TED.py 
#
# or
#
# $ESCHEROPTS/gaudiiter.py -n NUMITER -e NUMEVENTS $ESCHEROPTS/VeloMillepedeAlignModuleBoff.py $ESCHEROPTS/FEST-Data.py
#
##############################################################################
from Configurables import ( Escher, TrackSys, RecSysConf,RecMoniConf,VeloAlignment )
from Gaudi.Configuration import *
## from GaudiConf.Configuration import *
from GaudiKernel.ProcessJobOptions import importOptions
from Configurables import (ProcessPhase,AlignSensors,TrackStore,
                           VAlign,MagneticFieldSvc,
                           WriteAlignmentConditions,TrackVertexMonitor,
                           PatPVOffline)
from Configurables import (Velo__VeloClusterMonitor,
                           Velo__VeloExpertClusterMonitor,
                           Velo__VeloOccupancyMonitor,
                           Velo__VeloIPResolutionMonitor,PVOfflineTool,
                           Velo__VeloTrackMonitor,Velo__VeloTrackMonitorNT)
from Configurables import ( DecodeVeloRawBuffer,
                            Tf__PatVeloRTracking,
                            Tf__PatVeloSpaceTracking,
                            Tf__PatVeloGeneralTracking,Tf__PatVeloTrackTool,
                            Tf__PatVeloGeneric, 
                            DecodeVeloRawBuffer, PatPVOffline)
from Configurables import CondDBAccessSvc, UpdateManagerSvc
from Configurables import (TrackPrepareVelo,TrackContainerCopy)
from TrackFitter.ConfiguredFitters import *
from Configurables import ( TrackEventFitter, TrackMasterFitter, TrackKalmanFilter,
                            TrackProjectorSelector, TrackMasterExtrapolator,
                            TrackSimpleExtraSelector, TrackDistanceExtraSelector,
                            SimplifiedMaterialLocator, DetailedMaterialLocator,
                            MeasurementProvider, StateDetailedBetheBlochEnergyCorrectionTool)
from Configurables import PatPV3D, PVOfflineTool, LSAdaptPV3DFitter, PVSeed3DTool
from Configurables import PatPV3D, PVOfflineTool, LSAdaptPV3DFitter, PVSeed3DTool,PVSeedTool,LSAdaptPVFitter
from Configurables import PatPVOffline
from Configurables import PVOfflineTool, SimplePVSeedTool, SimplePVFitter

from GaudiKernel.SystemOfUnits import mm, m

Escher().DataType  = "2011"
## Escher().DDDBtag   = "MC11-20111102"
## Escher().CondDBtag = "sim-20111111-vc-md100"
from Configurables import UpdateManagerSvc, CondDB

#CondDB().LocalTags["SIMCOND"] = ["velo-20120515"]

Escher().DDDBtag   = "dddb-20130503"
Escher().CondDBtag   = "cond-20130710"
#Escher().CondDBtag   = "head-20110914"
#Escher().DDDBtag   = "head-20101206"
#Escher().CondDBtag   = "sim-20101210-vc-md100"
Escher().Simulation = False
## Escher().Detectors = ["VELO"]
Escher().InputType = "MDF" #"DST"
Escher().Kalman = True
Escher().Millepede = False
#Escher().TrackContainer = "Rec/Track/Velo" # Best, Velo, VeloR, Long, Upstream, Downstream, Ttrack, Muon or Calo
Escher().EvtMax = 1
Escher().Context = "Offline"

from Configurables import CondDB

#TrackSys().SpecialData = ['veloOpen']

RecSysConf().RecoSequence = ["VELO"]
#RecMoniConf().MoniSequence = ["VELO","Tr","Vertex"]
#RecMoniConf().ExpertHistos = True
#RecMoniConf().Context = "Offline"

TrackSys().TrackPatRecAlgorithms=["Velo"]


Escher().UseOracle= False
CondDB(UseOracle = False)
from Configurables import EventClockSvc
#EventClockSvc().InitialTime = 1270079584319872000 #1270079584012864000
    
def doMyAlignChanges():

    veloAlign=VAlign("VAlign")
    GaudiSequencer("AlignSequence").Members = [
        ]

    GaudiSequencer("MoniOTSeq").Members =[]
    GaudiSequencer("MoniSTSeq").Members =[]
    GaudiSequencer("InitCaloSeq").Members =[]
    
    GaudiSequencer("RecoVELOSeq").Members =[
        ]


appendPostConfigAction(doMyAlignChanges)

## dataName='collision_63949'
## EventSelector().Input = [
##     "DATA='castor:/castor/cern.ch/grid/lhcb/data/2009/RAW/FULL/LHCb/COLLISION09/63949/063949_0000000001.raw' SVC='LHCb::MDFSelector'"
##     ]

## velo_tag = "zs_1000um"
## localDb = CondDBAccessSvc("myCondLocal",
##                           ConnectionString ="sqlite_file:/afs/cern.ch/user/s/sogilvy/public/ForSilvia/mySIMCOND_veloweakmode.db/SIMCOND",
##                           DefaultTAG =  velo_tag)
## CondDB().addLayer( localDb )


## from Configurables import ( CondDB, CondDBAccessSvc )
## alignDBLayer = CondDBAccessSvc( 'AlignDBLayer' )
## alignDBLayer.ConnectionString ='sqlite_file:/afs/cern.ch/user/w/wouter/public/AlignDB/v3.0.db/LHCBCOND'
## CondDB().addLayer( alignDBLayer )

## velo_tag = "Metrology_newTz_newresocalib"
## localDb = CondDBAccessSvc("myCondLocal",
##                           ConnectionString ="sqlite_file:/afs/cern.ch/user/s/siborghi/public/VeloAlign2010.db/LHCBCOND",
##                           DefaultTAG =  velo_tag)
## CondDB().addLayer( localDb )

## velo_tag = "Velo2half_ModSensMetrology"
## velo_tag ="Metrology_correctTz_test3"
## localDb = CondDBAccessSvc("myCondLocal",
##                           ConnectionString ="sqlite_file:/afs/cern.ch/user/s/siborghi/public/VeloAlign2010.db/LHCBCOND",
##                           DefaultTAG =  velo_tag)
## CondDB().addLayer( localDb )
## velo_tag =  "Velo_testToFixTwist_kalm_47_it9"
## #velo_tag =  "Velo_testToFixTwist_kalm_30_it4"
## localDb = CondDBAccessSvc("myCondLocal",
##                           ConnectionString ="sqlite_file:/afs/cern.ch/user/s/siborghi/public/VeloAlign2010.db/LHCBCOND",
##                           DefaultTAG =  velo_tag)
## CondDB().addLayer( localDb )

## from Configurables import CondDBAccessSvc, CondDB, UpdateManagerSvc
## UpdateManagerSvc().ConditionsOverride += [
##     "Conditions/Alignment/Velo/VeloRight :=  double_v dPosXYZ = -0.15985 0.0436 0.05455; double_v dRotXYZ =-6.75e-05 0.7 0.0 ;",
##     "Conditions/Alignment/Velo/VeloLeft  :=  double_v dPosXYZ = 0.15985 -0.0436 -0.05455; double_v dRotXYZ = 9.75e-05 -4.50e-05 0.0;"
##     ]

## #by hand with overlap tracks
## from Configurables import CondDBAccessSvc, CondDB, UpdateManagerSvc
## UpdateManagerSvc().ConditionsOverride += [
##     "Conditions/Alignment/Velo/VeloRight :=  double_v dPosXYZ = -0.15985 0.0436 0.05455; double_v dRotXYZ =-6.75e-05 4.50e-05 0.0 ;",
##     "Conditions/Alignment/Velo/VeloLeft  :=  double_v dPosXYZ = 0.15985 -0.0336 -0.05455; double_v dRotXYZ = 7.95e-05 -5.00e-05 0.0;"
##     ]

## #CORRECTED
## from Configurables import CondDBAccessSvc, CondDB, UpdateManagerSvc
## UpdateManagerSvc().ConditionsOverride += [
##     "Conditions/Alignment/Velo/VeloRight :=  double_v dPosXYZ = -0.156906 0.033117 0.05455; double_v dRotXYZ =-8.75e-05 3.8e-05 0.0 ;",
##     "Conditions/Alignment/Velo/VeloLeft  :=  double_v dPosXYZ = 0.156906 -0.033117 -0.05455; double_v dRotXYZ = 8.75e-05 -3.8e-05 0.0;"
##     ]

## #CORRECTED2
## from Configurables import CondDBAccessSvc, CondDB, UpdateManagerSvc
## UpdateManagerSvc().ConditionsOverride += [
##     "Conditions/Alignment/Velo/VeloRight :=  double_v dPosXYZ = -0.156906 0.033117 0.05455; double_v dRotXYZ =-4.75e-05 3.8e-05 0.0 ;",
##     "Conditions/Alignment/Velo/VeloLeft  :=  double_v dPosXYZ = 0.156906 -0.033117 -0.05455; double_v dRotXYZ = 4.75e-05 -3.8e-05 0.0;"
##     ]

## #40it5
## from Configurables import CondDBAccessSvc, CondDB, UpdateManagerSvc
## UpdateManagerSvc().ConditionsOverride += [
##     "Conditions/Alignment/Velo/VeloRight :=  double_v dPosXYZ = -0.15985 0.0436 0.05455; double_v dRotXYZ =-6.75e-05 4.5e-05 0.0 ;",
##     "Conditions/Alignment/Velo/VeloLeft  :=  double_v dPosXYZ = 0.15985 -0.0436 -0.05455; double_v dRotXYZ = 6.75e-05 -4.5e-05 0.0;"
##     ]


## from Configurables import CondDBAccessSvc, CondDB, UpdateManagerSvc
## UpdateManagerSvc().ConditionsOverride += [
##     "Conditions/Alignment/Velo/VeloRight :=  double_v dPosXYZ = -0.15985 0.0436 0.05455; ",
##     "Conditions/Alignment/Velo/VeloLeft  :=  double_v dPosXYZ = 0.15985 -0.0436 -0.05455; "
##     ]
#40it5
from Configurables import CondDBAccessSvc, CondDB, UpdateManagerSvc
#UpdateManagerSvc().ConditionsOverride += [
#    "Conditions/Alignment/Velo/VeloRight :=  double_v dPosXYZ = -0.180 0.048 0.0; double_v dRotXYZ =-4.5e-05 4.1e-05 0.0 ;",
#    "Conditions/Alignment/Velo/VeloLeft  :=  double_v dPosXYZ = 0.144 -0.048 0.0; double_v dRotXYZ = 4.5e-05 -4.1e-05 0.0;",
#    "Conditions/Online/Velo/MotionSystem := double ResolPosRC =0 ; double ResolPosLA = 0 ; double ResolPosY = 0 ;"
#    ]

## from Configurables import CondDBAccessSvc, CondDB, UpdateManagerSvc
## UpdateManagerSvc().ConditionsOverride += [
## #    "Conditions/Alignment/Velo/Module02 :=  double_v dPosXYZ = -0.03901817086301505 -0.02716983182168431 0.006730523530251276; double_v dRotXYZ = 0.0101381012168183221 -0.000414339130890742 0.000164927576905833 ;",
## #    "Conditions/Alignment/Velo/Module03  :=  double_v dPosXYZ = -0.008371188855865574 0.007997850710948558 0.2000758155146514; double_v dRotXYZ = 0.01003886443224723057 -0.00162760478597386 -0.0005883210963775407;"

##     "Conditions/Alignment/Velo/Detector00-00 := double_v dPosXYZ = 0. 0. 0.; double_v dRotXYZ = 0. 0. 0.;",
##     "Conditions/Alignment/Velo/Detector00-01 := double_v dPosXYZ = 0. 0. 0.; double_v dRotXYZ = 0. 0. 0.;",
##     "Conditions/Alignment/Velo/Detector02-00 := double_v dPosXYZ = 0. 0. 0.; double_v dRotXYZ = 0. 0. 0.;",
##     "Conditions/Alignment/Velo/Detector02-01 := double_v dPosXYZ = 0. 0. 0.; double_v dRotXYZ = 0. 0. 0.;",
##     "Conditions/Alignment/Velo/Detector01-00 := double_v dPosXYZ = 0. 0. 0.; double_v dRotXYZ = 0. 0. 0.;",
##     "Conditions/Alignment/Velo/Detector01-01 := double_v dPosXYZ = 0. 0. 0.; double_v dRotXYZ = 0. 0. 0.;",
##     "Conditions/Alignment/Velo/Detector03-00 := double_v dPosXYZ = 0. 0. 0.; double_v dRotXYZ = 0. 0. 0.;",
##     "Conditions/Alignment/Velo/Detector03-01 := double_v dPosXYZ = 0. 0. 0.; double_v dRotXYZ = 0. 0. 0.;",
##     "Conditions/Alignment/Velo/VeloSystem  :=  double_v dPosXYZ = 0.144 -0.048 0.0; double_v dRotXYZ =0.00104 0 1.0e-01;"
##     ]

## from Configurables import CondDBAccessSvc, CondDB, UpdateManagerSvc
## UpdateManagerSvc().ConditionsOverride.append("Conditions/Alignment/Velo/VeloLeft := double_v XOffsetCoeffs =0 2.005")
## UpdateManagerSvc().ConditionsOverride.append("Conditions/Alignment/Velo/VeloRight := double_v XOffsetCoeffs =0 2.005")

## from Configurables import CondDBAccessSvc, CondDB, UpdateManagerSvc
## UpdateManagerSvc().ConditionsOverride += [
##     "Conditions/Alignment/Velo/VeloRight :=  double_v dPosXYZ = -0.075 0.0 0.0; double_v dRotXYZ = 0.0 0.0 0.0 ;",
##     "Conditions/Alignment/Velo/VeloLeft  :=  double_v dPosXYZ = 0.075 -0.0 0.0; double_v dRotXYZ = 0.0 0.0 0.0;",
##     "Conditions/Online/Velo/MotionSystem := double ResolPosRC =0 ; double ResolPosLA = 0 ; double ResolPosY = 0 ;",
##     ]

## from Configurables import ( CondDB, CondDBAccessSvc )
## localDb = CondDBAccessSvc("myCondLocal",
##                           ConnectionString ="sqlite_file:/afs/cern.ch/user/c/cbarsche/JaapReco/Alignmentv76-2520.db/LHCBCOND")
## CondDB().addLayer( localDb )


## localDb = CondDBAccessSvc("myCondLocal",
##                           ConnectionString ="sqlite_file:/afs/cern.ch/user/s/siborghi/cmtuser/Alignment_v9r2/Alignment/Escher/options/2010Align/As2012_only2half/AlignmentResults/Iter3/Alignment.db/LHCBCOND"
##                           )
## CondDB().addLayer( localDb )


## datasetName = "v76-2520"
datasetName = "std"
datasetName = "myv1"
ntupleDir=''
ntupleOutputFile = ntupleDir+'EscherNtuple'+datasetName+'.root'
histoOutputFile = ntupleDir+'EscherHisto'+datasetName+'.root' 
HistogramPersistencySvc().OutputFile = histoOutputFile
NTupleSvc().Output=["FILE1 DATAFILE='"+ntupleOutputFile+"' TYP='ROOT' OPT='NEW'"]


##############################################################################
# I/O datasets are defined in a separate file, see examples in 2008-TED_Data.py
##############################################################################



