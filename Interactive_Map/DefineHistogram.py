from ROOT import *
import os

if not os.path.exists("static/plots"):
    os.system("mkdir static/plots")

def GetAPlot(hist,histname):    
    if os.path.isfile("static/plots/"+histname+".png"):
        return "plots/"+histname+".png"
    else:
        gROOT.ProcessLine(".x tools/lhcbStyle.C")
        gStyle.SetOptStat("emr")
        gStyle.SetPadTopMargin(0.06) 
        c = TCanvas("c","c", 900, 900)
        hist.Draw()
        c.SaveAs("static/plots/"+histname+".png")
        return "plots/"+histname+".png"