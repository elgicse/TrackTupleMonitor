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

print '\n\tLoaded CondDBs...\n'

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

print '\n\tLoaded Surveys...\n'

import ROOT as r
r.gROOT.ProcessLine('.x ../Scripts/tools/lhcbStyle.C')
r.gStyle.SetPadBottomMargin(0.26)
r.gStyle.SetPadTopMargin(0.07)
r.gStyle.SetTitleOffset(1.59,"X")

plotdir = 'plots/'
if not os.path.exists(plotdir):
    os.system('mkdir %s'%plotdir)
cSaver = []

data_temp = {
    'Modules': pickle.load(open('../Pickle/Data_RotationsPerIOV.pkl', 'rb'))
}

#for key in data['Modules'].keys():
#    print key

from conf.TTModules import *
data = {
    'Modules': {}
}

for key in data_temp['Modules'].keys():
    data['Modules'][elenaNamesToOlafNames(key)] = data_temp['Modules'][key]

print '\n\tLoaded module geometry...\n'


def getAlignableFromDataDict(moduleDict, alignable, iov):
    coords = {'x':0, 'y':1, 'z':2}
    d = None
    if 'R' in alignable:
        d = moduleDict['angles'][iov]
    return d[coords[alignable[-1]]]

# Add real data!!!
def asinError(m, merr):
    p1 = 1./(m*m)
    der = r.TMath.Abs( -1.*p1*( 1./r.TMath.Sqrt(1.-p1) ) )
    return r.TMath.Sqrt( der*der*merr*merr )

centralModules = [  
                    'TTaURegionBModule1t', 'TTaURegionBModule1b',
                    'TTaXRegionBModule1t', 'TTaXRegionBModule1b',
                    'TTbVRegionBModule2t', 'TTbVRegionBModule2b',
                    'TTbXRegionBModule2t', 'TTbXRegionBModule2b'
]
rot = pickle.load(open('../Scripts/rotationsByIOV_data_HitsOnTrack_TT.pkl','rb'))
hits = {}
for iov in middates.keys():
    hits[iov] = {'Modules': {}}
    for key in rot.keys():
        hits[iov]['Modules'][elenaNamesToOlafNames(key)] = {}
        if key in centralModules:
            hits[iov]['Modules'][elenaNamesToOlafNames(key)]['Rx'] = 0.
            hits[iov]['Modules'][elenaNamesToOlafNames(key)]['Rx_err'] = 0.
        else:
            #print key, iov, rot[key][iov].keys()
            try:
                hits[iov]['Modules'][elenaNamesToOlafNames(key)]['Rx'] = r.TMath.ASin(1./rot[key][iov]['m'])
                hits[iov]['Modules'][elenaNamesToOlafNames(key)]['Rx_err'] = asinError( rot[key][iov]['m'], rot[key][iov]['m_err'] )
            except KeyError:
                # not enough data points for this module and iov
                hits[iov]['Modules'][elenaNamesToOlafNames(key)]['Rx'] = 0.
                hits[iov]['Modules'][elenaNamesToOlafNames(key)]['Rx_err'] = r.TMath.Pi()

print '\n\tREADY TO GO! Done with loading databases and data.\n'


