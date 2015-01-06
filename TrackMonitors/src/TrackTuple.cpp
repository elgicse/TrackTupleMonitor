// Include files 

// from Gaudi
#include "GaudiKernel/AlgFactory.h" 
#include "GaudiKernel/PhysicalConstants.h"

// local
#include "TrackTuple.h"

// track interfaces
#include "TrackInterfaces/IHitExpectation.h"

// kernel
#include "Kernel/ISTChannelIDSelector.h"
#include "Kernel/STLexicalCaster.h"
#include "Kernel/ITDetectorPlot.h"
#include "Kernel/TTDetectorPlot.h"
#include "Kernel/HitPattern.h"
#include "Kernel/Trajectory.h"

// detector
#include "STDet/DeSTDetector.h"
#include "STDet/DeSTSector.h"
#include "STDet/DeTTSector.h"
#include "STDet/DeSTSensor.h"

// Event
#include "Event/STCluster.h"
#include "Event/Measurement.h"
#include "Event/Node.h"
#include "Event/FitNode.h"
#include "Event/VPMeasurement.h"
//#include "Event/State.h"

// AIDA
#include "AIDA/IProfile1D.h"
#include "AIDA/IProfile2D.h"
#include "AIDA/IHistogram2D.h"
#include "AIDA/IHistogram1D.h"

#include "Event/ODIN.h"

#include "LoKi/select.h"

#include <sstream>

#include <cmath>

#include <boost/bind.hpp>
#include <boost/foreach.hpp>
#include <boost/assign/list_of.hpp>

#include <iostream>
using namespace std;


using namespace LHCb;
using namespace ST;
using namespace AIDA;
using namespace Gaudi;
using namespace boost::assign;

//-----------------------------------------------------------------------------
// Implementation file for class : TrackTuple
//
// 2009-06-16 : Johan Luisier
// 2010-07-27 : Frederic Dupertuis
//-----------------------------------------------------------------------------

// Declaration of the Algorithm Factory
DECLARE_ALGORITHM_FACTORY( TrackTuple )


//=============================================================================
// Standard constructor, initializes variables
//=============================================================================
TrackTuple::TrackTuple( const std::string& name,
                            ISvcLocator* pSvcLocator)
  : TrackMonitorTupleBase ( name , pSvcLocator ),
    m_totalExpected( 0u ),
    m_totalFound( 0u ),
    m_binSize( 10000. )
{
  declareProperty( "DetType"            , m_detType = "IT" );
  declareProperty( "ClusterCollector"   , m_clustercollectorName = m_detType+"ClusterCollector");  
  declareProperty( "HitExpectation"     , m_expectedHitsToolName = m_detType+"HitExpectation");  
  std::vector<double> tmp = list_of( 300. * Gaudi::Units::um );
  declareProperty( "Cuts"               , m_spacialCuts = tmp );
  declareProperty( "XLayerCut"          , m_xCut = 300. * Gaudi::Units::um );
  declareProperty( "StereoLayerCut"     , m_stereoCut = 300. * Gaudi::Units::um );
  declareProperty( "defaultCut"         , m_defaultCut = 300. * Gaudi::Units::um );
  declareProperty( "MinExpectedSectors" , m_minExpSectors = 1 );
  declareProperty( "MinNbResSectors"    , m_minNbResSectors = -10 );
  declareProperty( "MaxNbResSectors"    , m_maxNbResSectors = 10 );
  declareProperty( "MinDistToEdgeX"     , m_minDistToEdgeX = -1. );
  declareProperty( "MinDistToEdgeY"     , m_minDistToEdgeY = -1. );
  declareProperty( "MinStationPassed"   , m_minStationPassed = 1 );
  declareProperty( "MinCharge"          , m_minCharge = 0. );
  declareProperty( "EfficiencyPlot"     , m_effPlot = true );
  declareProperty( "ResidualsPlot"      , m_resPlot = false );
  declareProperty( "TakeEveryHit"       , m_everyHit = false);//true );
  declareProperty( "HitsOnTrack"        , m_hitsOnTrack = true);//true );
  declareProperty( "SingleHitPerSector" , m_singlehitpersector = false );
  declareProperty( "BranchBySector"     , m_branchBySector = false);
  declareProperty( "BranchByTrack"      , m_branchByTrack = true);
  declareProperty( "SkipEdges"          , m_skipEdges = true );
}

//=============================================================================
// Destructor
//=============================================================================
TrackTuple::~TrackTuple() {} 

//=============================================================================
// Initialization
//=============================================================================
StatusCode TrackTuple::initialize()
{
  StatusCode sc( TrackMonitorTupleBase::initialize() ); // must be executed first
  if ( sc.isFailure() ) return sc;  // error printed already by TrackMonitorTupleBase
  if ( msgLevel(MSG::DEBUG) ) debug() << "==> Initialize" << endmsg;
  
  m_clustercollectorName = m_detType+"ClusterCollector";
  m_expectedHitsToolName = m_detType+"HitExpectation";
  
  m_clustercollector = tool< ISTClusterCollector >( "STClusterCollector", m_clustercollectorName );
  m_expectedHits  = tool< IHitExpectation >( m_detType+"HitExpectation", m_expectedHitsToolName );
  
  m_tracker = getDet< DeSTDetector >( DeSTDetLocation::location( m_detType ) );
  m_NbrOfCuts = m_spacialCuts.size();
  m_foundSector.resize(m_NbrOfCuts);
  
  const DeSTDetector::Sectors& sectors = m_tracker->sectors();

  DeSTDetector::Sectors::const_iterator iterS = sectors.begin();

  for ( ; iterS != sectors.end(); ++iterS)
  {
    STChannelID elemID = (*iterS)->elementID();
    m_expectedSector[elemID.uniqueSector()] = 0u;
    m_nameMapSector[elemID.uniqueSector()] = *iterS;
    
    for (unsigned int i=0 ; i < m_NbrOfCuts; ++i )
    {
      m_foundSector[i][elemID.uniqueSector()] = 0u; 
    }
      
  } // iterS

  unsigned int iCut;

  for (iCut = 0; iCut < m_NbrOfCuts; ++iCut)
  {
    if ( std::abs( m_xCut - m_spacialCuts[iCut] ) < .005 )
      m_whichCut[0] = iCut;
    if ( std::abs( m_stereoCut -  m_spacialCuts[iCut]) < .005 )
      m_whichCut[1] = iCut;
  } // loop cuts

  for(iCut = 1; iCut < m_NbrOfCuts; iCut++)
  {
    m_binSize = std::min( m_binSize,
                          m_spacialCuts[ iCut ] - m_spacialCuts[ iCut - 1 ] );
  }
  
  //m_binSize = std::min( m_binSize, .01 );
  //m_binSize = std::max( m_binSize, .01 );

  m_binNumber = static_cast<unsigned int>( (m_spacialCuts.back() -
                                            m_spacialCuts.front()) / m_binSize );
  m_binNumber++;


  
  return StatusCode::SUCCESS;
}




