#!/usr/bin/env python
"""
STChannelID.py: retrieve ID and name of layers, sectors, etc. from an LHCb::STChannelID integer.

Sample usage:
In [1]: id = STChannelID(10815631)
In [2]: STNames().uniqueSectorName(id)
Out[2]: 'IT1ASideX1Sector2'
"""
__author__  = "Elena Graverini"
__email__   = "elena.graverini@cern.ch"
__version__ = "1.0"
__date__    = "03/12/2014"


class STChannelID():
    """
    STChannelID: retrieve detector type, station, region, layer, sector
    and strip from an LHCb::STChannelID integer.
    """
    def __init__(self, m_channelID):
        self.channelID           = long(m_channelID)
        self.stripBits           = 0
        self.sectorBits          = 10
        self.detRegionBits       = 15
        self.layerBits           = 18
        self.stationBits         = 21
        self.typeBits            = 23   
        self.stripMask           = 0x3ffL
        self.sectorMask          = 0x7c00L
        self.detRegionMask       = 0x38000L
        self.layerMask           = 0x1c0000L
        self.stationMask         = 0x600000L
        self.typeMask            = 0x1800000L
        self.typeTT              = 0
        self.typeIT              = 1
        self.uniqueLayerMask     = self.layerMask + self.stationMask
        self.uniqueDetRegionMask = self.detRegionMask + self.layerMask + self.stationMask
        self.uniqueSectorMask    = self.sectorMask + self.detRegionMask + self.layerMask + self.stationMask
    def type(self):
        return ((self.channelID & self.typeMask) >> self.typeBits)
    def isTT(self):
        return (self.type() == self.typeTT)
    def isIT(self):
        return (self.type() == self.typeIT)
    def station(self):
        return ((self.channelID & self.stationMask) >> self.stationBits)
    def detRegion(self):
        return ((self.channelID & self.detRegionMask) >> self.detRegionBits)
    def uniqueDetRegion(self):
        return ((self.channelID & self.uniqueDetRegionMask) >> self.detRegionBits)
    def layer(self):
        return ((self.channelID & self.layerMask) >> self.layerBits)
    def uniqueLayer(self):
        return ((self.channelID & self.uniqueLayerMask) >> self.layerBits)
    def sector(self):
        return ((self.channelID & self.sectorMask) >> self.sectorBits)
    def uniqueSector(self):
        return ((self.channelID & self.uniqueSectorMask) >> self.sectorBits)
    def strip(self):
        return ((self.channelID & self.stripMask) >> self.stripBits)


class STNames():
    """
    STNames: retrieve detector name, station name, region name,
    layer name and sector name from an STChannelID object.
    """
    def __init__(self):
        self.TTstations = ["a", "b"]
        self.TTlayers = [["X", "U"], ["V", "X"]]
        self.TTuniqueLayers = []
        for (ind,s) in enumerate(self.TTstations):
            for l in self.TTlayers[ind]:
                self.TTuniqueLayers.append('TT'+s+l)
        self.TTregions = ["A", "B", "C"]
        self.ITlayers = ["X1", "U", "V", "X2"]
        self.ITboxes = ["CSide", "ASide", "Bottom", "Top"]

    def detectorName(self, id):
        if id.isTT():
            return "TT"
        else:
            return "IT"

    def stationName(self, id):
        if id.isTT():
            return self.TTstations[id.station()-1]
        else:
            return str(id.station())

    def regionName(self, id):
        if id.isTT():
            return "Region" + self.TTregions[id.detRegion()-1]
        else:
            return self.ITboxes[id.detRegion()-1]

    def layerName(self, id):
        if id.isTT():
            return self.TTlayers[id.station()-1][id.layer()-1]
        else:
            return self.ITlayers[id.layer()-1]

    def uniqueLayerName(self, id):
        if id.isTT():
            name = (  self.detectorName(id)
                    + self.stationName(id)
                    + self.layerName(id)  )
        else:
            name = (  self.detectorName(id)
                    + self.stationName(id)
                    + self.regionName(id)
                    + self.layerName(id)  )
        return name

    def sectorName(self, id):
        return "Sector" + str(id.sector())

    def uniqueSectorName(self, id):
        if id.isTT():
            name = (  self.uniqueLayerName(id)
                    + self.regionName(id)
                    + self.sectorName(id)  )
        else:
            name = (  self.uniqueLayerName(id)
                    + self.sectorName(id)  )
        return name

    def locateTTSector(self, uSectorName):
        uLayer = uSectorName.split('Region')[0]
        region, sector = uSectorName.split('Region')[1].split('Sector')
        return uLayer, region, int(sector)