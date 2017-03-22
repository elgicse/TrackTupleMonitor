from tools.common import *

def RMSUnbiasedResidual(residual, err_measure, err_residual):
    return residual * math.sqrt(err_measure**2. / err_residual**2.)

def NormalSectorMonitoring(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector, lookup):
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
        histosBySector[sector] = {  'Residual':  [], 'UnbiasedResidual':  []  }
    # Loop on data
    ntracks = t.GetEntriesFast()
    bar = progressbar.ProgressBar(maxval=ntracks, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    for (itrack,track) in enumerate(t):
        bar.update(itrack+1)
        residuals = track.hit_residual
        err_measure = track.hit_errMeasure
        err_residual = track.hit_errResidual
        ids = track.clusterSTchanID
        for (i, id) in enumerate(ids):
            sector = get_sector(id)
            histosBySector[sector]['Residual'].append(residuals[i])
            histosBySector[sector]['UnbiasedResidual'].append(RMSUnbiasedResidual(residuals[i],err_measure[i],err_residual[i]))
    if save:
        outfile = r.TFile('../Out/'+shortFilename+'/%s/%s/Histograms/NormalSectorMonitoring.root'%(tracker, datatype), 'recreate')
        for sector in flatDetector:
            for gr in histosBySector[sector].keys():
                if len(histosBySector[sector][gr])>0: # skip empty modules
                    h = r.TH1F('%s_%s-%s'%(gr, sector, segment), '%s_%s-%s'%(gr, sector, segment), 100, min(histosBySector[sector][gr]), max(histosBySector[sector][gr]))
                    [ h.Fill(x) for x in histosBySector[sector][gr] ]
                    h.GetXaxis().SetTitle('Hit Residual [mm]')
                    h.GetXaxis().SetTitle('RMS-unbiased Hit Residual [mm]')
                    h.Write()
                    h.Delete()
        outfile.Close()
    return histosBySector