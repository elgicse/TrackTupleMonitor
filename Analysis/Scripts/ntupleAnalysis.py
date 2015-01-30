import sys, os
import math
import ROOT as r
from array import array
from conf import CreateDetectors
from conf.STChannelID import *
from conf.TTModules import *

studies = ['MagField', 'OverlapsHalfModules', 'Overlaps', 'ClusterSize', 'FullLayers', 'Outliers']
studies = ['Outliers']

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

def get_module(chanID):
    return TTModulesMap().findModule(STChannelID(int(chanID))).id

def get_half_module(chanID):
    return TTModulesMap().findHalfModule(STChannelID(int(chanID))).id

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
        print 'Sample usage: python -i ntupleAnalysis.py TT ../RootFiles/EveryHit/all2012-muEstimate-Edges-2cm.root save'
        print 'Exiting now...'
        sys.exit(0)
    inputFile = str(sys.argv[2])
    shortFilename = inputFile.split('/')[-1].replace('.root','')
    if not os.path.exists('../Out/'+shortFilename):
        os.system('mkdir ../Out/'+shortFilename)
    if not os.path.exists('../Out/'+shortFilename+'/%s'%tracker):
        os.system('mkdir ../Out/'+shortFilename+'/%s'%tracker)
    if 'EveryHit' in inputFile:
        datatype = 'EveryHit'
    elif 'HitsOnTrack' in inputFile:
        datatype = 'HitsOnTrack'
    else:
        print 'ERROR: could not understand data type (HitsOnTrack or EveryHit)'
        sys.exit(0)
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s'%(tracker, datatype))
    save = False
    try:
        if str(sys.argv[3]) == 'save':
            save = True
    except:
        pass
    if save:
        # avoid spawning canvases
        r.gROOT.SetBatch(r.kTRUE)
    flatDetector = flatten(detector)
    tFile = r.TFile(inputFile, 'read')
    t = tFile.Get(tracker+'HitEfficiencyTuple/TrackMonTuple')


    # Looking into possible magnetic field effects
    if 'MagField' in studies:
        if not os.path.exists('../Out/'+shortFilename+'/%s/%s/ResidualVSMomentum'%(tracker, datatype)):
            os.system('mkdir ../Out/'+shortFilename+'/%s/%s/ResidualVSMomentum'%(tracker, datatype))
        hPositive, hNegative = {}, {}
        for sector in flatDetector:
            hPositive[sector] = r.TGraph(); hPositive[sector].SetName(sector+'-pos'); hPositive[sector].SetTitle(sector+' Residual VS Momentum (charge = +1)');
            hNegative[sector] = r.TGraph(); hNegative[sector].SetName(sector+'-neg'); hNegative[sector].SetTitle(sector+' Residual VS Momentum (charge = -1)');
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
            hNegative[sector].GetXaxis().SetTitle('Track momentum [GeV]'); hNegative[sector].GetYaxis().SetTitle('Hit residuals [mm]')
        if save:
            for collection in [hPositive, hNegative]:
                for gr in collection.keys():
                    c1 = r.TCanvas(collection[gr].GetName(), collection[gr].GetTitle())
                    collection[gr].Draw('ap'); c1.Modified(); c1.Update()
                    label = r.TPaveText( 0.60 - r.gStyle.GetPadRightMargin(), 0.87 - r.gStyle.GetPadTopMargin(),
                                         0.95 - r.gStyle.GetPadRightMargin(), 0.95 - r.gStyle.GetPadTopMargin(), "BRNDC");
                    label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
                    label.SetTextFont(132); label.SetTextSize(0.06)
                    label.AddText(gr); label.Draw('same'); c1.Modified(); c1.Update()
                    c1.SaveAs('../Out/'+shortFilename+'/%s/%s/ResidualVSMomentum/%s.pdf'%(tracker, datatype, collection[gr].GetName()))
                    c1.Close()
    


    # Look at the overlaps in the single half-modules
    if 'OverlapsHalfModules' in studies:
        if tracker == 'IT':
            print 'Sorry I cannot do this for the IT, yet...'
            sys.exit(0)
        if not os.path.exists('../Out/'+shortFilename+'/%s/%s/OverlapsByHalfModule'%(tracker, datatype)):
            os.system('mkdir ../Out/'+shortFilename+'/%s/%s/OverlapsByHalfModule'%(tracker, datatype))
        listOfHM = listOfTTHalfModules()
        hOverlapsByHM = {}
        for hm in listOfHM:
            hOverlapsByHM[hm] = {  'HitXVSTrackY':     r.TGraph(),
                                   'TrackXVSTrackY':   r.TGraph(),
                                   'DeltaXVSTrackY':   r.TGraph(),
                                   'DeltaYVSTrackY':   r.TGraph(),
                                   'DeltaZVSTrackY':   r.TGraph(),
                                   'ResidualVSTrackY': r.TGraph()   }
        for track in t:
            for (lindex, layer) in enumerate(detector.keys()):
                if (track.__getattr__(layer+'_nHits') <= 1):
                    continue
                if datatype == 'EveryHit':
                    tsx = track.closestTrackState_x
                    tsy = track.closestTrackState_y
                    tsz = track.closestTrackState_z
                elif datatype == 'HitsOnTrack':
                    tsx = track.trackState_x
                    tsy = track.trackState_y
                    tsz = track.trackState_z
                ids = track.clusterSTchanID
                residuals = track.hit_residual
                cx = track.cluster_x
                cy = track.cluster_y
                cz = track.cluster_z
                for (i, id) in enumerate(ids):
                    if STNames().uniqueLayerName(STChannelID(ids[i])) == layer:
                        hm = get_half_module(id)
                        hOverlapsByHM[hm]['HitXVSTrackY'].SetPoint(     hOverlapsByHM[hm]['HitXVSTrackY'].GetN()    , float(cx[i]),        float(tsy[i]) )
                        hOverlapsByHM[hm]['TrackXVSTrackY'].SetPoint(   hOverlapsByHM[hm]['TrackXVSTrackY'].GetN()  , float(tsx[i]),       float(tsy[i]) )
                        hOverlapsByHM[hm]['DeltaXVSTrackY'].SetPoint(   hOverlapsByHM[hm]['DeltaXVSTrackY'].GetN()  , float(tsx[i])-float(cx[i]),
                                                                                                                                       float(tsy[i]) )
                        hOverlapsByHM[hm]['DeltaYVSTrackY'].SetPoint(   hOverlapsByHM[hm]['DeltaYVSTrackY'].GetN()  , float(tsy[i])-float(cy[i]),
                                                                                                                                       float(tsy[i]) )
                        hOverlapsByHM[hm]['DeltaZVSTrackY'].SetPoint(   hOverlapsByHM[hm]['DeltaZVSTrackY'].GetN()  , float(tsz[i])-float(cz[i]),
                                                                                                                                       float(tsy[i]) )
                        hOverlapsByHM[hm]['ResidualVSTrackY'].SetPoint( hOverlapsByHM[hm]['ResidualVSTrackY'].GetN(), float(residuals[i]), float(tsy[i]) )
        nonOverlappingHalfModules = []
        for hm in listOfHM:
            if hOverlapsByHM[hm]['HitXVSTrackY'].GetN() == 0:
                nonOverlappingHalfModules.append(hm)
            for gr in hOverlapsByHM[hm].keys():
                hOverlapsByHM[hm][gr].SetName(hm+'_'+gr); hOverlapsByHM[hm][gr].SetTitle(hm+' '+gr)
                hOverlapsByHM[hm][gr].GetYaxis().SetTitle('Track Y extrapolation [mm]')
            hOverlapsByHM[hm]['HitXVSTrackY'].GetXaxis().SetTitle('Cluster X position [mm]')
            hOverlapsByHM[hm]['TrackXVSTrackY'].GetXaxis().SetTitle('Track X extrapolation [mm]')
            hOverlapsByHM[hm]['DeltaXVSTrackY'].GetXaxis().SetTitle('(Track X extrapolation - cluster X position) [mm]')
            hOverlapsByHM[hm]['DeltaYVSTrackY'].GetXaxis().SetTitle('(Track Y extrapolation - cluster Y position) [mm]')
            hOverlapsByHM[hm]['DeltaZVSTrackY'].GetXaxis().SetTitle('(Track state Z - cluster Z position) [mm]')
            hOverlapsByHM[hm]['ResidualVSTrackY'].GetXaxis().SetTitle('Hit Residual [mm]')
        if save:
            for hm in listOfHM:
                outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/OverlapsByHalfModule/%s.root'%(tracker, datatype, hm), 'recreate')
                for gr in hOverlapsByHM[hm].keys():
                    hOverlapsByHM[hm][gr].Write()
                    c1 = r.TCanvas(hOverlapsByHM[hm][gr].GetName(), hOverlapsByHM[hm][gr].GetTitle(), 1600, 1000)
                    hOverlapsByHM[hm][gr].Draw('ap'); c1.Modified(); c1.Update()
                    # Add label with half module name
                    label = r.TPaveText( 0.60 - r.gStyle.GetPadRightMargin(), 0.87 - r.gStyle.GetPadTopMargin(),
                                         0.95 - r.gStyle.GetPadRightMargin(), 0.95 - r.gStyle.GetPadTopMargin(), "BRNDC");
                    label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
                    label.SetTextFont(132); label.SetTextSize(0.06)
                    label.AddText(hm); label.Draw('same'); c1.Modified(); c1.Update()
                    c1.SaveAs('../Out/'+shortFilename+'/%s/%s/OverlapsByHalfModule/%s'%(tracker, datatype, hm) + '-%s.pdf'%gr)
                    c1.Write(); c1.Close()
                outfile.Close()
        print '\nList of half modules where no overlapping hits were found:\n'
        for hm in nonOverlappingHalfModules:
            print hm


    
    # Look at the overlaps in the full layers
    if 'Overlaps' in studies:
        if not os.path.exists('../Out/'+shortFilename+'/%s/%s/Overlaps'%(tracker, datatype)):
            os.system('mkdir ../Out/'+shortFilename+'/%s/%s/Overlaps'%(tracker, datatype))
        if tracker == 'IT':
            detector = CreateDetectors.get_IT_layers(detector)
        hOverlaps = {}
        for (lindex,layer) in enumerate(detector.keys()):
            hOverlaps[layer] = {   'HitXVSTrackY':     r.TGraph(),
                                   'TrackXVSTrackY':   r.TGraph(),
                                   'DeltaXVSTrackY':   r.TGraph(),
                                   'DeltaYVSTrackY':   r.TGraph(),
                                   'DeltaZVSTrackY':   r.TGraph(),
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
                    tsx = track.closestTrackState_x
                    tsy = track.closestTrackState_y
                    tsz = track.closestTrackState_z
                elif datatype == 'HitsOnTrack':
                    tsx = track.trackState_x
                    tsy = track.trackState_y
                    tsz = track.trackState_z
                ids = track.clusterSTchanID
                residuals = track.hit_residual
                cy = track.cluster_y
                cz = track.cluster_z
                for (i, cx) in enumerate(track.cluster_x):
                    if STNames().uniqueLayerName(STChannelID(ids[i])) == layer:
                        hOverlaps[layer]['HitXVSTrackY'].SetPoint(     hOverlaps[layer]['HitXVSTrackY'].GetN()    , float(cx),           float(tsy[i]) )
                        hOverlaps[layer]['TrackXVSTrackY'].SetPoint(   hOverlaps[layer]['TrackXVSTrackY'].GetN()  , float(tsx[i]),       float(tsy[i]) )
                        hOverlaps[layer]['DeltaXVSTrackY'].SetPoint(   hOverlaps[layer]['DeltaXVSTrackY'].GetN()  , float(tsx[i])-float(cx),
                                                                                                                                         float(tsy[i]) )
                        hOverlaps[layer]['DeltaYVSTrackY'].SetPoint(   hOverlaps[layer]['DeltaYVSTrackY'].GetN()  , float(tsy[i])-float(cy[i]),
                                                                                                                                         float(tsy[i]) )
                        hOverlaps[layer]['DeltaZVSTrackY'].SetPoint(   hOverlaps[layer]['DeltaZVSTrackY'].GetN()  , float(tsz[i])-float(cz[i]),
                                                                                                                                         float(tsy[i]) )
                        hOverlaps[layer]['ResidualVSTrackY'].SetPoint( hOverlaps[layer]['ResidualVSTrackY'].GetN(), float(residuals[i]), float(tsy[i]) )
        for layer in detector.keys():
            for gr in hOverlaps[layer].keys():
                hOverlaps[layer][gr].SetName(layer+'_'+gr); hOverlaps[layer][gr].SetTitle(layer+' '+gr)
                hOverlaps[layer][gr].GetYaxis().SetTitle('Track Y extrapolation [mm]')
            hOverlaps[layer]['HitXVSTrackY'].GetXaxis().SetTitle('Cluster X position [mm]')
            hOverlaps[layer]['TrackXVSTrackY'].GetXaxis().SetTitle('Track X extrapolation [mm]')
            hOverlaps[layer]['DeltaXVSTrackY'].GetXaxis().SetTitle('(Track X extrapolation - cluster X position) [mm]')
            hOverlaps[layer]['DeltaYVSTrackY'].GetXaxis().SetTitle('(Track Y extrapolation - cluster Y position) [mm]')
            hOverlaps[layer]['DeltaZVSTrackY'].GetXaxis().SetTitle('(Track state Z - cluster Z position) [mm]')
            hOverlaps[layer]['ResidualVSTrackY'].GetXaxis().SetTitle('Hit Residual [mm]')
        hOverlaps['all'] = {    'HitXVSTrackY':        r.TMultiGraph(),
                                'TrackXVSTrackY':      r.TMultiGraph(),
                                'DeltaXVSTrackY':      r.TMultiGraph(),
                                'DeltaYVSTrackY':      r.TMultiGraph(),
                                'DeltaZVSTrackY':      r.TMultiGraph(),
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
            elif gr == 'DeltaXVSTrackY':
                hOverlaps['all'][gr].GetXaxis().SetTitle('(Track X extrapolation - cluster X position) [mm]')
            elif gr == 'DeltaYVSTrackY':
                hOverlaps['all'][gr].GetXaxis().SetTitle('(Track Y extrapolation - cluster Y position) [mm]')
            elif gr == 'DeltaZVSTrackY':
                hOverlaps['all'][gr].GetXaxis().SetTitle('(Track state Z - cluster Z position) [mm]')
            elif gr == 'ResidualVSTrackY':
                hOverlaps['all'][gr].GetXaxis().SetTitle('Hit residual [mm]')
        for c in cSaver:
            c.Modified(); c.Update()
        if save:
            for (lindex, layer) in enumerate(detector.keys()):
                outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/Overlaps/%s.root'%(tracker, datatype, layer), 'recreate')
                for gr in hOverlaps[layer].keys():
                    hOverlaps[layer][gr].Write()
                    c1 = r.TCanvas(hOverlaps[layer][gr].GetName(), hOverlaps[layer][gr].GetTitle(), 1600, 1000)
                    hOverlaps[layer][gr].Draw('ap'); c1.Modified(); c1.Update()
                    label = r.TPaveText( 0.85 - r.gStyle.GetPadRightMargin(), 0.87 - r.gStyle.GetPadTopMargin(),
                                         0.95 - r.gStyle.GetPadRightMargin(), 0.95 - r.gStyle.GetPadTopMargin(), "BRNDC");
                    label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
                    label.SetTextFont(132); label.SetTextSize(0.06); label.SetTextColor(gCol[lindex])
                    label.AddText(layer); label.Draw('same'); c1.Modified(); c1.Update()
                    c1.SaveAs('../Out/'+shortFilename+'/%s/%s/Overlaps/%s'%(tracker, datatype, layer) + '-%s.pdf'%gr)
                    c1.Write(); c1.Close()
                outfile.Close()
            outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/Overlaps/AllLayers.root'%(tracker, datatype), 'recreate')
            for gr in hOverlaps['all'].keys():
                hOverlaps['all'][gr].Write()
            for c in cSaver:
                c.SaveAs('../Out/'+shortFilename+'/%s/%s/Overlaps/'%(tracker, datatype) + '%s.pdf'%c.GetName())
                c.Write(); c.Close()
            outfile.Close()


    # Looking into the cluster size distribution
    if 'ClusterSize' in studies:
        if not os.path.exists('../Out/'+shortFilename+'/%s/%s/ClusterSizeBySector'%(tracker, datatype)):
            os.system('mkdir ../Out/'+shortFilename+'/%s/%s/ClusterSizeBySector'%(tracker, datatype))
        hCSize = {}
        for sector in flatDetector:
            hCSize[sector] = r.TH1I(sector, sector+' Cluster Size', 4, 0.5, 4.5)
        for track in t:
            if track.__getattr__('num'+tracker+'hits') > 0:
                ids = track.clusterSTchanID
                csize = track.clusterSize
                if len(ids) != len(csize):
                    print "ERROR: number of entries mismatch"
                    sys.exit(0)
                for (i, cs) in enumerate(csize):
                    hCSize[get_sector(ids[i])].Fill(int(cs))
        for sector in flatDetector:
            hCSize[sector].GetXaxis().SetTitle('Cluster size')
            if save:
                c1 = r.TCanvas(hCSize[sector].GetName(), hCSize[sector].GetTitle())
                hCSize[sector].Draw('cp'); c1.Modified(); c1.Update()
                label = r.TPaveText( 0.60 - r.gStyle.GetPadRightMargin(), 0.87 - r.gStyle.GetPadTopMargin(),
                                     0.95 - r.gStyle.GetPadRightMargin(), 0.95 - r.gStyle.GetPadTopMargin(), "BRNDC");
                label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
                label.SetTextFont(132); label.SetTextSize(0.06)
                label.AddText(sector); label.Draw('same'); c1.Modified(); c1.Update()
                mean = r.TPaveText( 0.60 - r.gStyle.GetPadRightMargin(), 0.80 - r.gStyle.GetPadTopMargin(),
                                     0.95 - r.gStyle.GetPadRightMargin(), 0.88 - r.gStyle.GetPadTopMargin(), "BRNDC");
                mean.SetFillColor(0); mean.SetTextAlign(32); mean.SetBorderSize(0)
                mean.SetTextFont(132); mean.SetTextSize(0.06)
                mean.AddText('Mean: %.2f'%hCSize[sector].GetMean()); mean.Draw('same'); c1.Modified(); c1.Update()
                rms = r.TPaveText( 0.60 - r.gStyle.GetPadRightMargin(), 0.73 - r.gStyle.GetPadTopMargin(),
                                     0.95 - r.gStyle.GetPadRightMargin(), 0.81 - r.gStyle.GetPadTopMargin(), "BRNDC");
                rms.SetFillColor(0); rms.SetTextAlign(32); rms.SetBorderSize(0)
                rms.SetTextFont(132); rms.SetTextSize(0.06)
                rms.AddText('RMS: %.2f'%hCSize[sector].GetRMS()); rms.Draw('same'); c1.Modified(); c1.Update()
                c1.SaveAs('../Out/'+shortFilename+'/%s/%s/ClusterSizeBySector/%s.pdf'%(tracker, datatype, hCSize[sector].GetName()))
                c1.Close()



    # Look at things in the full layers (not only overlaps)
    if 'FullLayers' in studies:
        if not os.path.exists('../Out/'+shortFilename+'/%s/%s/PlotsByLayer'%(tracker, datatype)):
            os.system('mkdir ../Out/'+shortFilename+'/%s/%s/PlotsByLayer'%(tracker, datatype))
        if tracker == 'IT':
            detector = CreateDetectors.get_IT_layers(detector)
        hFullLayers = {}
        for (lindex,layer) in enumerate(detector.keys()):
            hFullLayers[layer] = { 'HitXVSTrackY':     r.TGraph(),
                                   'TrackXVSTrackY':   r.TGraph(),
                                   'DeltaXVSTrackY':   r.TGraph(),
                                   'DeltaYVSTrackY':   r.TGraph(),
                                   'DeltaZVSTrackY':   r.TGraph(),
                                   'DeltaZVSStripMu':  r.TGraph(),
                                   'DeltaXVSStripMu':  r.TGraph(),
                                   'DeltaYVSStripMu':  r.TGraph(),
                                   'ResidualVSTrackY': r.TGraph()   }
            for gr in hFullLayers[layer].keys():
                hFullLayers[layer][gr].SetMarkerColor(gCol[lindex])
                hFullLayers[layer][gr].SetLineColor(gCol[lindex])
        for track in t:
            for (lindex, layer) in enumerate(detector.keys()):
                # Overlap condition
                #if (track.__getattr__(layer+'_nHits') <= 1):
                #    continue
                if datatype == 'EveryHit':
                    tsx = track.closestTrackState_x
                    tsy = track.closestTrackState_y
                    tsz = track.closestTrackState_z
                elif datatype == 'HitsOnTrack':
                    tsx = track.trackState_x
                    tsy = track.trackState_y
                    tsz = track.trackState_z
                ids = track.clusterSTchanID
                residuals = track.hit_residual
                cy = track.cluster_y
                cz = track.cluster_z
                mu = track.traj_mu
                for (i, cx) in enumerate(track.cluster_x):
                    if STNames().uniqueLayerName(STChannelID(ids[i])) == layer:
                        hFullLayers[layer]['HitXVSTrackY'].SetPoint(     hFullLayers[layer]['HitXVSTrackY'].GetN()    , float(cx),           float(tsy[i]) )
                        hFullLayers[layer]['TrackXVSTrackY'].SetPoint(   hFullLayers[layer]['TrackXVSTrackY'].GetN()  , float(tsx[i]),       float(tsy[i]) )
                        hFullLayers[layer]['DeltaXVSTrackY'].SetPoint(   hFullLayers[layer]['DeltaXVSTrackY'].GetN()  , float(tsx[i])-float(cx),
                                                                                                                                         float(tsy[i]) )
                        hFullLayers[layer]['DeltaYVSTrackY'].SetPoint(   hFullLayers[layer]['DeltaYVSTrackY'].GetN()  , float(tsy[i])-float(cy[i]),
                                                                                                                                         float(tsy[i]) )
                        hFullLayers[layer]['DeltaZVSTrackY'].SetPoint(   hFullLayers[layer]['DeltaZVSTrackY'].GetN()  , float(tsz[i])-float(cz[i]),
                                                                                                                                         float(tsy[i]) )
                        hFullLayers[layer]['DeltaZVSStripMu'].SetPoint(   hFullLayers[layer]['DeltaZVSStripMu'].GetN()  , float(tsz[i])-float(cz[i]),
                                                                                                                                         float(mu[i]) )
                        hFullLayers[layer]['DeltaXVSStripMu'].SetPoint(   hFullLayers[layer]['DeltaXVSStripMu'].GetN()  , float(tsx[i])-float(cx),
                                                                                                                                         float(mu[i]) )
                        hFullLayers[layer]['DeltaYVSStripMu'].SetPoint(   hFullLayers[layer]['DeltaYVSStripMu'].GetN()  , float(tsy[i])-float(cy[i]),
                                                                                                                                         float(mu[i]) )
                        hFullLayers[layer]['ResidualVSTrackY'].SetPoint( hFullLayers[layer]['ResidualVSTrackY'].GetN(), float(residuals[i]), float(tsy[i]) )
        for layer in detector.keys():
            for gr in hFullLayers[layer].keys():
                hFullLayers[layer][gr].SetName(layer+'_'+gr); hFullLayers[layer][gr].SetTitle(layer+' '+gr)
                hFullLayers[layer][gr].GetYaxis().SetTitle('Track Y extrapolation [mm]')
            hFullLayers[layer]['HitXVSTrackY'].GetXaxis().SetTitle('Cluster X position [mm]')
            hFullLayers[layer]['TrackXVSTrackY'].GetXaxis().SetTitle('Track X extrapolation [mm]')
            hFullLayers[layer]['DeltaXVSTrackY'].GetXaxis().SetTitle('(Track X extrapolation - cluster X position) [mm]')
            hFullLayers[layer]['DeltaYVSTrackY'].GetXaxis().SetTitle('(Track Y extrapolation - cluster Y position) [mm]')
            hFullLayers[layer]['DeltaZVSTrackY'].GetXaxis().SetTitle('(Track state Z - cluster Z position) [mm]')
            hFullLayers[layer]['DeltaZVSStripMu'].GetXaxis().SetTitle('(Track state Z - cluster Z position) [mm]')
            hFullLayers[layer]['DeltaXVSStripMu'].GetXaxis().SetTitle('(Track state X - cluster X position) [mm]')
            hFullLayers[layer]['DeltaYVSStripMu'].GetXaxis().SetTitle('(Track state Y - cluster Y position) [mm]')
            hFullLayers[layer]['DeltaZVSStripMu'].GetYaxis().SetTitle('Strip trajectory expansion param. (mu)')
            hFullLayers[layer]['DeltaXVSStripMu'].GetYaxis().SetTitle('Strip trajectory expansion param. (mu)')
            hFullLayers[layer]['DeltaYVSStripMu'].GetYaxis().SetTitle('Strip trajectory expansion param. (mu)')
            hFullLayers[layer]['ResidualVSTrackY'].GetXaxis().SetTitle('Hit Residual [mm]')
        hFullLayers['all'] = {    'HitXVSTrackY':      r.TMultiGraph(),
                                'TrackXVSTrackY':      r.TMultiGraph(),
                                'DeltaXVSTrackY':      r.TMultiGraph(),
                                'DeltaYVSTrackY':      r.TMultiGraph(),
                                'DeltaZVSTrackY':      r.TMultiGraph(),
                                'DeltaZVSStripMu':     r.TMultiGraph(),
                                'DeltaXVSStripMu':     r.TMultiGraph(),
                                'DeltaYVSStripMu':     r.TMultiGraph(),
                                'ResidualVSTrackY':    r.TMultiGraph()   }
        for layer in detector.keys():
            for gr in hFullLayers[layer].keys():
                hFullLayers['all'][gr].Add(hFullLayers[layer][gr])
        for gr in hFullLayers['all'].keys():
            hFullLayers['all'][gr].SetName('AllLayers'+'_'+gr); hFullLayers['all'][gr].SetTitle('All layers '+gr)
            cSaver.append(r.TCanvas(hFullLayers['all'][gr].GetName(), hFullLayers['all'][gr].GetTitle(), 1600, 1000))
            hFullLayers['all'][gr].Draw('ap')
            hFullLayers['all'][gr].GetYaxis().SetTitle('Track Y extrapolation [mm]')
            if gr == 'HitXVSTrackY':
                hFullLayers['all'][gr].GetXaxis().SetTitle('Cluster X position [mm]')
            elif gr == 'TrackXVSTrackY':
                hFullLayers['all'][gr].GetXaxis().SetTitle('Track X extrapolation [mm]')
            elif gr == 'DeltaXVSTrackY':
                hFullLayers['all'][gr].GetXaxis().SetTitle('(Track X extrapolation - cluster X position) [mm]')
            elif gr == 'DeltaYVSTrackY':
                hFullLayers['all'][gr].GetXaxis().SetTitle('(Track Y extrapolation - cluster Y position) [mm]')
            elif gr == 'DeltaZVSTrackY':
                hFullLayers['all'][gr].GetXaxis().SetTitle('(Track state Z - cluster Z position) [mm]')
            elif gr == 'DeltaZVSStripMu':
                hFullLayers['all'][gr].GetXaxis().SetTitle('(Track state Z - cluster Z position) [mm]')
                hFullLayers['all'][gr].GetYaxis().SetTitle('Strip trajectory expansion param. (mu)')
            elif gr == 'DeltaXVSStripMu':
                hFullLayers['all'][gr].GetXaxis().SetTitle('(Track state X - cluster X position) [mm]')
                hFullLayers['all'][gr].GetYaxis().SetTitle('Strip trajectory expansion param. (mu)')
            elif gr == 'DeltaYVSStripMu':
                hFullLayers['all'][gr].GetXaxis().SetTitle('(Track state Y - cluster Y position) [mm]')
                hFullLayers['all'][gr].GetYaxis().SetTitle('Strip trajectory expansion param. (mu)')
            elif gr == 'ResidualVSTrackY':
                hFullLayers['all'][gr].GetXaxis().SetTitle('Hit residual [mm]')
        for c in cSaver:
            c.Modified(); c.Update()
        if save:
            for (lindex, layer) in enumerate(detector.keys()):
                outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/PlotsByLayer/%s.root'%(tracker, datatype, layer), 'recreate')
                for gr in hFullLayers[layer].keys():
                    hFullLayers[layer][gr].Write()
                    c1 = r.TCanvas(hFullLayers[layer][gr].GetName(), hFullLayers[layer][gr].GetTitle(), 1600, 1000)
                    hFullLayers[layer][gr].Draw('ap'); c1.Modified(); c1.Update()
                    label = r.TPaveText( 0.85 - r.gStyle.GetPadRightMargin(), 0.87 - r.gStyle.GetPadTopMargin(),
                                         0.95 - r.gStyle.GetPadRightMargin(), 0.95 - r.gStyle.GetPadTopMargin(), "BRNDC")
                    label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
                    label.SetTextFont(132); label.SetTextSize(0.06); label.SetTextColor(gCol[lindex])
                    label.AddText(layer); label.Draw('same'); c1.Modified(); c1.Update()
                    c1.SaveAs('../Out/'+shortFilename+'/%s/%s/PlotsByLayer/%s'%(tracker, datatype, layer) + '-%s.png'%gr)
                    c1.Write(); c1.Close()
                outfile.Close()
            outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/PlotsByLayer/AllLayers.root'%(tracker, datatype), 'recreate')
            for gr in hFullLayers['all'].keys():
                hFullLayers['all'][gr].Write()
            for c in cSaver:
                c.SaveAs('../Out/'+shortFilename+'/%s/%s/PlotsByLayer/'%(tracker, datatype) + '%s.png'%c.GetName())
                c.Write(); c.Close()
            outfile.Close()

    # Study outliers in delta y
    if 'Outliers' in studies:
        outliers = {'DeltaY': {}} # Add cluster size etc.
        for track in t:
                if datatype == 'EveryHit':
                    tsx = track.closestTrackState_x
                    tsy = track.closestTrackState_y
                    tsz = track.closestTrackState_z
                elif datatype == 'HitsOnTrack':
                    tsx = track.trackState_x
                    tsy = track.trackState_y
                    tsz = track.trackState_z
                ids = track.clusterSTchanID
                residuals = track.hit_residual
                cx = track.cluster_x
                cy = track.cluster_y
                cz = track.cluster_z
                mu = track.traj_mu
                for i in xrange(len(track.cluster_x)):
                    delta_y = tsy[i]-cy[i]
                    if abs(delta_y) > 0.1:
                        sector = get_sector(ids[i])
                        half_module = get_half_module(ids[i])
                        xclust = cx[i]
                        xtrack = tsx[i]
                        yclust = cy[i]
                        ytrack = tsy[i]
                        zclust = cz[i]
                        ztrack = tsz[i]
                        outliers['DeltaY'].setdefault(half_module, {})
                        outliers['DeltaY'][half_module].setdefault(sector, {'cx':[], 'tsx':[], 'cy':[], 'tsy':[], 'cz':[], 'tsz':[]})
                        outliers['DeltaY'][half_module][sector]['cx'].append(xclust)
                        outliers['DeltaY'][half_module][sector]['cy'].append(yclust)
                        outliers['DeltaY'][half_module][sector]['cz'].append(zclust)
                        outliers['DeltaY'][half_module][sector]['tsx'].append(xtrack)
                        outliers['DeltaY'][half_module][sector]['tsy'].append(ytrack)
                        outliers['DeltaY'][half_module][sector]['tsz'].append(ztrack)
        # spawn colors
        nHM = len(outliers['DeltaY'])
        colors = range(1,nHM+1)
        outliers['mgr_ClusterXY'] = r.TMultiGraph()
        outliers['mgr_TrackXY'] = r.TMultiGraph()
        for (i,hm) in enumerate(outliers['DeltaY']):
            if len(outliers['DeltaY'][hm])>1:
                print hm, ' has %s sectors with outliers in DeltaY'%len(outliers['DeltaY'][hm])
            cx, cy, cz, tsx, tsy, tsz = [], [], [], [], [], []
            for sector in outliers['DeltaY'][hm]:
                cx.extend(outliers['DeltaY'][hm][sector]['cx'])
                cy.extend(outliers['DeltaY'][hm][sector]['cy'])
                cz.extend(outliers['DeltaY'][hm][sector]['cz'])
                tsx.extend(outliers['DeltaY'][hm][sector]['tsx'])
                tsy.extend(outliers['DeltaY'][hm][sector]['tsy'])
                tsz.extend(outliers['DeltaY'][hm][sector]['tsz'])
            hnum = r.TH1I('nOutliersDeltaY_%s'%hm, 'nOutliersDeltaY_%s'%hm, 21, -0.5, 20.5)
            hnum.Fill(sum([len(outliers['DeltaY'][hm][sector]['tsx']) for sector in outliers['DeltaY'][hm]]))
            outliers['DeltaY'][hm]['nOutliers'] = hnum
            outliers['DeltaY'][hm]['ClusterXY'] = r.TGraph(len(cx), array('f',cx), array('f',cy))
            outliers['DeltaY'][hm]['TrackXY'] = r.TGraph(len(tsx), array('f',tsx), array('f',tsy))
            outliers['DeltaY'][hm]['ClusterZ'] = r.TH1F('CZForYOutliers_%s'%sector,'CZForYOutliers_%s'%sector,10,min(cz),max(cz))
            [ outliers['DeltaY'][hm]['ClusterZ'].Fill(z) for z in cz ]
            outliers['DeltaY'][hm]['ClusterX'] = r.TH1F('CXForYOutliers_%s'%sector,'CXForYOutliers_%s'%sector,10,min(cx),max(cx))
            [ outliers['DeltaY'][hm]['ClusterX'].Fill(x) for x in cx ]
            outliers['DeltaY'][hm]['ClusterY'] = r.TH1F('CYForYOutliers_%s'%sector,'CYForYOutliers_%s'%sector,10,min(cy),max(cy))
            [ outliers['DeltaY'][hm]['ClusterY'].Fill(y) for y in cy ]
            outliers['DeltaY'][hm]['TrackZ'] = r.TH1F('TSZForYOutliers_%s'%sector,'TSZForYOutliers_%s'%sector,10,min(tsz),max(tsz))
            [ outliers['DeltaY'][hm]['TrackZ'].Fill(z) for z in tsz ]
            outliers['DeltaY'][hm]['TrackX'] = r.TH1F('TSXForYOutliers_%s'%sector,'TSXForYOutliers_%s'%sector,10,min(tsx),max(tsx))
            [ outliers['DeltaY'][hm]['TrackX'].Fill(x) for x in tsx ]
            outliers['DeltaY'][hm]['TrackY'] = r.TH1F('TSYForYOutliers_%s'%sector,'TSYForYOutliers_%s'%sector,10,min(tsy),max(tsy))
            [ outliers['DeltaY'][hm]['TrackY'].Fill(y) for y in tsy ]
            outliers['DeltaY'][hm]['ClusterXY'].SetMarkerColor(colors[i]), outliers['DeltaY'][hm]['ClusterXY'].SetTitle(hm)
            outliers['DeltaY'][hm]['TrackXY'].SetMarkerColor(colors[i]), outliers['DeltaY'][hm]['TrackXY'].SetTitle(hm)
            outliers['DeltaY'][hm]['ClusterZ'].SetMarkerColor(colors[i]), outliers['DeltaY'][hm]['ClusterZ'].SetTitle(hm)
            outliers['DeltaY'][hm]['TrackZ'].SetMarkerColor(colors[i]), outliers['DeltaY'][hm]['TrackZ'].SetTitle(hm)
            outliers['mgr_ClusterXY'].Add(outliers['DeltaY'][hm]['ClusterXY'])
            outliers['mgr_TrackXY'].Add(outliers['DeltaY'][hm]['TrackXY'])
        if save:
            if not os.path.exists('../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype)):
                os.system('mkdir ../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype))
            foutliers = r.TFile('../Out/'+shortFilename+'/%s/%s/Histograms/DeltaY.root'%(tracker, datatype), 'recreate')
            for hm in outliers['DeltaY']:
                for hist in outliers['DeltaY'][hm].values():
                    try:
                        print hist.GetName(), type(hist)
                    except AttributeError:
                        pass
                    if isinstance(hist, r.TH1F) or isinstance(hist, r.TH1I):
                        hist.Write()
            foutliers.Close()

