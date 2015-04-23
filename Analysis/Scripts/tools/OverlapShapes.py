from tools.common import *

def findTwoHitsIndices(track, (hm1, hm2), table):
    ids = track.clusterSTchanID
    index1, index2 = None, None
    if not (len(ids)<2):
        for (i, id) in enumerate(ids):
            test_hm = table[id]['hm']#get_half_module(id)
            if test_hm == hm1:
                index1 = i
            if test_hm == hm2:
                index2 = i
        if (index1!=None) and (index2!=None) and not (index1==index2):
            return index1, index2
        #else:
        #    print get_half_module(ids[index1]), get_half_module(ids[index2])
    return False



def OverlapShapes(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector, lookup):
    if tracker == 'IT':
        print 'Sorry I cannot do this for the IT, yet...'
        sys.exit(0)
    if not os.path.exists('../Out/'+shortFilename+'/%s/%s/OverlapsByHalfModule'%(tracker, datatype)):
        os.system('mkdir ../Out/'+shortFilename+'/%s/%s/OverlapsByHalfModule'%(tracker, datatype))
    listOfHM = listOfTTHalfModules()
    listOfPairs = listOfOverlappingTTPairs()
    hOverlapsByHM = {}
    for hm in listOfHM:
        hOverlapsByHM[hm] = {  'HitXVSTrackY':     r.TGraph(),
                               'HitDeltaXVSTrackY':r.TGraph(),
                               'HitDeltaYVSTrackY':r.TGraph(),
                               'HitDeltaZVSTrackY':r.TGraph()   }
    # Loop on data
    ntracks = t.GetEntriesFast()
    bar = progressbar.ProgressBar(maxval=ntracks*len(listOfPairs), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    for (itrack,track) in enumerate(t):
        for (lindex, layer) in enumerate(detector.keys()):
            if (track.__getattr__(layer+'_nHits') <= 1):
                continue
            for pair in listOfPairs:
                bar.update(itrack*len(listOfPairs)+1)
                idx = findTwoHitsIndices(track, pair, lookup)
                if not idx:
                    continue
                else:
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
                    hm1, hm2 = pair# = get_half_module(ids[idx[j]])
                    hOverlapsByHM[hm1]['HitXVSTrackY'].SetPoint(     hOverlapsByHM[hm1]['HitXVSTrackY'].GetN()  , float(cx[idx[0]]), float(tsy[idx[0]]) )
                    hOverlapsByHM[hm1]['HitDeltaXVSTrackY'].SetPoint(   hOverlapsByHM[hm1]['HitDeltaXVSTrackY'].GetN()  , float(cx[idx[0]])-float(cx[idx[1]]),
                                                                                                                                   float(tsy[idx[0]]) )
                    hOverlapsByHM[hm1]['HitDeltaYVSTrackY'].SetPoint(   hOverlapsByHM[hm1]['HitDeltaYVSTrackY'].GetN()  , float(cy[idx[0]])-float(cy[idx[1]]),
                                                                                                                                   float(tsy[idx[0]]) )
                    hOverlapsByHM[hm1]['HitDeltaZVSTrackY'].SetPoint(   hOverlapsByHM[hm1]['HitDeltaZVSTrackY'].GetN()  , float(cz[idx[0]])-float(cz[idx[1]]),
                                                                                                                                           float(tsy[idx[0]]) )
                    hOverlapsByHM[hm2]['HitXVSTrackY'].SetPoint(     hOverlapsByHM[hm2]['HitXVSTrackY'].GetN()  , float(cx[idx[1]]), float(tsy[idx[1]]) )
                    hOverlapsByHM[hm2]['HitDeltaXVSTrackY'].SetPoint(   hOverlapsByHM[hm2]['HitDeltaXVSTrackY'].GetN()  , float(cx[idx[1]])-float(cx[idx[0]]),
                                                                                                                                   float(tsy[idx[1]]) )
                    hOverlapsByHM[hm2]['HitDeltaYVSTrackY'].SetPoint(   hOverlapsByHM[hm2]['HitDeltaYVSTrackY'].GetN()  , float(cy[idx[1]])-float(cy[idx[0]]),
                                                                                                                                   float(tsy[idx[1]]) )
                    hOverlapsByHM[hm2]['HitDeltaZVSTrackY'].SetPoint(   hOverlapsByHM[hm2]['HitDeltaZVSTrackY'].GetN()  , float(cz[idx[1]])-float(cz[idx[0]]),
                                                                                                                                           float(tsy[idx[1]]) )
    for hm in listOfHM:
        for gr in hOverlapsByHM[hm].keys():
            hOverlapsByHM[hm][gr].SetName(hm+'_'+gr); hOverlapsByHM[hm][gr].SetTitle(hm+' '+gr)
            hOverlapsByHM[hm][gr].GetYaxis().SetTitle('Track Y extrapolation [mm]')
        hOverlapsByHM[hm]['HitXVSTrackY'].GetXaxis().SetTitle('Cluster X position [mm]')
        hOverlapsByHM[hm]['HitDeltaXVSTrackY'].GetXaxis().SetTitle('#Delta x between the two clusters [mm]')
        hOverlapsByHM[hm]['HitDeltaYVSTrackY'].GetXaxis().SetTitle('#Delta y between the two clusters [mm]')
        hOverlapsByHM[hm]['HitDeltaZVSTrackY'].GetXaxis().SetTitle('#Delta z between the two clusters [mm]')
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
    return hOverlapsByHM