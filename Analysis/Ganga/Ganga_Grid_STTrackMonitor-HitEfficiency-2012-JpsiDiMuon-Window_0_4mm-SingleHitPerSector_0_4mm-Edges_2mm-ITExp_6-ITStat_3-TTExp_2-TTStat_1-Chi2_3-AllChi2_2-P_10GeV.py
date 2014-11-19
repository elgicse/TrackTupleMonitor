#t = JobTemplate( application = DaVinci( version = "v32r2p12" ) )
t = JobTemplate( application = DaVinci( version = "v33r9" ) )
t.application.optsfile = [ File("/afs/cern.ch/user/i/ikomarov/Service_Task/STTrackMonitor-HitEfficiency/DaVinci/STTrackMonitor-HitEfficiency-2012-JpsiDiMuon-Window_0_4mm-SingleHitPerSector_0_4mm-Edges_2mm-ITExp_6-ITStat_3-TTExp_2-TTStat_1-Chi2_3-AllChi2_2-P_10GeV.py") ]
#t.application.platform = 'x86_64-slc5-gcc46-opt'

j = Job( t, backend = Dirac() )

#data_paths = [ '/LHCb/Collision12/Beam4000GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping20/90000000/DIMUON.DST'
#	       , '/LHCb/Collision12/Beam4000GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping20/90000000/DIMUON.DST' ]
#for data_path in data_paths:
#	if data_path == data_paths[0]:
#		lfns = BKQuery(path=str(data_path)).getDataset()
#	else:
#		lfns.files += BKQuery(path=str(data_path)).getDataset().files
#j.inputdata = lfns

j.inputdata = DaVinci().readInputData('Data_12_2.py')

#j.name = "STTrackMonitor-HitEfficiency-2012-JpsiDiMuon-Window_0_4mm-SingleHitPerSector_0_4mm-Edges_2mm-ITExp_6-ITStat_3-TTExp_2-TTStat_1-Chi2_3-AllChi2_2-P_10GeV"
j.name = "corr_STHE2"
j.splitter=SplitByFiles(filesPerJob=100)
j.splitter.bulksubmit = True
#j.outputfiles=[ DiracFile('*.root') ]
j.splitter.ignoremissing = True
j.outputfiles=[ MassStorageFile("*.root") ]
j.do_auto_resubmit = True
j.submit()
