# execfile('ganga_track_monitor_positionsByIOV.py')

import os, sys

import imp
setup = imp.load_source('setup', '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/Resolution/ganga/setup.py')

myPaths = setup.STMonPaths()

#common = imp.load_source('common', '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Scripts/tools/common.py')
#sys.path.append('/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Scripts/tools/')
#from common import IOVs2012


class IOVs2012():
    def __init__(self):
        self.intervals = {
             0 : {'start':'2012-04-01', 'end':'2012-04-17', 'firstrun':111183, 'lastrun':112916},
             1 : {'start':'2012-04-17', 'end':'2012-05-01', 'firstrun':113013, 'lastrun':113146},
             2 : {'start':'2012-05-01', 'end':'2012-05-12', 'firstrun':114205, 'lastrun':114287},
             3 : {'start':'2012-05-02', 'end':'2012-05-16', 'firstrun':114316, 'lastrun':115464},
             4 : {'start':'2012-05-16', 'end':'2012-05-31', 'firstrun':115518, 'lastrun':117103},
             5 : {'start':'2012-05-31', 'end':'2012-06-11', 'firstrun':117192, 'lastrun':118286},
             6 : {'start':'2012-06-11', 'end':'2012-07-02', 'firstrun':118326, 'lastrun':118880},
             7 : {'start':'2012-07-02', 'end':'2012-07-20', 'firstrun':119956, 'lastrun':122520},
             8 : {'start':'2012-07-20', 'end':'2012-07-25', 'firstrun':122540, 'lastrun':123803},
             9 : {'start':'2012-07-25', 'end':'2012-08-10', 'firstrun':123910, 'lastrun':125115},
            10 : {'start':'2012-08-10', 'end':'2012-08-28', 'firstrun':125566, 'lastrun':126680},
            11 : {'start':'2012-08-28', 'end':'2012-09-15', 'firstrun':126824, 'lastrun':128268},
            12 : {'start':'2012-09-15', 'end':'2012-10-12', 'firstrun':128411, 'lastrun':129978},
            13 : {'start':'2012-10-12', 'end':'2012-10-24', 'firstrun':130316, 'lastrun':130861},
            14 : {'start':'2012-10-24', 'end':'2012-11-08', 'firstrun':130911, 'lastrun':131940},
            15 : {'start':'2012-11-08', 'end':'2012-12-03', 'firstrun':131973, 'lastrun':133587},
            16 : {'start':'2012-12-03', 'end':'2012-12-31', 'firstrun':133624, 'lastrun':133785}
        }


iovs = IOVs2012()
firstruns = [iovs.intervals[iov]['firstrun'] for iov in iovs.intervals]
lastruns = [ run+100 for run in firstruns]
datasetString = '/Real Data/Reco14/Stripping20/90000000/DIMUON.DST'
datasets2 = []
for i in xrange(len(firstruns)):
    datasets2.append( '%s-%s'%(firstruns[i], lastruns[i]) + datasetString )
    print datasets2[i]

#datasets2 = [#'131973-133785/Real Data/Reco14/Stripping20/90000000/DIMUON.DST']#, # Last part of 2012 (Maurizio: good alignment)
#                '111183-131940/Real Data/Reco14/Stripping20/90000000/DIMUON.DST'] # First part of 2012 (Maurizio: bad alignment)

print
print datasets2

raw_input('')

optsPath = myPaths.optsPath
print optsPath

TrackTuplePath = "/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Options/"

#sys.exit(0)
gridProxy.renew()

for (i, ds) in enumerate([datasets2[0]]):
    bkq = BKQuery(path=str(ds),type="Run")
    j=Job(application='DaVinci')
    j.name = "Positions_IOV_%s_"%i
    j.name += ds.replace("/","_").replace(" ","")
    #j.application.version="v36r0"
    j.application.version="v36r2" #should work with root 6
    #j.application.optsfile=[ optsPath+"STTrackMonitor-JpsiDiMuon-HitsOnTracks.py", optsPath+"DV2012.py" ]
    j.application.optsfile=[ TrackTuplePath+"testTrackTuple-HitsOnTracks.py",
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
    print '(IOV %s)'%i
    jobtree.mkdir('STMonitoring/TrackTuple/2012Data/PositionsPerIOV')
    jobtree.add(j, 'STMonitoring/TrackTuple/2012Data/PositionsPerIOV')
    queues.add(j.submit)
    print 'fatto'
    #j.outputfiles=[ DiracFile('*.root') ]
