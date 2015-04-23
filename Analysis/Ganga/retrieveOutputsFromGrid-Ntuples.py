from __future__ import division
import sys, os
import ROOT as r

xmlOut = '/disk/data3/gangadir/egraveri/workspace/egraveri/LocalXML'
rootFile = [#'STTrackTuple-BranchByTrack-EveryHit-NTuples.root',
			 'STTrackTuple-BranchByTrack-HitsOnTrack-NTuples.root']

#myjobs = jobs.select(111, 112)
myjobs = [jobs(163)]

filesToHadd = ['']*len(myjobs)
completedSubjobs = 0
totalSubJobs = 0

notFoundLog = file(os.getcwd()+'/out/missedOutputLog.txt', 'w')

#analysisPath = '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/RootFiles/'
analysisPath = '/disk/data3/lhcb/elena/STAnalysis/RootFiles/'

#outFile = [os.getcwd()+'/out/%s.root'%j.name for j in myjobs]
copyToAnalysis = [  #   analysisPath+'EveryHit/runs131973-133785-end2012-muEstimate-Edges-closestState.root',
					analysisPath+'HitsOnTrack/runs131973-133785-end2012-muEstimate-Edges-closestState.root']

print 'Selected jobs ID and name:'
for j in myjobs:
	print j.id, j.name
print 'Target files:'
for p in copyToAnalysis:
	print p
ok = raw_input('Is it OK to continue?\n')
if ok == 'no' or ok == 'No':
	sys.exit(0)

os.system('. SetupProject.sh DaVinci v36r2')
#os.system('. SetupProject.sh ganga')
#os.system('. SetupProject.sh ROOT')
os.system('which root')

ok = raw_input('Is it OK to continue?\n')
if ok == 'no' or ok == 'No':
	sys.exit(0)

os.system('rm HaddLog.txt')
os.system('touch HaddLog.txt')
print 'Retrieving files to HADD...'

for (index, j) in enumerate(myjobs):
	slen = len(j.subjobs)
	for (subindex, sj) in enumerate(j.subjobs):
		#if subindex < slen/2.:
		totalSubJobs += 1
		if (sj.status=="completed" or sj.status=="completing"):
			outDir = '%s/%s/%s/output/'%(xmlOut, j.id, sj.id)
			if os.path.exists(outDir+rootFile[index]):
				f = r.TFile(outDir+rootFile[index], 'read')
				if f:
					if not f.IsZombie():
						#print 'Found output for job %s.%s'%(j.id, sj.id)
						filesToHadd[index] += (' '+outDir+rootFile[index])
						completedSubjobs += 1
					else:
						print >> notFoundLog, '%s.%s is zombie'%(j.id, sj.id)
						print '%s.%s is zombie'%(j.id, sj.id)
					f.Close()
					del f
				else:
					print >> notFoundLog, '%s.%s is corrupted'%(j.id, sj.id)
					print '%s.%s is corrupted'%(j.id, sj.id)
			else:
				print >> notFoundLog, '%s.%s not found'%(j.id, sj.id)
				print '%s.%s not found'%(j.id, sj.id)
				#continue

print filesToHadd
ok = raw_input("Ok?\n")
if ok == 'no' or ok == 'No':
	sys.exit(0)

print 'HADDing files...'
for j in xrange(len(myjobs)):
	#os.system('hadd -f %s %s'%(outFile[j], filesToHadd[j]))
	#os.system('cp %s %s'%(outFile[j], copyToAnalysis[j]))
	print 'Creating %s ...'%copyToAnalysis[j]
	if os.path.isfile(copyToAnalysis[j]):
		print "Removing old file..."
		os.system('rm %s'%copyToAnalysis[j])
	os.system('hadd -f %s %s >> HaddLog.txt'%(copyToAnalysis[j], filesToHadd[j]))

print '\n\nFound %s outputs in %s subjobs (%s jobs).'%(completedSubjobs, totalSubJobs, len(myjobs))
print '{:.1%} completed.'.format(completedSubjobs/totalSubJobs)