//=============================================================================
// Main execution
//=============================================================================
StatusCode TrackTuple::execute()
{
  if ( msgLevel(MSG::DEBUG) ) debug() << "==> Execute" << endmsg;


  if (m_branchBySector && !m_everyHit)
  {
    error() << "TrackTuple ERROR: trying to compute hit "
              << "efficiency using only hits on tracks! Set "
              << "TakeEveryHit and unset HitsOnTracks to avoid!\n";
    return StatusCode::FAILURE;
  }

  if (m_branchBySector && m_branchByTrack)
  {
    warning() << "TrackTuple WARNING: I'm producing an ntuple "
              << "branched by sector AND by track, possible "
              << "ntuple clash. To avoid, select either "
              << "BranchByTrack or BranchBySector.\n";
  }


  Tracks* tracks = get< LHCb::Tracks >( inputContainer() );
  Tracks::const_iterator It, Begin( tracks -> begin() ),
    End( tracks -> end() );

  std::vector<LHCbID> expectedHits;
  std::vector<unsigned int> expectedSectors;
  std::vector<unsigned int> existingSectors;
  std::vector<unsigned int> foundSectors;
  std::vector<unsigned int>::iterator itFoundSectors;
  ISTClusterCollector::Hits prefoundHits;
  ISTClusterCollector::Hits foundHits;
  StatusCode inSensor;
  bool inActiveSensor;
  unsigned int nbFoundHits,nbExpHits,nbExpSectors,nbFoundSectors;
  int nbResHits,nbResSectors;
  State trackState;
  // if computing hit efficiency use only active regions
  Gaudi::XYZPoint toleranceOnEdge(- std::max(0.,m_minDistToEdgeX), - std::max(0.,m_minDistToEdgeY), 0.);
  // otherwise keep the whole sensor surface
  if (!m_skipEdges)
  {
    toleranceOnEdge = Gaudi::XYZPoint(0., 0., 0.);
  }

  DeSTSector* sector = 0;
  std::vector<DeSTSensor*> sensors;
  

  // Loop on tracks
  for (It = Begin; It != End; It++)
  {
    //info() << "Test property is activated in execution (verbose)"<< std::endl;
    //info() << endmsg;

    // Clearing all the std::vectors !
    expectedHits.clear();
    prefoundHits.clear();
    foundHits.clear();
    expectedSectors.clear();
    foundSectors.clear();

    // ask for tracks crossing enough stations
    if( ! hasMinStationPassed( (*It) ) )
      continue;
        
    // collect the list of expected hits
    m_expectedHits -> collect( **It, expectedHits );

    // remove tracks with too few expected hits
    nbExpHits = expectedHits.size();
    if ( nbExpHits < m_minExpSectors ) 
      continue; 

    // collect the list of found hits
    m_clustercollector -> execute( **It, prefoundHits );
    
    nbFoundHits = prefoundHits.size();
    // Number of hits not found
    nbResHits = (int)(nbFoundHits) - (int)(nbExpHits);
    
    if(fullDetail()){
      plot(nbFoundHits, "Control/NbFoundHits","Number of found hits",-0.5,24.5,25);
      plot(nbExpHits,   "Control/NbExpHits",  "Number of expected hits",-0.5,24.5,25);
      plot(nbResHits,   "Control/NbResHits",  "Number of found - expected hits",-5.5,7.5,13);
    }
        
    // convert the expected hits into unique sectors, cutting sensor edges if m_skipEdges=true
    BOOST_FOREACH(LHCbID id, expectedHits)
    {
      if( m_minDistToEdgeX > 0. || m_minDistToEdgeY > 0.){
        sector = m_tracker -> findSector( id.stID() );
        //info()<<"Sector is "<<sector<<endl;
        if ( sector == 0 ){
          info() << "Should not happen !" << endmsg;
          continue;
        }
        sensors = sector -> sensors();
        inActiveSensor = false;
        BOOST_FOREACH(DeSTSensor* sensor, sensors)
        {
          inSensor = extrapolator() -> propagate( (**It), sensor -> plane(), trackState, sensor -> thickness() );
          if( inSensor.isSuccess() ){
            inActiveSensor = sensor -> globalInActive(trackState.position(), toleranceOnEdge) ;
            if( inActiveSensor ) break;
          }
        }
        
        if( inActiveSensor )
        {
          expectedSectors.push_back(id.stID().uniqueSector());
        }
      }// end if (m_minDistToEdgeX > 0. || m_minDistToEdgeY > 0.).. maybe this condition can be removed?!?!?
    }// end (convert the expected hits into unique sectors cutting sensor edges)

    nbExpSectors = expectedSectors.size();

    // remove tracks with too few expected hits
    if ( nbExpSectors < m_minExpSectors ) 
      continue; 
        
    // Filling foundHits and foundSectors
    BOOST_FOREACH(ISTClusterCollector::Hit hit, prefoundHits)
    {
      // if the hit sector is in the list of expected sectors
      if(find( expectedSectors.begin(), expectedSectors.end(), hit.cluster->channelID().uniqueSector() ) != expectedSectors.end()){
        // push hit in foundHits and sector in foundSectors, if not already there
        if(find(foundSectors.begin(), foundSectors.end(), hit.cluster->channelID().uniqueSector()) == foundSectors.end()){
          foundHits.push_back(hit);
          foundSectors.push_back(hit.cluster->channelID().uniqueSector());
        }else if( !m_singlehitpersector )
          {foundHits.push_back(hit);} // push hit in foundHits anyways
        else
          continue;
      }
    }

    nbExpHits = nbExpSectors;
    nbFoundHits = foundHits.size();
    nbResHits = (int)(nbFoundHits) - (int)(nbExpHits);
    
    nbFoundSectors = foundSectors.size();
    nbResSectors = (int)(nbFoundSectors) - (int)(nbExpSectors);
    
    // remove track with too much found - expected hits
    if ( nbResHits > m_maxNbResSectors ) {
      if (msgLevel(MSG::DEBUG)) debug() << "Possible track expectation mismatch";
      continue;
    }
    
    // remove track with too few found - expected sectors
    if ( nbResSectors < m_minNbResSectors ) {
      if (msgLevel(MSG::DEBUG)) debug() << "Possible track expectation mismatch";
      continue;
    }
    
    if(fullDetail()){
      plot(nbFoundHits, "Control/NbFoundHitsFinal","Number of found hits after full selection",-0.5,24.5,25);
      plot(nbExpHits, "Control/NbExpHitsFinal","Number of expected hits after full selection",-0.5,24.5,25);
      plot(nbResHits, "Control/NbResHitsFinal","Number of found - expected hits after full selection",-5.5,7.5,13);
      plot(nbFoundSectors, "Control/NbFoundSectorsFinal","Number of found sectors after full selection",-0.5,24.5,25);
      plot(nbExpSectors, "Control/NbExpSectorsFinal","Number of expected sectors after full selection",-0.5,24.5,25);
      plot(nbResSectors, "Control/NbResSectorsFinal","Number of found - expected sectors after full selection",-5.5,7.5,13);
    }
        
    std::vector<unsigned int>::iterator iterExp = expectedSectors.begin();

    Tuple tup_test  =nTuple ("TrackMonTuple") ;
    tup_test -> column ("TrackCounter", 1);
    if( exist<LHCb::ODIN>(LHCb::ODINLocation::Default) )
      {
        LHCb::ODIN* report = get<LHCb::ODIN>(LHCb::ODINLocation::Default);
        if ( ! tup_test->column( "RunNumber", report->runNumber() ) ) return StatusCode::FAILURE;
        if (msgLevel(MSG::DEBUG)) debug() << "Run number:  " << report->runNumber() << endreq;
      }

    if (m_branchByTrack)
    {
      // Add track info to the tuple
      tup_test->column("p",        (*It)->p());
      tup_test->column("pt",       (*It)->pt());
      tup_test->column("phi",      (*It)->phi());
      tup_test->column("eta",      (*It)->pseudoRapidity());
      tup_test->column("charge",   (*It)->charge());
      tup_test->column("nDoF",     (*It)->nDoF());
      tup_test->column("chi2",     (*It)->chi2());
      tup_test->column("probChi2", (*It)->probChi2());

      unsigned int numTTHits = 0;
      unsigned int numITHits = 0;
      //// Number of ST hits on track
      //// ATTENTION: CAPS TO 4 FOR TT AND 12 FOR IT
      //LHCb::HitPattern hitpattern( (*It)->lhcbIDs());
      //tup_test->column("numIThits", (unsigned int)hitpattern.numITHits());
      //tup_test->column("numTThits", (unsigned int)hitpattern.numTTHits());


      // store vectors of clusters information in the ntuple, track by track
      unsigned int maxhits = 30;//0; // vector size
      //if (m_detType == "TT")
      //  maxhits = hitpattern.numTTHits();
      //if (m_detType == "IT")
      //  maxhits = hitpattern.numITHits();
      std::vector<unsigned int> clusterSize;   clusterSize.reserve(maxhits);
      std::vector<int> clusterStrip;           clusterStrip.reserve(maxhits);
      std::vector<double> clusterCharge;       clusterCharge.reserve(maxhits);
      std::vector<double> clusterNoise;        clusterNoise.reserve(maxhits);
      std::vector<double> clusterISfrac;       clusterISfrac.reserve(maxhits);
      std::vector<float> cluster_x;            cluster_x.reserve(maxhits);
      std::vector<float> cluster_y;            cluster_y.reserve(maxhits);
      std::vector<float> cluster_z;            cluster_z.reserve(maxhits);
      std::vector<float> trackState_x;         trackState_x.reserve(maxhits);
      std::vector<float> trackState_y;         trackState_y.reserve(maxhits);
      std::vector<float> trackState_z;         trackState_z.reserve(maxhits);
      std::vector<int> clusterSTchanID;        clusterSTchanID.reserve(maxhits);
      std::vector<double> hit_residual;        hit_residual.reserve(maxhits);
      std::vector<double> traj_mu;             traj_mu.reserve(maxhits);
      //std::vector<unsigned int> hit_layer;     hit_layer.reserve(maxhits);
      //std::vector<unsigned int> hit_sector;    hit_sector.reserve(maxhits);



      //const std::vector<LHCb::LHCbID>& ids = (*It) -> lhcbIDs();

      // Use only hits from tracks
      // Fill: residual, residual error, track projection coordinates
      if (m_hitsOnTrack && !m_everyHit)
      {
        std::vector<double> hit_errMeasure;      hit_errMeasure.reserve(maxhits);
        std::vector<double> hit_errResidual;     hit_errResidual.reserve(maxhits);

        std::vector<const LHCb::STMeasurement*> measVector; measVector.reserve(maxhits);
        LHCb::Track::ConstNodeRange nodes = (*It) -> nodes();
        LHCb::Track::ConstNodeRange::const_iterator iNodes = nodes.begin();
        for ( ; iNodes != nodes.end(); ++iNodes )
        {
          const LHCb::FitNode* fNode = dynamic_cast<const LHCb::FitNode*>(*iNodes);
          if ( fNode->hasMeasurement() == false ) continue;
          if ( m_hitsOnTrack && ( (*iNodes)->type() != LHCb::Node::HitOnTrack ) ) continue;
          if ( (*iNodes)->errResidual2() <= TrackParameters::lowTolerance ) continue;
          // Count number of TT and IT hits
          if ( fNode->measurement().type() != LHCb::Measurement::TT ) numTTHits++;
          if ( fNode->measurement().type() != LHCb::Measurement::IT ) numITHits++;
          if ( m_detType == "TT" && fNode->measurement().type() != LHCb::Measurement::TT ) continue;
          if ( m_detType == "IT" && fNode->measurement().type() != LHCb::Measurement::IT ) continue;
          const STMeasurement* aHit = dynamic_cast<const STMeasurement*>(&fNode->measurement());
          measVector.push_back(aHit);
          hit_residual.push_back( (*iNodes)->residual() );
          hit_errResidual.push_back( (*iNodes)->errResidual() );
          const LHCb::State & aState = (*iNodes)->state();
          trackState_x.push_back( (float)(aState.x()) );
          trackState_y.push_back( (float)(aState.y()) );
          trackState_z.push_back( (float)(aState.z()) );
          const LHCb::STCluster * aCluster = aHit->cluster();
          clusterSTchanID.push_back( (int)(aCluster->channelID()) );
          clusterSize.push_back(   aCluster->size() );
          clusterStrip.push_back(  aCluster->strip() );
          clusterCharge.push_back( aCluster->totalCharge() );
          double interStripFrac = (aHit->cluster())->interStripFraction();
          clusterISfrac.push_back( interStripFrac );
          const DeSTSector* sector = m_tracker->findSector(aCluster->channelID());
          double noise = sector->noise(aCluster->channelID()); 
          clusterNoise.push_back( noise );
          std::auto_ptr<LHCb::Trajectory> traj = m_tracker -> trajectory( aCluster->channelID(), interStripFrac );
          double mu = traj.get()->muEstimate(aState.position());
          //std::cout << "mu: " << mu << "\t";
          LHCb::Trajectory::Point midStripPosition = traj.get()->position(mu);//0.5
          traj_mu.push_back(mu);
          //std::cout << "at 0.5: " << midStripPosition.x() << ", " << midStripPosition.y() << "\t";
          //midStripPosition = traj.get()->position(0.5);//0.5
          //std::cout << "at mu: " << midStripPosition.x() << ", " << midStripPosition.y() << std::endl;
          cluster_x.push_back( (float)(midStripPosition.x()) );
          cluster_y.push_back( (float)(midStripPosition.y()) );
          cluster_z.push_back( (float)(midStripPosition.z()) );
          hit_errMeasure.push_back( aHit->errMeasure() );
        }
        // Count hits per ST layer
        const DeSTDetector::Layers& layers = m_tracker->layers();
        BOOST_FOREACH(DeSTLayer * layer, layers)
        {
          //bool foundHit = crossedLayer((*It), layer);
          //unsigned int nHitsOnLayer_withIDs = hitsOnLayer( (*It), layer );
          unsigned int nHitsOnLayer = hitsOnLayer( measVector, layer );
          //std::cout << layer->nickname()+" IDs: " << nHitsOnLayer_withIDs << "\t measurements: " << nHitsOnLayer << std::endl;
          tup_test -> column(layer->nickname()+"_nHits", nHitsOnLayer);
        }
        /*
        // Fill: chID, cluster size, strip, charge, interstrip frac,
        // noise, cluster position, measurement error
        BOOST_FOREACH(const LHCb::STMeasurement* aHit, measVector)
        {
          const LHCb::STCluster * aCluster = aHit->cluster();
          if ( (aCluster->isTT() && m_detType == "TT") || (aCluster->isIT() && m_detType == "IT") )
          {
            // Fill vectors of cluster info
            //clusterSTchanID.push_back( int(aHit.cluster->channelID()) );
            clusterSTchanID.push_back( (int)(aCluster->channelID()) );
            clusterSize.push_back(   aCluster->size() );
            clusterStrip.push_back(  aCluster->strip() );
            clusterCharge.push_back( aCluster->totalCharge() );
            double interStripFrac = (aHit->cluster())->interStripFraction();
            clusterISfrac.push_back( interStripFrac );
            const DeSTSector* sector = m_tracker->findSector(aCluster->channelID());
            double noise = sector->noise(aCluster->channelID()); 
            clusterNoise.push_back( noise );
            std::auto_ptr<LHCb::Trajectory> traj = m_tracker -> trajectory( aCluster->channelID(), interStripFrac );
            //double mu = traj.get()->muEstimate(aState.position())
            LHCb::Trajectory::Point midStripPosition = traj.get()->position(0.5);//mu
            cluster_x.push_back( (float)(midStripPosition.x()) );
            cluster_y.push_back( (float)(midStripPosition.y()) );
            cluster_z.push_back( (float)(midStripPosition.z()) );
            //hit_residual.push_back( aHit->residual );
            // retrieve the error on the measurement
            //LHCb::LHCbID hit_LHCbID = findHitId( (*It), aHit );
    
            //std::cout << "prima" << std::endl;
    
            //const LHCb::State & aState = (*It)->closestState( midStripPosition.z() );
            //std::cout << "in mezzo" << std::endl;//<< (char*)aState << std::endl;
            //trackState_x.push_back( (float)(aState.x()) );
            //trackState_y.push_back( (float)(aState.y()) );
            //trackState_z.push_back( (float)(aState.z()) );
            //std::cout << "dopo" << std::endl;
    
            //const LHCb::LHCbID idToPass = hit_LHCbID;
            //bool flag = (*It)->isOnTrack( hit_LHCbID );
            //std::cout << "ID " << hit_LHCbID.lhcbID() << " is on track: " << flag << std::endl;
            //std::cout << "num TT hits: " << hitpattern.numTTHits() << " num IT hits: " << hitpattern.numITHits() << std::endl;
            //const LHCb::Measurement * meas = (*It)->measurement( hit_LHCbID ); // THESE TWO LINES CAUSE A CRASH OR NO FARRAYS FILLED
            //std::cout << "meas" << (char*)meas << std::endl;
            //hit_errMeasure.push_back( meas->errMeasure() ); // THESE TWO LINES CAUSE A CRASH OR NO FARRAYS FILLED
            hit_errMeasure.push_back( aHit->errMeasure() ); // THESE TWO LINES CAUSE A CRASH OR NO FARRAYS FILLED
    //        
    //        // retrieve the error on the residual
    //        double errResidual2 = retrieveErrResidual2( (*It), hit_LHCbID );
    //        hit_errResidual2.push_back(errResidual2);
            //hit_layer.push_back(  aCluster->layerName() );
            //hit_sector.push_back( aCluster->sectorName() );
            //std::cout << "Channel ID: " << aCluster->channelID() << std::endl;
            //std::cout << "Layer name: " << aCluster->layerName() << " (uint: " << (aCluster->channelID()).uniqueLayer() << " )" << std::endl;
            //std::cout << "Sector name: " << aCluster->sectorName() << " (uint: " << (aCluster->channelID()).uniqueSector() << " )" << std::endl;
    
          }// end if (TT or IT)
        }// end loop on hits
        */
        tup_test -> farray( "trackState_x",    trackState_x, "len",    maxhits );
        tup_test -> farray( "trackState_y",    trackState_y, "len",    maxhits );
        tup_test -> farray( "trackState_z",    trackState_z, "len",    maxhits );
        tup_test -> farray( "hit_errMeasure",  hit_errMeasure, "len",  maxhits );
        tup_test -> farray( "hit_errResidual", hit_errResidual, "len", maxhits );
      }// end if (hits on track)


      // std::cout << "foundHits: " << foundHits.size() << "\t STMeasurements: " << measVector.size() << std::endl; // sconsiglio di decommentarlo...
  
      //DeSTDetector::Layers::const_iterator iterL = layers.begin();
      //for ( ; iterL != layers.end(); ++iterL){
        //bool foundHit = foundHitInLayer(foundHits, *It, (*iterL)->id(), m_defaultCut);
        //tup_test -> column ((*iterL)->nickname(), foundHit);


      // Use hits from the cluster collector
      // Fill: chID, size, strip, charge, interstrip frac,
      //       noise, cluster position, residual,
      //       closest state track projection coordinates
      else if (m_everyHit && !m_hitsOnTrack)
      {
        // Count hits per ST layer
        const DeSTDetector::Layers& layers = m_tracker->layers();
        BOOST_FOREACH(DeSTLayer * layer, layers)
        {
          //bool foundHit = crossedLayer((*It), layer);
          //unsigned int nHitsOnLayer_withIDs = hitsOnLayer( (*It), layer );
          unsigned int nHitsOnLayer = hitsOnLayer( foundHits, layer );
          //std::cout << layer->nickname()+" IDs: " << nHitsOnLayer_withIDs << "\t measurements: " << nHitsOnLayer << std::endl;
          tup_test -> column(layer->nickname()+"_nHits", nHitsOnLayer);
        }

        BOOST_FOREACH(ISTClusterCollector::Hit aHit, foundHits)
        {
          // Count number of TT and IT hits
          if ( aHit.cluster->isTT() ) numTTHits++;
          if ( aHit.cluster->isIT() ) numITHits++;
          if ( (aHit.cluster->isTT() && m_detType == "TT") || (aHit.cluster->isIT() && m_detType == "IT") )
          {
            // Fill vectors of cluster info
            //clusterSTchanID.push_back( int(aHit.cluster->channelID()) );
            clusterSTchanID.push_back( (int)(aHit.cluster->channelID()) );
            clusterSize.push_back( aHit.cluster->size() );
            clusterStrip.push_back( aHit.cluster->strip() );
            clusterCharge.push_back( aHit.cluster->totalCharge() );
            double interStripFrac = aHit.cluster->interStripFraction();
            clusterISfrac.push_back( interStripFrac );
            const DeSTSector* sector = m_tracker->findSector(aHit.cluster->channelID());
            double noise = sector->noise(aHit.cluster->channelID()); 
            clusterNoise.push_back( noise );
            // retrieve the error on the measurement
            //LHCb::LHCbID hit_LHCbID = findHitId( (*It), aHit );
            //std::cout << "prima" << std::endl;
            std::auto_ptr<LHCb::Trajectory> traj = m_tracker -> trajectory( aHit.cluster->channelID(), interStripFrac );
            LHCb::Trajectory::Point midStripPosition = traj.get()->position(0.5);
            const LHCb::State & aState = (*It)->closestState( midStripPosition.z() );
            //std::cout << "in mezzo" << std::endl;//<< (char*)aState << std::endl;
            trackState_x.push_back( (float)(aState.x()) );
            trackState_y.push_back( (float)(aState.y()) );
            trackState_z.push_back( (float)(aState.z()) );
            double mu = traj.get()->muEstimate(aState.position());
            traj_mu.push_back(mu);
            LHCb::Trajectory::Point hitPosition = traj.get()->position(mu);//0.5);
            cluster_x.push_back( (float)(hitPosition.x()) );
            cluster_y.push_back( (float)(hitPosition.y()) );
            cluster_z.push_back( (float)(hitPosition.z()) );
            hit_residual.push_back( aHit.residual );
            //std::cout << "dopo" << std::endl;
            //const LHCb::LHCbID idToPass = hit_LHCbID;
        //  bool flag = (*It)->isOnTrack( hit_LHCbID );
        //  std::cout << "ID " << hit_LHCbID.lhcbID() << "is on track: " << flag << std::endl;
        //  std::cout << "num TT hits: " << hitpattern.numTTHits() << " num IT hits: " << hitpattern.numITHits() << std::endl;
        //  const LHCb::Measurement * meas = (*It)->measurement( hit_LHCbID ); // THESE TWO LINES CAUSE A CRASH OR NO FARRAYS FILLED
        //  std::cout << "meas" << (char*)meas << std::endl;
        //  hit_errMeasure.push_back( meas->errMeasure() ); // THESE TWO LINES CAUSE A CRASH OR NO FARRAYS FILLED
    //        
    //        // retrieve the error on the residual
    //        double errResidual2 = retrieveErrResidual2( (*It), hit_LHCbID );
    //        hit_errResidual2.push_back(errResidual2);

          }// end if (TT or IT)
        }// end loop on hits
        tup_test -> farray( "closestTrackState_x",    trackState_x, "len", maxhits );
        tup_test -> farray( "closestTrackState_y",    trackState_y, "len", maxhits );
        tup_test -> farray( "closestTrackState_z",    trackState_z, "len", maxhits );
      }// end if (every hit)

      else
      {
        error() << "TrackTuple ERROR: cannot select both TakeEveryHits and HitsOnTracks!\n";
        return StatusCode::FAILURE;
      } // if both m_hitsOnTrack and m_everyHit are true




      //std::cout << "end of cycle" << std::endl;
  
      tup_test -> farray( "clusterSTchanID", clusterSTchanID, "len", maxhits );
      tup_test -> farray( "clusterSize",     clusterSize, "len",     maxhits );
      tup_test -> farray( "clusterStrip",    clusterStrip, "len",    maxhits );
      tup_test -> farray( "clusterCharge",   clusterCharge, "len",   maxhits );
      tup_test -> farray( "clusterNoise",    clusterNoise, "len",    maxhits );
      tup_test -> farray( "clusterISfrac",   clusterISfrac, "len",   maxhits );
      tup_test -> farray( "traj_mu",         traj_mu, "len",         maxhits );
      tup_test -> farray( "cluster_x",       cluster_x, "len",       maxhits );
      tup_test -> farray( "cluster_y",       cluster_y, "len",       maxhits );
      tup_test -> farray( "cluster_z",       cluster_z, "len",       maxhits );
      tup_test -> farray( "hit_residual",    hit_residual, "len",    maxhits );

      tup_test->column("numIThits", numITHits);
      tup_test->column("numTThits", numTTHits);

      //tup_test -> farray( "hit_layer",       hit_layer, "len", 100 );
      //tup_test -> farray( "hit_sector",      hit_sector, "len", 100 );

    }// end if m_branchByTrack



    // Store residual information sector by sector
    if (m_branchBySector)
    {
      bool foundHit = false;
      const DeSTDetector::Sectors& sectors = m_tracker->sectors();
      BOOST_FOREACH(DeSTSector * sector, sectors)
      {
        //info()<<sector->nickname()<<endl<<endmsg;
        tup_test -> column (sector->nickname(), -1000000 * Gaudi::Units::um);
      }
      for ( ; iterExp != expectedSectors.end(); ++iterExp)
      {
        ++m_expectedSector[*iterExp];
        ++m_totalExpected;
        foundHit = false;
        double min_cut = m_whichCut[0];
        for (unsigned int i = 0; i < m_NbrOfCuts; ++i)
        {
          foundHit = foundHitInSector(foundHits, *It, *iterExp, m_spacialCuts[i], (sector ->isStereo() && i == m_whichCut[1])||(! sector -> isStereo() &&  i == m_whichCut[0]));
          if (foundHit)
          {
            if ( sector ->isStereo() && i == m_whichCut[1] )
              ++m_totalFound;
            else if ( ! sector -> isStereo() &&  i == m_whichCut[0] )
              ++m_totalFound;
            if (m_spacialCuts[i] < min_cut)
              min_cut = m_spacialCuts[i];
            ++m_foundSector[i][*iterExp]; 
          }
        } // loop cuts
        double res = foundResInSector(foundHits, *It, *iterExp, min_cut);
        tup_test -> column (m_nameMapSector[*iterExp]->nickname(), res);
      } // loop expected
    }// branchBySector

    tup_test -> write () ;
  } // loop tracks

  return StatusCode::SUCCESS;
}

