from tools.common import *

def FullLayers(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector, lookup):
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
    # Loop on data
    ntracks = t.GetEntriesFast()
    bar = progressbar.ProgressBar(maxval=ntracks, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    for (itrack,track) in enumerate(t):
        bar.update(itrack+1)
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
                c1.SaveAs('../Out/'+shortFilename+'/%s/%s/PlotsByLayer/%s'%(tracker, datatype, layer) + '-%s-%s.png'%(gr,segment))
                c1.Write(); c1.Close()
            outfile.Close()
        outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/PlotsByLayer/AllLayers.root'%(tracker, datatype), 'recreate')
        for gr in hFullLayers['all'].keys():
            hFullLayers['all'][gr].Write()
        for c in cSaver:
            c.SaveAs('../Out/'+shortFilename+'/%s/%s/PlotsByLayer/'%(tracker, datatype) + '%s-%s.png'%(c.GetName(),segment))
            c.Write(); c.Close()
        outfile.Close()
    return hFullLayers