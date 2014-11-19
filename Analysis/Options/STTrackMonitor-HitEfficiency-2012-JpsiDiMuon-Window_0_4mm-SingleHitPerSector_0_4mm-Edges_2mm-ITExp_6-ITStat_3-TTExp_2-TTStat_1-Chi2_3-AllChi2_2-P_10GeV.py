########################################################################################
## Code: ST hit efficiency, resolution and signal-to-noise ratio performances         ##
## Author: Frederic Dupertuis                                                         ##
########################################################################################

########################################################################################
## Taking the stripping candidates particles and dump its charged daughters tracks    ##
########################################################################################

# The list of stripping candidates and selection to apply
# Example of selection: (PT>1500.*MeV) & (INTREE( ('mu+'==ABSID) & (PT>800.*MeV)))
particlesAndCuts = { "/Event/Dimuon/Phys/FullDSTDiMuonJpsi2MuMuDetachedLine/Particles" : "ALL" }

from PhysSelPython.Wrappers import Selection, SelectionSequence, AutomaticData
from Configurables import FilterDesktop
from Gaudi.Configuration  import *


myInputParticlesList = []
myParticlesFilterList = []
myParticlesList = []
myParticlesSeqList = []
myParticlesLocationList = []

filterSeq = GaudiSequencer( 'FilterSeq' )
filterSeq.ModeOR = True

codeIN = ""

for particles, cuts in particlesAndCuts.iteritems():
    codeIN = codeIN.replace("||","|")
    codeIN += "(CONTAINS( '"+str(particles)+"' )>0) || "
    
    myParticlesName = particles.split("/")[-2]

    myInputParticlesList += [ AutomaticData( Location = particles ) ]
    
    myParticlesFilterList += [ FilterDesktop( myParticlesName+"Filter",
                                              Code = cuts ) ]
    myParticlesList += [ Selection( myParticlesName,
                                    Algorithm = myParticlesFilterList[-1],
                                    RequiredSelections = [ myInputParticlesList[-1] ] ) ]
    
    myParticlesSeqList += [ SelectionSequence( myParticlesName+"Seq",
                                               TopSelection = myParticlesList[-1] ) ]

    myParticlesLocationList += [ myParticlesList[-1].outputLocation() ]
    
    filterSeq.Members += [ myParticlesSeqList[-1].sequence() ]

codeIN = codeIN.replace(" || ","")

from Configurables import LoKi__VoidFilter as EventFilter

inputFilter = EventFilter( name = 'InputFilter',
                           Code = codeIN )

from Configurables import ChargedParticlesToTracks

tracks = ChargedParticlesToTracks("ChargedParticlesToTracks")
tracks.ParticlesLocations = myParticlesLocationList
tracks.TracksOutputLocation = "/Event/Rec/Track/MyBest"
# Refit of the tracks
tracks.RefitTracks = True
# Dump the mother particle invariant mass
tracks.FullDetail = True
# Mother particle invariant mass window cut
tracks.MassWindow = 40.
# Offset in the PDG mass of the mother particle
tracks.MassOffset = 3.

########################################################################################
## Apply tracks selection                                                             ##
########################################################################################

from Configurables import TrackContainerCleaner, TrackSelector

# Selection for hit resolution and signal-to-noise ratio:
# P>10 GeV/c and track chi2 < 3
cleaner = TrackContainerCleaner( 'GoodTracks' )
cleaner.inputLocation = "/Event/Rec/Track/MyBest"
cleaner.addTool( TrackSelector, name = 'Selector' )
cleaner.Selector.MinPCut    = 10000.
cleaner.Selector.MaxChi2Cut = 3.
cleaner.Selector.TrackTypes = [ "Long" ]

# Additional selection for hit efficiency:
# total track, T track, Velo segment and matching chi2 < 2
cleaner2 = TrackContainerCleaner( 'ExcellentTracks' )
cleaner2.inputLocation = "/Event/Rec/Track/MyBest"
cleaner2.addTool( TrackSelector, name = 'Selector' )
cleaner2.Selector.MaxChi2Cut = 2.
cleaner2.Selector.MaxChi2PerDoFMatch = 2.
cleaner2.Selector.MaxChi2PerDoFDownstream = 2.
cleaner2.Selector.MaxChi2PerDoFVelo = 2.
cleaner2.Selector.TrackTypes = [ "Long" ]

