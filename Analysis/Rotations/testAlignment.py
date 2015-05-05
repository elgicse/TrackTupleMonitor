# to run gaudirun.py testAlignment2.py
import GaudiPython

from GaudiPython import gbl

from ROOT import TH1, TH2, TCanvas, Math, TH2F, TLegend

import os
import sys

from ROOT import gROOT, gRandom, gStyle
from ROOT import TCanvas, TF1, TH1F, TH2F
BRUNELOPTS = os.environ[ 'ESCHEROPTS' ]

OPTIONS = 'AlignVeloTest.py'
datasetName='Reco14'



appMgr = GaudiPython.AppMgr( outputlevel = 3, joboptions = OPTIONS )

EVT = appMgr.evtSvc()

SEL=appMgr.evtSel()

det = appMgr.detSvc()

# get some math-stuff
Math = GaudiPython.gbl.ROOT.Math

gROOT.Reset()
gStyle.SetOptStat(0)
gStyle.SetPadColor(10)
gStyle.SetFrameFillColor(10)
gStyle.SetFillColor(10)
gStyle.SetTitleFillColor(10)
gStyle.SetTitleBorderSize(0)
gStyle.SetCanvasColor(10) 
histoRightR = TH2F( "histoRightR", "Right R Sensor origin in global frame",1000, -0.1, 0.1,1000, -0.1, 0.1 )
histoRightPhi = TH2F( "histoRightPhi", "Right Phi Sensor origin in global frame",1000, -0.1, 0.1,1000, -0.1, 0.1 )
histoRightRPhi = TH2F( "histoRightRPhi", "Right R-Phi Sensor origin in global frame",1000, -0.1, 0.1,1000, -0.1, 0.1 )
histoLeftR = TH2F( "histoLeftR", "Left R Sensor origin in global frame",1000, -0.1, 0.1,1000, -0.1, 0.1 )
histoLeftPhi = TH2F( "histoLeftPhi", "Left Phi Sensor origin in global frame",1000, -0.1, 0.1,1000, -0.1, 0.1 )
histoLeftRPhi = TH2F( "histoLeftRPhi", "Left R-Phi Sensor origin in global frame",1000, -0.1, 0.1,1000, -0.1, 0.1 )

histoRightXZ = TH2F( "histoRighXZ", "Right Sensor origin in global frame XZ",1200, -300, 800,1000,-0.5, 0.5 )
histoRightYZ = TH2F( "histoRightYZ", "Right Sensor origini in global frame YZ",1200, -300, 800,1000,-0.5, 0.5 )
histoLeftXZ = TH2F( "histoLeftXZ", "Left Sensor origin in global frame XZ",1200, -300, 800,1000,-0.5, 0.5 )
histoLeftYZ = TH2F( "histoLeftYZ", "Left Sensor origini in global frame YZ",1200, -300, 800,1000,-0.5, 0.5 )

first_R = '/dd/Structure/LHCb/BeforeMagnetRegion/Velo/VeloLeft/Module00/RPhiPair00/Detector-00'
r_sensor = det[ first_R ]

base_left = '/dd/Structure/LHCb/BeforeMagnetRegion/Velo/VeloLeft/Module'
base_right = '/dd/Structure/LHCb/BeforeMagnetRegion/Velo/VeloRight/Module'
rphi = '/RPhiPair'
det00 = '/Detector-00'
det01 = '/Detector-01'

nametxt='Right_'+datasetName+'.txt'
writefile =open(nametxt,'w')
nametxt='Left_'+datasetName+'.txt'
writefileL =open(nametxt,'w')

