#-- GAUDI jobOptions generated on Thu Nov 13 15:36:53 2014
#-- Contains event types : 
#--   90000000 - 1 files - 102 events - 0.01 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-54132 

#--  StepId : 54132 
#--  StepName : Stripping20-Merging-DV-v32r2p1 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v32r2p1 
#--  OptionFiles : $APPCONFIGOPTS/Merging/DV-Stripping-Merging.py 
#--  DDDB : dddb-20120831 
#--  CONDDB : cond-20120831 
#--  ExtraPackages : AppConfig.v3r150 
#--  Visible : N 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00020198/0000/00020198_00000033_1.dimuon.dst'
], clear=True)
FileCatalog().Catalogs += [ 'xmlcatalog_file:testDiMuon.xml' ]
