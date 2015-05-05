from __future__ import division
import sys, os
import ROOT as r

xmlOut = '/disk/data3/gangadir/egraveri/workspace/egraveri/LocalXML'
rootFile = 'STTrackTuple-BranchByTrack-HitsOnTrack-NTuples.root'

myjobs = jobs.select(218, 236)

analysisPath = '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/'

#outFile = [os.getcwd()+'/out/%s.root'%j.name for j in myjobs]
copyToAnalysis = [ ]

print 'Selected jobs ID and name:'
for j in myjobs:
	copyToAnalysis.append( analysisPath + 'IOV_%s.root'%j.name.split('IOV_')[1].split('_')[0] )
	print j.id, j.name.split('IOV_')[1].split('_')[0]
print 'Target files:'
for p in copyToAnalysis:
	print p
ok = raw_input('Is it OK to continue?\n')
if ok == 'no' or ok == 'No':
	sys.exit(0)


for (index, j) in enumerate(myjobs):
	outDir = '%s/%s/%s/output/'%(xmlOut, j.id, j.subjobs[0].id)
	print 'cp %s %s'%(outDir+rootFile, copyToAnalysis[index])
	os.system('cp %s %s'%(outDir+rootFile, copyToAnalysis[index]))
