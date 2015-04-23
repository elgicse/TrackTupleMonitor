###############################################################################
# File for running alignment using the default reconstruction sequence.
###############################################################################
# Syntax is:
#   
#   gaudipariter.py -n 4 -p 8 -e 200000 /afs/cern.ch/user/g/gdujany/LHCb/Alignment/align2011/newAlignment/align2halves/align2halves.py | tee output.txt
#  
#   -n <number of iterations>
#   -p <number of processes>
#   -e <number of events>
#
# SetupProject Alignment 
###############################################################################
from Gaudi.Configuration import *
import GaudiKernel.SystemOfUnits as units
from TrackMonitors.BGIRecoConf import BGIRecoConf
from Configurables import CondDB, CondDBAccessSvc, RecSysConf

RecSysConf().RecoSequence = ["Decoding", "VELO", "Tr", "Vertex", "TT"]


# try:
#     import pickle
#     opts = pickle.load(open('../../options.pkl','rb'))   
# except IOError:
#     opts = {}
    
# dataset = opts.get('dataset','beamgas')
# runNum = opts.get('runNum',112867)

# isBeamGas = dataset != 'collisions'


# if isBeamGas:
#     BGIRecoConf().RecoVELOSeq = GaudiSequencer("RecoVELOSeq")
#     BGIRecoConf().RecoVertexSeq = GaudiSequencer("RecoVertexSeq")
#     BGIRecoConf().PV3DTuning = False
#     BGIRecoConf().PVAlgorithm = 'PatPV3D'
#     BGIRecoConf().PVSeedTool = 'PVSeed3DTool'
#     BGIRecoConf().PVFitterTool = 'LSAdaptPV3DFitter'
#     BGIRecoConf().PrimaryVertices = "Rec/Vertex/Primary"

from Configurables import Escher
theApp = Escher()
theApp.DataType   = "2012" # Check that this is true
from Configurables import CondDB
CondDB(LatestGlobalTagByDataType=theApp.DataType)
# theApp.CondDBtag = "sim-20130522-vc-md100"#'sim-20111111-vc-md100'
# theApp.DDDBtag = "dddb-20130929"#'MC11-20111102'
theApp.Simulation = False
#theApp.WithMC = True
theApp.InputType  = "DST" #"MDF"
theApp.PrintFreq = 5000
theApp.EvtMax = 3 #00 #2000#160000 #20000
#theApp.SkipEvents = 20 
theApp.DatasetName = 'Align'
#theApp.UseFileStager = True

# Refit Velo segment of long tracks to not be biased by Tracker

# from Configurables import GaudiSequencer
# trackRefitSeq = GaudiSequencer("TrackRefitSeq")

# # create a track list for tracks with velo hits
# from Configurables import TrackContainerCopy, TrackSelector
# velotrackselector = TrackContainerCopy("TracksWithVeloHits",
#                                        inputLocation = "Rec/Track/Best",
#                                        outputLocation = "Rec/Track/TracksWithVeloHits",
#                                        Selector = TrackSelector())
# velotrackselector.Selector.MinNVeloRHits =3
# velotrackselector.Selector.MinNVeloPhiHits =3

# # refit the tracks in that list
# from TrackFitter.ConfiguredFitters import *
# velotrackrefitter = ConfiguredEventFitter(Name = "TracksWithVeloHitsFitter",
#                                           TracksInContainer = "Rec/Track/TracksWithVeloHits",
#                                           FieldOff=True)
# velotrackrefitter.Fitter.MeasProvider.IgnoreIT = True
# velotrackrefitter.Fitter.MeasProvider.IgnoreOT = True
# velotrackrefitter.Fitter.MeasProvider.IgnoreTT = True
# velotrackrefitter.Fitter.MeasProvider.IgnoreMuon = True
# velotrackrefitter.Fitter.MakeNodes = True
# velotrackrefitter.Fitter.MakeMeasurements = True

# trackRefitSeq.Members += [velotrackselector, velotrackrefitter]

########################################

# Implement local alignment files
from Configurables import CondDBAccessSvc, CondDB, UpdateManagerSvc
localDb= CondDBAccessSvc("myCondLocal",
                         ConnectionString="sqlite_file:../../SilviaAlign.db/LHCBCOND"  # se usi gaudipariter 
                         #DefaultTAG = 'mis'+str(rndMisNum),
                         )
CondDB().addLayer( localDb )


### VERTEX SELECTION ##############
from TAlignment.VertexSelections import VertexSelection

def myConfiguredPVSelection():
    # we assume that the PV reconstruction has already been performed.
    # (can always add later)
    inputlocation = "Rec/Vertex/Primary"
    outputlocation = "Rec/Vertex/AlignPrimaryVertices"
    from Configurables import TrackPVRefitter,VertexListRefiner,GaudiSequencer
    pvrefitter = TrackPVRefitter("AlignPVRefitter",
                                 PVContainer =  "Rec/Vertex/Primary")
    pvselector = VertexListRefiner("AlignPVSelector",
                                   InputLocation = "Rec/Vertex/Primary",
                                   OutputLocation = "Rec/Vertex/AlignPrimaryVertices",
                                   MaxChi2PerDoF = 5,
                                   MinNumTracks = 8, # 10 org
                                   MinNumLongTracks = 0 ) # 2 org
    seq = GaudiSequencer("AlignPVSelSeq")
    seq.Members += [ pvrefitter, pvselector ]
    sel = VertexSelection(Name = "DefaultPVSelection",
                          Location = "Rec/Vertex/AlignPrimaryVertices",
                          Algorithm = seq)
    return sel

