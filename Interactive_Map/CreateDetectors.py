"""
This script creates dictionaries with the names of IT and TT sectors
Sectors can be accessed through:
for i in IT.values():
    for j in i.values():
        for k in j.values():
            print k.values()
or
for i in TT.values():
    for j in i.values():
        print j.values():

"""
import pickle

def TT_reg_len(det,region):
    top = 25
    if ((det[2]=='a') and (region == 'RegionB')):
        top = 19
    if ((det[2]=='b') and (region == 'RegionB')):
        top = 27

    return range(1, top)

def TT_div_info(det, region, sector):
    nX = 6
    nY = 4
    sector_iy = sector-1
    sector_ix = sector-1
    if ((det[2]=='a') and (region == 'RegionB')):
        nX = 3
        nY = 6
    if ((det[2]=='b') and (region == 'RegionB')):
        nX = 5
        if ((sector>4) and (sector<23)):
            sector_iy = sector+1
            sector_ix = sector+1
            nY = 6
        if (sector>22):
            sector_iy = sector-7
            sector_ix = sector-7

    width = str(float(100*1./nX))+"%"
    height = str(float(100*1./nY))+"%"
    top = str(float(100*1./nY)*(nY-sector_iy%nY-1))+"%"
    left = str(float(100*1./nX)*(nX-int((sector_ix-sector_ix%nY)/nY)-1))+"%"
    return {'width':width, 
            'height':height, 
            'top':top, 
            'left':left,
            'position':'absolute',
            'border':' 1px solid #000000',
            'text-align':'center'}

def TT_layer_info(a):
    if a == 'TTaU':
        return {'position':'absolute',
                'top': '0%',
                'left': '0%',
                'width':'50%',
                'height':'50%',
                'border':'1px dashed'}
    if a == 'TTaX':
        return {'position':'absolute',
                'top': '0%',
                'left': '50%',
                'width':'50%',
                'height':'50%',
                'border':'1px dashed'}
    if a == 'TTbV':
        return {'position':'absolute',
                'top': '50%',
                'left': '0%',
                'width':'50%',
                'height':'50%',
                'border':'1px dashed'}
    if a == 'TTbX':
        return {'position':'absolute',
                'top': '50%',
                'left': '50%',
                'width':'50%',
                'height':'50%',
                'border':'1px dashed'}
    return {}

def TT_side_info(a,r):
    if (r == 'RegionA'): return {'position':'absolute',
                                'border':' 5px solid #00FFFF',
                                'top':' 0%',
                                'left':' 0%',
                                'width':'32%',
                                'height':'99%'}

    if (r == 'RegionB'): return {'position':'absolute',
                                'border':' 5px solid #FF00FF',
                                'top':' 0%',
                                'left':' 33.3%',
                                'width':'32%',
                                'height':'99%'}

    if (r == 'RegionC'): return {'position':'absolute',
                                'border':' 5px solid #FFFF00',
                                'top':' 0%',
                                'left':' 66.6%',
                                'width':'32%',
                                'height':'99%'}
    return {}

def IT_station_info(st):
    if st == 'IT1': return{'position':'absolute',
                            'top': '0%',
                            'left': '0%',
                            'width':'100%',
                            'height':'33.3%',
                            'border':'1px dashed',
                            'text-align':'left'}
    if st == 'IT2': return{'position':'absolute',
                            'top': '33.3%',
                            'left': '0%',
                            'width':'100%',
                            'height':'33.3%',
                            'border':'1px dashed',
                            'text-align':'left'}
    if st == 'IT3': return{'position':'absolute',
                            'top': '66.6%',
                            'left': '0%',
                            'width':'100%',
                            'height':'33.3%',
                            'border':'1px dashed',
                            'text-align':'left'}
    return {}

def IT_side_info(st,s):
    
    if s == 'ASide': return{'position':'absolute',
                                'border':' 5px solid #00FFFF',
                                'top':' 30%',
                                'left':' 0%',
                                'width':'33.3%',
                                'height':'40%'}
    if s == 'CSide': return{'position':'absolute',
                                'border':' 5px solid #00FF00',
                                'top':' 30%',
                                'left':' 66.6%',
                                'width':'33.3%',
                                'height':'40%'}
    if s == 'Bottom': return{'position':'absolute',
                                'border':' 5px solid #FF00FF',
                                'top':' 60%',
                                'left':' 33.3%',
                                'width':'33.3%',
                                'height':'40%'}
    if s == 'Top': return{'position':'absolute',
                                'border':' 5px solid #FFFF00',
                                'top':' 0%',
                                'left':' 33.3%',
                                'width':'33.3%',
                                'height':'40%'}
    return {}

