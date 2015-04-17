from tools.common import *

def MagField(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector):
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s/ResidualVSMomentum'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s/ResidualVSMomentum'%(tracker, datatype))
    hPositive, hNegative = {}, {}
    for sector in flatDetector:
        hPositive[sector] = r.TGraph(); hPositive[sector].SetName(sector+'-pos'); hPositive[sector].SetTitle(sector+' Residual VS Momentum (charge = +1)');
        hNegative[sector] = r.TGraph(); hNegative[sector].SetName(sector+'-neg'); hNegative[sector].SetTitle(sector+' Residual VS Momentum (charge = -1)');
    # Loop on data
    ntracks = t.GetEntriesFast()
    bar = progressbar.ProgressBar(maxval=ntracks, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    for (itrack,track) in enumerate(t):
        bar.update(itrack+1)
        if track.__getattr__('num'+tracker+'hits') > 0:
            ids = track.clusterSTchanID
            residuals = track.hit_residual
            if len(ids) != len(residuals):
                print "ERROR: number of entries mismatch"
                sys.exit(0)
            for (i, res) in enumerate(residuals):
                if track.charge == -1:
                    hNegative[get_sector(ids[i])].SetPoint( hNegative[get_sector(ids[i])].GetN(), float(track.p/1000.), float(res))
                else:
                    hPositive[get_sector(ids[i])].SetPoint( hPositive[get_sector(ids[i])].GetN(), float(track.p/1000.), float(res))
    for sector in flatDetector:
        hPositive[sector].GetXaxis().SetTitle('Track momentum [GeV]'); hPositive[sector].GetYaxis().SetTitle('Hit residuals [mm]')
        hNegative[sector].GetXaxis().SetTitle('Track momentum [GeV]'); hNegative[sector].GetYaxis().SetTitle('Hit residuals [mm]')
    if save:
        for collection in [hPositive, hNegative]:
            for gr in collection.keys():
                c1 = r.TCanvas(collection[gr].GetName(), collection[gr].GetTitle())
                collection[gr].Draw('ap'); c1.Modified(); c1.Update()
                label = r.TPaveText( 0.60 - r.gStyle.GetPadRightMargin(), 0.87 - r.gStyle.GetPadTopMargin(),
                                     0.95 - r.gStyle.GetPadRightMargin(), 0.95 - r.gStyle.GetPadTopMargin(), "BRNDC");
                label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
                label.SetTextFont(132); label.SetTextSize(0.06)
                label.AddText(gr); label.Draw('same'); c1.Modified(); c1.Update()
                c1.SaveAs('../Out/'+shortFilename+'/%s/%s/ResidualVSMomentum/%s-%s.pdf'%(tracker, datatype, collection[gr].GetName(), segment))
                c1.Close()
    return hPositive, hNegative