### TRACK SELECTION ##############
from TAlignment.TrackSelections import TrackRefiner

class myGoodLongVeloTracks( TrackRefiner ):
    def __init__( self, Name = "myGoodLongVeloTracks", InputLocation = "Rec/Track/TracksWithVeloHits", #"Rec/Track/Best",
                  Fitted = True ) :
        TrackRefiner.__init__(self, Name = Name, InputLocation = InputLocation, Fitted = Fitted)
    def configureSelector( self, a ):
        from Configurables import TrackSelector
        a.Selector = TrackSelector()
        a.Selector.MinPCut  =   5000
        a.Selector.MaxPCut  = 200000
        a.Selector.MinPtCut =    200
        a.Selector.TrackTypes = ["Long"]
        a.Selector.MinNVeloRHits = 5
        a.Selector.MinNVeloPhiHits = 5
        if self._fitted:
            a.Selector.MaxChi2Cut = 5
            a.Selector.MaxChi2PerDoFMatch = 5
            a.Selector.MaxChi2PerDoFVelo = 5
            a.Selector.MaxChi2PerDoFDownstream = 5

class myVeloBackwardCollTracks( TrackRefiner ):
    def __init__( self, Name = "myVeloBackwardCollTracks", InputLocation = "Rec/Track/TracksWithVeloHits", #"Rec/Track/Best",
                  Fitted = True ) :
        TrackRefiner.__init__(self, Name = Name, InputLocation = InputLocation, Fitted = Fitted)
    def configureSelector( self, a ):
        from Configurables import TrackSelector
        a.Selector = TrackSelector()
        a.Selector.TrackTypes = ["Backward", "Velo"]
        a.Selector.MinNVeloRHits = 5
        a.Selector.MinNVeloPhiHits = 5
        a.Selector.MaxNVeloHoles = 0
        if self._fitted:
            a.Selector.MaxChi2Cut = 5


### ALIGNABLES & CONSTRAINTS ##############
from TAlignment.Alignables import Alignables
from TAlignment.SurveyConstraints import *


def myconfigureVeloSensorAlignment():
    TAlignment().WriteCondSubDetList  += ['Velo']

    elements = Alignables()
    elements.Velo("None")
    #elements.VeloRight("Tx") # Se aggiungo o tolgo alignables cambiarlo anche ai constrains
    #elements.VeloLeft("Tx")  # Se aggiungo o tolgo alignables cambiarlo anche ai constrains
    elements.VeloRight("TxTyTzRxRyRz") # Se aggiungo o tolgo alignables cambiarlo anche ai constrains
    elements.VeloLeft("TxTyTzRxRyRz")  # Se aggiungo o tolgo alignables cambiarlo anche ai constrains
    # elements.VeloRight("None") # Se aggiungo o tolgo alignables cambiarlo anche ai constrains
    # elements.VeloLeft("None")  # Se aggiungo o tolgo alignables cambiarlo anche ai constrains
    #elements.VeloModules("TxRy")
    #elements.VeloModules("TxTyTzRxRyRz")#('None')#
    elements.VeloModules("TxTyRz")#('None')#
    elements.VeloPhiSensors('None')#("TxTy")
    elements.VeloRSensors("None")
    TAlignment().ElementsToAlign += list(elements)

    surveyconstraints = SurveyConstraints()

    surveyconstraints.All()

    # For MC I have to use different Constraints because Tz is different!
    # surveyconstraints.XmlFiles[:2] = ['../../Modules.xml', '../../Detectors.xml']
    
    print surveyconstraints
    constraints = []
    # surveyconstraints.XmlUncertainties += ["Velo/VeloLeft/Module10 : 0.000002 0.000002 0.000002 0.00000002 0.00000002 0.00000002"]
    # surveyconstraints.XmlUncertainties += ["Velo/VeloLeft/Module10/RPhiPair10/Detector-00 : 0.0000002 0.0000002 0.0000002 0.00000002 0.00000002 0.00000002"]
    # surveyconstraints.XmlUncertainties += ["Velo/VeloLeft/Module10/RPhiPair10/Detector-01 : 0.0000002 0.0000002 0.0000002 0.00000002 0.00000002 0.00000002"]

   
    # Global Constraints
    surveyconstraints.Constraints += [ "Velo      : 0 0 0 -0.0001 0 -0.0001 : 0.2 0.2 0.2 0.0001 0.0001 0.001",
                                       "Velo/Velo(Right|Left) : 0 0 0 0 0 0 : 10 1 0.4 0.01 0.01 0.001" ]
    
    # fix average mean and modules inside each half
    constraints.append( "VeloHalfAverage  : Velo/Velo(Left|Right) :  Tx Ty Tz Rx Ry Rz: total" )
   

    constraints.append("VeloAInternal : Velo/VeloRight/Module..: Tx Ty Rz Szx Szy")
    constraints.append("VeloCInternal : Velo/VeloLeft/Module..: Tx Ty Rz  Szx Szy")


    
    # constraints.append("VeloFixModule10 : Velo/VeloLeft/Module10: Tx Ty Tz Rx Ry Rz")
    # constraints.append("VeloFixModule11 : Velo/VeloRight/Module11: Tx Ty Tz Rx Ry Rz")
    # constraints.append("VeloFixModule32 : Velo/VeloLeft/Module32: Tx Ty Tz Rx Ry Rz")
    # constraints.append("VeloFixModule33 : Velo/VeloRight/Module33: Tx Ty Tz Rx Ry Rz")
    
    # constraints.append("VeloFixSensors10 : Velo/VeloLeft/Module10/RPhiPair10/.*: Tx Ty Tz Rx Ry Rz")
    # constraints.append("VeloFixSensors11 : Velo/VeloRight/Module11/RPhiPair11/.*: Tx Ty Tz Rx Ry Rz")
    # constraints.append("VeloFixSensors32 : Velo/VeloLeft/Module32/RPhiPair32/.*: Tx Ty Tz Rx Ry Rz")
    # constraints.append("VeloFixSensors33 : Velo/VeloRight/Module33/RPhiPair33/.*: Tx Ty Tz Rx Ry Rz")

    
    print TAlignment().Constraints
    TAlignment().Constraints      = constraints
    print TAlignment().Constraints
   

