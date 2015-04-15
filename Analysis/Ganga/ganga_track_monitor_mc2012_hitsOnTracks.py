import os, sys

import imp
setup = imp.load_source('setup', '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/Resolution/ganga/setup.py')
#from setup import *

myPaths = setup.STMonPaths()

MD8 = myPaths.selectData(['MC', '2012', 'Pythia8', 'MagDown'])
MU8 = myPaths.selectData(['MC', '2012', 'Pythia8', 'MagUp'])
MD6 = myPaths.selectData(['MC', '2012', 'Pythia6', 'MagDown'])
MU6 = myPaths.selectData(['MC', '2012', 'Pythia6', 'MagUp'])
optsPath = myPaths.optsPath

gridProxy.renew()

#diMuonOptFile = "HitEfficiency-Resolution-DiMuon-MC.py"
TrackTuplePath = "/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Options/"

hitsOnTrack = TrackTuplePath+"testTrackTuple-HitsOnTracks-MC.py"


print 'Submitting 2012 MC Pythia8 MagDown...'
for ds in MD8:
    print ds
    bkq = BKQuery(path=str(ds))
    j=Job(application='DaVinci')
    j.name = "HitEfficiency_TrackMonitor_Overlaps"
    j.name+=ds.replace("/","_").replace(" ","")
    #j.application.version="v35r0"
    j.application.version="v36r2" #should work with root 6
    #j.application.optsfile=[ optsPath+"STTrackMonitor-JpsiDiMuon-HitsOnTracks-MC.py", optsPath+"MC2012-MagDown.py" ]
    j.application.optsfile=[ hitsOnTrack, optsPath+"MC2012-MagDown.py" ]
    j.application.user_release_area=myPaths.userReleaseArea
    j.inputdata = bkq.getDataset()
    j.backend=Dirac()
    j.backend.settings['CPUTime']=5*172800
    j.backend.settings['BannedSites'] = ['LCG.GRIDKA.de', 'LCG.IN2P3.fr', 'LCG.PIC.es', 'LCG.NIKHEF.nl', 'LCG.SARA.nl']
    j.splitter = SplitByFiles(filesPerJob=5, ignoremissing=True)
    j.outputfiles=[ '*.root' ]
    j.do_auto_resubmit=True
    print 'sto per submittare per %s'%ds
    jobtree.mkdir('STMonitoring/TrackTuple/2012MC/Pythia8/MagDown')
    jobtree.add(j, 'STMonitoring/TrackTuple/2012MC/Pythia8/MagDown')
    queues.add(j.submit)
    print 'fatto'

print 'Submitting 2012 MC Pythia8 MagUp...'
for ds in MU8:
    print ds
    bkq = BKQuery(path=str(ds))
    j=Job(application='DaVinci')
    j.name = "HitEfficiency_TrackMonitor_Overlaps"
    j.name+=ds.replace("/","_").replace(" ","")
    #j.application.version="v35r0"
    j.application.version="v36r2" #should work with root 6
    j.application.optsfile=[ hitsOnTrack, optsPath+"MC2012-MagUp.py" ]
    j.application.user_release_area=myPaths.userReleaseArea
    j.inputdata = bkq.getDataset()
    j.backend=Dirac()
    j.backend.settings['CPUTime']=5*172800
    j.backend.settings['BannedSites'] = ['LCG.GRIDKA.de', 'LCG.IN2P3.fr', 'LCG.PIC.es', 'LCG.NIKHEF.nl', 'LCG.SARA.nl']
    j.splitter = SplitByFiles(filesPerJob=5, ignoremissing=True)
    j.outputfiles=[ '*.root' ]
    j.do_auto_resubmit=True
    print 'sto per submittare per %s'%ds
    jobtree.mkdir('STMonitoring/TrackTuple/2012MC/Pythia8/MagUp')
    jobtree.add(j, 'STMonitoring/TrackTuple/2012MC/Pythia8/MagUp')
    queues.add(j.submit)
    print 'fatto'


print 'Submitting 2012 MC Pythia6 MagDown...'
for ds in MD6:
    print ds
    bkq = BKQuery(path=str(ds))
    j=Job(application='DaVinci')
    j.name = "HitEfficiency_TrackMonitor_Overlaps"
    j.name+=ds.replace("/","_").replace(" ","")
    #j.application.version="v35r0"
    j.application.version="v36r2" #should work with root 6
    j.application.optsfile=[ hitsOnTrack, optsPath+"MC2012-MagDown.py" ]
    j.application.user_release_area=myPaths.userReleaseArea
    j.inputdata = bkq.getDataset()
    j.backend=Dirac()
    j.backend.settings['CPUTime']=5*172800
    j.backend.settings['BannedSites'] = ['LCG.GRIDKA.de', 'LCG.IN2P3.fr', 'LCG.PIC.es', 'LCG.NIKHEF.nl', 'LCG.SARA.nl']
    j.splitter = SplitByFiles(filesPerJob=5, ignoremissing=True)
    j.outputfiles=[ '*.root' ]
    j.do_auto_resubmit=True
    print 'sto per submittare per %s'%ds
    jobtree.mkdir('STMonitoring/TrackTuple/2012MC/Pythia6/MagDown')
    jobtree.add(j, 'STMonitoring/TrackTuple/2012MC/Pythia6/MagDown')
    queues.add(j.submit)
    print 'fatto'

print 'Submitting 2012 MC Pythia6 MagUp...'
for ds in MU6:
    print ds
    bkq = BKQuery(path=str(ds))
    j=Job(application='DaVinci')
    j.name = "HitEfficiency_TrackMonitor_Overlaps"
    j.name+=ds.replace("/","_").replace(" ","")
    #j.application.version="v35r0"
    j.application.version="v36r2" #should work with root 6
    j.application.optsfile=[ hitsOnTrack, optsPath+"MC2012-MagUp.py" ]
    j.application.user_release_area=myPaths.userReleaseArea
    j.inputdata = bkq.getDataset()
    j.backend=Dirac()
    j.backend.settings['CPUTime']=5*172800
    j.backend.settings['BannedSites'] = ['LCG.GRIDKA.de', 'LCG.IN2P3.fr', 'LCG.PIC.es', 'LCG.NIKHEF.nl', 'LCG.SARA.nl']
    j.splitter = SplitByFiles(filesPerJob=5, ignoremissing=True)
    j.outputfiles=[ '*.root' ]
    j.do_auto_resubmit=True
    print 'sto per submittare per %s'%ds
    jobtree.mkdir('STMonitoring/TrackTuple/2012MC/Pythia6/MagUp')
    jobtree.add(j, 'STMonitoring/TrackTuple/2012MC/Pythia6/MagUp')
    queues.add(j.submit)
    print 'fatto'