import argparse, importlib
from IPython import embed
from tools.common import *

# Parse commandline inputs
ap = argparse.ArgumentParser(
    description='ST track analysis script')
ap.add_argument('-st', '--studies', help='List of sstudies to execute.\nDefault is the full list:\n IOV, PositionsSectors, PositionsHalfModules,\nOutliers, FullLayers, ClusterSize,\nOverlaps, OverlapsHalfModules, MagField\n',
                nargs='+', default='CLZvsTY IOV PositionsSectors PositionsHalfModules Outliers FullLayers ClusterSize Overlaps OverlapsHalfModules MagField'.split())
ap.add_argument('-t', '--tracker', help='Tracking detector: IT or TT', default='TT', type=str)
ap.add_argument('-i', '--inputfile', help='Input file', required=True, type=str)
ap.add_argument('-s', '--save', help='Save outputs to disk', action='store_true')
ap.add_argument('-b', '--batch', help='Enable batch mode', action='store_true')
args = ap.parse_args()

ipshell = embed

if __name__ == '__main__':
    # Parse arguments
    print
    for arg in vars(args):
        globals()[arg]=vars(args)[arg]
        print arg, ' set to ', vars(args)[arg]
    print
    print 'Activated analyses:'
    for s in studies:
        print '\t', s
    print

    # Prepare execution
    if tracker == 'TT':
        detector = CreateDetectors.create_TT()
    elif tracker == 'IT':
        detector = CreateDetectors.create_IT()
    else:
        print 'ERROR: please select tracker (IT or TT).'
        print 'Sample usage: python -i ntupleAnalysis.py TT ../RootFiles/EveryHit/all2012-muEstimate-Edges-2cm.root save'
        print 'Exiting now...'
        sys.exit()
    inputfile = str(sys.argv[2])
    shortFilename = inputfile.split('/')[-1].replace('.root','')
    if not os.path.exists('../Out/'+shortFilename):
        os.system('mkdir ../Out/'+shortFilename)
    if not os.path.exists('../Out/'+shortFilename+'/%s'%tracker):
        os.system('mkdir ../Out/'+shortFilename+'/%s'%tracker)
    if 'EveryHit' in inputfile:
        datatype = 'EveryHit'
    elif 'HitsOnTrack' in inputfile:
        datatype = 'HitsOnTrack'
    else:
        print 'ERROR: could not understand data type (HitsOnTrack or EveryHit)'
        sys.exit()
    if 'begin2012' in inputfile:
        segment = 'begin2012'
    elif 'end2012' in inputfile:
        segment = 'end2012'
    elif studies == ['IOV']:
        print 'WARNING: could not understand data segment (begin or end 2012)'
        print 'Going on with IOV studies...'
    else:
        print 'ERROR: could not understand data segment (begin or end 2012)'
        sys.exit()
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s'%(tracker, datatype))
    if batch:
        # avoid spawning canvases
        r.gROOT.SetBatch(r.kTRUE)
        # turn off ipython
        def ipshell(header):
            pass
    flatDetector = flatten(detector)
    tFile = r.TFile(inputfile, 'read')
    t = tFile.Get(tracker+'HitEfficiencyTuple/TrackMonTuple')

    # Do the analysis
    results = {}
    for s in studies:
        print
        print 'Starting', s, '...'
        module = importlib.import_module('tools.'+s)
        func = getattr(module, s)
        results[s] = func(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector)

    # Access interactive shell
    ipshell(header='Hit Ctrl-D to exit interpreter and continue program.')
    print