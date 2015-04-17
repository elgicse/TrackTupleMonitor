from tools.common import *

def PositionsHalfModules(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector):
    if tracker == 'IT':
        print 'Sorry I cannot do this for the IT, yet...'
        sys.exit(0)
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype))
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s/PlotsByHalfModule'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s/PlotsByHalfModule'%(tracker, datatype))
    listOfHM = listOfTTHalfModules()
    histosByHM = {}
    for hm in listOfHM:
        histosByHM[hm] = {  'HitXVSTrackY':     r.TGraph(),
                            'HitZVSTrackY':     r.TGraph(),
                            'TrackXVSTrackY':   r.TGraph(),
                            'DeltaXVSTrackY':   r.TGraph(),
                            'DeltaYVSTrackY':   r.TGraph(),
                            'DeltaZVSTrackY':   r.TGraph(),
                            'ResidualVSTrackY': r.TGraph(),
                            'cx':  [], 'cy':  [], 'cz':  [],
                            'tsx': [], 'tsy': [], 'tsz': []   }
    # Loop on data
    ntracks = t.GetEntriesFast()
    bar = progressbar.ProgressBar(maxval=ntracks, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    for (itrack,track) in enumerate(t):
        bar.update(itrack+1)
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
        #histosByHM[hm]['cx'].extend(cx)
        #histosByHM[hm]['cy'].extend(cy)
        #histosByHM[hm]['cz'].extend(cz)
        #histosByHM[hm]['tsx'].extend(tsx)
        #histosByHM[hm]['tsy'].extend(tsy)
        #histosByHM[hm]['tsz'].extend(tsz)
        for (i, id) in enumerate(ids):
            hm = get_half_module(id)
            histosByHM[hm]['cx'].append(cx[i])
            histosByHM[hm]['cy'].append(cy[i])
            histosByHM[hm]['cz'].append(cz[i])
            histosByHM[hm]['tsx'].append(tsx[i])
            histosByHM[hm]['tsy'].append(tsy[i])
            histosByHM[hm]['tsz'].append(tsz[i])
            histosByHM[hm]['HitXVSTrackY'].SetPoint(     histosByHM[hm]['HitXVSTrackY'].GetN()    , float(cx[i]),        float(tsy[i]) )
            histosByHM[hm]['HitZVSTrackY'].SetPoint(     histosByHM[hm]['HitZVSTrackY'].GetN()    , float(cz[i]),        float(tsy[i]) )
            histosByHM[hm]['TrackXVSTrackY'].SetPoint(   histosByHM[hm]['TrackXVSTrackY'].GetN()  , float(tsx[i]),       float(tsy[i]) )
            histosByHM[hm]['DeltaXVSTrackY'].SetPoint(   histosByHM[hm]['DeltaXVSTrackY'].GetN()  , float(tsx[i])-float(cx[i]),
                                                                                                                           float(tsy[i]) )
            histosByHM[hm]['DeltaYVSTrackY'].SetPoint(   histosByHM[hm]['DeltaYVSTrackY'].GetN()  , float(tsy[i])-float(cy[i]),
                                                                                                                           float(tsy[i]) )
            histosByHM[hm]['DeltaZVSTrackY'].SetPoint(   histosByHM[hm]['DeltaZVSTrackY'].GetN()  , float(tsz[i])-float(cz[i]),
                                                                                                                           float(tsy[i]) )
            histosByHM[hm]['ResidualVSTrackY'].SetPoint( histosByHM[hm]['ResidualVSTrackY'].GetN(), float(residuals[i]), float(tsy[i]) )
    for hm in listOfHM:
        for gr in histosByHM[hm].keys():
            if isinstance(histosByHM[hm][gr], r.TGraph):
                histosByHM[hm][gr].SetName(hm+'_'+gr); histosByHM[hm][gr].SetTitle(hm+' '+gr)
                histosByHM[hm][gr].GetYaxis().SetTitle('Track Y extrapolation [mm]')
        histosByHM[hm]['HitXVSTrackY'].GetXaxis().SetTitle('Cluster X position [mm]')
        histosByHM[hm]['HitZVSTrackY'].GetXaxis().SetTitle('Cluster Z position [mm]')
        histosByHM[hm]['TrackXVSTrackY'].GetXaxis().SetTitle('Track X extrapolation [mm]')
        histosByHM[hm]['DeltaXVSTrackY'].GetXaxis().SetTitle('(Track X extrapolation - cluster X position) [mm]')
        histosByHM[hm]['DeltaYVSTrackY'].GetXaxis().SetTitle('(Track Y extrapolation - cluster Y position) [mm]')
        histosByHM[hm]['DeltaZVSTrackY'].GetXaxis().SetTitle('(Track state Z - cluster Z position) [mm]')
        histosByHM[hm]['ResidualVSTrackY'].GetXaxis().SetTitle('Hit Residual [mm]')
    if save:
        outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/Histograms/PositionsByHM.root'%(tracker, datatype), 'recreate')
        for hm in listOfHM:
            for gr in histosByHM[hm].keys():
                if isinstance(histosByHM[hm][gr], r.TGraph):
                    #histosByHM[hm][gr].Write()
                    c1 = r.TCanvas(histosByHM[hm][gr].GetName(), histosByHM[hm][gr].GetTitle(), 1600, 1000)
                    histosByHM[hm][gr].Draw('ap'); c1.Modified(); c1.Update()
                    # Add label with half module name
                    label = r.TPaveText( 0.60 - r.gStyle.GetPadRightMargin(), 0.87 - r.gStyle.GetPadTopMargin(),
                                         0.95 - r.gStyle.GetPadRightMargin(), 0.95 - r.gStyle.GetPadTopMargin(), "BRNDC");
                    label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
                    label.SetTextFont(132); label.SetTextSize(0.06)
                    label.AddText(hm); label.Draw('same'); c1.Modified(); c1.Update()
                    c1.SaveAs('../Out/'+shortFilename+'/%s/%s/PlotsByHalfModule/%s'%(tracker, datatype, hm) + '-%s-%s.png'%(gr,segment))
                    #c1.Write()
                    c1.Close()
                elif isinstance(histosByHM[hm][gr], list):
                    if len(histosByHM[hm][gr])>0: # skip empty modules
                        h = r.TH1F('%s_%s-%s'%(gr, hm, segment), '%s_%s-%s'%(gr, hm, segment), 100, min(histosByHM[hm][gr]), max(histosByHM[hm][gr]))
                        [ h.Fill(x) for x in histosByHM[hm][gr] ]
                        h.Write()
                        h.Delete()
        outfile.Close()
    return histosByHM