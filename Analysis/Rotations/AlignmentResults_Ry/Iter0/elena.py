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

#RecSysConf().RecoSequence = ["Decoding", "VELO", "Tr", "Vertex", "TT"]

from Configurables import Escher
theApp = Escher()
theApp.DataType   = "2012" # Check that this is true
from Configurables import CondDB
CondDB(LatestGlobalTagByDataType=theApp.DataType)
# theApp.CondDBtag = "sim-20130522-vc-md100"#'sim-20111111-vc-md100'
# theApp.DDDBtag = "dddb-20130929"#'MC11-20111102'
theApp.Simulation = True
#theApp.WithMC = True
theApp.InputType  = "DST" #"MDF"
theApp.PrintFreq = 5000
theApp.EvtMax = 3 #00 #2000#160000 #20000
#theApp.SkipEvents = 20 
theApp.DatasetName = 'Align'
#theApp.UseFileStager = True

from Configurables import UpdateManagerSvc
UpdateManagerSvc().ConditionsOverride += [ "Conditions/Alignment/TT/TTaXLayerR1Module1T := double_v dPosXYZ = 0.0 0. 0.; double_v dRotXYZ = 0. 1. 0.;" ]


### VERTEX SELECTION ##############
from TAlignment.VertexSelections import configuredPVSelection

### TRACK SELECTION ##############
from TAlignment.TrackSelections import GoodLongTracks

### ALIGNABLES & CONSTRAINTS ##############
from TAlignment.Alignables import Alignables
from TAlignment.SurveyConstraints import *


def myconfigureTTAlignment():
    TAlignment().WriteCondSubDetList  += ['TT']

    elements = Alignables()
    elements.TT("None")
    elements.TTLayers("None")
    elements.TTHalfLayers("None")
    elements.TTSplitLayers("None")
    elements.TTBoxes("None")
    elements.TTHalfModules("None")
    elements.TTModules("None")
    TAlignment().ElementsToAlign += list(elements)

    surveyconstraints = SurveyConstraints()

    surveyconstraints.All()

    # For MC I have to use different Constraints because Tz is different!
    # surveyconstraints.XmlFiles[:2] = ['../../Modules.xml', '../../Detectors.xml']
    
    print surveyconstraints
   

# specify the input to the alignment
from Configurables import TAlignment


TAlignment().TrackSelections = [ GoodLongTracks() ]


TAlignment().PVSelection = configuredPVSelection()

myconfigureTTAlignment()


#########################################

print 'ALIGNABLE:'
print TAlignment().ElementsToAlign
print 'TAlignment():'
print TAlignment().__slots__


# disable the HltErrorFilter
from Configurables import LoKi__HDRFilter as HDRFilter
hltErrorFilter = HDRFilter('HltErrorFilter').Enable = False


# In digi MC do not have trigger infos so remove ...
GaudiSequencer('HltFilterSeq').Enable = False 


dataName = 'TestTT'
#ntupleDir='/tmp/gdujany'
#ntupleOutputFile = ntupleDir+'KalmanNtuple_'+dataName+'.root'
histoOutputFile = 'KalmanHisto_'+dataName+'.root'
HistogramPersistencySvc().OutputFile = histoOutputFile
#NTupleSvc().Output=["FILE1 DATAFILE='"+ntupleOutputFile+"' TYP='ROOT' OPT='NEW'"]

from GaudiConf import IOHelper

prodNumber = 15517 
fileList = ['/lhcb/MC/MC11a/ALLSTREAMS.DST/{0:0>8}/0000/{0:0>8}_{1:0>8}_1.allstreams.dst'.format(prodNumber, i) for i in range(1,190)]
IOHelper().inputFiles(['PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod'+file for file in fileList], clear=True)



