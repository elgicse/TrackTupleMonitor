from flask import Flask
from flask import render_template
from flask import abort, redirect, url_for, request, flash
from ROOT import *
from CreateDetectors import *
import pickle
import sys
import os
sys.path.append("../Analysis/Scripts/conf")
from TTModules import *
import json


# Avoid spawning canvases
gROOT.SetBatch(kTRUE)

# Prepare a Flask application
app = Flask(__name__)

# Load the list of unique sector names
f = open('NameList.pkl')
NameList = pickle.load(f)

# Create detectors
tt_d = create_TT()
it_d = create_IT()
histos = {'it':{},'tt':{}}

# Add efficiency VS time histograms loading from a pickle file
#pickle_file = 'TT_Efficiency_Per_Run.pkl'
#hist_name = 'Efficiency_time_dependence'
#Add_Pkl(tt_d, pickle_file, hist_name,histos)

# Add residual, unbiased residual, signal to noise histograms loading from an ntuple
ntuple = 'data/STTrackMonitor-2012.root'
#Add_NTuple('data/DeltaY.root', it_d, tt_d, histos)
#Add_NTuple(ntuple, it_d, tt_d,histos)

collection = Normalize_Colours(tt_d, it_d)

#For .root file with 
#Pay attention, that this folder should be in static folder.
#Names should be given as <Sector/Module name><-Type of histogram, can be optional>.<extension>
#folder_with_plots = 'preloaded_pictures'
#Add_Folder(folder_with_plots, it_d, tt_d,histos)
folder_with_plots = 'PlotsBySector'#HalfModule'
Add_Folder(folder_with_plots, it_d, tt_d,histos)
#print json.dumps(it_d,sort_keys=True, indent=4)

# Handle sector plot drawing and the default template
# Drawing_mode handles the menu
@app.route("/",methods = ('GET', 'POST'))
@app.route("/index",methods = ('GET', 'POST'))
def hello():
    global Drawing_mode
    if request.method == 'POST':
        for m in ['IT_hist', 'TT_hist','IT_prop', 'TT_prop']:
            try:
                Drawing_mode[m]=request.form[m]
            except:
                pass
        return render_template('index.html', tt = tt_d, it=it_d, dm = Drawing_mode, collections = collection, hist_coll = histos)
    Drawing_mode = {'TT_hist':'', 'IT_hist':'','TT_prop':'', 'IT_prop':''}
    return render_template('index.html', tt = tt_d, it=it_d, dm = Drawing_mode, collections = collection, hist_coll = histos)

# Handle sector plots (e.g. when you click on a sector)
@app.route("/<d>",methods = ('GET', 'POST'))
def Detector(d):
    """
    if d == "IT":
        if request.method == 'POST':
            return render_template('IT.html', it=it_d)
        return render_template('IT.html', it=it_d)
    if d == "TT":
        if request.method == 'POST':
            return render_template('TT.html', tt=tt_d)
        return render_template('TT.html', tt=tt_d)
    """
    if d in NameList['TTNames']: 
        p_name = Parse_Name(d)
        return render_template('Sector.html', sec=tt_d[p_name['layer']][p_name['side']][p_name['sector']], histoname = hname)
    if d in NameList['ITNames']: 
        p_name = Parse_Name(d)
        return render_template('Sector.html', sec=it_d[p_name['station']][p_name['side']][p_name['layer']][p_name['sector']], histoname = hname)
    return redirect(url_for('hello'))


# Execute the program
if __name__ == "__main__":
    Drawing_mode = {'TT_hist':'', 'IT_hist':'','TT_prop':'', 'IT_prop':''}
    app.debug = False # Disable this when the code is ready!
    app.run(port=5000)
