from tools.common import *

def Overlaps(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector):
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
    # Loop on data
    ntracks = t.GetEntriesFast()
    bar = progressbar.ProgressBar(maxval=ntracks, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    for (itrack,track) in enumerate(t):
        bar.update(itrack+1)
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
                c1.SaveAs('../Out/'+shortFilename+'/%s/%s/Overlaps/%s'%(tracker, datatype, layer) + '-Overlaps-%s-%s.pdf'%(gr,segment))
                c1.Write(); c1.Close()
            outfile.Close()
        outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/Overlaps/AllLayers.root'%(tracker, datatype), 'recreate')
        for gr in hOverlaps['all'].keys():
            hOverlaps['all'][gr].Write()
        for c in cSaver:
            c.SaveAs('../Out/'+shortFilename+'/%s/%s/Overlaps/'%(tracker, datatype) + '-Overlaps-%s-%s.pdf'%(c.GetName(),segment))
            c.Write(); c.Close()
        outfile.Close()
    return hOverlaps