def plotChange(element, alignable, append=True, save=True, addData=True, addSurvey=True, addHits=False):
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
    grlist = []
    gr = r.TH1F(element+'_'+alignable+'_CondDB', element+'_'+alignable+'_CondDB', len(iovs), 0, 1)
    changeslist = []
    dblist = []
    for iov in iovs:
        gr.SetBinContent(iov, db[iov][collection][element][alignable])
        dblist.append(db[iov][collection][element][alignable])
        #print db[iov][collection][element][alignable]
    changeslist.append(dblist)
    print
    #unit = 'mm'
    #if 'R' in alignable:
    #    unit = 'rad'
    #gr.GetYaxis().SetTitle(alignable+' [%s]'%unit)
    #gr.GetXaxis().SetTitle('2012 alignment IOV')
    for iov in iovs:
        gr.GetXaxis().SetBinLabel(iov+1, IOVs2012_instance.intervals[iov]['start'].replace('2012-','') + ' to ' 
                + IOVs2012_instance.intervals[iov]['end'].replace('2012-',''))
    c1 = r.TCanvas(element+'_'+alignable, element+'_'+alignable)
    #gr.Draw('p')
    grlist.append(gr)

    if addSurvey:
        surveylist = []
        grsurvey = r.TH1F(element+'_'+alignable+'_Survey', element+'_'+alignable+'_Survey', len(iovs), 0, 1)
        for iov in iovs:
            grsurvey.SetBinContent(iov, surveys[collection][element][alignable] )
            surveylist.append( surveys[collection][element][alignable] )
        grsurvey.SetMarkerColor(r.kGreen)
        #grsurvey.Draw('p same')
        grlist.append(grsurvey)
        changeslist.append( surveylist)

    if addData:
        if (not collection=='Modules') or (not 'R' in alignable):
            print 'Sorry, for geometry I have only Modules and Rotations'
            return None
        datalist = []
        grdata = r.TH1F(element+'_'+alignable+'_Data', element+'_'+alignable+'_Data', len(iovs), 0, 1)
        for iov in iovs:
            grdata.SetBinContent(iov, getAlignableFromDataDict(data[collection][element], alignable, iov) )
            datalist.append( getAlignableFromDataDict(data[collection][element], alignable, iov) )
        grdata.SetMarkerColor(r.kRed)
        #grdata.Draw('p same')
        grlist.append(grdata)
        changeslist.append( datalist)

    if addHits:
        if (not collection=='Modules') or (not 'Rx' in alignable):
            print 'Sorry, for data I have only Modules and Rx'
            return None
        hitslist = []
        grhits = r.TH1F(element+'_'+alignable+'_Hits', element+'_'+alignable+'_Hits', len(iovs), 0, 1)
        for iov in iovs:
            grhits.SetBinContent(iov, hits[iov][collection][element][alignable] )
            grhits.SetBinError(iov, hits[iov][collection][element][alignable+'_err'] )
            hitslist.append( hits[iov][collection][element][alignable] )
        grhits.SetMarkerColor(r.kBlue)
        grhits.SetLineColor(r.kBlue)
        #grdata.Draw('p same')
        grlist.append(grhits)
        changeslist.append( hitslist)

    stack = r.THStack(element+'_'+alignable,element+'_'+alignable)
    
    for g in grlist:
        stack.Add(g)
    r.gStyle.SetErrorX(0.0001)
    stack.Draw('p nostack')

    unit = 'mm'
    if 'R' in alignable:
        unit = 'rad'
    stack.GetYaxis().SetTitle(alignable+' [%s]'%unit)
    #stack.GetXaxis().SetTitle('2012 alignment IOV')
    #label = r.TPaveText( 0.55 - r.gStyle.GetPadRightMargin(), 0.07 + r.gStyle.GetPadBottomMargin(),
    #                     0.95 - r.gStyle.GetPadRightMargin(), 0.15 + r.gStyle.GetPadBottomMargin(), "BRNDC");
    label = r.TPaveText( 0.30, 0.036, 0.70, 0.116, "BRNDC");
    label.SetFillColor(0); label.SetTextAlign(12); label.SetBorderSize(0)
    label.SetTextFont(132); label.SetTextSize(0.06)
    label.AddText(element); label.Draw('same'); c1.Modified(); c1.Update()

    leg = r.TLegend(0.53, 0.49, 0.91, 0.70)
    leg.AddEntry(gr, 'CondDB', 'p')
    if addData:
        leg.AddEntry(grdata, 'Geometry', 'p')
    if addHits:
        leg.AddEntry(grhits, 'Data', 'p')
    if addSurvey:
        leg.AddEntry(grsurvey, 'Survey', 'p')
    leg.Draw('same'); c1.Modified(); c1.Update()

    r.gPad.RedrawAxis('g')
    if append:
        cSaver.append( (c1, gr, label) )
    if save:
        c1.Print(plotdir+c1.GetName()+'.pdf')
        c1.Print(plotdir+c1.GetName()+'.png')
    return changeslist, c1, grlist, label, leg, stack


yes = raw_input('\n\n\t Make all plots?\n')
if yes.lower() == 'yes':
    for key in rot.keys():
        r.gROOT.SetBatch(r.kTRUE)
        plotChange('Modules/%s'%elenaNamesToOlafNames(key), 'Rx', addHits=True )
        plotChange('Modules/%s'%elenaNamesToOlafNames(key), 'Ry', addHits=False )
        plotChange('Modules/%s'%elenaNamesToOlafNames(key), 'Rz', addHits=False )
        plotChange('Modules/%s'%elenaNamesToOlafNames(key), 'Ty', addHits=False, addData=False )
        plotChange('Modules/%s'%elenaNamesToOlafNames(key), 'Tz', addHits=False, addData=False )
        plotChange('Modules/%s'%elenaNamesToOlafNames(key), 'Tx', addHits=False, addData=False )


r.gROOT.SetBatch(r.kFALSE)
