import sys, os
import math
#from fish import ProgressFish
import progressbar
import ROOT as r
from array import array
from conf import CreateDetectors
from conf.STChannelID import *
from conf.TTModules import *

cSaver = []
r.gROOT.ProcessLine('.x tools/lhcbStyle.C')

# Graph colors
gCol = [7,8,4,6,1,2,5]#[r.kBlack, r.kRed, r.kGreen, r.kBlue, r.kYellow, r.kMagenta, r.kCyan, r.kViolet, r.kOrange]
#//int colors[10] = {0,11,5,7,3,6,2,4,12,1};
#// int colors[10] = {0,5,11,7,3,6,2,12,4,1};
#int colors[10] = {0,0,5,7,3,6,2,4,1,1};
#lhcbStyle->SetPalette(10,colors);

class IOVs2012():
    def __init__(self):
        self.intervals = {
             0 : {'start':'2012-04-01', 'end':'2012-04-17', 'firstrun':111183, 'lastrun':112916},
             1 : {'start':'2012-04-17', 'end':'2012-05-01', 'firstrun':113013, 'lastrun':113146},
             2 : {'start':'2012-05-01', 'end':'2012-05-12', 'firstrun':114205, 'lastrun':114287},
             3 : {'start':'2012-05-02', 'end':'2012-05-16', 'firstrun':114316, 'lastrun':115464},
             4 : {'start':'2012-05-16', 'end':'2012-05-31', 'firstrun':115518, 'lastrun':117103},
             5 : {'start':'2012-05-31', 'end':'2012-06-11', 'firstrun':117192, 'lastrun':118286},
             6 : {'start':'2012-06-11', 'end':'2012-07-02', 'firstrun':118326, 'lastrun':118880},
             7 : {'start':'2012-07-02', 'end':'2012-07-20', 'firstrun':119956, 'lastrun':122520},
             8 : {'start':'2012-07-20', 'end':'2012-07-25', 'firstrun':122540, 'lastrun':123803},
             9 : {'start':'2012-07-25', 'end':'2012-08-10', 'firstrun':123910, 'lastrun':125115},
            10 : {'start':'2012-08-10', 'end':'2012-08-28', 'firstrun':125566, 'lastrun':126680},
            11 : {'start':'2012-08-28', 'end':'2012-09-15', 'firstrun':126824, 'lastrun':128268},
            12 : {'start':'2012-09-15', 'end':'2012-10-12', 'firstrun':128411, 'lastrun':129978},
            13 : {'start':'2012-10-12', 'end':'2012-10-24', 'firstrun':130316, 'lastrun':130861},
            14 : {'start':'2012-10-24', 'end':'2012-11-08', 'firstrun':130911, 'lastrun':131940},
            15 : {'start':'2012-11-08', 'end':'2012-12-03', 'firstrun':131973, 'lastrun':133587},
            16 : {'start':'2012-12-03', 'end':'2012-12-31', 'firstrun':133624, 'lastrun':133785}
        }
    def GetInterval(self,runNumber):
        for i in self.intervals:
            if self.intervals[i]['firstrun'] <= runNumber <= self.intervals[i]['lastrun']:
                return i, self.intervals[i]
        #print 'Could not find IOV for run '+str(runNumber)
        #print 'EXITING'
        # DIRTY trick for MC!!
        return 0, {'start':'MC', 'end':'MC', 'firstrun':0, 'lastrun':99999}
        sys.exit()


class InMoreLayers(Exception): pass

def run_number(event):
    return int(event.RunNumber)

def GetIOV(event):
    n = run_number(event)
    return IOVs2012().GetInterval(n)[0]

def get_sector(chanID):
    return STNames().uniqueSectorName(STChannelID(int(chanID)))

def get_module(chanID):
    return TTModulesMap_instance.findModule(STChannelID(int(chanID))).id

def get_half_module(chanID):
    return TTModulesMap_instance.findHalfModule(STChannelID(int(chanID))).id

def flatten(d):
    out = []
    if isinstance(d, (list, tuple)):
        for item in d:
            out.extend(flatten(item))  
    elif isinstance(d, (str, int, float, unicode)):
        out.append(d)
    elif isinstance(d, (dict)):
        for dictkey in d.keys():
            out.extend(flatten(d[dictkey]))
    return out

def profileClusterSize(tree=None):
    if not tree:
        f = r.TFile("../RootFiles/HitsOnTrack/all2012-muEstimate-Edges-closestState.root")
        tree = f.Get("TTHitEfficiencyTuple/TrackMonTuple")
    c = r.TCanvas()
    tree.Draw("clusterSize : TMath::Sin(pt/p)*TMath::Cos(phi)","","prof")
    c.Modified(); c.Update()
    cSaver.append(c)

def profileClusterCharge(tree=None):
    if not tree:
        f = r.TFile("../RootFiles/HitsOnTrack/all2012-muEstimate-Edges-closestState.root")
        tree = f.Get("TTHitEfficiencyTuple/TrackMonTuple")
    c = r.TCanvas()
    #tree.Draw("clusterCharge : TMath::Sqrt(p*p-pt*pt)/p","","prof")
    tree.Draw("clusterCharge : TMath::Cos(pt/p)","","prof")
    c.Modified(); c.Update()
    cSaver.append(c)

def plotCosTheta(tree=None):
    if not tree:
        f = r.TFile("../RootFiles/HitsOnTrack/all2012-muEstimate-Edges-closestState.root")
        tree = f.Get("TTHitEfficiencyTuple/TrackMonTuple")
    c = r.TCanvas()
    tree.Draw("TMath::Cos(pt/p)","","")
    c.Modified(); c.Update()
    cSaver.append(c)