/**
 * Checks whether there is a hit in the given sector.
 *
 * @param hits list of clusters.
 * @param testsector uniqueID of the wanted sector
 * @param resCut window size
 *
 * @return \e true if yes.
 */
bool TrackTuple::foundHitInSector( const ISTClusterCollector::Hits& hits,
                                     Track* const& track,
                                     const unsigned int testsector,
                                     const double resCut,
                                     const bool toplot ) const
{
  BOOST_FOREACH(ISTClusterCollector::Hit aHit, hits)
    {
      if ( aHit.cluster->channelID().uniqueSector() == testsector ){
        if(fullDetail()&&toplot){
          plot(aHit.residual, "Control/HitResidual","Hit residual",-resCut,resCut,static_cast<unsigned int>(resCut*100+0.01)*2);
          plot(aHit.cluster->totalCharge(), "Control/HitCharge","Hit charge",0.,200.,200);
        }
        if(m_resPlot&&toplot){
          std::string name("perSector/Residuals_");
          name += aHit.cluster->sectorName();
          plot(aHit.residual, name,"Hit residual",-resCut,resCut,static_cast<unsigned int>(resCut*100+0.01)*2);
        }
        if( fabs(aHit.residual) < resCut ){
          if ( !( m_everyHit || track -> isOnTrack( LHCbID( aHit.cluster -> channelID() ) ) ) )
            continue;
          if( aHit.cluster->totalCharge() < m_minCharge )
            continue;
          return true;
        }
      }
    } // foreach
  
  return false;
}

