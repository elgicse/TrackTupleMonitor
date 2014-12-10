import sys, os
import math
import ROOT as r
from conf import CreateDetectors
from conf.STChannelID import *

def get_sector(chanID):
    return STNames().uniqueSectorName(STChannelID(int(chanID)))

def flatten(d):
    out = []
    if isinstance(d, (list, tuple)):
        for item in d:
            out.extend(flatten(item))  
    elif isinstance(d, (str, int, float, unicode)):
        out.append(d)
    elif isinstance(d, (dict)):
        for dictkey in d.keys():
            out.extend(flatten(d[dictkey]))
    return out

if __name__ == '__main__':
    tracker = str(sys.argv[1])
    if tracker == 'TT':
        detector = CreateDetectors.create_TT()
    elif tracker == 'IT':
        detector = CreateDetectors.create_IT()
    else:
        print 'ERROR: please select tracker (IT or TT).'
        print 'Sample usage: python ntupleAnalysis.py TT ../RootFiles/EveryHit/runs131973-133785-end2012.root'
        print 'Exiting now...'
        sys.exit(0)
    flatDetector = flatten(detector)
    inputFile = str(sys.argv[2])
    tFile = r.TFile(inputFile, 'read')
    t = tFile.Get(tracker+'HitEfficiencyTuple/TrackMonTuple')

    # Looking into possible magnetic field effects
    if not os.path.exists('../Out/ResidualVSMomentum'):
        os.system('mkdir ../Out/ResidualVSMomentum')
    hPositive, hNegative = {}, {}
    for sector in flatDetector:
        hPositive[sector] = r.TH2F(sector+'-pos', sector + ' |Residual| VS Momentum', 50, 3000, 210000, 20, -0.4, 0.4)    #sector+'-positive', sector+'-positive')
        hNegative[sector] = r.TH2F(sector+'-neg', sector + ' |Residual| VS Momentum', 50, 3000, 210000, 20, -0.4, 0.4)    #sector+'-negative', sector+'-negative')
    for track in t:
        if track.__getattr__('num'+tracker+'hits') > 0:
            ids = track.clusterSTchanID
            residuals = track.hit_residual
            if len(ids) != len(residuals):
                print "ERROR: number of entries mismatch"
                sys.exit(0)
            for (i, res) in enumerate(residuals):
                if track.charge == -1:
                    hNegative[get_sector(ids[i])].Fill(float(track.p), math.fabs(float(res)))
                else:
                    hPositive[get_sector(ids[i])].Fill(float(track.p), math.fabs(float(res)))

    # Look at the overlaps
    hOverlaps = {}
    for layer in detector.keys():
        hOverlaps[layer] = {   'HitXVSTrackY':     r.TH2F( layer+'_HitXVSTrackY'    , layer+' HitXVSTrackY'    , 100, -800., 800., 100, -800., 800. ),
                               'TrackXVSTrackY':   r.TH2F( layer+'_TrackXVSTrackY'  , layer+' TrackXVSTrackY'  , 100, -800., 800., 100, -800., 800. ),
                               'ResidualVSTrackY': r.TH2F( layer+'_ResidualVSTrackY', layer+' ResidualVSTrackY', 40,   -0.4,  0.4, 100, -800., 800. )   }
    for track in t:
        for layer in detector.keys():
            if track.__getattr__(layer+'_nHits') > 1:
                tsy = track.closestTrackState_y
                tsx = track.closestTrackState_x
                residuals = track.hit_residual
                for (i, cx) in enumerate(track.cluster_x):
                    hOverlaps[layer]['HitXVSTrackY'].Fill(    float(cx),           float(tsy[i]))
                    hOverlaps[layer]['TrackXVSTrackY'].Fill(  float(tsx[i]),       float(tsy[i]))
                    hOverlaps[layer]['ResidualVSTrackY'].Fill(float(residuals[i]), float(tsy[i]))




