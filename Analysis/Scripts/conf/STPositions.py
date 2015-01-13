#!/usr/bin/env python
"""
STPositions.py: retrieve TT and IT sector positions (previously saved in an ntuple).
"""

__author__  = "Elena Graverini"
__email__   = "elena.graverini@cern.ch"
__version__ = "1.0"
__date__    = "09/01/2015"


import sys, os
import pickle
import ROOT as r
from STChannelID import *
from TTModules import *

def retrieveSTPositions(tracker, filename, verbose=False):
    f = r.TFile(filename, 'read')
    t = f.Get(tracker+'HitEfficiencyTuple/SectorPositions')
    positions = {}
    if verbose:
        for sector in t:
            print STNames().uniqueSectorName(STChannelID(int(sector.sectorID)))
            for (i,x) in enumerate(sector.sensor_x):
                print i, x, sector.sensor_y[i], sector.sensor_z[i]
    for sector in t:
        name = STNames().uniqueSectorName(STChannelID(int(sector.sectorID)))
        positions[ name ] = {}
        xm, ym, zm = 0., 0., 0.
        for (i,x) in enumerate(sector.sensor_x):
            positions[ name ][ i ] = ( x, sector.sensor_y[i], sector.sensor_z[i] )
            xm += x
            ym += sector.sensor_y[i]
            zm += sector.sensor_z[i]
        positions[ name ][ 'average' ] = ( xm/len(sector.sensor_x), ym/len(sector.sensor_x), zm/len(sector.sensor_x) )
    return positions

def savePositionsToPickle(tracker, filename, verbose=False):
    positions = retrieveSTPositions(tracker, filename, verbose)
    filename = filename.split('/')[-1]
    path = os.path.abspath(__file__).split("Scripts")[0] + "Pickle/"
    output = open(path+filename.replace('.root','-%spositions.pkl'%tracker), 'wb')
    pickle.dump(positions, output)
    output.close()

def loadPositionsFromPickle(picklefile):
    f = open(picklefile)
    positions = pickle.load(f)
    f.close()
    return positions

def TTHalfModuleAvgPosition(halfModuleId, positions):
    uLayer, region, moduleNum, position = locateTTHalfModule(halfModuleId)
    index = 0
    if 'b' in position:
        index = 1
    sectors = TTModulesMap().dictOfHalfModules[uLayer]['Region'+region][moduleNum][index].sectors
    xm, ym, zm = 0., 0., 0.
    for uName in sectors:
        xm += positions[uName]['average'][0]
        ym += positions[uName]['average'][1]
        zm += positions[uName]['average'][2]
    return ( xm/len(sectors), ym/len(sectors), zm/len(sectors) )