bool TrackTuple::foundHitInLayer( const ISTClusterCollector::Hits& hits,
                                     Track* const& track,
                                     const unsigned int testlayer,
                                     const double resCut ) const
{
  BOOST_FOREACH(ISTClusterCollector::Hit aHit, hits)
    {
      if ( aHit.cluster->channelID().uniqueLayer() == testlayer ){
        if( fabs(aHit.residual) < resCut ){
          if ( !( m_everyHit || track -> isOnTrack( LHCbID( aHit.cluster -> channelID() ) ) ) )
            continue;
          if( aHit.cluster->totalCharge() < m_minCharge )
            continue;
          return true;
        }
      }
    } // foreach
  return false;
}

double TrackTuple::foundResInSector( const ISTClusterCollector::Hits& hits,
                                     Track* const& track,
                                     const unsigned int testsector,
                                     const double resCut ) const
{
  BOOST_FOREACH(ISTClusterCollector::Hit aHit, hits)
    {
      if ( aHit.cluster->channelID().uniqueSector() == testsector ){
        if( fabs(aHit.residual) < resCut ){
          if ( !( m_everyHit || track -> isOnTrack( LHCbID( aHit.cluster -> channelID() ) ) ) )
            continue;
          if( aHit.cluster->totalCharge() < m_minCharge )
            continue;
          return aHit.residual;
        }
      }
    } // foreach
  
  return -500000.* Gaudi::Units::um;
}

