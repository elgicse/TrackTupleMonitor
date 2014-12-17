######################################################
# Setup paths for ST monitoring
#
# Author: Elena Graverini (elena.graverini@cern.ch)
# Last modified: 24/09/2014
######################################################

class STMonPaths:
    """ Modify these paths according to your system """
    def __init__(self):
        self.optsPath = '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/Resolution/options/'
        self.userReleaseArea = '/afs/cern.ch/user/e/egraveri/cmtuser'
        self.datasets = {
            'trackMonitor2012' :
            ['/LHCb/Collision12/Beam4000GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping20/90000000/DIMUON.DST',
             '/LHCb/Collision12/Beam4000GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping20/90000000/DIMUON.DST'],
            
            'trackMonitor2011' :
            ['/LHCb/Collision11/Beam3500GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping20r1/90000000/DIMUON.DST',
             '/LHCb/Collision11/Beam3500GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping20r1/90000000/DIMUON.DST'],
            
            'mc2011-Pythia6' :
            ['/MC/2011/Beam3500GeV-2011-MagDown-Nu2-Pythia6/Sim08a/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/13144001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagDown-Nu2-Pythia6/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/12442001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagDown-Nu2-Pythia6/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/11442001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagDown-Nu2-Pythia6/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/13442001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagDown-Nu2-Pythia6/Sim08a/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/24142001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagUp-Nu2-Pythia6/Sim08a/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/13144001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagUp-Nu2-Pythia6/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/12442001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagUp-Nu2-Pythia6/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/11442001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagUp-Nu2-Pythia6/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/13442001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagUp-Nu2-Pythia6/Sim08a/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/24142001/ALLSTREAMS.DST'],
            
            'mc2011-Pythia8' :
            ['/MC/2011/Beam3500GeV-2011-MagDown-Nu2-Pythia8/Sim08a/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/13144001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagDown-Nu2-Pythia8/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/12442001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagDown-Nu2-Pythia8/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/11442001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagDown-Nu2-Pythia8/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/13442001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagUp-Nu2-Pythia8/Sim08a/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/13144001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagUp-Nu2-Pythia8/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/12442001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagUp-Nu2-Pythia8/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/11442001/ALLSTREAMS.DST',
             '/MC/2011/Beam3500GeV-2011-MagUp-Nu2-Pythia8/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/13442001/ALLSTREAMS.DST'],

            'mc2012-Pythia6' :
            ['/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13144001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/11442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/24142001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13144001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/11442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/24142001/ALLSTREAMS.DST'],

            'mc2012-Pythia8' :
            ['/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13144001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/11442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia8/Sim08b/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/24142001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13144001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/11442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13442001/ALLSTREAMS.DST',
             '/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia8/Sim08b/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/24142001/ALLSTREAMS.DST']
            }
        self.allDatasets = []
        for key in self.datasets:
            self.allDatasets.extend(self.datasets[key])

    def selectData(self, options, warnings=False):
    	""" Given a list of options (as strings), return the corrisponding dataset(s) """
        # utilizza cio' che e' scritto nei nomi dei dataset per suddividerli in 'cartelle'
        if type(options) == str: # if only 1 option is provided, we don't want to split the string in letters
        	options = [options]
    	if warnings:
    		for opt in options:
    			if opt not in ['MagUp', 'MagDown', 'MC', 'Collision11', 'Collision12', '2011', '2012', '3500GeV', '4000GeV', 'Pythia8', 'Pythia6', 'Nu2-', 'Nu2.5']:
    				print 'selectData WARNING: option %s unknown'%opt
    	selected = []
    	for dataset in self.allDatasets:
    		flag = True
    		for opt in options:
    			if not dataset.__contains__(opt):
    				flag = False
    		if flag:
    			selected.append(dataset)
    	return list(set(selected)) # there might be repetitions

        
