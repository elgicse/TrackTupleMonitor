#-- GAUDI jobOptions generated on Mon Jul  6 11:02:44 2015
#-- Contains event types : 
#--   90000000 - 23 files - 958121 events - 87.60 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-127012 

#--  StepId : 127012 
#--  StepName : Stripping21-Merging-DV-v36r1 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v36r1 
#--  OptionFiles : $APPCONFIGOPTS/Merging/DV-Stripping-Merging.py 
#--  DDDB : dddb-20130929-1 
#--  CONDDB : cond-20141107 
#--  ExtraPackages : AppConfig.v3r203;SQLDDDB.v7r10 
#--  Visible : N 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001462_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001502_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001510_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001528_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001542_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001549_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001616_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001632_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001673_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001681_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001695_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001700_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001726_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001730_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001758_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001797_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001828_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001859_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001869_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001903_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001928_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001957_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00001972_1.dimuon.dst'
], clear=True)
FileCatalog().Catalogs += [ 'xmlcatalog_file:dimuonMDPFN.xml' ]
