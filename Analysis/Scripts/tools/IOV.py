from tools.common import *

def IOV(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector):
    if tracker == 'IT':
        print 'Sorry I cannot do this for the IT, yet...'
        sys.exit(0)
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype))
    #if not os.path.exists('../Out/'+shortFilename+'/%s/%s/PlotsBySector'%(tracker, datatype)):
    #    os.system('mkdir ../Out/'+shortFilename+'/%s/%s/PlotsBySector'%(tracker, datatype))
    #
    # Book Histograms
    histosBySector = {}
    for sector in flatDetector:
        histosBySector[sector] = { 
            #'AvgResidualByIOV': r.TH2F(sector+'-AvgResidualByIOV', sector+'-AvgResidualByIOV', 17, 0, 17, 100, 0., 0.06),
            #'ResidualRMSByIOV': r.TH2F(sector+'-ResidualRMSByIOV', sector+'-ResidualRMSByIOV', 17, 0, 17, 100, 0., 0.06)
            'AvgResidualByIOV': r.TH1F('AvgResidualByIOV_'+sector, 'AvgResidualByIOV_'+sector, len(IOVs2012().intervals), 0, 1),
            'ResidualRMSByIOV': r.TH1F('ResidualRMSByIOV_'+sector, 'ResidualRMSByIOV_'+sector, len(IOVs2012().intervals), 0, 1),
            'DeltaZSlopeByIOV': r.TH1F('DeltaZSlopeByIOV_'+sector, 'DeltaZSlopeByIOV_'+sector, len(IOVs2012().intervals), 0, 1)
        }
        for i in IOVs2012().intervals:
            histosBySector[sector]['ResidualsByIOV-'+str(i)] = r.TH1F(sector+'-ResidualsByIOV-'+str(i), sector+'-ResidualsByIOV-'+str(i), 100, 0., 0.06)
            histosBySector[sector]['DeltaZByIOV-'+str(i)] = r.TGraph()
            histosBySector[sector]['DeltaZByIOV-'+str(i)].SetTitle(sector+'-DeltaZByIOV-'+str(i))
            histosBySector[sector]['DeltaZByIOV-'+str(i)].SetName(sector+'-DeltaZByIOV-'+str(i))
    # Loop on data
    ntracks = t.GetEntriesFast()
    bar = progressbar.ProgressBar(maxval=ntracks, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    for (itrack, track) in enumerate(t):
        #fish.animate(amount=itrack)
        bar.update(itrack+1)
        if datatype == 'EveryHit':
            tsx = track.closestTrackState_x
            tsy = track.closestTrackState_y
            tsz = track.closestTrackState_z
        elif datatype == 'HitsOnTrack':
            tsx = track.trackState_x
            tsy = track.trackState_y
            tsz = track.trackState_z
        iov = GetIOV(track)
        ids = track.clusterSTchanID
        residuals = track.hit_residual
        cx = track.cluster_x
        cy = track.cluster_y
        cz = track.cluster_z
        for (i, id) in enumerate(ids):
            sector = get_sector(id)
            histosBySector[sector]['ResidualsByIOV-'+str(iov)].Fill(residuals[i])
            histosBySector[sector]['DeltaZByIOV-'+str(iov)].SetPoint(   histosBySector[sector]['DeltaZByIOV-'+str(iov)].GetN(),
                        float(tsz[i])-float(cz[i]), float(tsy[i]) )
    bar.finish()
    for sector in flatDetector:
        #avg, rms = [], []
        for iov in xrange(len(IOVs2012().intervals)):
            #avg.append( histosBySector[sector]['ResidualsByIOV-'+iov].GetMean() )
            #rms.append( histosBySector[sector]['ResidualsByIOV-'+iov].GetRMS() )
            avg = histosBySector[sector]['ResidualsByIOV-'+str(iov)].GetMean() 
            rms = histosBySector[sector]['ResidualsByIOV-'+str(iov)].GetRMS() 
            avge = histosBySector[sector]['ResidualsByIOV-'+str(iov)].GetMeanError() 
            rmse = histosBySector[sector]['ResidualsByIOV-'+str(iov)].GetRMSError() 
            #print iov, len(IOVs2012().intervals)
            histosBySector[sector]['AvgResidualByIOV'].SetBinContent(iov, avg)
            histosBySector[sector]['ResidualRMSByIOV'].SetBinContent(iov, rms)
            histosBySector[sector]['AvgResidualByIOV'].SetBinError(iov, avge)
            histosBySector[sector]['ResidualRMSByIOV'].SetBinError(iov, rmse)
            histosBySector[sector]['ResidualRMSByIOV'].GetXaxis().SetBinLabel(iov+1, IOVs2012().intervals[iov]['start'].replace('2012-','') + ' to ' 
                + IOVs2012().intervals[iov]['end'].replace('2012-',''))
            histosBySector[sector]['AvgResidualByIOV'].GetXaxis().SetBinLabel(iov+1, IOVs2012().intervals[iov]['start'].replace('2012-','') + ' to ' 
                + IOVs2012().intervals[iov]['end'].replace('2012-',''))
            if histosBySector[sector]['DeltaZByIOV-'+str(iov)].GetN() > 2:
                histosBySector[sector]['DeltaZByIOV-'+str(iov)].Fit('pol1', 'q')
                func = histosBySector[sector]['DeltaZByIOV-'+str(iov)].GetFunction("pol1")
                #print func.GetParameter(0), func.GetParameter(1), func.GetChisquare(), histosBySector[sector]['DeltaZByIOV-'+str(iov)].GetN(), sector, iov
                histosBySector[sector]['DeltaZSlopeByIOV'].SetBinContent(iov, func.GetParameter(1))
                histosBySector[sector]['DeltaZSlopeByIOV'].SetBinError(iov, func.GetParError(1))
            histosBySector[sector]['DeltaZSlopeByIOV'].GetXaxis().SetBinLabel(iov+1, IOVs2012().intervals[iov]['start'].replace('2012-','') + ' to ' 
                + IOVs2012().intervals[iov]['end'].replace('2012-',''))
    # Style up
    r.gStyle.SetPadBottomMargin(0.30)
    r.gROOT.ForceStyle()
    if save:
        outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/Histograms/ResidualsByIOV.root'%(tracker, datatype), 'recreate')
        for sector in flatDetector:
            for h in histosBySector[sector].keys():
                if ('Avg' in h) or ('RMS' in h) or ('Slope' in h):
                    histosBySector[sector][h].GetXaxis().LabelsOption('v')
                    histosBySector[sector][h].Write()
        outfile.Close()
    return histosBySector