for i in range(21):
  names = []
  number_right = '%02d' % ( 2 * i + 1)
  name_right00 = base_right + number_right + rphi + number_right + det00
  name_right01 = base_right + number_right + rphi + number_right + det01
  names.append( name_right00 )
  names.append( name_right01 )
  print  ' NAME ='+ name_right00 + ' NAME ='+ name_right01
  pointR = pointPhi = GaudiPython.gbl.ROOT.Math.XYZPoint()
  #pointR = pointPhi = Math.XYZPoint()
  
  averagexRight=0.
  averageyRight=0.
  for name in names:
    print 'name='+ name
    sensor = det[ name ]
    print 'sens='
    if sensor.type() == r_sensor.type():
      print 'sensor is R type'
      point = GaudiPython.gbl.ROOT.Math.XYZPoint()
      #point = Gaudi.Math.XYZPoint()
      #print 'SetXYZ'
      point.SetXYZ( 0, 0, 0)
      #print 'SetXYZ'
      pointR = globalPoint = sensor.geometry().toGlobal( point )
      #print 'Global point'
      histoRightR.Fill( globalPoint.X(), globalPoint.Y() )
      averagexRight=averagexRight+globalPoint.X()
      averageyRight=averageyRight+globalPoint.Y()
      #print 'i='+str(i)
      writefile.write('R sensor ');
      writefile.write(str(i));
      writefile.write(' ');
      writefile.write(str(1));
      writefile.write(' ');
      writefile.write(str(globalPoint.X()));
      writefile.write(' ');
      writefile.write(str(globalPoint.Y()));
      writefile.write(' ');
      writefile.write(str(globalPoint.Z()));
      writefile.write('\n');
      histoRightXZ.Fill( pointR.Z(), pointR.X() )
      histoRightYZ.Fill( pointR.Z(), pointR.Y() )
                  
    if sensor.type() != r_sensor.type():
      print 'sensor is Phi type'
      point = GaudiPython.gbl.ROOT.Math.XYZPoint()
      point.SetXYZ(0, 0, 0)
      pointPhi = globalPoint = sensor.geometry().toGlobal( point )
      histoRightPhi.Fill( globalPoint.X(), globalPoint.Y() )
      averagexRight=averagexRight+globalPoint.X()
      averageyRight=averageyRight+globalPoint.Y()
      writefile.write('Phi sensor ');
      writefile.write(str(i));
      writefile.write(' ');
      writefile.write(str(0));
      writefile.write(' ');
      writefile.write(str(globalPoint.X()));
      writefile.write(' ');
      writefile.write(str(globalPoint.Y()));
      writefile.write(' ');
      writefile.write(str(globalPoint.Z()));
      writefile.write('\n');
      histoRightXZ.Fill( pointPhi.Z(), pointPhi.X() )
      histoRightYZ.Fill( pointPhi.Z(), pointPhi.Y() )
  histoRightRPhi.Fill( pointR.X() - pointPhi.X(), pointR.Y() - pointPhi.Y() )

  averagexRight=averagexRight/42.
  averageyRight=averageyRight/42.
  #print "Average Right x=%d y=%d" % (averagexRight,averageyRight)
  names = []
  number_left = '%02d' % ( 2 * i )
  name_left00 = base_left + number_left + rphi + number_left + det00
  name_left01 = base_left + number_left + rphi + number_left + det01
  names.append( name_left00 )
  names.append( name_left01 )
  pointR = pointPhi = GaudiPython.gbl.ROOT.Math.XYZPoint()
  for name in names:
    print name
    sensor = det[ name ]
    if sensor.type() == r_sensor.type():
      point = GaudiPython.gbl.ROOT.Math.XYZPoint()
      point.SetXYZ( 0, 0, 0)
      pointR = globalPoint = sensor.geometry().toGlobal( point )
      print "RSensPos(x,y,z)=("+str(globalPoint.X())+","+str(globalPoint.Y())+","+str(globalPoint.Z())+")"
      histoLeftR.Fill( globalPoint.X(), globalPoint.Y() )
      writefileL.write('R sensor ');
      writefileL.write(str(i));
      writefileL.write(' ');
      writefileL.write(str(1));
      writefileL.write(' ');
      writefileL.write(str(globalPoint.X()));
      writefileL.write(' ');
      writefileL.write(str(globalPoint.Y()));
      writefileL.write(' ');
      writefileL.write(str(globalPoint.Z()));
      writefileL.write('\n');
      histoLeftXZ.Fill( pointR.Z(), pointR.X() )
      histoLeftYZ.Fill( pointR.Z(), pointR.Y() )
    if sensor.type() != r_sensor.type():
      point = GaudiPython.gbl.ROOT.Math.XYZPoint()
      point.SetXYZ( 0, 0, 0)
      pointPhi = globalPoint = sensor.geometry().toGlobal( point )
      print "PhiSensPos(x,y,z)=("+str(globalPoint.X())+","+str(globalPoint.Y())+","+str(globalPoint.Z())+")"
      histoLeftPhi.Fill( globalPoint.X(), globalPoint.Y() )
      writefileL.write('Phi sensor ');
      writefileL.write(str(i));
      writefileL.write(' ');
      writefileL.write(str(0));
      writefileL.write(' ');
      writefileL.write(str(globalPoint.X()));
      writefileL.write(' ');
      writefileL.write(str(globalPoint.Y()));
      writefileL.write(' ');
      writefileL.write(str(globalPoint.Z()));
      writefileL.write('\n');
      histoLeftXZ.Fill( pointPhi.Z(), pointPhi.X() )
      histoLeftYZ.Fill( pointPhi.Z(), pointPhi.Y() )
  histoLeftRPhi.Fill( pointR.X() - pointPhi.X(), pointR.Y() - pointPhi.Y() )

