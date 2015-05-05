from tools.common import *
Delta_run = [ SplitIOVs_instance.intervals[i+1]['firstrun']-SplitIOVs_instance.intervals[i]['lastrun'] for i in xrange(len(SplitIOVs_instance.intervals)-1)]
for int in IOVs2012_instance.intervals:
    print int, IOVs2012_instance.intervals[int]['firstrun'], IOVs2012_instance.intervals[int]['lastrun']
f = r.TFile('../RootFiles/HitsOnTrack/all2012-muEstimate-Edges-closestState.root','read')
t = f.Get('TTHitEfficiencyTuple/TrackMonTuple')
badSplitIovList = [39,49,89,99,109,139,149]

runlist = []

for track in t:
    if GetSplitIOV(track) in badSplitIovList:
        runlist.append(run_number(track))
runlist = list(set(runlist))
lll = [ (IOVs2012_instance.GetInterval(run_n)[0], IOVs2012_instance.GetInterval(run_n), run_n) for run_n in runlist  ]
d = {}
for item in lll:
    d.setdefault(item[0], [])
    d[item[0]].append(item[-1])
res = {}
for i in d:
    res[i] = ( IOVs2012_instance.intervals[i],  d[i])

for item in res:
    print item, '\t', res[item][0], '\n\t\t', res[item][1]

# Program
detector = CreateDetectors.create_TT()
r.gROOT.SetBatch(r.kTRUE)
save = True
histosByHM = {}
rotations = {}
listOfHM = listOfTTHalfModules()
for hm in listOfHM:
    histosByHM[hm] = { 
        'AvgResidualByIOV': r.TH1F('AvgResidualByIOV_'+hm, 'AvgResidualByIOV_'+hm, len(runlist), 0, 1),
        'ResidualRMSByIOV': r.TH1F('ResidualRMSByIOV_'+hm, 'ResidualRMSByIOV_'+hm, len(runlist), 0, 1),
        'RxByIOV': r.TH1F('RxByIOV_'+hm, 'RxByIOV_'+hm, len(runlist), 0, 1)
    }
    for i,run in enumerate(runlist):
        histosByHM[hm]['ResidualsByIOV-'+str(i)] = r.TH1F(hm+'-ResidualsByIOV-'+str(i), hm+'-ResidualsByIOV-'+str(i), 100, 0., 0.06)
        histosByHM[hm]['HitZvsTrackYByIOV-'+str(i)] = r.TGraph()
        histosByHM[hm]['HitZvsTrackYByIOV-'+str(i)].SetTitle(hm+'-HitZvsTrackYByIOV-'+str(i))
        histosByHM[hm]['HitZvsTrackYByIOV-'+str(i)].SetName(hm+'-HitZvsTrackYByIOV-'+str(i))
