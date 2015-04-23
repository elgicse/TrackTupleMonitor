from __future__ import division
import sys, os
import ROOT as r

xmlOut = '/disk/data3/gangadir/egraveri/workspace/egraveri/LocalXML'
#rootFile = 'STTrackMonitors.root'
#rootFile = 'STTrackMonitor-HitEfficiency.root'
rootFile = 'STTrackTuple-BranchByTrack-HitsOnTrack-NTuples.root'


#ids = [131]
#ids.extend(range(121,130))
#ids.extend(range(132,142))
#myjobs = [jobs(i) for i in ids]#jobs.select(121,141)
myjobs = jobs.select(142,161)

filesToHadd = ['']*len(myjobs)
completedSubjobs = 0
totalSubJobs = 0

notFoundLog = file(os.getcwd()+'/out/missedOutputLog.txt', 'w')

#analysisPath = '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/Resolution/Analysis/RootFiles/Reco14/HitsOnTracks/'
#analysisPath = '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TTPerformance/RootFiles/HitsOnTracks/'
analysisPath = '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/RootFiles/'


#copyToAnalysis = [analysisPath+'/RootFiles/Reco14/HitsOnTracks/STTrackMonitor-2011-MagUp.root',
#				analysisPath+'/RootFiles/Reco14/HitsOnTracks/STTrackMonitor-2011-MagDown.root',
#				analysisPath+'/RootFiles/Reco14/HitsOnTracks/STTrackMonitor-2012-MagUp.root',
#				analysisPath+'/RootFiles/Reco14/HitsOnTracks/STTrackMonitor-2012-MagDown.root']
copyToAnalysis = []

oo = ""
i = 0
for j in myjobs:
	c = j.name.split("_")
	#d = c[3].split("-")
	d = c[5].split("-")
	print c, d
	#o = "_".join([c[2],d[2],d[-1]])
	o = "_".join([c[0],c[1],c[2],d[2],d[-1]])
	if oo == o : i+=1
	else : i=0
	#copyToAnalysis.append(analysisPath+ 'MC'+o + "_"+str(i)+'.root')
	copyToAnalysis.append((analysisPath+ 'MC'+c[4]+'_'+o + "_"+str(i)+'.root').replace("HitEfficiency_TrackMonitor_Overlaps","TrackTuple"))
	#oo = "_".join([c[2],d[2],d[-1]])
	oo = "_".join([c[0],c[1],c[2],d[2],d[-1]])

print 'Selected jobs ID and name:'
for j in myjobs:
	print j.id, j.name
print 'Target files:'
for p in copyToAnalysis:
	print p
ok = raw_input('Is it OK to continue?\n')
if ok == 'no' or ok == 'No':
	sys.exit(0)
	exit()

#os.system('. SetupProject.sh DaVinci v36r0')
os.system('. SetupProject.sh DaVinci v36r2')
os.system('which root')

ok = raw_input('Is it OK to continue?\n')
if ok == 'no' or ok == 'No':
	sys.exit(0)

os.system('rm HaddLog.txt')
os.system('touch HaddLog.txt')
print 'Retrieving files to HADD...'

for (index, j) in enumerate(myjobs):
	for sj in j.subjobs:
		totalSubJobs += 1
		if (sj.status=="completed" or sj.status=="completing"):
			outDir = '%s/%s/%s/output/'%(xmlOut, j.id, sj.id)
			if os.path.exists(outDir+rootFile):
				#print 'Found output for job %s.%s'%(j.id, sj.id)
				f = r.TFile(outDir+rootFile, 'read')
				if f:
					if not f.IsZombie():
						filesToHadd[index] += (' '+outDir+rootFile)
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

print 'HADDing files...'
for j in xrange(len(myjobs)):
	#os.system('hadd -f %s %s'%(outFile[j], filesToHadd[j]))
	#os.system('cp %s %s'%(outFile[j], copyToAnalysis[j]))
	print 'Creating %s ...'%copyToAnalysis[j]
	os.system('hadd -f %s %s >> HaddLog.txt'%(copyToAnalysis[j], filesToHadd[j]))

print '\n\nFound %s outputs in %s subjobs (%s jobs).'%(completedSubjobs, totalSubJobs, len(myjobs))
print '{:.1%} completed.'.format(completedSubjobs/totalSubJobs)
