from Gaudi.Configuration import *
from Configurables import DetCondTest__TestConditionAlg as TestAlg
from Configurables import LoadDDDB, DDDBConf, CondDB

DDDBConf() # Configure the detector description
conddb = CondDB()
conddb.LatestGlobalTagByDataTypes = ['2012']

from Configurables import UpdateManagerSvc
UpdateManagerSvc().ConditionsOverride += [ "Conditions/Alignment/TT/TTaXLayerR1Module1T := double_v dPosXYZ = 0. 0. 0.; double_v dRotXYZ = 0. 0. 1.;" ]

testAlg = TestAlg("TestCond")
testAlg.Conditions = [ "Conditions/Alignment/TT/TTaXLayerR1Module1T" ]

app = ApplicationMgr()
app.TopAlg = [ TestAlg("TestCond") ]

app.EvtSel = "NONE"
app.EvtMax = 1
