#!/usr/bin/python
# Execute e.g. with:
# python analyze.py -i ../RootFiles/HitsOnTrack/runs131973-133785-end2012-muEstimate-Edges-closestState.root -st RotationsPerIOV -s -b
import argparse, importlib

# Parse commandline inputs
ap = argparse.ArgumentParser(prog='python analyze.py',
    description='ST track analysis script', add_help=True)
ap.add_argument('-st', '--studies', help='List of studies to execute.\nDefault is none.',
#                nargs='+', default='CLZvsTY RotationsPerIOV IOV PositionsSectors PositionsHalfModules Outliers FullLayers ClusterSize Overlaps OverlapsHalfModules MagField'.split())
                nargs='+', default=' '.split())
ap.add_argument('-t', '--tracker', help='Tracking detector: IT or TT', default='TT', type=str)
ap.add_argument('-i', '--inputfile', help='Input file', required=True, type=str)
ap.add_argument('-s', '--save', help='Save outputs to disk', action='store_true')
ap.add_argument('-b', '--batch', help='Enable batch mode', action='store_true')

args = ap.parse_args()


# I put this import here because somehow it conflicts with argparse's builtin help
from tools.common import *

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
        if os.path.isfile('../Pickle/TTchIDlookupTable.pkl'):
            lookup = pickle.load(open('../Pickle/TTchIDlookupTable.pkl','r'))
        else:
            lookup = dictOfTTChannelIDs(save=True)
    elif tracker == 'IT':
        print "Missing IT lookup table. Exiting."
        quit()
        #detector = CreateDetectors.create_IT()
    else:
        print 'ERROR: please select tracker (IT or TT).'
        print 'Sample usage: python -i ntupleAnalysis.py TT ../RootFiles/EveryHit/all2012-muEstimate-Edges-2cm.root save'
        print 'Exiting now...'
        sys.exit()
    shortFilename = inputfile.split('/')[-1].replace('.root','')
    if not os.path.exists('../Out/'+shortFilename):
        os.system('mkdir ../Out/'+shortFilename)
    if not os.path.exists('../Out/'+shortFilename+'/%s'%tracker):
        os.system('mkdir ../Out/'+shortFilename+'/%s'%tracker)
    datatype = ''
    if 'EveryHit' in inputfile:
        datatype = 'EveryHit'
    elif 'HitsOnTrack' in inputfile:
        datatype = 'HitsOnTrack'
    elif not studies==['Corners']:
        print 'ERROR: could not understand data type (HitsOnTrack or EveryHit)'
        sys.exit()
    segment = 'all2012'
    if 'begin2012' in inputfile:
        segment = 'begin2012'
    elif 'end2012' in inputfile:
        segment = 'end2012'
    #elif 'all2012' in inputfile:
    #    segment = 'all2012'
    #elif studies == ['IOV']:
    #    print 'WARNING: could not understand data segment (begin or end 2012)'
    #    print 'Going on with IOV studies...'
    #else:
    #    print 'ERROR: could not understand data segment (begin or end 2012)'
    #    sys.exit()
    print
    print 'datatype set to %s'%datatype
    print 'segment set to %s'%segment
    print
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s'%(tracker, datatype))
    if not batch:
        from IPython import embed
        ipshell = embed
    else:
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
        results[s] = func(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector, lookup)

    # Access interactive shell
    ipshell(header='Hit Ctrl-D to exit interpreter and continue program.')
    print