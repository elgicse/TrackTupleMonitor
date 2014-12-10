import sys, os
import math
import ROOT as r
from conf import CreateDetectors
from conf.STChannelID import *

r.gROOT.ProcessLine('.x tools/lhcbStyle.C')

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
    inputFile = str(sys.argv[2])
    if 'EveryHit' in inputFile:
        datatype = 'EveryHit'
    elif 'HitsOnTrack' in inputFile:
        datatype = 'HitsOnTrack'
    else:
        print 'ERROR: could not understand data type (HitsOnTrack or EveryHit)'
        sys.exit(0)
    flatDetector = flatten(detector)
    tFile = r.TFile(inputFile, 'read')
    t = tFile.Get(tracker+'HitEfficiencyTuple/TrackMonTuple')

    # Looking into possible magnetic field effects
    if not os.path.exists('../Out/ResidualVSMomentum'):
        os.system('mkdir ../Out/ResidualVSMomentum')
    hPositive, hNegative = {}, {}
    for sector in flatDetector:
        hPositive[sector] = r.TGraph(); hPositive[sector].SetName(sector+'-pos'); hPositive[sector].SetTitle(sector+' |Residual| VS Momentum (charge = +1)')
        hNegative[sector] = r.TGraph(); hNegative[sector].SetName(sector+'-neg'); hNegative[sector].SetTitle(sector+' |Residual| VS Momentum (charge = -1)')
    for track in t:
        if track.__getattr__('num'+tracker+'hits') > 0:
            ids = track.clusterSTchanID
            residuals = track.hit_residual
            if len(ids) != len(residuals):
                print "ERROR: number of entries mismatch"
                sys.exit(0)
            for (i, res) in enumerate(residuals):
                if track.charge == -1:
                    hNegative[get_sector(ids[i])].SetPoint( hNegative[get_sector(ids[i])].GetN(), float(track.p/1000.), math.fabs(float(res)))
                else:
                    hPositive[get_sector(ids[i])].SetPoint( hPositive[get_sector(ids[i])].GetN(), float(track.p/1000.), math.fabs(float(res)))
    for sector in flatDetector:
        hPositive[sector].GetXaxis().SetTitle('Track momentum [GeV]'); hPositive[sector].GetYaxis().SetTitle('Hit residuals (absolute values) [mm]')
        hNegative[sector].GetXaxis().SetTitle('Track momentum [GeV]'); hPositive[sector].GetYaxis().SetTitle('Hit residuals (absolute values) [mm]')

    # Look at the overlaps
    hOverlaps = {}
    for layer in detector.keys():
        hOverlaps[layer] = {   'HitXVSTrackY':     r.TGraph(),
                               'TrackXVSTrackY':   r.TGraph(),
                               'ResidualVSTrackY': r.TGraph()   }
    for track in t:
        for layer in detector.keys():
            if track.__getattr__(layer+'_nHits') > 1:
                if datatype == 'EveryHit':
                    tsy = track.closestTrackState_y
                    tsx = track.closestTrackState_x
                elif datatype == 'HitsOnTrack':
                    tsy = track.trackState_y
                    tsx = track.trackState_x
                residuals = track.hit_residual
                for (i, cx) in enumerate(track.cluster_x):
                    hOverlaps[layer]['HitXVSTrackY'].SetPoint(     hOverlaps[layer]['HitXVSTrackY'].GetN()    , float(cx),           float(tsy[i]) )
                    hOverlaps[layer]['TrackXVSTrackY'].SetPoint(   hOverlaps[layer]['TrackXVSTrackY'].GetN()  , float(tsx[i]),       float(tsy[i]) )
                    hOverlaps[layer]['ResidualVSTrackY'].SetPoint( hOverlaps[layer]['ResidualVSTrackY'].GetN(), float(residuals[i]), float(tsy[i]) )
    for layer in detector.keys():
        for gr in hOverlaps[layer].keys():
            hOverlaps[layer][gr].GetYaxis().SetTitle('Track Y extrapolation [mm]')
        hOverlaps[layer]['HitXVSTrackY'].GetXaxis().SetTitle('Cluster X position [mm]')
        hOverlaps[layer]['TrackXVSTrackY'].GetXaxis().SetTitle('Track X extrapolation [mm]')
        hOverlaps[layer]['ResidualVSTrackY'].GetXaxis().SetTitle('Hit Residual [mm]')