//=============================================================================
//  Finalize
//=============================================================================
StatusCode TrackTuple::finalize()
{
  if ( msgLevel(MSG::DEBUG) ) debug() << "==> Finalize" << endmsg;
  
  if ( (m_totalExpected == 0) && (m_branchBySector) )
  {
    warning() << "I'm sorry, but no track was found, please check that"
              << " you selected the right track type." << std::endl
              << "Your selection was : ";
    for (unsigned int i( 0 ); i < m_wantedTypes.size(); i++)
      warning() << m_wantedTypes[ i ] << ' ';
    warning() << endmsg;
    return TrackMonitorTupleBase::finalize();
  }
  

  std::map<unsigned int, DeSTSector*>::const_iterator iterS = m_nameMapSector.begin();
 
  std::vector<double>::const_iterator cutBegin( m_spacialCuts.begin() ),
    cutEnd( m_spacialCuts.end() ), cutIt;

  STChannelID channelID;
  std::string nick, root;

  unsigned int i, presentCut( 0u );

  //  double totExpected = 0; double totFound = 0;
  double nExpected, nFound, err;
  double eff  = 999.0;
  
  Histo2DProperties* prop;
  Histo2DProperties* propSectorStatus;
  Histo2DProperties* propNbHits;
  Histo2DProperties* propNbFoundHits;
  
  if(m_detType=="IT"){
    prop = new ST::ITDetectorPlot( "EfficiencyPlot", "Efficiency Plot" );
    propSectorStatus = new ST::ITDetectorPlot( "SectorStatus", "Sector Status Plot" );
    propNbHits = new ST::ITDetectorPlot( "NbExpHits", "Number of Expected Hits Plot" );
    propNbFoundHits = new ST::ITDetectorPlot( "NbFoundHits", "Number of Found Hits Plot" );
  }else{
    prop = new ST::TTDetectorPlot( "EfficiencyPlot", "Efficiency Plot" );
    propSectorStatus = new ST::TTDetectorPlot( "SectorStatus", "Sector Status Plot" );
    propNbHits = new ST::TTDetectorPlot( "NbExpHits", "Number of Expected Hits Plot" );
    propNbFoundHits = new ST::TTDetectorPlot( "NbFoundHits", "Number of Found Hits Plot" );
  }
  
  IHistogram2D* histoEff = 0;
  if(m_effPlot){
    histoEff = book2D( prop->name() , prop->title(),
                       prop->minBinX(), prop->maxBinX(), prop->nBinX(),
                       prop->minBinY(), prop->maxBinY(), prop->nBinY());
  }
  
  IProfile2D* histoSectorStatus = bookProfile2D( propSectorStatus->name() , propSectorStatus->title(),
                                                 propSectorStatus->minBinX(), propSectorStatus->maxBinX(), propSectorStatus->nBinX(),
                                                 propSectorStatus->minBinY(), propSectorStatus->maxBinY(), propSectorStatus->nBinY());
  
  IHistogram2D* histoNbHits = book2D( propNbHits->name() , propNbHits->title(),
                                      propNbHits->minBinX(), propNbHits->maxBinX(), propNbHits->nBinX(),
                                      propNbHits->minBinY(), propNbHits->maxBinY(), propNbHits->nBinY());
  
  IHistogram2D* histoNbFoundHits = book2D( propNbFoundHits->name() , propNbFoundHits->title(),
                                           propNbFoundHits->minBinX(), propNbFoundHits->maxBinX(), propNbFoundHits->nBinX(),
                                           propNbFoundHits->minBinY(), propNbFoundHits->maxBinY(), propNbFoundHits->nBinY());

  for (; iterS != m_nameMapSector.end(); ++iterS )
  {
    channelID = iterS -> second -> elementID();
    nick   = iterS -> second -> nickname();
    iterS->second->isStereo() == true ? presentCut = m_whichCut[1]: presentCut = m_whichCut[0] ;
      
    root = "perSector";
    
    // how many were expected ?
    nExpected = static_cast<double>( m_expectedSector[ iterS -> first ] );
    
    if (nExpected >= 1)
    {
      if(fullDetail())
        plot(-10., root + "/NbFoundHits_" + nick,
             "Number of Found Hits vs Cut",
             m_spacialCuts.front() - m_binSize / 2.,
             m_spacialCuts.back() + m_binSize / 2.,
             m_binNumber, nExpected);
      if(fullDetail())
        plot(-10., root + "/NbExpHits_" + nick,
             "Number of Found Hits vs Cut",
             m_spacialCuts.front() - m_binSize / 2.,
             m_spacialCuts.back() + m_binSize / 2.,
             m_binNumber, nExpected);
      if(m_effPlot){
        if(fullDetail())
          profile1D(-10., nExpected, root + "/Eff_" + nick,
                    "Efficiency vs Cut",
                    m_spacialCuts.front() - m_binSize / 2.,
                    m_spacialCuts.back() + m_binSize / 2.,
                    m_binNumber);
      }
      if(m_detType=="IT"){
        ST::ITDetectorPlot::Bins theBins = static_cast<ST::ITDetectorPlot*>(propSectorStatus)->toBins(channelID); 
        histoSectorStatus -> fill( theBins.xBin, theBins.yBin, 1 );
      }else{
        ST::TTDetectorPlot::Bins theBins = 
          static_cast<ST::TTDetectorPlot*>(propSectorStatus)->toBins(static_cast<DeTTSector*>(iterS->second)); 
        for(int ybin(theBins.beginBinY);ybin<theBins.endBinY;ybin++){
          histoSectorStatus -> fill( theBins.xBin, ybin, 1 );
        }
      }
      
      for (i = 0; i < m_NbrOfCuts; ++i)
	    {
	      nFound = static_cast<double>( m_foundSector[i][iterS->first] );
	      eff = 100. * nFound / nExpected;
	      err = sqrt( eff * (100. - eff) / nExpected );
       
        if(fullDetail())
          plot(m_spacialCuts[i], root + "/NbFoundHits_" + nick,
               "Number of Found Hits vs Cut",
               m_spacialCuts.front() - m_binSize / 2.,
               m_spacialCuts.back() + m_binSize / 2.,
               m_binNumber, nFound);
        if(fullDetail())
          plot(m_spacialCuts[i], root + "/NbExpHits_" + nick,
               "Number of Exp Hits vs Cut",
               m_spacialCuts.front() - m_binSize / 2.,
               m_spacialCuts.back() + m_binSize / 2.,
               m_binNumber, nExpected);
        if(m_effPlot){
          if(fullDetail())
            profile1D(m_spacialCuts[i], eff, root + "/Eff_" + nick,
                      "Efficiency vs cut",
                      m_spacialCuts.front() - m_binSize / 2.,
                      m_spacialCuts.back() + m_binSize / 2.,
                      m_binNumber);
        }
        if ( i == presentCut )
        {
          verbose() << nick << ' ' << eff
                    << " +/- " << err << " (found " << nFound
                    << " for cut " << m_spacialCuts[i] << ")" << endmsg;
          
          if(m_detType=="IT"){
            ST::ITDetectorPlot::Bins theBins = static_cast<ST::ITDetectorPlot*>(propSectorStatus)->toBins(channelID); 
            if(m_effPlot)
              histoEff -> fill( theBins.xBin, theBins.yBin, eff );
            histoNbHits -> fill( theBins.xBin, theBins.yBin, nExpected );
            histoNbFoundHits -> fill( theBins.xBin, theBins.yBin, nFound );
          }else{
            ST::TTDetectorPlot::Bins theBins = 
              static_cast<ST::TTDetectorPlot*>(propSectorStatus)->toBins(static_cast<DeTTSector*>(iterS->second)); 
            for(int ybin(theBins.beginBinY);ybin<theBins.endBinY;ybin++){
              if(m_effPlot)
                histoEff -> fill( theBins.xBin, ybin, eff );
              histoNbHits -> fill( theBins.xBin, ybin, nExpected );
              histoNbFoundHits -> fill( theBins.xBin, ybin, nFound );
            }
          }
        }
	    } // i
    } //nExpected
    else
    {
      if(m_detType=="IT"){
        ST::ITDetectorPlot::Bins theBins = static_cast<ST::ITDetectorPlot*>(propSectorStatus)->toBins(channelID); 
        if(m_effPlot)
          histoEff -> fill( theBins.xBin, theBins.yBin, -1 );
        histoSectorStatus -> fill( theBins.xBin, theBins.yBin, -1 );
        histoNbHits -> fill( theBins.xBin, theBins.yBin, 0 );
        histoNbFoundHits -> fill( theBins.xBin, theBins.yBin, 0 );
      }else{
        ST::TTDetectorPlot::Bins theBins = 
          static_cast<ST::TTDetectorPlot*>(propSectorStatus)->toBins(static_cast<DeTTSector*>(iterS->second));
        for(int ybin(theBins.beginBinY);ybin<theBins.endBinY;ybin++){
          if(m_effPlot)
            histoEff -> fill( theBins.xBin, ybin, -1 );
          histoSectorStatus -> fill( theBins.xBin, ybin, -1 );
          histoNbHits -> fill( theBins.xBin, ybin, 0 );
          histoNbFoundHits -> fill( theBins.xBin, ybin, 0 );
        }
      }
    }
  } // iterS
  /*
  if(m_detType=="IT"){
    delete static_cast<ST::ITDetectorPlot*>(prop);
    delete static_cast<ST::ITDetectorPlot*>(propSectorStatus);
    delete static_cast<ST::ITDetectorPlot*>(propNbHits);
    delete static_cast<ST::ITDetectorPlot*>(propNbFoundHits);
  }else{
    delete static_cast<ST::TTDetectorPlot*>(prop);
    delete static_cast<ST::TTDetectorPlot*>(propSectorStatus);
    delete static_cast<ST::TTDetectorPlot*>(propNbHits);
    delete static_cast<ST::TTDetectorPlot*>(propNbFoundHits);
  }
  */
  delete prop;
  delete propSectorStatus;
  delete propNbHits;
  delete propNbFoundHits;
  
  return TrackMonitorTupleBase::finalize();  // must be called after all other actions
}

