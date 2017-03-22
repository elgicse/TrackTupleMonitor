import os
os.system('python analyze.py -i ../RootFiles/HitsOnTrack/all2012-muEstimate-Edges-closestState.root')

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
# TTaURegionBModule1t 2697217 2699776
# TTaURegionBModule1b 2694145 2696704
# TTaXRegionBModule1t 2435073 2437632
# TTaXRegionBModule1b 2432001 2434560
# TTbVRegionBModule2t 4536321 4538880
# TTbVRegionBModule2b 4533249 4535808
# TTbXRegionBModule2t 4798465 4801024
# TTbXRegionBModule2b 4795393 4797952
TTaUt_min, TTaUt_max = min(TTaURegionBModule1t), max(TTaURegionBModule1t)
TTaUb_min, TTaUb_max = min(TTaURegionBModule1b), max(TTaURegionBModule1b)
TTaXt_min, TTaXt_max = min(TTaXRegionBModule1t), max(TTaXRegionBModule1t)
TTaXb_min, TTaXb_max = min(TTaXRegionBModule1b), max(TTaXRegionBModule1b)
TTbUt_min, TTbUt_max = min(TTbVRegionBModule2t), max(TTbVRegionBModule2t)
TTbUb_min, TTbUb_max = min(TTbVRegionBModule2b), max(TTbVRegionBModule2b)
TTbXt_min, TTbXt_max = min(TTbXRegionBModule2t), max(TTbXRegionBModule2t)
TTbXb_min, TTbXb_max = min(TTbXRegionBModule2b), max(TTbXRegionBModule2b)

t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTaUt_min, TTaUt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTaUb_min, TTaUb_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTaXt_min, TTaXt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTaXb_min, TTaXb_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbUt_min, TTbUt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbUb_min, TTbUb_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbXt_min, TTbXt_max))
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbXb_min, TTbXb_max))

# Now look at funny things
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(TTbXt_min, TTbXt_max))
# make markers blue
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s && TTbX_nHits == 2'%(TTbXt_min, TTbXt_max), 'same')
# make markers red
TTbXRegionBModule3t = []
for chan in lookup:                                                            
    if lookup[chan]['hm'] == 'TTbXRegionBModule3t': TTbXRegionBModule3t.append(chan)
accanto_min, accanto_max = min(TTbXRegionBModule3t), max(TTbXRegionBModule3t)
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(accanto_min, accanto_max), 'same')
# make markers green
TTbXRegionBModule1t = []                                                     
for chan in lookup:                                                          
    if lookup[chan]['hm'] == 'TTbXRegionBModule1t': TTbXRegionBModule1t.append(chan)
accanto2_min, accanto2_max = min(TTbXRegionBModule1t), max(TTbXRegionBModule1t)
t.Draw('cluster_y:cluster_x','clusterSTchanID >= %s && clusterSTchanID <= %s'%(accanto2_min, accanto2_max), 'same')
