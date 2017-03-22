#-- GAUDI jobOptions generated on Mon Jul  6 10:36:22 2015
#-- Contains event types : 
#--   90000000 - 31 files - 1185006 events - 101.78 GBytes


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
IOHelper('ROOT').inputFiles(['LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000356_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000384_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000403_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000411_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000418_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000437_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000445_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000454_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000456_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000460_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000471_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000489_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000506_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000508_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000520_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000531_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000545_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000576_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000589_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000592_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000618_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000634_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000645_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000659_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000679_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000687_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000695_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000698_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000713_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000732_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041834/0000/00041834_00000744_1.dimuon.dst'
], clear=True)
FileCatalog().Catalogs += [ 'xmlcatalog_file:diMuonCERN.xml' ]
