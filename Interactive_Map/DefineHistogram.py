from ROOT import *
import os

if not os.path.exists("static/plots"):
    os.system("mkdir static/plots")

def GetAPlot(hist,histname):
    """ Looks for a png files. If it is not there,
    it produces it by saving a ROOT histogram  as .png """
    if not os.path.isfile("static/plots/"+histname+".png"):
        gROOT.ProcessLine(".x tools/lhcbStyle.C")
        gStyle.SetOptStat("emr")
        gStyle.SetPadTopMargin(0.06) 
        c = TCanvas("c","c", 900, 900)
        hist.Draw()
        c.SaveAs("static/plots/"+histname+".png")
    dic = {"plot":"plots/"+histname+".png", "init_properties":{}, "properties":{'mean':hist_mean(hist)
                                                            , 'sigma':hist_sigma(hist)
                                                            }}
    for p in dic['properties']:
        dic['init_properties'][p]=dic['properties'][p]

    return dic

def hist_mean(hist):
    return hist.GetMean()

def hist_sigma(hist):
    return hist.GetRMS()