c1 = TCanvas( "c1", "Sensor origins", 10, 10, 900, 600 )
c1.Divide(2,2)
#c1.Divide(3,2)
c1.cd(1)
histoRightR.Draw("box")
c1.cd(2)
histoRightPhi.Draw("box")
c1.cd(3)
#histoRightRPhi.Draw("box")
#c1.cd(4)
histoLeftR.Draw("box")
c1.cd(4)
#c1.cd(5)
histoLeftPhi.Draw("box")
#c1.cd(6)
#histoLeftRPhi.Draw("box")
#c1.SaveAs( "alignment_check.root" )


histoLeftXZ.SetMarkerColor(4);
histoLeftXZ.SetLineColor(4);
histoLeftXZ.SetMarkerStyle(25);
histoLeftXZ.SetMarkerSize(0.5);

histoLeftYZ.SetMarkerColor(4);
histoLeftYZ.SetLineColor(4);
histoLeftYZ.SetMarkerStyle(25);
histoLeftYZ.SetMarkerSize(0.5);

histoRightXZ.SetMarkerColor(2);
histoRightXZ.SetLineColor(2);
histoRightXZ.SetMarkerStyle(25);
histoRightXZ.SetMarkerSize(0.5);

histoRightYZ.SetMarkerColor(2);
histoRightYZ.SetLineColor(2);
histoRightYZ.SetMarkerStyle(25);
histoRightYZ.SetMarkerSize(0.5);

histoLeftXZ.SetTitle("Sensor origin in LHCb global frame")
histoLeftXZ.GetYaxis().SetTitle("x position (mm)");
histoLeftXZ.GetXaxis().SetTitle("z position (mm)");
histoLeftYZ.SetTitle("Sensor origin in LHCb global frame")
histoLeftYZ.GetYaxis().SetTitle("y position (mm)");
histoLeftYZ.GetXaxis().SetTitle("z position (mm)");

leg = TLegend(0.1,0.8,0.23,0.9);
leg.AddEntry(histoLeftXZ,"A side","p");
leg.AddEntry(histoRightXZ,"C side","p");


c11 = TCanvas( "c1", "Sensor origins", 10, 10, 900, 600 )
#c11.Divide(1,2)
c11.SetGrid();
#c11.SetGrid();
#c11.cd(1)
histoLeftXZ.Draw()
histoRightXZ.Draw("same")
leg.Draw();
namepdf='SensPosX_'+datasetName+'.pdf'
c11.SaveAs(namepdf)

#c11.cd(2)
histoLeftYZ.Draw()
histoRightYZ.Draw("same")
leg.Draw();
namepdf='SensPosY_'+datasetName+'.pdf'
c11.SaveAs(namepdf)

appMgr.exit()
