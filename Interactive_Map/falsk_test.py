from flask import Flask
from flask import render_template
from flask import abort, redirect, url_for
from ROOT import *
from CreateDetectors import *

import pickle
f = open('NameList.pkl')
NameList = pickle.load(f)


tt_d = create_TT()
it_d = create_IT()
f = open('Collection.pkl')
IT_hists = pickle.load(f)



hname ='Efficiency_time_dependence'
Add_Histograms(it_d, IT_hists, hname)

for h in GetHistosFromNT('STTrackMonitor-2012.root'):
    if h[0] == 'T':
        f = open(h+".pkl")
        TT_hists = pickle.load(f)
        Add_Histograms(tt_d, TT_hists, h)
    if h[0] == 'I':
        f = open(h+".pkl")
        IT_hists = pickle.load(f)
        Add_Histograms(it_d, IT_hists, h)

app = Flask(__name__)

 


@app.route("/")
@app.route("/index")
def hello():
    return render_template('index.html', tt = tt_d, it=it_d)
    #return "Hello World!"

@app.route("/<d>")
def Detector(d):
    if d == "IT":
        return render_template('IT.html', it=it_d)
    if d == "TT":
        return render_template('TT.html', tt=tt_d)
    if d in NameList['TTNames']: 
        p_name = Parse_Name(d)
        return render_template('Sector.html', sec=tt_d[p_name['layer']][p_name['side']][p_name['sector']], histoname = hname)
    if d in NameList['ITNames']: 
        p_name = Parse_Name(d)
        return render_template('Sector.html', sec=it_d[p_name['station']][p_name['side']][p_name['layer']][p_name['sector']], histoname = hname)
    return redirect(url_for('hello'))
    #return render_template('Sector.html', sec=d)

if __name__ == "__main__":
    app.run()