/**
 * Stupid function that allows to print the number with 2 decimals,
 * since using std::setprecision and std::fixed directly in the info()
 * screws everythings up.
 *
 * @param nbr number (double) to print
 * @param digits number of wanted decimal (2 is the default)
 *
 * @return a string with the correct number of decimals.
 */
std::string TrackTuple::formatNumber(const double& nbr,
                                       const unsigned int& digits ) const
{
  std::stringstream ss;
  ss.setf(std::ios::fixed, std::ios::floatfield);
  ss << std::setprecision( digits ) << nbr;
  return ss.str();
}

/**
 *
 */
bool TrackTuple::hasMinStationPassed(LHCb::Track* const& aTrack) const
{
  std::set<unsigned int> stations;
  const std::vector<LHCb::LHCbID>& ids = aTrack -> lhcbIDs();

  for (std::vector<LHCb::LHCbID>::const_iterator iter = ids.begin(); iter != ids.end(); ++iter){
    if (m_detType == "IT"){
      if (iter->isIT() == true ) 
        stations.insert( iter->stID().station() );
    }else{
      if (iter->isTT() == true ) 
        stations.insert( iter->stID().station() );
    }
  }

  if(fullDetail())
    plot(stations.size(), "Control/NbCrossedStation","Number of stations crossed by the track",-0.5,3.5,4);

  if(stations.size() >= m_minStationPassed)
    return true;
  
  return false;
}