# Loop on data
ntracks = t.GetEntriesFast()
bar = progressbar.ProgressBar(maxval=ntracks, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
for (itrack, track) in enumerate(t):
    bar.update(itrack+1)
    run = run_number(track)
    if not run in runlist:
        continue
    for (lindex, layer) in enumerate(detector.keys()):
        if (track.__getattr__(layer+'_nHits') != 1):
            continue
        tsx = track.trackState_x
        tsy = track.trackState_y
        tsz = track.trackState_z
        ids = track.clusterSTchanID
        residuals = track.hit_residual
        cx = track.cluster_x
        cy = track.cluster_y
        cz = track.cluster_z
        for (i, id) in enumerate(ids):
            if STNames_instance.uniqueLayerName(STChannelID(ids[i])) == layer:
                hm = get_half_module(id)
                histosByHM[hm]['ResidualsByIOV-'+str(runlist.index(run))].Fill(residuals[i])
                histosByHM[hm]['HitZvsTrackYByIOV-'+str(runlist.index(run))].SetPoint(   histosByHM[hm]['HitZvsTrackYByIOV-'+str(runlist.index(run))].GetN(),
                            float(cz[i]), float(tsy[i]) )
bar.finish()
# Analyse histos
shortFilename = 'all2012-muEstimate-Edges-closestState'
os.system('mkdir ../Out/'+shortFilename+'/%s/%s/PlotsByHalfModule_LastRuns'%('TT', 'HitsOnTrack'))
os.system('mkdir ../Out/'+shortFilename+'/%s/%s/Histograms_LastRuns'%('TT', 'HitsOnTrack'))
for hm in listOfHM:
    #avg, rms = [], []
    rotations[hm] = {}
    for run in xrange(len(runlist)):
        rotations[hm][run] = {}
        #avg.append( histosByHM[hm]['ResidualsByIOV-'+iov].GetMean() )
        #rms.append( histosByHM[hm]['ResidualsByIOV-'+iov].GetRMS() )
        avg = histosByHM[hm]['ResidualsByIOV-'+str(run)].GetMean()
        rms = histosByHM[hm]['ResidualsByIOV-'+str(run)].GetRMS() 
        avge = histosByHM[hm]['ResidualsByIOV-'+str(run)].GetMeanError() 
        rmse = histosByHM[hm]['ResidualsByIOV-'+str(run)].GetRMSError() 
        #print iov, len(IOVs2012().intervals)
        histosByHM[hm]['AvgResidualByIOV'].SetBinContent(run+1, avg)
        histosByHM[hm]['ResidualRMSByIOV'].SetBinContent(run+1, rms)
        histosByHM[hm]['AvgResidualByIOV'].SetBinError(run+1, avge)
        histosByHM[hm]['ResidualRMSByIOV'].SetBinError(run+1, rmse)
        histosByHM[hm]['ResidualRMSByIOV'].GetXaxis().SetBinLabel(run+1, str(runlist[run]))
        histosByHM[hm]['AvgResidualByIOV'].GetXaxis().SetBinLabel(run+1, str(runlist[run]))
        if histosByHM[hm]['HitZvsTrackYByIOV-'+str(run)].GetN() > 2:
            r.gStyle.SetOptFit(r.kTRUE)
            c1 = r.TCanvas(histosByHM[hm]['HitZvsTrackYByIOV-'+str(run)].GetName(), histosByHM[hm]['HitZvsTrackYByIOV-'+str(run)].GetTitle(), 1600, 1000) #debug
            histosByHM[hm]['HitZvsTrackYByIOV-'+str(run)].Draw('ap') #debug
            histosByHM[hm]['HitZvsTrackYByIOV-'+str(run)].Fit('pol1', 'q')
            func = histosByHM[hm]['HitZvsTrackYByIOV-'+str(run)].GetFunction("pol1")
            func.SetLineColor(r.kRed)
            label = r.TPaveText( 0.55 - r.gStyle.GetPadRightMargin(), 0.07 + r.gStyle.GetPadBottomMargin(),
                                 0.95 - r.gStyle.GetPadRightMargin(), 0.15 + r.gStyle.GetPadBottomMargin(), "BRNDC");
            label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
            label.SetTextFont(132); label.SetTextSize(0.06)
            label.AddText(hm+' '+str(runlist[run])); label.Draw('same'); c1.Modified(); c1.Update()
            c1.Modified(); c1.Update() #debug
            if save:
                c1.SaveAs('../Out/'+shortFilename+'/%s/%s/PlotsByHalfModule_LastRuns/%s-HitZvsTrackY-run%s.png'%('TT', 'HitsOnTrack', hm, runlist[run]))
            c1.Close() #debug
            #print func.GetParameter(0), func.GetParameter(1), func.GetChisquare(), histosByHM[hm]['HitZvsTrackYByIOV-'+str(iov)].GetN(), hm, iov
            histosByHM[hm]['RxByIOV'].SetBinContent(run+1, func.GetParameter(1) ) #fitToTheta( func.GetParameter(1) ))
            histosByHM[hm]['RxByIOV'].SetBinError(run+1, func.GetParError(1) ) #fitToTheta( func.GetParError(1) ))
            rotations[hm][run]['m'] = func.GetParameter(1)
            rotations[hm][run]['m_err'] = func.GetParError(1)
            rotations[hm][run]['q'] = func.GetParameter(0)
            rotations[hm][run]['q_err'] = func.GetParError(0)
        histosByHM[hm]['RxByIOV'].GetXaxis().SetBinLabel(run+1, str(runlist[run]))
# Style up
r.gStyle.SetPadBottomMargin(0.30)
r.gROOT.ForceStyle()
if save:
    pickle.dump( rotations, open('rotationsByRun_lastRuns.pkl', 'wb') )
    outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/Histograms_LastRuns/RotationsByRun-LastRuns-%s.root'%('TT', 'HitsOnTrack', 'all2012'), 'recreate')
    for hm in listOfHM:
        for h in histosByHM[hm].keys():
            if ('Avg' in h) or ('RMS' in h) or ('Rx' in h):
                histosByHM[hm][h].GetXaxis().LabelsOption('v')
                histosByHM[hm][h].Write()
    outfile.Close()