from Configurables import LoKi__ODINFilter as RunFilter
runf = RunFilter ( 'RunFilter' , Preambulo = [ "from LoKiCore.math import *" , "from LoKiNumbers.decorators import *" ] , Code = "ODIN_RUNNUMBER(0, 131973)", Location = "DAQ/ODIN")
#from Configurables import LoKi__VoidFilter as RunFilter
#runf = RunFilter ( 'RunFilter' , Preambulo = [ "from LoKiCore.math import *" , "from LoKiNumbers.decorators import *" ] , Code = "ODIN_RUNNUMBER(131973)")
########################################################################################
## Calculating hit efficiency                                                         ##
########################################################################################

# Search window (residual) for STEfficiency
itwindow = 0.4
# Search window (residual) for STClusterCollector
itcollectorwindow = itwindow
# Tolerance for X an Y in the first estimate of the track crossing the silicion position
# and central position of the cluster
itxTol = 1.
ityTol = 0.

# Search window (residual) for STEfficiency
ttwindow = 0.4
# Search window (residual) for STClusterCollector
ttcollectorwindow = ttwindow
# Tolerance for X an Y in the first estimate of the track crossing the silicion position
# and central position of the cluster
ttxTol = 1.
ttyTol = 0.

from Configurables import STEfficiency, STClusterCollector, STSelectChannelIDByElement, TrackTuple

itEff = TrackTuple( "ITHitEfficiency" )
itEff.TracksInContainer  = "/Event/Rec/Track/MyBest"
itEff.DetType            = "IT"
# Steps for hit efficiency measurements as a function of search window
itEff.Cuts               = [ 2.e-3, 5.e-3, 1.e-2, 2.e-2, 3.e-2, 4.e-2, 6.e-2, 8.e-2, 1.e-1, 1.5e-1, 2.e-1, 3.e-1, 4.e-1 ]
# Search window (must be at least larger than the last value of Cuts property)
itEff.XLayerCut          = itwindow
itEff.StereoLayerCut     = itwindow
# Minimum number of expected sectors required
itEff.MinExpectedSectors = 6
# Maximum number of found - expected hits
itEff.MaxNbResSectors    = 10
# Minimum number of stations where hits are on the track
itEff.MinStationPassed   = 3
# Edge size excluded of the computation
itEff.MinDistToEdgeX     = 2.
itEff.MinDistToEdgeY     = 2.
# Not dump the efficiency plot, because of the merging afterwards
itEff.EfficiencyPlot     = False
# Dump all the biased residual histograms
itEff.ResidualsPlot      = True
# Dump all the control histograms (for experts)
itEff.FullDetail         = True
# No more than one found hit per sector
itEff.SingleHitPerSector = True
# Take hits found by STClusterCollector
itEff.TakeEveryHit       = True
#itEff.TestProperty       = True
itEff.OutputLevel        = 3

ttEff = TrackTuple( "TTHitEfficiency" )
ttEff.TracksInContainer  = "/Event/Rec/Track/MyBest"
ttEff.DetType            = "TT"
ttEff.Cuts               = [ 2.e-3, 5.e-3, 1.e-2, 2.e-2, 3.e-2, 4.e-2, 6.e-2, 8.e-2, 1.e-1, 1.5e-1, 2.e-1, 3.e-1, 4.e-1 ]
ttEff.XLayerCut          = ttwindow
ttEff.StereoLayerCut     = ttwindow
# Minimum number of expected sectors required
ttEff.MinExpectedSectors = 2
# Maximum number of found - expected hits
ttEff.MaxNbResSectors    = 10
# Minimum number of stations where hits are on the track
itEff.MinStationPassed   = 1
# Edge size excluded of the computation
ttEff.MinDistToEdgeX     = 2.
ttEff.MinDistToEdgeY     = 2.
# Not dump the efficiency plot, because of the merging afterwards
ttEff.EfficiencyPlot     = False
# Dump all the biased residual histograms
ttEff.ResidualsPlot      = True
# Dump all the control histograms (for experts)
ttEff.FullDetail         = True
# Dump all the control histograms (for experts)
ttEff.SingleHitPerSector = True
# Take hits found by STClusterCollector
ttEff.TakeEveryHit       = True
ttEff.OutputLevel        = 3

# Collecting the ST clusters
itClusterCollector = STClusterCollector( "ToolSvc.ITClusterCollector" )
itClusterCollector.DetType           = "IT"
itClusterCollector.ignoreHitsOnTrack = False
itClusterCollector.xTol              = itxTol
itClusterCollector.yTol              = ityTol
itClusterCollector.window            = itcollectorwindow
itClusterCollector.MagFieldOn        = True
itClusterCollector.dataLocation      = "/Event/Raw/IT/Clusters"