def IT_layer_info(st,s,l):
    if l == 'X1': return {'position':'absolute',
                        'top':' 0%',
                        'left':' 0%',
                        'width':'100%',
                        'height':'25%'}
    if l == 'U': return {'position':'absolute',
                        'top':' 25%',
                        'left':' 0%',
                        'width':'100%',
                        'height':'25%'}
    if l == 'V': return {'position':'absolute',
                        'top':' 50%',
                        'left':' 0%',
                        'width':'100%',
                        'height':'25%'}
    if l == 'X2': return {'position':'absolute',
                        'top':' 75%',
                        'left':' 0%',
                        'width':'100%',
                        'height':'25%'}
    return {}

def Parse_Name(d):
    f = open('NameList.pkl')
    NameList = pickle.load(f)
    if d in NameList['TTNames']:
        return {'side':d[4:11],'layer':d[0:4],'sector':d[17:],'station':''}
    if d in NameList['ITNames']:
        station = d[0:3]
        sides = {'A':'ASide', 'B':'Bottom', 'C':'CSide', 'T':'Top'}
        side = sides[d[3]]
        layer = d[3+len(side):3+len(side)+1]
        if layer=='X':
            layer = d[3+len(side):3+len(side)+2]
        sector = str(d[len(d)-1])
        return {'station':station,'side':side,'layer':layer,'sector':sector}
    return d


def IT_div_info(st,s,l,n):
    nX = 7
    width = str(float(1./nX)*100)+"%"
    height = "100%"
    top = "0%"
    left = str(float(nX-n)/nX*100)+"%"
    return {'width':width, 
            'height':height, 
            'top':top, 
            'left':left,
            'position':'absolute',
            'border':'1px solid #000000',
            'text-align':'center'}

def create_TT():
    f = open('NameList.pkl')
    NameList = pickle.load(f) 
    TT = {}
    layer = ['TTaU','TTaX','TTbV','TTbX']
    side = ['RegionA','RegionB','RegionC']
    for l in layer:
        TT[l]={'layer_info':TT_layer_info(l)}
        for si in side:
            TT[l][si]={'side_info': TT_side_info(l,si)}
            for s in TT_reg_len(l,si):
                Info = {'Name':l+si+'Sector'+str(s), 'div_info':TT_div_info(l,si,s),'Histograms':{}}
                #if a+r+'Sector'+str(s) in NameList['TTNames']:
                TT[l][si][str(s)] = Info
                    #print a+r+'Sector'+str(s)
    return TT

def create_IT():
    f = open('NameList.pkl')
    NameList = pickle.load(f) 
    IT = {}
    station = ['IT1','IT2','IT3']
    side = ['ASide','CSide','Bottom','Top']
    layer = ['X1','X2','U','V']
    for st in station:
        IT[st]={'station_info':IT_station_info(st)}
        for s in side:
            IT[st][s]= {'side_info':IT_side_info(st,s)}
            for l in layer:
                IT[st][s][l]={'layer_info':IT_layer_info(st,s,l)}
                for n in range(1,8):
                    Info = {'Name':st+s+l+'Sector'+str(n), 'div_info':IT_div_info(st,s,l,n),'Histograms':{}}
                    IT[st][s][l][str(n)]=Info
    return IT

def Add_Histograms(det, hist_set, hist_name=''):
    f = open('NameList.pkl')
    NameList = pickle.load(f) 
    for k in hist_set:
        if k in NameList['TTNames']:
            p_name = Parse_Name(k)
            if p_name['station']:
                det[p_name['station']][p_name['side']][p_name['layer']][p_name['sector']]['Histograms'][hist_name]=hist_set[k]
            else:
                det[p_name['layer']][p_name['side']][p_name['sector']]['Histograms'][hist_name]=hist_set[k]
    return 