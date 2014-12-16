import sys, os
import math
import ROOT as r
from conf import CreateDetectors
from conf.STChannelID import *

cSaver = []
r.gROOT.ProcessLine('.x tools/lhcbStyle.C')
# Graph colors
gCol = [7,8,4,6,1,2,5]#[r.kBlack, r.kRed, r.kGreen, r.kBlue, r.kYellow, r.kMagenta, r.kCyan, r.kViolet, r.kOrange]
#//int colors[10] = {0,11,5,7,3,6,2,4,12,1};
#// int colors[10] = {0,5,11,7,3,6,2,12,4,1};
#int colors[10] = {0,0,5,7,3,6,2,4,1,1};
#lhcbStyle->SetPalette(10,colors);

class InMoreLayers(Exception): pass

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
        print 'Sample usage: python ntupleAnalysis.py TT ../RootFiles/EveryHit/runs131973-133785-end2012.root save'
        print 'Exiting now...'
        sys.exit(0)
    if not os.path.exists('../Out/%s'%tracker):
        os.system('mkdir ../Out/%s'%tracker)
    inputFile = str(sys.argv[2])
    if 'EveryHit' in inputFile:
        datatype = 'EveryHit'
    elif 'HitsOnTrack' in inputFile:
        datatype = 'HitsOnTrack'
    else:
        print 'ERROR: could not understand data type (HitsOnTrack or EveryHit)'
        sys.exit(0)
    if not os.path.exists('../Out/%s/%s'%(tracker, datatype)):
        os.system('mkdir ../Out/%s/%s'%(tracker, datatype))
    save = False
    try:
        if str(sys.argv[3]) == 'save':
            save = True
    except:
        pass
    flatDetector = flatten(detector)
    tFile = r.TFile(inputFile, 'read')
    t = tFile.Get(tracker+'HitEfficiencyTuple/TrackMonTuple')

    # Looking into possible magnetic field effects
    if not os.path.exists('../Out/%s/%s/ResidualVSMomentum'%(tracker, datatype)):
        os.system('mkdir ../Out/%s/%s/ResidualVSMomentum'%(tracker, datatype))
    hPositive, hNegative = {}, {}
    for sector in flatDetector:
        hPositive[sector] = r.TGraph(); hPositive[sector].SetName(sector+'-pos'); hPositive[sector].SetTitle(sector+' Residual VS Momentum (charge = +1)')
        hNegative[sector] = r.TGraph(); hNegative[sector].SetName(sector+'-neg'); hNegative[sector].SetTitle(sector+' Residual VS Momentum (charge = -1)')
    for track in t:
        if track.__getattr__('num'+tracker+'hits') > 0:
            ids = track.clusterSTchanID
            residuals = track.hit_residual
            if len(ids) != len(residuals):
                print "ERROR: number of entries mismatch"
                sys.exit(0)
            for (i, res) in enumerate(residuals):
                if track.charge == -1:
                    hNegative[get_sector(ids[i])].SetPoint( hNegative[get_sector(ids[i])].GetN(), float(track.p/1000.), float(res))
                else:
                    hPositive[get_sector(ids[i])].SetPoint( hPositive[get_sector(ids[i])].GetN(), float(track.p/1000.), float(res))
    for sector in flatDetector:
        hPositive[sector].GetXaxis().SetTitle('Track momentum [GeV]'); hPositive[sector].GetYaxis().SetTitle('Hit residuals [mm]')
        hNegative[sector].GetXaxis().SetTitle('Track momentum [GeV]'); hPositive[sector].GetYaxis().SetTitle('Hit residuals [mm]')

    # Look at the overlaps
    if not os.path.exists('../Out/%s/%s/Overlaps'%(tracker, datatype)):
        os.system('mkdir ../Out/%s/%s/Overlaps'%(tracker, datatype))
    if tracker == 'IT':
        detector = CreateDetectors.get_IT_layers(detector)
    hOverlaps = {}
    for (lindex,layer) in enumerate(detector.keys()):
        hOverlaps[layer] = {   'HitXVSTrackY':     r.TGraph(),
                               'TrackXVSTrackY':   r.TGraph(),
                               'ResidualVSTrackY': r.TGraph()   }
        for gr in hOverlaps[layer].keys():
            hOverlaps[layer][gr].SetMarkerColor(gCol[lindex])
            hOverlaps[layer][gr].SetLineColor(gCol[lindex])
    for track in t:
        for (lindex, layer) in enumerate(detector.keys()):
            if (track.__getattr__(layer+'_nHits') <= 1):
                continue
            ## makes sure we have two hits in ONLY one layer!
            #try:
            #    for otherlayer in ( detector.keys()[:lindex] + detector.keys()[lindex+1:] ):
            #        if (track.__getattr__(otherlayer+'_nHits') > 1):
            #            raise InMoreLayers
            #except InMoreLayers: 
            #    continue
            if datatype == 'EveryHit':
                tsy = track.closestTrackState_y
                tsx = track.closestTrackState_x
            elif datatype == 'HitsOnTrack':
                tsy = track.trackState_y
                tsx = track.trackState_x
            ids = track.clusterSTchanID
            residuals = track.hit_residual
            for (i, cx) in enumerate(track.cluster_x):
                if STNames().uniqueLayerName(STChannelID(ids[i])) == layer:
                    hOverlaps[layer]['HitXVSTrackY'].SetPoint(     hOverlaps[layer]['HitXVSTrackY'].GetN()    , float(cx),           float(tsy[i]) )
                    hOverlaps[layer]['TrackXVSTrackY'].SetPoint(   hOverlaps[layer]['TrackXVSTrackY'].GetN()  , float(tsx[i]),       float(tsy[i]) )
                    hOverlaps[layer]['ResidualVSTrackY'].SetPoint( hOverlaps[layer]['ResidualVSTrackY'].GetN(), float(residuals[i]), float(tsy[i]) )
    for layer in detector.keys():
        for gr in hOverlaps[layer].keys():
            hOverlaps[layer][gr].SetName(layer+'_'+gr); hOverlaps[layer][gr].SetTitle(layer+' '+gr)
            hOverlaps[layer][gr].GetYaxis().SetTitle('Track Y extrapolation [mm]')
        hOverlaps[layer]['HitXVSTrackY'].GetXaxis().SetTitle('Cluster X position [mm]')
        hOverlaps[layer]['TrackXVSTrackY'].GetXaxis().SetTitle('Track X extrapolation [mm]')
        hOverlaps[layer]['ResidualVSTrackY'].GetXaxis().SetTitle('Hit Residual [mm]')
    hOverlaps['all'] = {    'HitXVSTrackY':        r.TMultiGraph(),
                            'TrackXVSTrackY':      r.TMultiGraph(),
                            'ResidualVSTrackY':    r.TMultiGraph()   }
    for layer in detector.keys():
        for gr in hOverlaps[layer].keys():
            hOverlaps['all'][gr].Add(hOverlaps[layer][gr])
    for gr in hOverlaps['all'].keys():
        hOverlaps['all'][gr].SetName('AllLayers'+'_'+gr); hOverlaps['all'][gr].SetTitle('All layers '+gr)
        cSaver.append(r.TCanvas(hOverlaps['all'][gr].GetName(), hOverlaps['all'][gr].GetTitle(), 1600, 1000))
        hOverlaps['all'][gr].Draw('ap')
        hOverlaps['all'][gr].GetYaxis().SetTitle('Track Y extrapolation [mm]')
        if gr == 'HitXVSTrackY':
            hOverlaps['all'][gr].GetXaxis().SetTitle('Cluster X position [mm]')
        elif gr == 'TrackXVSTrackY':
            hOverlaps['all'][gr].GetXaxis().SetTitle('Track X extrapolation [mm]')
        elif gr == 'ResidualVSTrackY':
            hOverlaps['all'][gr].GetXaxis().SetTitle('Hit residual [mm]')
    for c in cSaver:
        c.Modified(); c.Update()
    if save:
        for layer in detector.keys():
            outfile = r.TFile('../Out/%s/%s/Overlaps/%s.root'%(tracker, datatype, layer), 'recreate')
            for gr in hOverlaps[layer].keys():
                hOverlaps[layer][gr].Write()
                c1 = r.TCanvas(hOverlaps[layer][gr].GetName(), hOverlaps[layer][gr].GetTitle(), 1600, 1000)
                hOverlaps[layer][gr].Draw('ap'); c1.Modified(); c1.Update()
                c1.SaveAs('../Out/%s/%s/Overlaps/%s'%(tracker, datatype, layer) + '-%s.pdf'%gr)
                c1.Write(); c1.Close()
            outfile.Close()
        outfile = r.TFile('../Out/%s/%s/Overlaps/AllLayers.root'%(tracker, datatype), 'recreate')
        for gr in hOverlaps['all'].keys():
            hOverlaps['all'][gr].Write()
        for c in cSaver:
            c.SaveAs('../Out/%s/%s/Overlaps/'%(tracker, datatype) + '%s.pdf'%c.GetName())
            c.Write(); c.Close()
        outfile.Close()