bool TrackTuple::crossedLayer(LHCb::Track* const& aTrack,
                                DeSTLayer * &aLayer) const
                                //unsigned int aLayer) const
{
  const std::vector<LHCb::LHCbID>& ids = aTrack -> lhcbIDs();
  for (std::vector<LHCb::LHCbID>::const_iterator iter = ids.begin(); iter != ids.end(); ++iter)
  {
    if ( aLayer->contains( iter->stID() ) )
      return true;
    //unsigned int theLayer = (iter->stID()).uniqueLayer();
    //if (theLayer == aLayer)
    //  return true;
  }
  return false;
}


unsigned int TrackTuple::hitsOnLayer(std::vector<const LHCb::STMeasurement*> measVector,
                                     DeSTLayer * &aLayer) const
{
  unsigned int counter = 0;
  for (std::vector<const LHCb::STMeasurement*>::const_iterator iter = measVector.begin(); iter != measVector.end(); ++iter)
  {
    if ( aLayer->contains( (*iter)->channelID() ) )
      counter = counter + 1;
  }
  return counter;
}

unsigned int TrackTuple::hitsOnLayer(ISTClusterCollector::Hits hits,//LHCb::Track* const& aTrack,
                                    DeSTLayer * &aLayer) const
{
  unsigned int counter = 0;
  BOOST_FOREACH(ISTClusterCollector::Hit aHit, hits)
  {
    if ( aLayer->contains( (aHit.cluster)->channelID() ) )
      counter = counter + 1;
  }
  //const std::vector<LHCb::LHCbID>& ids = aTrack -> lhcbIDs();
  //for (std::vector<LHCb::LHCbID>::const_iterator iter = ids.begin(); iter != ids.end(); ++iter)
  //{
  //  if ( aLayer->contains( iter->stID() ) )
  //    counter = counter + 1;
  //}
  return counter;
}


