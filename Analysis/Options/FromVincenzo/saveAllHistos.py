import os,sys

from Gaudi.Configuration import *
from Gaudi.Configurables import *
from Configurables import GaudiSequencer

#Save all
minIThits = os.environ[ 'MINITHITS' ]
minTThits = os.environ[ 'MINTTHITS' ]
ApplicationMgr().ExtSvc += [ "NTupleSvc" ]
NTupleSvc().Output = ["FILE1 DATAFILE='/afs/cern.ch/user/v/vibattis/cmtuser/Urania_v3r0/ST/STSpilloverAnalysis/bash/RecoLoop_minIT%s_minTT%s.root' TYP='ROOT' OPT='NEW'" % (minIThits,minTThits) ]
