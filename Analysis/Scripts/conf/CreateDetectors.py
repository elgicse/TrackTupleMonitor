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


def create_TT():
    f = open('NameList.pkl')
    NameList = pickle.load(f) 
    TT = {}
    ab = ['TTaU','TTaX','TTbV','TTbX']
    region = ['RegionA','RegionB','RegionC']
    for a in ab:
        TT[a]={}
        for r in region:
            TT[a][r]={}
            for s in range(1,25):
                if a+r+'Sector'+str(s) in NameList['TTNames']:
                    TT[a][r][str(s)] = a+r+'Sector'+str(s)
                    print a+r+'Sector'+str(s)
    return TT

def create_IT():
    f = open('NameList.pkl')
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