# coding: utf-8
lookup.keys()
TTaURegionBModule1t = []
TTaURegionBModule1b = []
TTaXRegionBModule1t = []
TTaXRegionBModule1b = []
TTbVRegionBModule2t = []
TTbVRegionBModule2b = []
TTbXRegionBModule2t = []
TTbXRegionBModule2b = []
for chan in lookup:
    if lookup[chan]['hm'] == 'TTaURegionBModule1t': TTaURegionBModule1t.append(chan)
    if lookup[chan]['hm'] == 'TTaURegionBModule1b': TTaURegionBModule1b.append(chan)
    if lookup[chan]['hm'] == 'TTaXRegionBModule1t': TTaXRegionBModule1t.append(chan)
    if lookup[chan]['hm'] == 'TTaXRegionBModule1b': TTaXRegionBModule1b.append(chan)
    if lookup[chan]['hm'] == 'TTbVRegionBModule2t': TTbVRegionBModule2t.append(chan)
    if lookup[chan]['hm'] == 'TTbVRegionBModule2b': TTbVRegionBModule2b.append(chan)
    if lookup[chan]['hm'] == 'TTbXRegionBModule2t': TTbXRegionBModule2t.append(chan)
    if lookup[chan]['hm'] == 'TTbXRegionBModule2b': TTbXRegionBModule2b.append(chan)
    
print 'TTaURegionBModule1t', min(TTaURegionBModule1t), max(TTaURegionBModule1t)
print 'TTaURegionBModule1b', min(TTaURegionBModule1b), max(TTaURegionBModule1b)
print 'TTaXRegionBModule1t', min(TTaXRegionBModule1t), max(TTaXRegionBModule1t)
print 'TTaXRegionBModule1b', min(TTaXRegionBModule1b), max(TTaXRegionBModule1b)
print 'TTbVRegionBModule2t', min(TTbVRegionBModule2t), max(TTbVRegionBModule2t)
print 'TTbVRegionBModule2b', min(TTbVRegionBModule2b), max(TTbVRegionBModule2b)
print 'TTbXRegionBModule2t', min(TTbXRegionBModule2t), max(TTbXRegionBModule2t)
print 'TTbXRegionBModule2b', min(TTbXRegionBModule2b), max(TTbXRegionBModule2b)
get_ipython().magic(u'paste')
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTaUt_min, TTaUt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTaUb_min, TTaUb_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTaXt_min, TTaXt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTaXb_min, TTaXb_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbUt_min, TTbUt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbUb_min, TTbUb_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbXt_min, TTbXt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbXb_min, TTbXb_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbUt_min, TTbUt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s && RunNumber==115377'%(TTbUt_min, TTbUt_max), 'same')
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s && RunNumber>114277 && RunNumber<115443'%(TTbUt_min, TTbUt_max), 'same')
c = r.TCanvas()
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbUt_min, TTbUt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbXb_min, TTbXb_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbXt_min, TTbXt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbUt_min, TTbUt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbXt_min, TTbXt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s && TTbX_nHits == 2'%(TTbXt_min, TTbXt_max), 'same')
for chan in lookup:
    if lookup[chan]['hm'] == 'TTbXRegionBModule3t': TTbXRegionBModule3t.append(chan)
    
TTbXRegionBModule3t = []
for chan in lookup:
    if lookup[chan]['hm'] == 'TTbXRegionBModule3t': TTbXRegionBModule3t.append(chan)
    
accanto_min, accanto_max = min(TTbXRegionBModule3t), max(TTbXRegionBModule3t)
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(accanto_min, accanto_max), 'same')
TTbXRegionBModule1t = []
accanto2_min, accanto2_max = min(TTbXRegionBModule1t), max(TTbXRegionBModule1t)
for chan in lookup:
    if lookup[chan]['hm'] == 'TTbXRegionBModule1t': TTbXRegionBModule1t.append(chan)
    
accanto2_min, accanto2_max = min(TTbXRegionBModule1t), max(TTbXRegionBModule1t)
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(accanto2_min, accanto2_max), 'same')
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s && TTbX_nHits==1'%(accanto_min, accanto_max), 'same')
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s && TTbX_nHits==2'%(accanto_min, accanto_max), 'same')
cc = r.TCanvas()
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(accanto_min, accanto_max))
TTbXRegionBModule3b = []
for chan in lookup:                                                            
        if lookup[chan]['hm'] == 'TTbXRegionBModule3b': TTbXRegionBModule3b.append(chan)
    
accantob_min, accantob_max = min(TTbXRegionBModule3b), max(TTbXRegionBModule3b)
t.Draw('cluster_y:cluster_x','(clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s)'%(accanto_min, accanto_max, accantob_min, accantob_max))
TTbXRegionBModule1b = []
for chan in lookup:                                                            
        if lookup[chan]['hm'] == 'TTbXRegionBModule1b': TTbXRegionBModule1b.append(chan)
    
