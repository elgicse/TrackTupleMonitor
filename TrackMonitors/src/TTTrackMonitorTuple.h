// $Id: TTTrackMonitor.h,v 1.3 2010-03-19 14:12:07 wouter Exp $
#ifndef TTTRACKMONITORTUPLE_H
#define TTTRACKMONITORTUPLE_H 1
 
// Include files
 
// from Gaudi
#include "TrackMonitorTupleBase.h"

namespace LHCb {
  class Track ;
  class LHCbID ;
}

/** @class TTTrackMonitorTuple TTTrackMonitorTuple.h "TrackCheckers/TTTrackMonitorTuple"
 * 
 * Class for TT track monitoring with ntuple
 *  @author E. Graverini
 *  @date   13-11-2014
 */                 
                                                           
class TTTrackMonitorTuple : public TrackMonitorTupleBase {
                                                                             
 public:
                                                                             
  /** Standard construtor */
  TTTrackMonitorTuple( const std::string& name, ISvcLocator* pSvcLocator );
                                                                             
  /** Destructor */
  virtual ~TTTrackMonitorTuple();

  /** Algorithm initialize */
  virtual StatusCode initialize();

  /** Algorithm execute */
  virtual StatusCode execute();

 private:


  void fillHistograms(const LHCb::Track& track, 
                      const std::vector<LHCb::LHCbID>& itIDs,
		      const std::string& type) const ;

  unsigned int histoBin(const LHCb::STChannelID& chan) const;

  double ProjectedAngle() const;

  double m_refZ;
  double m_xMax;
  double m_yMax;

  unsigned int m_minNumTTHits;
  std::string m_clusterLocation;
  
  bool m_plotsBySector;//< individual plots by sector
  bool m_hitsOnTrack;//< plot only hits on tracks
  
};


#endif // TRACKMONITORTUPLE_H
