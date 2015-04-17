from tools.common import *

def OverlapsHalfModules(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector):
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
    # Loop on data
    ntracks = t.GetEntriesFast()
    bar = progressbar.ProgressBar(maxval=ntracks, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    for (itrack,track) in enumerate(t):
        bar.update(itrack+1)
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
                c1.SaveAs('../Out/'+shortFilename+'/%s/%s/OverlapsByHalfModule/%s'%(tracker, datatype, hm) + '-%s-%s.pdf'%(gr,segment))
                c1.Write(); c1.Close()
            outfile.Close()
    print '\nList of half modules where no overlapping hits were found:\n'
    for hm in nonOverlappingHalfModules:
        print hm
    return hOverlapsByHM