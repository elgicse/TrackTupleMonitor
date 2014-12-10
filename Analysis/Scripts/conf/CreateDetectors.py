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

pickleDir = '../Pickle/'


def create_TT():
    f = open(pickleDir+'NameList.pkl')
    NameList = pickle.load(f) 
    TT = {}
    layers = ['TTaU','TTaX','TTbV','TTbX']
    region = ['RegionA','RegionB','RegionC']
    for l in layers:
        TT[l]={}
        for r in region:
            TT[l][r]={}
            nSectors = 25
            if ('a' in l) and ('B' in r):
                nSectors = 19
            if ('b' in l) and ('B' in r):
                nSectors = 27
            for s in range(1,nSectors+1):
                if l+r+'Sector'+str(s) in NameList['TTNames']:
                    TT[l][r][str(s)] = l+r+'Sector'+str(s)
    return TT

def create_IT():
    f = open(pickleDir+'NameList.pkl')
    NameList = pickle.load(f) 
    IT = {}
    ITs = ['IT1','IT2','IT3']
    side = ['ASide','CSide','Bottom','Top']
    xuw = ['X1','X2','U','V']
    for i in ITs:
        IT[i]={}
        for s in side:
            IT[i][s]= {}
            for x in xuw:
                IT[i][s][x]={}
                for n in range(1,8):
                    if i+s+x+'Sector'+str(n) in NameList['ITNames']:
                        IT[i][s][x][str(n)]=i+s+x+'Sector'+str(n)
    return IT