import GaudiPython
OPTIONS = 'AlignVeloTest.py'
appMgr = GaudiPython.AppMgr( outputlevel = 3, joboptions = OPTIONS )
det = appMgr.detSvc()
first_R = '/dd/Structure/LHCb/BeforeMagnetRegion/TT'
r_sensor = det[ first_R ]
r_sensor.name()
children = r_sensor.childIDetectorElements()
for c in children:
    print c.name()
ttax = '/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer'
ttax_de = det[ ttax ]

children = ttax_de.childIDetectorElements()
for c in children:
    print c.name()
"""
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module1T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module1B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module2T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module2B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module3T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module3B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module4T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module4B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module5T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module5B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module6T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module6B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R2Module1T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R2Module1B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R2Module2T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R2Module2B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R2Module3T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R2Module3B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module1T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module1B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module2T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module2B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module3T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module3B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module4T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module4B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module5T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module5B
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module6T
/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R3Module6B
"""
hmt = '/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module1T'
hm_top = det[hmt]
hmb = '/dd/Structure/LHCb/BeforeMagnetRegion/TT/TTa/TTaXLayer/R1Module1B'
hm_bot = det[hmb]
from GaudiPython import gbl
point = GaudiPython.gbl.ROOT.Math.XYZPoint()
point.SetXYZ( 1, 0, 0)
hm_top.geometry().toGlobal( point )
hm_top.geometry().toGlobal( point ).X()
# -644.0323047983479
hm_bot.geometry().toGlobal( point ).X()
# -642.0457192606865
hm_bot.geometry().toLocal( point ).X()
# 644.0389797178177
hm_top.geometry().toLocal( point ).X()
# -644.0389797178292


"""
Half moduli top e bottom hanno la X invertita nei SDR locali!!!
"""
