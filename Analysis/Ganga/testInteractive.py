from Configurables import DaVinci
print "default"
print DaVinci()
DaVinci().EvtMax = 15
print "before"
print DaVinci()
from Configurables import DaVinci
DaVinci().Simulation = True
print "after"
print DaVinci()



#j=Job(application='DaVinci')
#j.name = "test"
#