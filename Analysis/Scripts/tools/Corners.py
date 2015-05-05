from tools.common import *

'''PositionsFilenames = {
        0:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_0.root',
        1:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_1.root',
        2:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_2.root',
        3:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_3.root',
        4:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_4.root',
        5:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_5.root',
        6:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_6.root',
        7:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_7.root',
        8:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_8.root',
        9:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_9.root',
        10:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_10.root',
        11:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_11.root',
        12:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_12.root',
        13:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_13.root',
        14:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_14.root',
        15:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_15.root',
        16:'/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/IOV_16.root',
}'''

PositionsFilenames = {}
dataDir = '/afs/cern.ch/user/e/egraveri/cmtuser/STMonitoring/TrackTupleMonitor/Analysis/Rotations/Data/'
for i in xrange(17):
    PositionsFilenames[i] = dataDir+'IOV_%s.root'%i

def retrieveSTPositionsPerIOV(iov, positions, tracker, filename, verbose=False):
    print filename
    f = r.TFile(filename, 'read')
    t = f.Get(tracker+'HitEfficiencyTuple/SectorPositions')
    positions[iov] = {}
    for sector in t:
        #name = lookup[sector.sectorID]['uniqueSector'] #STNames_instance.uniqueSectorName(STChannelID(int(sector.sectorID)))
        name = STNames_instance.uniqueSectorName(STChannelID(int(sector.sectorID)))
        if verbose:
            print name
        # There are N sensors per sector
        positions[iov][ name ] = { 'centre': { 'x': list(sector.sensor_x),  'y': list(sector.sensor_y),  'z': list(sector.sensor_z) },
                                   'corner1':{ 'x': list(sector.corner1_x), 'y': list(sector.corner1_y), 'z': list(sector.corner1_z) },
                                   'corner2':{ 'x': list(sector.corner2_x), 'y': list(sector.corner2_y), 'z': list(sector.corner2_z) },
                                   'corner3':{ 'x': list(sector.corner3_x), 'y': list(sector.corner3_y), 'z': list(sector.corner3_z) },
                                   'corner4':{ 'x': list(sector.corner4_x), 'y': list(sector.corner4_y), 'z': list(sector.corner4_z) }   }
        #for (i,x) in enumerate(sector.sensor_x):
        #    if verbose:
        #        print i, x, sector.sensor_y[i], sector.sensor_z[i]
        #    positions[ name ][ i ] = ( x, sector.sensor_y[i], sector.sensor_z[i] )
    return positions

'''
def findCorners(xs, ys, zs):
    corners = {}
    # low x, low y
    x = min(xs)
    y = min(ys)
    z_idxs_x = [i for i,xi in enumerate(xs) if xi == x]
    z_idxs_y = [i for i,yi in enumerate(ys) if yi == y]
    z_idx = list( set(z_idxs_x).intersection(set(z_idxs_y)) )[0]
    z = zs[z_idx]
    corners['LowXLowY'] = {'x':x, 'y':y, 'z':z}
    # low x, large y
    x = min(xs)
    y = max(ys)
    z_idxs_x = [i for i,xi in enumerate(xs) if xi == x]
    z_idxs_y = [i for i,yi in enumerate(ys) if yi == y]
    z_idx = list( set(z_idxs_x).intersection(set(z_idxs_y)) )[0]
    z = zs[z_idx]
    corners['LowXLargeY'] = {'x':x, 'y':y, 'z':z}
    # large x, large y
    x = max(xs)
    y = max(ys)
    z_idxs_x = [i for i,xi in enumerate(xs) if xi == x]
    z_idxs_y = [i for i,yi in enumerate(ys) if yi == y]
    z_idx = list( set(z_idxs_x).intersection(set(z_idxs_y)) )[0]
    z = zs[z_idx]
    corners['LargeXLargeY'] = {'x':x, 'y':y, 'z':z}
    # large x, low y
    x = max(xs)
    y = min(ys)
    z_idxs_x = [i for i,xi in enumerate(xs) if xi == x]
    z_idxs_y = [i for i,yi in enumerate(ys) if yi == y]
    z_idx = list( set(z_idxs_x).intersection(set(z_idxs_y)) )[0]
    z = zs[z_idx]
    corners['LargeXLowY'] = {'x':x, 'y':y, 'z':z}
    return corners
'''

from operator import itemgetter

def mean(lst):
    return sum(lst)/len(lst)

def sortingKey(item, lst, what, (whatelse, where), reverse=False):
    """
    Sort by "what" if "whatelse" is in the right region
    """
    if where == 'Large':
        flag = not ( item[whatelse] > mean([point[whatelse] for point in lst]) )
    elif where == 'Low':
        flag = not ( item[whatelse] <= mean([point[whatelse] for point in lst]) )
    ordering = item[what]
    if reverse: 
        ordering *= (-1)
    return (flag, ordering)

def sortingKey2(item, points, corner):
    pass