# specify the input to the alignment
from Configurables import TAlignment


TAlignment().TrackSelections = [ myGoodLongVeloTracks(),
                                 myVeloBackwardCollTracks() ]


TAlignment().PVSelection = myConfiguredPVSelection()

myconfigureVeloSensorAlignment()


#########################################

print 'ALIGNABLE:'
print TAlignment().ElementsToAlign
print 'TAlignment():'
print TAlignment().__slots__


# disable the HltErrorFilter
from Configurables import LoKi__HDRFilter as HDRFilter
hltErrorFilter = HDRFilter('HltErrorFilter').Enable = False

# Remove Outliers
from Configurables import TrackEventFitter
TrackEventFitter('FitVelo').Fitter.MaxNumberOutliers = 0
TrackEventFitter('TrackRefitter').Fitter.MaxNumberOutliers = 0

# for some reason, this crashed when running over many events:
from Configurables import GaudiSequencer
GaudiSequencer('MoniVELOSeq').Enable = False

# In digi MC do not have trigger infos so remove ...
GaudiSequencer('HltFilterSeq').Enable = False 

# Initialize initial time as in digi all events have initial time equal to zero
from Configurables import  AlignAlgorithm
AlignAlgorithm( "Alignment" ).ForcedInitialTime = 1


# add a filter to select only beam-gas events
def redefinefilters() :
    # disable the hltfilterseq for beamgas events
    from Configurables import LoKi__ODINFilter  as ODINFilter
    odinFiltNonBB  = ODINFilter ('ODINBXTypeFilterNonBB', Code = 'ODIN_BXTYP < 3') # mettere sia 1 che 2, 3 e` BB 1 o 2 sono solo beam 1 o 2
    odinFiltBB  = ODINFilter ('ODINBXTypeFilterNonBB', Code = 'ODIN_BXTYP == 3')
    if isBeamGas: GaudiSequencer("HltFilterSeq").Members.append( odinFiltNonBB ) 
    else: GaudiSequencer("HltFilterSeq").Members.append( odinFiltBB ) 
    GaudiSequencer("RecoTrSeq").Members += [ trackRefitSeq ]  # refit tracks with only velo information

appendPostConfigAction( redefinefilters )

# Change z-range in plots PV left-right deltax versus z
from TrackMonitors.TrackMonitorsConf import TrackVertexMonitor
TrackVertexMonitor().MinZPV = -1 * units.meter
TrackVertexMonitor().MaxZPV = 1 * units.meter
TrackVertexMonitor().NumProfileBins = 100

dataName = 'beamgas' if isBeamGas else 'D02KPi'
#ntupleDir='/tmp/gdujany'
#ntupleOutputFile = ntupleDir+'KalmanNtuple_'+dataName+'.root'
histoOutputFile = 'KalmanHisto_'+dataName+'.root'
HistogramPersistencySvc().OutputFile = histoOutputFile
#NTupleSvc().Output=["FILE1 DATAFILE='"+ntupleOutputFile+"' TYP='ROOT' OPT='NEW'"]


from GaudiConf import IOHelper

prodNumber = 15517 #c'e' prod number 13946 che e' uguale
fileList = ['/lhcb/MC/MC11a/ALLSTREAMS.DST/{0:0>8}/0000/{0:0>8}_{1:0>8}_1.allstreams.dst'.format(prodNumber, i) for i in range(1,190)]
IOHelper().inputFiles(['PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod'+file for file in fileList], clear=True)

# print  fileList


