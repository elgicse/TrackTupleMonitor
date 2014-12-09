ST monitoring tools
===================


TrackTuple monitoring algorithm for DaVinci
-------------------

This ntuple-making monitoring algorithm that comes in three versions:
- a tool for resolution and hit efficiency studies: it produces an ntuple branch for every ST layer, filled event by event by the residual of the hit in that layer.
- a tool with a different ntuple layout, where every branch contains a different piece of information: number of hits on each layer, position of the track extrapolation, position of the cluster, cluster charge, noise, residual, inter-strip fraction... This, in turn, comes in two different "flavours":
  - "HitsOnTrack": I collect the hits based on the information stored in the track itself
  - "TakeEveryHit": I start from a track, then collected the clusters using the same selection as Frederic and Ilya (and probably someone before them, I saw the name of a certain Johan Louisier) did for their hit efficiency studies: they used the STClusterCollector tool, that basically locates the sector in which the hit is expected and collects hits within a default window of 20mm around the expected position. In this case we are less biased by how the alignment worked when the tracks were created, but we haven't access to informations such as the hit residual error (that is something belonging to the scope of track fitting). Hopefully we won't need this information (otherwise, I'll use the "HitsOnTrack" mode)



ST interactive monitor
-------------------

Runing interactive monitor:
- Install flask
- Put .root file with histograms for each sector to the folder where falsk\_test.py is. Pay attention, that histograms in your tuple should be named using schema \<Something\>\<SectorName\>, i.e. Very\_Interesting\_Hist\_TTaURegionA22
- run falsk\_test.py 
- open http://127.0.0.1:5000/index in your browser.
- PROFIT!
