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

myInputParticlesList = []
myParticlesFilterList = []
myParticlesList = []
myParticlesSeqList = []
myParticlesLocationList = []

from Configurables import GaudiSequencer

filterSeq = GaudiSequencer( 'FilterSeq' )
filterSeq.ModeOR = True

mainSeq = GaudiSequencer( 'MainSeq' )
mainSeq.MeasureTime = True
mainSeq.IgnoreFilterPassed = False

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
cleanerGoodTracks = TrackContainerCleaner( 'GoodTracks' )
cleanerGoodTracks.inputLocation = "/Event/Rec/Track/MyBest"
cleanerGoodTracks.addTool( TrackSelector, name = 'Selector' )
cleanerGoodTracks.Selector.MinPCut    = 10000.
cleanerGoodTracks.Selector.MaxChi2Cut = 3.
cleanerGoodTracks.Selector.TrackTypes = [ "Long" ]

# Additional selection for hit efficiency:
# total track, T track, Velo segment and matching chi2 < 2
cleanerExcellentTracks = TrackContainerCleaner( 'ExcellentTracks' )
cleanerExcellentTracks.inputLocation = "/Event/Rec/Track/MyBest"
cleanerExcellentTracks.addTool( TrackSelector, name = 'Selector' )
cleanerExcellentTracks.Selector.MaxChi2Cut = 2.
cleanerExcellentTracks.Selector.MaxChi2PerDoFMatch = 2.
cleanerExcellentTracks.Selector.MaxChi2PerDoFDownstream = 2.
cleanerExcellentTracks.Selector.MaxChi2PerDoFVelo = 2.
cleanerExcellentTracks.Selector.TrackTypes = [ "Long" ]

########################################################################################
## Calculating hit efficiency                                                         ##
########################################################################################

# Search window (residual) for STEfficiency
itwindow = 2.#0.4
# Search window (residual) for STClusterCollector
itcollectorwindow = itwindow
# Tolerance for X and Y in the first estimate of the track crossing the silicon position
# and central position of the cluster
itxTol = 2.#1.
ityTol = 2.#0.

# Search window (residual) for STEfficiency
ttwindow = 2.#0.4
# Search window (residual) for STClusterCollector
ttcollectorwindow = ttwindow
# Tolerance for X and Y in the first estimate of the track crossing the silicon position
# and central position of the cluster
ttxTol = 2.#1.
ttyTol = 2.#0.

from Configurables import STClusterCollector, STSelectChannelIDByElement, TrackTuple

itEffTuple = TrackTuple( "ITHitEfficiencyTuple" )
itEffTuple.TracksInContainer  = "/Event/Rec/Track/MyBest"
itEffTuple.DetType            = "IT"
# Steps for hit efficiency measurements as a function of search window
itEffTuple.Cuts               = [ 2.e-3, 5.e-3, 1.e-2, 2.e-2, 3.e-2, 4.e-2, 6.e-2, 8.e-2, 1.e-1, 1.5e-1, 2.e-1, 3.e-1, 4.e-1 ]
# Search window (must be at least larger than the last value of Cuts property)
itEffTuple.XLayerCut          = itwindow
itEffTuple.StereoLayerCut     = itwindow
# Minimum number of expected sectors required
itEffTuple.MinExpectedSectors = 6
# Maximum number of found - expected hits
itEffTuple.MaxNbResSectors    = 10
# Minimum number of stations where hits are on the track
itEffTuple.MinStationPassed   = 3
# Edge size excluded of the computation
itEffTuple.MinDistToEdgeX     = 2.
itEffTuple.MinDistToEdgeY     = 2.
# Not dump the efficiency plot, because of the merging afterwards
itEffTuple.EfficiencyPlot     = False
# Dump all the biased residual histograms
itEffTuple.ResidualsPlot      = False#True
# Dump all the control histograms (for experts)
itEffTuple.FullDetail         = False#True
# No more than one found hit per sector
itEffTuple.SingleHitPerSector = True
# NTuple branching
itEffTuple.BranchBySector     = False
itEffTuple.BranchByTrack      = True
# Take hits found by STClusterCollector
itEffTuple.TakeEveryHit       = True
# Take hits on tracks
itEffTuple.HitsOnTrack        = False
# Skip or allow dead areas
itEffTuple.SkipEdges          = False#True
# Set output level
itEffTuple.OutputLevel        = 3
# Save sector positions in ntuple
itEffTuple.SaveSectorPositions= True

