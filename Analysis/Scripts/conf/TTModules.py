#!/usr/bin/env python
"""
TTModules.py: retrieve TT module or half module from an LHCb::STChannelID integer or from a uniqueSectorName.

Modules are numbered per unique layer and region, starting from 0 at the largest x (rightest).
"""

__author__  = "Elena Graverini"
__email__   = "elena.graverini@cern.ch"
__version__ = "1.0"
__date__    = "18/12/2014"


from STChannelID import *



class TTModulesMap():
    def __init__(self):
        self.numberOfModules = {   'TTaX': { 'RegionA': 6, 'RegionB': 3, 'RegionC': 6 },
                                   'TTaU': { 'RegionA': 6, 'RegionB': 3, 'RegionC': 6 },
                                   'TTbV': { 'RegionA': 6, 'RegionB': 5, 'RegionC': 6 },
                                   'TTbX': { 'RegionA': 6, 'RegionB': 5, 'RegionC': 6 }   }
        self.dictOfModules = {}
        for uniqueLayer in STNames().TTuniqueLayers:
            self.dictOfModules[uniqueLayer] = {}
            for region in STNames().TTregions:
                self.dictOfModules[uniqueLayer]['Region'+region] = []
                nModules = self.numberOfModules[uniqueLayer]['Region'+region]
                for i in range(nModules):
                    nSectors = 4
                    if 'B' in region:
                        nSectors = 3
                    if ('TTb' in uniqueLayer) and ( (i==0) or (i==nModules-1) ):
                        nSectors = 4
                    id = uniqueLayer+'Region'+region+'Module'+str(i)
                    self.dictOfModules[uniqueLayer]['Region'+region].append( TTModule( id, nSectors, True, uniqueLayer, 'Region'+region ) )
    #def find(inputData):
    #    if type(inputData) == str:
    #        return self.findByUniqueSector(inputData)
    #    elif 'STChannelID' in str(inputData.__class__):
    #        return self.findBySTChannelID(inputData)
    #    elif type(inputData) == int or type(inputData) == long:
    #        return self.findByChannelID(inputData)
    #    else:
    #        print 'TTModulesMap ERROR: could not understand input!'
    #        return False
    def findModule(self, id):
        ul = STNames().uniqueLayerName(id)
        reg = STNames().regionName(id)
        sector = int(id.sector())
        if sector == 0:
            print 'TTModulesMap ERROR: sector numbering starts from 0!!'
            sys.exit(0)
        if (reg != 'RegionB'):
            iModule = (sector-1)/4
        elif (reg == 'RegionB') and ('TTb' in ul):
            if sector<5:
                iModule = (sector-1)/4#%4
            if sector>22:
                iModule = 4
            if 5<=sector<=22:
                iModule = (sector-1-4)/6+1
        elif (reg == 'RegionB') and ('TTa' in ul):
            iModule = (sector-1)/6#%6
        #print iModule, sector, ul, reg
        return self.dictOfModules[ul][reg][iModule]
    def findHalfModule(self, id):
        module = self.findModule(id)
        sector = int(id.sector())
        if 'B'in STNames().regionName(id) and 'TTb' in STNames().uniqueLayerName(id):
            if 4<id.sector()<23:
                if (sector+1)%6 >= 3:
                    return module.topHalf
                else:
                    return module.bottomHalf
            elif id.sector()<=4:
                if id.sector() in [3,4]:
                    return module.topHalf
                else:
                    return module.bottomHalf
            elif id.sector()>=23:
                if id.sector() in [25,26]:
                    return module.topHalf
                else:
                    return module.bottomHalf    
        if (sector-1)%4 > 2:
            return module.topHalf
        else:
            return module.bottomHalf



class TTModule():
    def __init__(self, id, nSectors=4, parent=True, uniqueLayer='TTaX', region='RegionB', position='Top'):
        self.id          = str(id)
        self.nSectors    = nSectors
        self.parent      = parent
        self.uniqueLayer = uniqueLayer
        self.region      = region
        self.position    = position
        if parent:
            self.topHalf    = TTModule(id=self.id+'t', nSectors=self.nSectors/2, parent=False, uniqueLayer=self.uniqueLayer, region=self.region, position='Top')
            self.bottomHalf = TTModule(id=self.id+'b', nSectors=self.nSectors/2, parent=False, uniqueLayer=self.uniqueLayer, region=self.region, position='Bottom')
            self.position   = None


if __name__ == '__main__':
    import ROOT as r
    f = r.TFile('../../RootFiles/EveryHit/runs131973-133785-end2012.root','read')
    t = f.Get('TTHitEfficiencyTuple/TrackMonTuple')
    for (i, track) in enumerate(t):
        ids = track.clusterSTchanID
        chids = [long(id) for id in ids]
        if len(chids)>=4:
            id = STChannelID(chids[3])
            if not id.isTT():
                print 'Not TT.'
                sys.exit(0)
            if 'TTb' in STNames().uniqueLayerName(id) and 'B' in STNames().regionName(id):
                print id.sector(), STNames().uniqueSectorName(id), '\t', TTModulesMap().findHalfModule(id).id