accanto2b_min, accanto2b_max = min(TTbXRegionBModule3b), max(TTbXRegionBModule3b)
ccc = r.TCanvas()
t.Draw('cluster_y:cluster_x','(clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s)'%(accanto_min, accanto_max, accantob_min, accantob_max, accanto2_min, accanto2_max, accanto2b_min, accanto2b_max))
get_ipython().magic(u'paste')
t.Draw('cluster_y:cluster_x','(clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s)'%(accanto_min, accanto_max, accantob_min, accantob_max, accanto2_min, accanto2_max, accanto2b_min, accanto2b_max))
TTbXRegionBModule3b = []
for chan in lookup:                                                            
    if lookup[chan]['hm'] == 'TTbXRegionBModule3b': TTbXRegionBModule3b.append(chan)
    
accanto2b_min, accanto2b_max = min(TTbXRegionBModule3b), max(TTbXRegionBModule3b)
t.Draw('cluster_y:cluster_x','(clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s)'%(accanto_min, accanto_max, accantob_min, accantob_max, accanto2_min, accanto2_max, accanto2b_min, accanto2b_max))
TTbXRegionBModule3t = []
for chan in lookup:                                                            
    if lookup[chan]['hm'] == 'TTbXRegionBModule3t': TTbXRegionBModule3t.append(chan)
    
accanto2_min, accanto2_max = min(TTbXRegionBModule3t), max(TTbXRegionBModule3t)
t.Draw('cluster_y:cluster_x','(clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s)'%(accanto_min, accanto_max, accantob_min, accantob_max, accanto2_min, accanto2_max, accanto2b_min, accanto2b_max))
TTbXRegionBModule1t = []
TTbXRegionBModule1b = []
for chan in lookup:                                                            
    if lookup[chan]['hm'] == 'TTbXRegionBModule1t': TTbXRegionBModule1t.append(chan)
    
for chan in lookup:                                                            
    if lookup[chan]['hm'] == 'TTbXRegionBModule1b': TTbXRegionBModule1b.append(chan)
    
accanto_min, accanto_max = min(TTbXRegionBModule3t), max(TTbXRegionBModule3t)
accantob_min, accantob_max = min(TTbXRegionBModule3b), max(TTbXRegionBModule3b)
accanto2_min, accanto2_max = min(TTbXRegionBModule1t), max(TTbXRegionBModule1t)
accanto2b_min, accanto2b_max = min(TTbXRegionBModule1b), max(TTbXRegionBModule1b)
t.Draw('cluster_y:cluster_x','(clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s)'%(accanto_min, accanto_max, accantob_min, accantob_max, accanto2_min, accanto2_max, accanto2b_min, accanto2b_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbXt_min, TTbXt_max), 'same')
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbXb_min, TTbXb_max), 'same')
cccc = r.TCanvas()
TTaURegionBModule2t = []
TTaURegionBModule2b = []
TTaURegionBModule0t = []
TTaURegionBModule0b = []
TTbVRegionBModule1t = []
TTbVRegionBModule1b = []
TTbVRegionBModule3t = []
TTbVRegionBModule3b = []
for chan in lookup:
    if lookup[chan]['hm'] == 'TTaURegionBModule2t': TTaURegionBModule2t.append(chan)
    if lookup[chan]['hm'] == 'TTaURegionBModule2b': TTaURegionBModule2b.append(chan)
    if lookup[chan]['hm'] == 'TTaURegionBModule0t': TTaURegionBModule0t.append(chan)
    if lookup[chan]['hm'] == 'TTaURegionBModule0b': TTaURegionBModule0b.append(chan)
    if lookup[chan]['hm'] == 'TTbVRegionBModule1t': TTbVRegionBModule1t.append(chan)
    if lookup[chan]['hm'] == 'TTbVRegionBModule1b': TTbVRegionBModule1b.append(chan)
    if lookup[chan]['hm'] == 'TTbVRegionBModule3t': TTbVRegionBModule3t.append(chan)
    if lookup[chan]['hm'] == 'TTbVRegionBModule3b': TTbVRegionBModule3b.append(chan)
    
t.Draw('cluster_y:cluster_x','(clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s)'%( min(TTaURegionBModule2t), max(TTaURegionBModule2t), min(TTaURegionBModule2b), max(TTaURegionBModule2b), min(TTaURegionBModule0t), max(TTaURegionBModule0t), min(TTaURegionBModule0b), max(TTaURegionBModule0b) ))
t.Draw('cluster_y:cluster_x','(clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s) || (clusterSTchanID >= %s && clusterSTchanID <= %s)'%( min(TTbVRegionBModule1t), max(TTbVRegionBModule1t), min(TTbVRegionBModule1b), max(TTbVRegionBModule1b), min(TTbVRegionBModule3t), max(TTbVRegionBModule3t), min(TTbVRegionBModule3b), max(TTbVRegionBModule3b) ), 'same')
get_ipython().magic(u'save farfalle 1-94')