LHCb::LHCbID TrackTuple::findHitId(LHCb::Track* const& aTrack,
                                    const LHCb::STMeasurement* aHit) const
                                    //ISTClusterCollector::Hit aHit) const
{
  LHCb::LHCbID hitId(0);
  //std::cout << "Looking for LHCbID of channel " << aHit.cluster->channelID() << std::endl;
  //std::cout << "Looking for LHCbID of channel " << (aHit->cluster())->channelID() << std::endl;
  const std::vector<LHCb::LHCbID>& ids = aTrack -> lhcbIDs();
  for (std::vector<LHCb::LHCbID>::const_iterator iter = ids.begin(); iter != ids.end(); ++iter)
  {
    //if ( aHit.cluster->channelID() == iter->stID() )
    if ( (aHit->cluster())->channelID() == iter->stID() )
      hitId = (*iter);
  }
  //if (hitId.lhcbID() == 0)
    //std::cout << "LHCbID of channel " << aHit.cluster->channelID() << " NOT FOUND!" << std::endl;
    //std::cout << "LHCbID of channel " << (aHit->cluster())->channelID() << " NOT FOUND!" << std::endl;
  return hitId;
}


namespace {
  enum HitType {VeloR=0, VeloPhi, VPX, VPY, TT, IT, OT, Muon, HitTypeUnknown} ;
  const std::string HitTypeName[] = {"VeloR","VeloPhi","VPX","VPY","TT","IT","OT","Muon"} ;
  double      HitTypeMaxRes[] = {0.1,0.1,0.1,0.1,0.5,0.5,2.0,10} ;
  
  inline HitType hittypemap( const LHCb::Measurement& meas ) {
    LHCb::Measurement::Type type = meas.type() ;

    HitType rc = HitTypeUnknown ;
    switch( type ) {
    case LHCb::Measurement::Calo:
    case LHCb::Measurement::Origin :
    case LHCb::Measurement::Unknown: rc = HitTypeUnknown ; break ;
      
    case LHCb::Measurement::VP:
      {
        const LHCb::VPMeasurement* vpmeas = dynamic_cast<const LHCb::VPMeasurement*>(&meas);
        rc = vpmeas && vpmeas->projection() == LHCb::VPMeasurement::X ? VPX : VPY;
      }
      break;
    case LHCb::Measurement::VeloLiteR:
    case LHCb::Measurement::VeloR:   rc = VeloR ; break ;

    case LHCb::Measurement::VeloLitePhi:
    case LHCb::Measurement::VeloPhi: rc = VeloPhi ; break ;

    case LHCb::Measurement::UT :
    case LHCb::Measurement::UTLite :
    case LHCb::Measurement::TTLite:
    case LHCb::Measurement::TT: rc = TT; break;

    case LHCb::Measurement::FT :
    case LHCb::Measurement::ITLite:
    case LHCb::Measurement::IT: rc = IT; break;

    case LHCb::Measurement::OT: rc = OT; break;

    case LHCb::Measurement::Muon: rc = Muon; break;
    }
    return rc;
  }
}


double TrackTuple::retrieveErrResidual2(LHCb::Track* const& aTrack,
                                        LHCb::LHCbID aID) const
{
  double errResidual2;
  HitType mtype = VeloR; // initialize to avoid compiler warning
  LHCb::Track::ConstNodeRange nodes = aTrack -> nodes();
  for( LHCb::Track::ConstNodeRange::const_iterator inode = nodes.begin() ;
        inode != nodes.end(); ++inode)
  {
    if( (*inode)->type() == LHCb::Node::HitOnTrack 
        // discard extremely small fraction of hits with zero error
        // on residual. (e.g. a downstream track with only one
        // active TT hit)
        && (*inode)->errResidual2() > TrackParameters::lowTolerance 
        && (mtype = hittypemap( (*inode)->measurement() ) )!=HitTypeUnknown )
    {
      if ( (*inode)->measurement().lhcbID() == aID )
      {
        errResidual2 = (*inode)->errResidual2();
      }// end if (node is associated to the current measurement)
    }// end if (node not discarded)
  }// end loop on nodes
  return errResidual2;
}



//=============================================================================
