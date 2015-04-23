from tools.common import *

def ClusterSize(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector, lookup):
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s/ClusterSizeBySector'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s/ClusterSizeBySector'%(tracker, datatype))
    hCSize = {}
    for sector in flatDetector:
        hCSize[sector] = r.TH1I(sector, sector+' Cluster Size', 4, 0.5, 4.5)
    # Loop on data
    ntracks = t.GetEntriesFast()
    bar = progressbar.ProgressBar(maxval=ntracks, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    for (itrack,track) in enumerate(t):
        bar.update(itrack+1)
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
            c1.SaveAs('../Out/'+shortFilename+'/%s/%s/ClusterSizeBySector/%s-%s.pdf'%(tracker, datatype, hCSize[sector].GetName(), segment))
            c1.Close()
    return hCSize