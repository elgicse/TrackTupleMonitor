from tools.common import *

def Outliers(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector, lookup):
    outliers = {'DeltaY': {}} # Add cluster size etc.
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
            mu = track.traj_mu
            for i in xrange(len(track.cluster_x)):
                delta_y = tsy[i]-cy[i]
                if abs(delta_y) > 0.1:
                    sector = get_sector(ids[i])
                    half_module = get_half_module(ids[i])
                    xclust = cx[i]
                    xtrack = tsx[i]
                    yclust = cy[i]
                    ytrack = tsy[i]
                    zclust = cz[i]
                    ztrack = tsz[i]
                    outliers['DeltaY'].setdefault(half_module, {})
                    outliers['DeltaY'][half_module].setdefault(sector, {'cx':[], 'tsx':[], 'cy':[], 'tsy':[], 'cz':[], 'tsz':[]})
                    outliers['DeltaY'][half_module][sector]['cx'].append(xclust)
                    outliers['DeltaY'][half_module][sector]['cy'].append(yclust)
                    outliers['DeltaY'][half_module][sector]['cz'].append(zclust)
                    outliers['DeltaY'][half_module][sector]['tsx'].append(xtrack)
                    outliers['DeltaY'][half_module][sector]['tsy'].append(ytrack)
                    outliers['DeltaY'][half_module][sector]['tsz'].append(ztrack)
    # spawn colors
    nHM = len(outliers['DeltaY'])
    colors = range(1,nHM+1)
    outliers['mgr_ClusterXY'] = r.TMultiGraph()
    outliers['mgr_TrackXY'] = r.TMultiGraph()
    for (i,hm) in enumerate(outliers['DeltaY']):
        if len(outliers['DeltaY'][hm])>1:
            print hm, ' has %s sectors with outliers in DeltaY'%len(outliers['DeltaY'][hm])
        cx, cy, cz, tsx, tsy, tsz = [], [], [], [], [], []
        for sector in outliers['DeltaY'][hm]:
            cx.extend(outliers['DeltaY'][hm][sector]['cx'])
            cy.extend(outliers['DeltaY'][hm][sector]['cy'])
            cz.extend(outliers['DeltaY'][hm][sector]['cz'])
            tsx.extend(outliers['DeltaY'][hm][sector]['tsx'])
            tsy.extend(outliers['DeltaY'][hm][sector]['tsy'])
            tsz.extend(outliers['DeltaY'][hm][sector]['tsz'])
        hnum = r.TH1I('nOutliersDeltaY_%s-%s'%(hm,segment), 'nOutliersDeltaY_%s-%s'%(hm,segment), 21, -0.5, 20.5)
        hnum.Fill(sum([len(outliers['DeltaY'][hm][sector]['tsx']) for sector in outliers['DeltaY'][hm]]))
        outliers['DeltaY'][hm]['nOutliers'] = hnum
        outliers['DeltaY'][hm]['ClusterXY'] = r.TGraph(len(cx), array('f',cx), array('f',cy))
        outliers['DeltaY'][hm]['TrackXY'] = r.TGraph(len(tsx), array('f',tsx), array('f',tsy))
        outliers['DeltaY'][hm]['ClusterZ'] = r.TH1F('CZForYOutliers_%s-%s'%(hm,segment),'CZForYOutliers_%s-%s'%(hm,segment),10,min(cz),max(cz))
        [ outliers['DeltaY'][hm]['ClusterZ'].Fill(z) for z in cz ]
        outliers['DeltaY'][hm]['ClusterX'] = r.TH1F('CXForYOutliers_%s-%s'%(hm,segment),'CXForYOutliers_%s-%s'%(hm,segment),10,min(cx),max(cx))
        [ outliers['DeltaY'][hm]['ClusterX'].Fill(x) for x in cx ]
        outliers['DeltaY'][hm]['ClusterY'] = r.TH1F('CYForYOutliers_%s-%s'%(hm,segment),'CYForYOutliers_%s-%s'%(hm,segment),10,min(cy),max(cy))
        [ outliers['DeltaY'][hm]['ClusterY'].Fill(y) for y in cy ]
        outliers['DeltaY'][hm]['TrackZ'] =  r.TH1F('TSZForYOutliers_%s-%s'%(hm,segment),'TSZForYOutliers_%s-%s'%(hm,segment),10,min(tsz),max(tsz))
        [ outliers['DeltaY'][hm]['TrackZ'].Fill(z) for z in tsz ]
        outliers['DeltaY'][hm]['TrackX'] =  r.TH1F('TSXForYOutliers_%s-%s'%(hm,segment),'TSXForYOutliers_%s-%s'%(hm,segment),10,min(tsx),max(tsx))
        [ outliers['DeltaY'][hm]['TrackX'].Fill(x) for x in tsx ]
        outliers['DeltaY'][hm]['TrackY'] =  r.TH1F('TSYForYOutliers_%s-%s'%(hm,segment),'TSYForYOutliers_%s-%s'%(hm,segment),10,min(tsy),max(tsy))
        [ outliers['DeltaY'][hm]['TrackY'].Fill(y) for y in tsy ]
        outliers['DeltaY'][hm]['ClusterXY'].SetMarkerColor(colors[i]), outliers['DeltaY'][hm]['ClusterXY'].SetTitle(hm)
        outliers['DeltaY'][hm]['TrackXY'].SetMarkerColor(colors[i]), outliers['DeltaY'][hm]['TrackXY'].SetTitle(hm)
        outliers['DeltaY'][hm]['ClusterZ'].SetMarkerColor(colors[i]), outliers['DeltaY'][hm]['ClusterZ'].SetTitle(hm)
        outliers['DeltaY'][hm]['TrackZ'].SetMarkerColor(colors[i]), outliers['DeltaY'][hm]['TrackZ'].SetTitle(hm)
        outliers['mgr_ClusterXY'].Add(outliers['DeltaY'][hm]['ClusterXY'])
        outliers['mgr_TrackXY'].Add(outliers['DeltaY'][hm]['TrackXY'])
    if save:
        if not os.path.exists('../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype)):
            os.system('mkdir ../Out/'+shortFilename+'/%s/%s/Histograms'%(tracker, datatype))
        foutliers = r.TFile('../Out/'+shortFilename+'/%s/%s/Histograms/DeltaY.root'%(tracker, datatype), 'recreate')
        for hm in outliers['DeltaY']:
            for hist in outliers['DeltaY'][hm].values():
                if isinstance(hist, r.TH1F) or isinstance(hist, r.TH1I):
                    hist.Write()
        foutliers.Close()
    return outliers