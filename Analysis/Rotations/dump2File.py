#!/usr/bin/env python
import sys, os, time
from datetime import datetime

sys.path.append('../Scripts')
from tools.common import *

middates = {}
for iov in IOVs2012_instance.intervals:
    d1 = datetime.strptime(IOVs2012_instance.intervals[iov]['start'],"%Y-%m-%d").date()
    d2 = datetime.strptime(IOVs2012_instance.intervals[iov]['end'],"%Y-%m-%d").date()
    mid = d1 + (d2-d1) / 2
    #print d1, d2, mid
    middates[iov] = mid

#time1 = '28/02/2012 14.33'
#time2 = '10/04/2012 14.33'

#assert(False)

def getTimeStr(t0):
    return str(int(time.mktime(time.strptime(str(t0), '%Y-%m-%d'))))+'0'*9
#    return str(int(time.mktime(time.strptime(t0, '%d/%m/%Y %H.%M'))))+'0'*9

def dump_db(i, date):
    os.system(os.path.expandvars('dump_db_to_files.py -c sqlite_file:$SQLITEDBPATH/LHCBCOND.db/LHCBCOND -s /Conditions/TT/Alignment -d dir%s -t '%i + getTimeStr(date)))
#os.system(os.path.expandvars('dump_db_to_files.py -c sqlite_file:$SQLITEDBPATH/LHCBCOND.db/LHCBCOND -s /Conditions/TT/Alignment -d dir1 -t '+getTimeStr(time1)))
#
#os.system(os.path.expandvars('dump_db_to_files.py -c sqlite_file:$SQLITEDBPATH/LHCBCOND.db/LHCBCOND -s /Conditions/TT/Alignment -d dir2 -t '+getTimeStr(time2)))

#os.system(os.path.expandvars('dump_db_to_files.py -c sqlite_file:$SQLITEDBPATH/LHCBCOND.db/LHCBCOND -s /Conditions/TT/Alignment -d dir1'))

dump_databases = False

if dump_databases:
    for idate in middates:
        dump_db(idate, middates[idate])

from diffXML import readXML
path = '/Conditions/TT/Alignment/'
db = {}
keys = ['Tx', 'Ty', 'Tz', 'Rx', 'Ry', 'Rz']
keyspivot = ['Tx', 'Ty', 'Tz', 'Rx', 'Ry', 'Rz', 'PivotX', 'PivotY', 'PivotZ']

def loadXML(filename, survey=False):
    if survey:
        dic1=readXMLPivot(filename)
        mykeys = keyspivot
    else:
        dic1 = readXML(filename)
        mykeys = keys
    dic2 = {}
    for key in dic1.keys():
        dic2[key] = dict( zip(mykeys, dic1[key]) )
    return dic2

for idate in middates:
    db[idate] = {}
    db[idate]['Modules']   = loadXML('dir%s'%idate+path+'Modules.xml')   
    db[idate]['Sensors']   = loadXML('dir%s'%idate+path+'Sensors.xml')   
    db[idate]['Detectors'] = loadXML('dir%s'%idate+path+'Detectors.xml') 

def readXMLPivot(inFile):
    import xml.etree.ElementTree
    from GaudiKernel.SystemOfUnits import *

    tree = xml.etree.ElementTree.parse(inFile)
    root = tree.getroot()
    alignParams = {}
    [Px, Py, Pz] = [0]*3
    for alignable in root:
        name = alignable.attrib['name']
        for vec in alignable:
            if vec.attrib['name'] == 'dPosXYZ':
                [Tx, Ty, Tz] = [float(eval(i)) for i in vec.text.split()]
            elif vec.attrib['name'] == 'dRotXYZ':
                [Rx, Ry, Rz] = [float(eval(i)) for i in vec.text.split()] 
            elif vec.attrib['name'] == 'pivotXYZ':
                [Px, Py, Pz] = [float(eval(i)) for i in vec.text.split()] 

        alignParams[name] = [Tx, Ty, Tz, Rx, Ry, Rz, Px, Py, Pz]
    return alignParams

surveys = {
    'Modules': loadXML('/afs/cern.ch/lhcb/software/releases/ALIGNMENT/ALIGNMENT_v9r2/Alignment/TAlignment/surveyxml/TT/Modules.xml', survey=True),
    'Detectors': loadXML('/afs/cern.ch/lhcb/software/releases/ALIGNMENT/ALIGNMENT_v9r2/Alignment/TAlignment/surveyxml/TT/Detectors.xml', survey=True),
    'Sensors': loadXML('/afs/cern.ch/lhcb/software/releases/ALIGNMENT/ALIGNMENT_v9r2/Alignment/TAlignment/surveyxml/TT/Sensors.xml', survey=True)
}

import ROOT as r
r.gROOT.ProcessLine('.x ../Scripts/tools/lhcbStyle.C')
r.gStyle.SetPadBottomMargin(0.26)
r.gStyle.SetPadTopMargin(0.07)
r.gStyle.SetTitleOffset(1.59,"X")

plotdir = 'plots/'
if not os.path.exists(plotdir):
    os.system('mkdir %s'%plotdir)
cSaver = []

#from array import array

def plotChange(element, alignable, append=True, save=True):
    '''
    element is a string like collection/element
    e.g.: Modules/TTbVLayerR3Module1T
    '''
    iovs = middates.keys()
    values = []
    element = element.split('/')
    collection = element[0]
    element = element[1]
    #for iov in iovs:
    #    values.append( db[iov][collection][element][alignable] )
    #gr = r.TGraph(len(iovs), array('d',iovs), array('d',values))
    gr = r.TH1F(element+'_'+alignable, element+'_'+alignable, len(iovs), 0, 1)
    for iov in iovs:
        gr.SetBinContent(iov, db[iov][collection][element][alignable])
    unit = 'mm'
    if 'R' in alignable:
        unit = 'mrad'
    gr.GetYaxis().SetTitle(alignable+' [%s]'%unit)
    gr.GetXaxis().SetTitle('2012 alignment IOV')
    for iov in iovs:
        gr.GetXaxis().SetBinLabel(iov+1, IOVs2012_instance.intervals[iov]['start'].replace('2012-','') + ' to ' 
                + IOVs2012_instance.intervals[iov]['end'].replace('2012-',''))
    c1 = r.TCanvas(element+'_'+alignable, element+'_'+alignable)
    gr.Draw('p')
    label = r.TPaveText( 0.55 - r.gStyle.GetPadRightMargin(), 0.07 + r.gStyle.GetPadBottomMargin(),
                         0.95 - r.gStyle.GetPadRightMargin(), 0.15 + r.gStyle.GetPadBottomMargin(), "BRNDC");
    label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
    label.SetTextFont(132); label.SetTextSize(0.06)
    label.AddText(element); label.Draw('same'); c1.Modified(); c1.Update()
    r.gPad.RedrawAxis('g')
    if append:
        cSaver.append( (c1, gr, label) )
    if save:
        c1.Print(plotdir+c1.GetName()+'.pdf')
        c1.Print(plotdir+c1.GetName()+'.png')
    return c1, gr, label