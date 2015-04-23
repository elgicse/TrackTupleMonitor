from tools.common import *

def PositionsSectors(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector, lookup):
    if tracker == 'IT':
        print 'Sorry I cannot do this for the IT, yet...'
        sys.exit(0)
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype))
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s/PlotsBySector'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s/PlotsBySector'%(tracker, datatype))
    #listOfHM = listOfTTHalfModules()
    histosBySector = {}
    for sector in flatDetector:
        histosBySector[sector] = {  'HitXVSTrackY':     r.TGraph(),
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
        # come fa a funzionare???
        #histosBySector[sector]['cx'].extend(cx)
        #histosBySector[sector]['cy'].extend(cy)
        #histosBySector[sector]['cz'].extend(cz)
        #histosBySector[sector]['tsx'].extend(tsx)
        #histosBySector[sector]['tsy'].extend(tsy)
        #histosBySector[sector]['tsz'].extend(tsz)
        for (i, id) in enumerate(ids):
            sector = get_sector(id)
            histosBySector[sector]['cx'].append(cx[i])
            histosBySector[sector]['cy'].append(cy[i])
            histosBySector[sector]['cz'].append(cz[i])
            histosBySector[sector]['tsx'].append(tsx[i])
            histosBySector[sector]['tsy'].append(tsy[i])
            histosBySector[sector]['tsz'].append(tsz[i])
            histosBySector[sector]['HitXVSTrackY'].SetPoint(     histosBySector[sector]['HitXVSTrackY'].GetN()    , float(cx[i]),        float(tsy[i]) )
            histosBySector[sector]['TrackXVSTrackY'].SetPoint(   histosBySector[sector]['TrackXVSTrackY'].GetN()  , float(tsx[i]),       float(tsy[i]) )
            histosBySector[sector]['DeltaXVSTrackY'].SetPoint(   histosBySector[sector]['DeltaXVSTrackY'].GetN()  , float(tsx[i])-float(cx[i]),
                                                                                                                           float(tsy[i]) )
            histosBySector[sector]['DeltaYVSTrackY'].SetPoint(   histosBySector[sector]['DeltaYVSTrackY'].GetN()  , float(tsy[i])-float(cy[i]),
                                                                                                                           float(tsy[i]) )
            histosBySector[sector]['DeltaZVSTrackY'].SetPoint(   histosBySector[sector]['DeltaZVSTrackY'].GetN()  , float(tsz[i])-float(cz[i]),
                                                                                                                           float(tsy[i]) )
            histosBySector[sector]['ResidualVSTrackY'].SetPoint( histosBySector[sector]['ResidualVSTrackY'].GetN(), float(residuals[i]), float(tsy[i]) )
    for sector in flatDetector:
        for gr in histosBySector[sector].keys():
            if isinstance(histosBySector[sector][gr], r.TGraph):
                histosBySector[sector][gr].SetName(sector+'_'+gr); histosBySector[sector][gr].SetTitle(sector+' '+gr)
                histosBySector[sector][gr].GetYaxis().SetTitle('Track Y extrapolation [mm]')
        histosBySector[sector]['HitXVSTrackY'].GetXaxis().SetTitle('Cluster X position [mm]')
        histosBySector[sector]['TrackXVSTrackY'].GetXaxis().SetTitle('Track X extrapolation [mm]')
        histosBySector[sector]['DeltaXVSTrackY'].GetXaxis().SetTitle('(Track X extrapolation - cluster X position) [mm]')
        histosBySector[sector]['DeltaYVSTrackY'].GetXaxis().SetTitle('(Track Y extrapolation - cluster Y position) [mm]')
        histosBySector[sector]['DeltaZVSTrackY'].GetXaxis().SetTitle('(Track state Z - cluster Z position) [mm]')
        histosBySector[sector]['ResidualVSTrackY'].GetXaxis().SetTitle('Hit Residual [mm]')
    if save:
        outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/Histograms/PositionsBySector.root'%(tracker, datatype), 'recreate')
        for sector in flatDetector:
            for gr in histosBySector[sector].keys():
                if isinstance(histosBySector[sector][gr], r.TGraph):
                    #histosByHM[hm][gr].Write()
                    c1 = r.TCanvas(histosBySector[sector][gr].GetName(), histosBySector[sector][gr].GetTitle(), 1600, 1000)
                    histosBySector[sector][gr].Draw('ap'); c1.Modified(); c1.Update()
                    # Add label with half module name
                    label = r.TPaveText( 0.60 - r.gStyle.GetPadRightMargin(), 0.87 - r.gStyle.GetPadTopMargin(),
                                         0.95 - r.gStyle.GetPadRightMargin(), 0.95 - r.gStyle.GetPadTopMargin(), "BRNDC");
                    label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
                    label.SetTextFont(132); label.SetTextSize(0.06)
                    label.AddText(sector); label.Draw('same'); c1.Modified(); c1.Update()
                    c1.SaveAs('../Out/'+shortFilename+'/%s/%s/PlotsBySector/%s'%(tracker, datatype, sector) + '-%s-%s.png'%(gr,segment))
                    #c1.Write()
                    c1.Close()
                elif isinstance(histosBySector[sector][gr], list):
                    if len(histosBySector[sector][gr])>0: # skip empty modules
                        h = r.TH1F('%s_%s-%s'%(gr, sector, segment), '%s_%s-%s'%(gr, sector,segment), 100, min(histosBySector[sector][gr]), max(histosBySector[sector][gr]))
                        [ h.Fill(x) for x in histosBySector[sector][gr] ]
                        h.Write()
                        h.Delete()
        outfile.Close()
    return histosBySector