ttEffTuple = TrackTuple( "TTHitEfficiencyTuple" )
ttEffTuple.TracksInContainer  = "/Event/Rec/Track/MyBest"
ttEffTuple.DetType            = "TT"
ttEffTuple.Cuts               = [ 2.e-3, 5.e-3, 1.e-2, 2.e-2, 3.e-2, 4.e-2, 6.e-2, 8.e-2, 1.e-1, 1.5e-1, 2.e-1, 3.e-1, 4.e-1 ]
ttEffTuple.XLayerCut          = ttwindow
ttEffTuple.StereoLayerCut     = ttwindow
# Minimum number of expected sectors required
ttEffTuple.MinExpectedSectors = 2
# Maximum number of found - expected hits
ttEffTuple.MaxNbResSectors    = 10
# Minimum number of stations where hits are on the track
itEffTuple.MinStationPassed   = 1
# Edge size excluded of the computation
ttEffTuple.MinDistToEdgeX     = 2.
ttEffTuple.MinDistToEdgeY     = 2.
# Not dump the efficiency plot, because of the merging afterwards
ttEffTuple.EfficiencyPlot     = False
# Dump all the biased residual histograms
ttEffTuple.ResidualsPlot      = False#True
# Dump all the control histograms (for experts)
ttEffTuple.FullDetail         = False#True
# No more than one found hit per sector
ttEffTuple.SingleHitPerSector = True
# NTuple branching
ttEffTuple.BranchBySector     = False
ttEffTuple.BranchByTrack      = True
# Take hits found by STClusterCollector
ttEffTuple.TakeEveryHit       = True
# Take hits on tracks
ttEffTuple.HitsOnTrack        = False
# Skip or allow dead areas
ttEffTuple.SkipEdges          = False#True
# Set output level
ttEffTuple.OutputLevel        = 3
# Save sector positions in ntuple
ttEffTuple.SaveSectorPositions= True

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
## Other tools required + DaVinci settings                                            ##
########################################################################################

from Configurables import GaudiSequencer

mainSeq = GaudiSequencer( 'MainSeq' )
mainSeq.MeasureTime = True
mainSeq.IgnoreFilterPassed = False

from Configurables import DecodeVeloRawBuffer, RawBankToSTClusterAlg, UnpackTrack, STOfflinePosition

itClusterPosition = STOfflinePosition('ToolSvc.ITClusterPosition')
itClusterPosition.DetType  = 'IT'

ttClusterPosition = STOfflinePosition('ToolSvc.STOfflinePosition')

from Configurables import HltRoutingBitsFilter

physFilter = HltRoutingBitsFilter( "PhysFilter", RequireMask = [ 0x0, 0x4, 0x0 ] )

veloDecoder = DecodeVeloRawBuffer('VeloDecoder')
veloDecoder.DecodeToVeloLiteClusters = False
veloDecoder.DecodeToVeloClusters = True

itDecoder = RawBankToSTClusterAlg('ITDecoder') 
itDecoder.DetType = 'IT'

ttDecoder = RawBankToSTClusterAlg('TTDecoder')

mainSeq.Members += [ inputFilter, filterSeq,
                     UnpackTrack(), 
                     veloDecoder, ttDecoder, itDecoder,
                     tracks,
                     cleanerGoodTracks, 
                     itEffTuple, ttEffTuple ]

# Usual DaVinci stuff
from Configurables import DaVinci
DaVinci().EvtMax   = 1000#300
DaVinci().PrintFreq = 1000

filename = "STTrackTuple"
if ttEffTuple.BranchBySector and not ttEffTuple.BranchByTrack:
  filename += "-BranchBySector"
elif not ttEffTuple.BranchBySector and ttEffTuple.BranchByTrack:
  filename += "-BranchByTrack"
if ttEffTuple.BranchByTrack and ttEffTuple.TakeEveryHit:
  filename += "-EveryHit"
elif ttEffTuple.BranchByTrack and ttEffTuple.HitsOnTrack:
  filename += "-HitsOnTrack"
DaVinci().HistogramFile = filename+"-Hists.root"
DaVinci().UserAlgorithms = [ mainSeq ]

DaVinci().DataType = "2012"

from Configurables import CondDB, CondDBAccessSvc
CondDB().UseLatestTags = ["2012"]

from Configurables import NTupleSvc
itEffTuple.NTupleLUN = "TC"
ttEffTuple.NTupleLUN = "TC"
NTupleSvc().Output += ["TC DATAFILE='%s-NTuples.root' TYP='ROOT' OPT='NEW'"%filename]
