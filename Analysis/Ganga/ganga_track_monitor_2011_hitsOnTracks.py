import os, sys

os.system("kinit -l 7d")
os.system(aklog)

import imp
setup = imp.load_source('setup', '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/Resolution/ganga/setup.py')

myPaths = setup.STMonPaths()

datasets2 = myPaths.selectData(['Collision11', '3500GeV'])

print datasets2

optsPath = myPaths.optsPath
print optsPath

TrackTuplePath = "/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Options/"

#sys.exit(0)
gridProxy.renew()

for ds in datasets2:
    bkq = BKQuery(path=str(ds),type="Run")
    j=Job(application='DaVinci')
    j.name = "TrackTuple_2011_hitsOnTrack"
    j.name += ds.replace("/","_").replace(" ","")
    #j.application.version="v36r0"
    j.application.version="v36r2" #should work with root 6
    #j.application.optsfile=[ optsPath+"STTrackMonitor-JpsiDiMuon-HitsOnTracks.py", optsPath+"DV2012.py" ]
    j.application.optsfile=[ TrackTuplePath+"testTrackTuple-HitsOnTracks.py",
                                optsPath+"DV2011.py" ]
    j.application.user_release_area=myPaths.userReleaseArea
    j.inputdata = bkq.getDataset()
    j.backend=Dirac()
    j.backend.settings['CPUTime']=5*172800
    j.backend.settings['BannedSites'] = ['LCG.GRIDKA.de', 'LCG.IN2P3.fr', 'LCG.PIC.es', 'LCG.NIKHEF.nl', 'LCG.SARA.nl']
    j.splitter = SplitByFiles(filesPerJob=10, ignoremissing=True)
    j.outputfiles=[ '*.root' ]
    j.do_auto_resubmit=True
    print 'sto per submittare per %s'%ds
    jobtree.mkdir('STMonitoring/TrackTuple/2011Data/HitsOnTrack')
    jobtree.add(j, 'STMonitoring/TrackTuple/2011Data/HitsOnTrack')
    queues.add(j.submit)
    print 'fatto'
    #j.outputfiles=[ DiracFile('*.root') ]