def findCorners(xs, ys, zs):
    points = zip(xs, ys, zs)
    #print points
    #for p in points:
    #    print p
    x,y,z = 0,1,2
    corners = {}
    '''corners['LowXLowY'] = sorted( sorted(points, key=itemgetter(y)), key=itemgetter(x) )[0]
    corners['LargeXLowY'] = sorted( sorted(points, key=itemgetter(y)), key=itemgetter(x), reverse=True )[0]
    corners['LowXLargeY'] = sorted( sorted(points, key=itemgetter(y), reverse=True), key=itemgetter(x) )[0]
    corners['LargeXLargeY'] = sorted( sorted(points, key=itemgetter(y), reverse=True), key=itemgetter(x), reverse=True )[0]'''
    corners['LowXLowY'] = sorted( sorted(points, key=itemgetter(x)), 
                                    key=lambda item: sortingKey(item, points, y, (x,'Low')) )[0]
    corners['LargeXLowY'] = sorted( sorted(points, key=itemgetter(x), reverse=True), 
                                    key=lambda item: sortingKey(item, points, y, (x,'Large')) )[0]
    corners['LargeXLargeY'] = sorted( sorted(points, key=itemgetter(x), reverse=True), 
                                    key=lambda item: sortingKey(item, points, y, (x,'Large'), reverse=True) )[0]
    corners['LowXLargeY'] = sorted( sorted(points, key=itemgetter(x)), 
                                    key=lambda item: sortingKey(item, points, y, (x,'Low'), reverse=True) )[0]
    return corners

def findRotations(corners):
    #for key in corners:
    #    print key, corners[key]
    # Define midpoints of the sides
    A = ( r.TVector3(*corners['LargeXLowY'])   + r.TVector3(*corners['LowXLowY'])   ) * 0.5
    B = ( r.TVector3(*corners['LowXLargeY'])   + r.TVector3(*corners['LowXLowY'])   ) * 0.5
    C = ( r.TVector3(*corners['LargeXLargeY']) + r.TVector3(*corners['LowXLargeY']) ) * 0.5
    D = ( r.TVector3(*corners['LargeXLargeY']) + r.TVector3(*corners['LargeXLowY']) ) * 0.5
    #for p in (A,B,C,D):
    #    print p.X(), p.Y(), p.Z()
    # Define rotation angles
    Rx = r.TMath.ASin( (C.Z() - A.Z())/r.TMath.Abs(C.Y() - A.Y()) )
    Ry = r.TMath.ASin( (B.Z() - A.Z())/r.TMath.Abs(B.X() - A.X()) )
    Rz = r.TMath.ASin( (B.Y() - D.Y())/r.TMath.Abs(B.X() - D.X()) )
    return Rx, Ry, Rz

def moduleCornersAndRotations(sect_dict, listOfHM):
    module_dict = {}
    for hm in listOfHM:
        sectors, sectorNumbers = sectorsInHalfModule(hm)
        module_dict[hm] = {'centre':{}, 'corners':{}, 'angles':{}}
        '''module_dict[hm]['sectors'] = {}
        for sector in sectors:
            module_dict[hm]['sectors'][sector] = {}
            for iov in IOVs2012_instance.intervals:
                module_dict[hm]['sectors'][sector][iov] = sect_dict[iov][sector]'''
        for iov in IOVs2012_instance.intervals:
            listx, listy, listz = [], [], []
            centrx, centry, centrz = [], [], []
            for sector in sectors:
                centrx.extend( list(sect_dict[iov][sector]['centre']['x']) )
                centry.extend( list(sect_dict[iov][sector]['centre']['y']) )
                centrz.extend( list(sect_dict[iov][sector]['centre']['z']) )
                for i in range(1,5):
                    listx.extend(list( sect_dict[iov][sector]['corner%s'%i]['x'] ))
                    listy.extend(list( sect_dict[iov][sector]['corner%s'%i]['y'] ))
                    listz.extend(list( sect_dict[iov][sector]['corner%s'%i]['z'] ))
            #listx = sect_dict[iov][sector][]
            #x = min([module_dict[hm]['sectors'][sector][iov]['x'] for sector in sectors])
            #y = min([module_dict[hm]['sectors'][sector][iov]['y'] for sector in sectors])
            #cornerLowXLowY = { 'x': x,
            #                   'y': y,
            #                  'z': module_dict[hm]['sectors'][sector][iov]['z'][ module_dict[hm]['sectors'][sector][iov]['x'].index(  ) ]
            #                }
            corners = findCorners(listx, listy, listz)
            module_dict[hm]['centre'][iov] = ( mean(centrx), mean(centry), mean(centrz) )
            module_dict[hm]['corners'][iov] = corners
            angles = findRotations(corners)
            module_dict[hm]['angles'][iov] = angles
    return module_dict

def Corners(tracker, datatype, flatDetector, t, save, shortFilename, segment, detector, lookup):
    d = {}
    for iov in IOVs2012_instance.intervals:
        retrieveSTPositionsPerIOV(iov, d, tracker, PositionsFilenames[iov])#'../RootFiles/'+shortFilename+'.root')
    listOfHM = listOfTTHalfModules()

    mod_d = moduleCornersAndRotations(d, listOfHM)

    if save:
        pickle.dump(mod_d, open('../Pickle/Data_RotationsPerIOV.pkl', 'wb'))

    return mod_d