ttClusterCollector = STClusterCollector( "ToolSvc.TTClusterCollector" )
ttClusterCollector.DetType           = "TT"
ttClusterCollector.ignoreHitsOnTrack = False
ttClusterCollector.xTol              = ttxTol
ttClusterCollector.yTol              = ttyTol
ttClusterCollector.window            = ttcollectorwindow
ttClusterCollector.MagFieldOn        = True
ttClusterCollector.dataLocation      = "/Event/Raw/TT/Clusters"

########################################################################################
## Calculating hit resolution and signal-to-noise ratio                               ##
########################################################################################

from Configurables import ITTrackMonitor, TTTrackMonitor, TrackMonitor

trackMon = TrackMonitor('TrackMonitor')
trackMon.TracksInContainer = "/Event/Rec/Track/MyBest"

itMon = ITTrackMonitor('ITTrackMonitor')
itMon.TracksInContainer = "/Event/Rec/Track/MyBest"
# Dump all the plots
itMon.FullDetail = True
# Dump all the plots per layers
itMon.plotsByLayer = True
# Minimum number of found hits on track
itMon.minNumITHits = 6

ttMon = TTTrackMonitor('TTTrackMonitor')
ttMon.TracksInContainer = "/Event/Rec/Track/MyBest"
# Dump all the plots
ttMon.FullDetail = True
# Minimum number of found hits on track
ttMon.minNumTTHits = 2

########################################################################################
## Other tools required + DaVinci settings                                            ##
########################################################################################

from Configurables import GaudiSequencer

mainSeq = GaudiSequencer( 'MainSeq' )
mainSeq.MeasureTime = True
mainSeq.IgnoreFilterPassed = False

from Configurables import DecodeVeloRawBuffer, RawBankToSTClusterAlg, UnpackTrack, STOfflinePosition

itClusterPosition = STOfflinePosition('ToolSvc.ITClusterPosition')
itClusterPosition.DetType  = 'IT'
#itClusterPosition.ErrorVec = [ 0.28, 0.2, 0.3, 0.32 ]
#itClusterPosition.APE      = 0.05

ttClusterPosition = STOfflinePosition('ToolSvc.STOfflinePosition')
#ttClusterPosition.ErrorVec = [ 0.29, 0.34, 0.32, 0.46 ]
#ttClusterPosition.APE      = 0.197

from Configurables import HltRoutingBitsFilter

physFilter = HltRoutingBitsFilter( "PhysFilter", RequireMask = [ 0x0, 0x4, 0x0 ] )

veloDecoder = DecodeVeloRawBuffer('VeloDecoder')
veloDecoder.DecodeToVeloLiteClusters = False
veloDecoder.DecodeToVeloClusters = True

itDecoder = RawBankToSTClusterAlg('ITDecoder') 
itDecoder.DetType = 'IT'

ttDecoder = RawBankToSTClusterAlg('TTDecoder')

from Configurables import CondDB, CondDBAccessSvc
# Adding an extra slice of the database (example: alignment constants)
#mycalib = CondDBAccessSvc( 'myCalib' )
#mycalib.ConnectionString = 'sqlite_file:/afs/cern.ch/user/m/mamartin/public/AlignDB/v6.2series.db/LHCBCOND'
#CondDB().addLayer( mycalib )

# Using latest databases tags
CondDB().UseLatestTags = ["2012"]

mainSeq.Members += [ inputFilter, filterSeq, 
                     #runf,
                     UnpackTrack(), 
                     veloDecoder, ttDecoder, itDecoder,
                     tracks,
                     #addhits,
                     #eventfitter, eventfitter2,
                     cleaner, itEff, ttEff,
                     #trackMon, itMon, ttMon, 
                     cleaner2
                     #,itEff
                     #,ttEff
                      ]

# Usual DaVinci stuff
from Configurables import DaVinci
DaVinci().EvtMax   = -1
#DaVinci().SkipEvents = 10000
DaVinci().PrintFreq = 10000 
DaVinci().DataType = "2012"

#DaVinci().DDDBtag = "head-20111102"
#DaVinci().CondDBtag = "head-20111111"
#DaVinci().HistogramFile = "STTrackMonitor-HitEfficiency.root"
DaVinci().HistogramFile = "DVnTuples.root"
DaVinci().TupleFile = "DVnTuples.root"
DaVinci().UserAlgorithms = [ mainSeq ]
#DaVinci().Input = ["/afs/cern.ch/user/i/ikomarov/Service_Task/STTrackMonitor-HitEfficiency/DaVinci/00020198_00000007_1.dimuon.dst","/afs/cern.ch/user/i/ikomarov/Service_Task/STTrackMonitor-HitEfficiency/DaVinci/00020241_00000007_1.dimuon.dst"]
