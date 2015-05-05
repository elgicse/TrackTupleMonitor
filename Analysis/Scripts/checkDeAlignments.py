# coding: utf-8
from tools.common import *
hm = 'TTaXRegionCModule0t'
from tools.Corners import retrieveSTPositionsPerIOV
positions = {}
tracker = 'TT'
listOfHM = listOfTTHalfModules()

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
        for iov in [0]:
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
            corners = findCorners(listx, listy, listz)
            module_dict[hm]['centre'][iov] = ( mean(centrx), mean(centry), mean(centrz) )
            module_dict[hm]['corners'][iov] = corners
            angles = findRotations(corners)
            module_dict[hm]['angles'][iov] = angles
    return module_dict


from tools.Corners import findCorners, findRotations, sortingKey, mean
'''
positions = retrieveSTPositionsPerIOV(0, positions, tracker, '../Options/STTrackTuple-BranchByTrack-HitsOnTrack-NTuples-DeAlignedRy.root')
mod_d = moduleCornersAndRotations(positions, listOfHM)
mod_d[hm]
positions = {}
positions = retrieveSTPositionsPerIOV(0, positions, tracker, '../Options/STTrackTuple-BranchByTrack-HitsOnTrack-NTuples-DeAlignedRx.root')
mod_d = moduleCornersAndRotations(positions, listOfHM)
mod_d[hm]
positions = {}
positions = retrieveSTPositionsPerIOV(0, positions, tracker, '../Options/STTrackTuple-BranchByTrack-HitsOnTrack-NTuples-DeAlignedRx.root')
mod_d = moduleCornersAndRotations(positions, listOfHM)
mod_d[hm]
positions = {}
positions = retrieveSTPositionsPerIOV(0, positions, tracker, '../Options/STTrackTuple-BranchByTrack-HitsOnTrack-NTuples-DeAlignedRz.root')
mod_d = moduleCornersAndRotations(positions, listOfHM)
mod_d[hm]
positions = {}
positions = retrieveSTPositionsPerIOV(0, positions, tracker, '../Options/STTrackTuple-BranchByTrack-HitsOnTrack-NTuples-DeAlignedRy.root')
mod_d = moduleCornersAndRotations(positions, listOfHM)
mod_d[hm]
positions = {}
positions = retrieveSTPositionsPerIOV(0, positions, tracker, '../Options/STTrackTuple-BranchByTrack-HitsOnTrack-NTuples-DeAlignedRx.root')
mod_d = moduleCornersAndRotations(positions, listOfHM)
mod_d[hm]
'''
read_Rx = {}
read_Rx = retrieveSTPositionsPerIOV(0, read_Rx, tracker, '../Options/STTrackTuple-BranchByTrack-HitsOnTrack-NTuples-DeAlignedRx.root')
ana_Rx = moduleCornersAndRotations(read_Rx, listOfHM)
read_Ry = {}
read_Ry = retrieveSTPositionsPerIOV(0, read_Ry, tracker, '../Options/STTrackTuple-BranchByTrack-HitsOnTrack-NTuples-DeAlignedRy.root')
ana_Ry = moduleCornersAndRotations(read_Ry, listOfHM)
read_Rz = {}
read_Rz = retrieveSTPositionsPerIOV(0, read_Rz, tracker, '../Options/STTrackTuple-BranchByTrack-HitsOnTrack-NTuples-DeAlignedRz.root')
ana_Rz = moduleCornersAndRotations(read_Rz, listOfHM)

print 'On Rx:'
print ana_Rx[hm]
print
print 'On Ry:'
print ana_Ry[hm]
print
print 'On Rz:'
print ana_Rz[hm]
print
