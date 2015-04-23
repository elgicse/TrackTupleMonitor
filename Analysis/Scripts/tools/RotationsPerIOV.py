from tools.common import *
import pickle

def fitToTheta(m):
    return (math.pi/2.) - math.atan(m)

def RotationsPerIOV(tracker, datatype, listOfHM, t, save, shortFilename, segment, detector):
    if tracker == 'IT':
        print 'Sorry I cannot do this for the IT, yet...'
        sys.exit(0)
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype))
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s/PlotsByHalfModule'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s/PlotsByHalfModule'%(tracker, datatype))
    #
    # Book Histograms
    histosByHM = {}
    rotations = {}
    listOfHM = listOfTTHalfModules()
    for hm in listOfHM:
        histosByHM[hm] = { 
            #'AvgResidualByIOV': r.TH2F(hm+'-AvgResidualByIOV', hm+'-AvgResidualByIOV', 17, 0, 17, 100, 0., 0.06),
            #'ResidualRMSByIOV': r.TH2F(hm+'-ResidualRMSByIOV', hm+'-ResidualRMSByIOV', 17, 0, 17, 100, 0., 0.06)
            'AvgResidualByIOV': r.TH1F('AvgResidualByIOV_'+hm, 'AvgResidualByIOV_'+hm, len(IOVs2012().intervals), 0, 1),
            'ResidualRMSByIOV': r.TH1F('ResidualRMSByIOV_'+hm, 'ResidualRMSByIOV_'+hm, len(IOVs2012().intervals), 0, 1),
            'RxByIOV': r.TH1F('RxByIOV_'+hm, 'RxByIOV_'+hm, len(IOVs2012().intervals), 0, 1)
        }
        for i in IOVs2012().intervals:
            histosByHM[hm]['ResidualsByIOV-'+str(i)] = r.TH1F(hm+'-ResidualsByIOV-'+str(i), hm+'-ResidualsByIOV-'+str(i), 100, 0., 0.06)
            histosByHM[hm]['HitZvsTrackYByIOV-'+str(i)] = r.TGraph()
            histosByHM[hm]['HitZvsTrackYByIOV-'+str(i)].SetTitle(hm+'-HitZvsTrackYByIOV-'+str(i))
            histosByHM[hm]['HitZvsTrackYByIOV-'+str(i)].SetName(hm+'-HitZvsTrackYByIOV-'+str(i))
    # Loop on data
    ntracks = t.GetEntriesFast()
    bar = progressbar.ProgressBar(maxval=ntracks, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    for (itrack, track) in enumerate(t):
        bar.update(itrack+1)
        for (lindex, layer) in enumerate(detector.keys()):
            if (track.__getattr__(layer+'_nHits') != 1):
                continue
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
                if STNames().uniqueLayerName(STChannelID(ids[i])) == layer:
                    hm = get_half_module(id)
                    histosByHM[hm]['ResidualsByIOV-'+str(iov)].Fill(residuals[i])
                    histosByHM[hm]['HitZvsTrackYByIOV-'+str(iov)].SetPoint(   histosByHM[hm]['HitZvsTrackYByIOV-'+str(iov)].GetN(),
                                float(cz[i]), float(tsy[i]) )
    bar.finish()
    for hm in listOfHM:
        #avg, rms = [], []
        rotations[hm] = {}
        for iov in xrange(len(IOVs2012().intervals)):
            rotations[hm][iov] = {}
            #avg.append( histosByHM[hm]['ResidualsByIOV-'+iov].GetMean() )
            #rms.append( histosByHM[hm]['ResidualsByIOV-'+iov].GetRMS() )
            avg = histosByHM[hm]['ResidualsByIOV-'+str(iov)].GetMean() 
            rms = histosByHM[hm]['ResidualsByIOV-'+str(iov)].GetRMS() 
            avge = histosByHM[hm]['ResidualsByIOV-'+str(iov)].GetMeanError() 
            rmse = histosByHM[hm]['ResidualsByIOV-'+str(iov)].GetRMSError() 
            #print iov, len(IOVs2012().intervals)
            histosByHM[hm]['AvgResidualByIOV'].SetBinContent(iov, avg)
            histosByHM[hm]['ResidualRMSByIOV'].SetBinContent(iov, rms)
            histosByHM[hm]['AvgResidualByIOV'].SetBinError(iov, avge)
            histosByHM[hm]['ResidualRMSByIOV'].SetBinError(iov, rmse)
            histosByHM[hm]['ResidualRMSByIOV'].GetXaxis().SetBinLabel(iov+1, IOVs2012().intervals[iov]['start'].replace('2012-','') + ' to ' 
                + IOVs2012().intervals[iov]['end'].replace('2012-',''))
            histosByHM[hm]['AvgResidualByIOV'].GetXaxis().SetBinLabel(iov+1, IOVs2012().intervals[iov]['start'].replace('2012-','') + ' to ' 
                + IOVs2012().intervals[iov]['end'].replace('2012-',''))
            if histosByHM[hm]['HitZvsTrackYByIOV-'+str(iov)].GetN() > 2:
                r.gStyle.SetOptFit(r.kTRUE)
                c1 = r.TCanvas(histosByHM[hm]['HitZvsTrackYByIOV-'+str(iov)].GetName(), histosByHM[hm]['HitZvsTrackYByIOV-'+str(iov)].GetTitle(), 1600, 1000) #debug
                histosByHM[hm]['HitZvsTrackYByIOV-'+str(iov)].Draw('ap') #debug
                histosByHM[hm]['HitZvsTrackYByIOV-'+str(iov)].Fit('pol1', 'q')
                func = histosByHM[hm]['HitZvsTrackYByIOV-'+str(iov)].GetFunction("pol1")
                func.SetLineColor(r.kRed)
                label = r.TPaveText( 0.55 - r.gStyle.GetPadRightMargin(), 0.07 + r.gStyle.GetPadBottomMargin(),
                                     0.95 - r.gStyle.GetPadRightMargin(), 0.15 + r.gStyle.GetPadBottomMargin(), "BRNDC");
                label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
                label.SetTextFont(132); label.SetTextSize(0.06)
                label.AddText(hm+' '+str(iov)); label.Draw('same'); c1.Modified(); c1.Update()
                c1.Modified(); c1.Update() #debug
                if save:
                    c1.SaveAs('../Out/'+shortFilename+'/%s/%s/PlotsByHalfModule/%s-HitZvsTrackY-IOV%s.png'%(tracker, datatype, hm, iov))
                c1.Close() #debug
                #print func.GetParameter(0), func.GetParameter(1), func.GetChisquare(), histosByHM[hm]['HitZvsTrackYByIOV-'+str(iov)].GetN(), hm, iov
                histosByHM[hm]['RxByIOV'].SetBinContent(iov, func.GetParameter(1) ) #fitToTheta( func.GetParameter(1) ))
                histosByHM[hm]['RxByIOV'].SetBinError(iov, func.GetParError(1) ) #fitToTheta( func.GetParError(1) ))
                rotations[hm][iov]['m'] = func.GetParameter(1)
                rotations[hm][iov]['m_err'] = func.GetParError(1)
                rotations[hm][iov]['q'] = func.GetParameter(0)
                rotations[hm][iov]['q_err'] = func.GetParError(0)
            histosByHM[hm]['RxByIOV'].GetXaxis().SetBinLabel(iov+1, IOVs2012().intervals[iov]['start'].replace('2012-','') + ' to ' 
                + IOVs2012().intervals[iov]['end'].replace('2012-',''))
    # Style up
    r.gStyle.SetPadBottomMargin(0.30)
    r.gROOT.ForceStyle()
    if save:
        pickle.dump( rotations, open('rotationsByIOV.pkl', 'wb') )
        outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/Histograms/RotationsByIOV-%s.root'%(tracker, datatype, segment), 'recreate')
        for hm in listOfHM:
            for h in histosByHM[hm].keys():
                if ('Avg' in h) or ('RMS' in h) or ('Rx' in h):
                    histosByHM[hm][h].GetXaxis().LabelsOption('v')
                    histosByHM[hm][h].Write()
        outfile.Close()
    return histosByHM