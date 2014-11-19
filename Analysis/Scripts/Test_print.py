import pickle

f = open('Runs.pkl')
runs = pickle.load(f)

f = open('NameList.pkl')
NameList = pickle.load(f) 

print runs
print NameList
import os
import inspect
from pprint import pprint
from itertools import product
import math

import ROOT as R
from ROOT import gStyle
gStyle.SetOptStat(False)
#from ROOT import RooFit as RF

window = 0.3

local_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

detector = 'IT'

f_input = R.TFile(local_dir + "/DVnTuples.root")
if detector == 'TT':
    tree = f_input.TTHitEfficiency
else:
    tree = f_input.ITHitEfficiency
t = tree.Get("TestTuple")
print t
Events = {}


nPeriods = 10

#nPeriods -=1
n_merged_runs = (len(runs)-len(runs)%nPeriods)/nPeriods

binned_runs = {}
run_init = runs[0]
j = 0
for i in range(1, len(runs)+1):
    run_fin = runs[i-1]
    if i%n_merged_runs == 0:
       binned_runs[j] = {"Initial":run_init, "Final":run_fin}
       j+=1
       run_init = runs[i]
#Don't forget to include runs, which didn't fit to the last bin
binned_runs[j] = {"Initial":run_init, "Final":str(int(runs[len(runs)-1])+1)}
binned_runs.keys().sort()

PerSector_Events = {}

test_list = ['IT3CSideX2Sector1','IT3CSideX2Sector2']
for s in test_list:
#for index, s in enumerate(NameList[detector + 'Names']):
    Events = {}
    print str(s) + "  ("+str(index)+"/"+str(len(NameList[detector + 'Names']))+")"
    for r in binned_runs.keys():
        cut = "(RunNumber >= " + binned_runs[r]["Initial"] + ")&&(RunNumber < " + binned_runs[r]["Final"] + ")"
        #print cut
        #if t.GetEntries(cut) == 0:
        #    continue
        #if t.GetEntries("("+s+">-10000)&&"+cut)>0:
        Events[str(r)] = {"Found": t.GetEntries("(abs("+s+")<"+str(window)+")&&"+cut),"Expected": t.GetEntries("("+s+">-1000)&&"+cut)}
        print Events[str(r)]
        #Events[str(r)] = {"Found": t.GetEntries("("+s+">-500)&&"+cut),"Expected": t.GetEntries("("+s+">-1000)&&"+cut)}
    PerSector_Events[s] = Events

for pse in PerSector_Events:
    hist = R.TH1F("hist"+pse,pse,nPeriods+1, 0, 1)
    i = 1
    for r in binned_runs.keys():
        f = float(PerSector_Events[str(pse)][str(r)]['Found'])
        e = float(PerSector_Events[str(pse)][str(r)]['Expected'])
        d = e -f
        if e > 0:
            eff = f/e
            err = 1 / e * (f*d/e)**0.5
        else:
            eff = 0
            err = 0
        print "Expected efficiency:  " + str(eff) + "+/-" + str(err)
        hist.SetBinContent(i, eff)
        hist.SetBinError(i, err)
        hist.GetXaxis().SetBinLabel(i, str(binned_runs[r]["Initial"]) + " - "+ str(binned_runs[r]["Final"]))
        hist.GetYaxis().SetRangeUser(0.98, 1.01)
        i +=1
    c = R.TCanvas("c"+pse,"c"+pse, 900, 900)
    hist.Draw()
    c.SaveAs("plots/"+pse+".pdf")
    hist.SaveAs("Cs/"+pse+".C")


