#-- GAUDI jobOptions generated on Thu Feb 19 14:58:25 2015
#-- Contains event types : 
#--   90000000 - 1 files - 2050 events - 0.21 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-124248 

#--  StepId : 124248 
#--  StepName : Stripping20r1-Merging-DV-v32r2p3 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v32r2p3 
#--  OptionFiles : $APPCONFIGOPTS/Merging/DV-Stripping-Merging.py 
#--  DDDB : dddb-20130111 
#--  CONDDB : cond-20130114 
#--  ExtraPackages : AppConfig.v3r159 
#--  Visible : N 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/LHCb/Collision11/DIMUON.DST/00022761/0000/00022761_00000176_1.dimuon.dst'
], clear=True)
FileCatalog().Catalogs += [ 'xmlcatalog_file:testDiMuon2011.xml' ]
