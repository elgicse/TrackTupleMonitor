# Import classes
from Configurables import GaudiSequencer
from GaudiKernel.Configurable import appendPostConfigAction

# Include TrackTuple algorithm
from Configurables import TrackTuple

itTrTuple = TrackTuple('ITTrackTuple')
itTrTuple.DetType = "IT"
itTrTuple.SaveSectorPositions = False
itTrTuple.HitsOnTrack = True
itTrTuple.TakeEveryHit = False
itTrTuple.BranchBySector = False
itTrTuple.BranchByTrack = True
itTrTuple.MinDistToEdgeX = 0.0
itTrTuple.MinDistToEdgeY = 0.0

ttTrTuple = TrackTuple('TTTrackTuple')
ttTrTuple.DetType = "TT"
ttTrTuple.SaveSectorPositions = False
ttTrTuple.HitsOnTrack = True
ttTrTuple.TakeEveryHit = False
ttTrTuple.BranchBySector = False
ttTrTuple.BranchByTrack = True
ttTrTuple.MinDistToEdgeX = 0.0
ttTrTuple.MinDistToEdgeY = 0.0

# Include Spillover Tool
from Configurables import STSpilloverTool
itTrTuple.addTool(STSpilloverTool, name='ITSpilloverTool')
ttTrTuple.addTool(STSpilloverTool, name='TTSpilloverTool')

def PostConfigurationActions():
    GaudiSequencer('MoniTrSeq').Members += [ itTrTuple ]
    GaudiSequencer('MoniTrSeq').Members += [ ttTrTuple ]

from GaudiKernel.Configurable import appendPostConfigAction
appendPostConfigAction(PostConfigurationActions)

# Save Tuple
ApplicationMgr().ExtSvc += [ "NTupleSvc" ]
NTupleSvc().Output = ["FILE1 DATAFILE='MonTuple.root' TYP='ROOT' OPT='NEW'"]
