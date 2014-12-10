import os, sys

import imp
setup = imp.load_source('setup', '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/Resolution/ganga/setup.py')

myPaths = setup.STMonPaths()

datasets2 = ['131973-133785/Real Data/Reco14/Stripping20/90000000/DIMUON.DST']#, # Last part of 2012 (Maurizio: good alignment)
            #    '111183-131940/Real Data/Reco14/Stripping20/90000000/DIMUON.DST'] # First part of 2012 (Maurizio: bad alignment)

print datasets2

optsPath = myPaths.optsPath
print optsPath

TrackTuplePath = "/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Options/"

#sys.exit(0)
gridProxy.renew()

for ds in datasets2:
    bkq = BKQuery(path=str(ds),type="Run")
    j=Job(application='DaVinci')
    j.name = "TrackTuple_2012_everyHit"
    j.name += ds.replace("/","_").replace(" ","")
    #j.application.version="v36r0"
    j.application.version="v36r2" #should work with root 6
    #j.application.optsfile=[ optsPath+"STTrackMonitor-JpsiDiMuon-HitsOnTracks.py", optsPath+"DV2012.py" ]
    j.application.optsfile=[ TrackTuplePath+"testTrackTuple-EveryHit.py",
                                optsPath+"DV2012.py" ]
    j.application.user_release_area=myPaths.userReleaseArea
    j.inputdata = bkq.getDataset()
    j.backend=Dirac()
    j.backend.settings['CPUTime']=5*172800
    j.backend.settings['BannedSites'] = ['LCG.GRIDKA.de', 'LCG.IN2P3.fr', 'LCG.PIC.es', 'LCG.NIKHEF.nl', 'LCG.SARA.nl']
    j.splitter = SplitByFiles(filesPerJob=10, ignoremissing=True)
    j.outputfiles=[ '*.root' ]
    j.do_auto_resubmit=True
    print 'sto per submittare per %s'%ds
    jobtree.mkdir('STMonitoring/TrackTuple/2012Data/EveryHit')
    jobtree.add(j, 'STMonitoring/TrackTuple/2012Data/EveryHit')
    queues.add(j.submit)
    print 'fatto'
    #j.outputfiles=[ DiracFile('*.root') ]
