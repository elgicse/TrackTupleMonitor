#Wed Nov 12 13:47:43 2014"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from GaudiKernel.Proxy.Configurable import *

class VertexCompare( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'DefaultName', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'DefaultName', # str
    'produceNtuple' : True, # bool
    'produceHistogram' : True, # bool
    'inputVerticesName1' : 'Rec/Vertex/Primary', # str
    'inputVerticesName2' : 'Rec/Vertex/Primary', # str
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(VertexCompare, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'VertexCompare'
  pass # class VertexCompare

class UTTrackMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TracksInContainer' : 'Rec/Track/Best', # str
    'Extrapolator' : 'TrackMasterExtrapolator', # str
    'SplitByAlgorithm' : False, # bool
    'SplitByType' : False, # bool
    'ReferenceZ' : 2500.0000, # float
    'minNumUTHits' : 2, # int
    'InputData' : 'Raw/UT/Clusters', # str
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(UTTrackMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'UTTrackMonitor'
  pass # class UTTrackMonitor

class TTTrackMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TracksInContainer' : 'Rec/Track/Best', # str
    'Extrapolator' : 'TrackMasterExtrapolator', # str
    'SplitByAlgorithm' : False, # bool
    'SplitByType' : False, # bool
    'ReferenceZ' : 2500.0000, # float
    'minNumITHits' : 2, # int
    'InputData' : 'Raw/TT/Clusters', # str
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TTTrackMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TTTrackMonitor'
  pass # class TTTrackMonitor

class TrackVertexMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TrackContainer' : 'Rec/Track/Best', # str
    'PVContainer' : 'Rec/Vertex/Primary', # str
    'MaxIP' : 0.50000000, # float
    'MaxIPProfile' : 0.10000000, # float
    'MaxDz' : 5.0000000, # float
    'MaxRPV' : 1.0000000, # float
    'MinZPV' : -200.00000, # float
    'MaxZPV' : 200.00000, # float
    'MinZPV_Wide' : -1500.0000, # float
    'MaxZPV_Wide' : 1500.0000, # float
    'MaxLongTrackChisqPerDof' : 5.0000000, # float
    'MinLongTrackMomentum' : 5.0000000, # float
    'NumProfileBins' : 20, # int
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'MaxZPV_Wide' : """ Wide z window for PV plot """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'MinZPV_Wide' : """ Wide z window for PV plot """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackVertexMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackVertexMonitor'
  pass # class TrackVertexMonitor

class TrackVeloOverlapMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TrackLocation' : 'Rec/Track/Best', # str
    'OmitOutliers' : False, # bool
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackVeloOverlapMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackVeloOverlapMonitor'
  pass # class TrackVeloOverlapMonitor

class TrackV0Monitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'V0Location' : 'Rec/Vertex/V0', # str
    'MaxIPChi2' : 25.000000, # float
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackV0Monitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackV0Monitor'
  pass # class TrackV0Monitor

class TrackTuple( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'DefaultName', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'DefaultName', # str
    'TracksInContainer' : 'Rec/Track/Best', # str
    'Extrapolator' : 'TrackMasterExtrapolator', # str
    'SplitByAlgorithm' : False, # bool
    'SplitByType' : True, # bool
    'DetType' : 'IT', # str
    'ClusterCollector' : 'ITClusterCollector', # str
    'HitExpectation' : 'ITHitExpectation', # str
    'Cuts' : [ 0.30000000 ], # list
    'XLayerCut' : 0.30000000, # float
    'StereoLayerCut' : 0.30000000, # float
    'MinExpectedSectors' : 1, # int
    'MinNbResSectors' : -10, # int
    'MaxNbResSectors' : 10, # int
    'MinDistToEdgeX' : -1.0000000, # float
    'MinDistToEdgeY' : -1.0000000, # float
    'MinStationPassed' : 1, # int
    'MinCharge' : 0.0000000, # float
    'EfficiencyPlot' : True, # bool
    'ResidualsPlot' : False, # bool
    'TakeEveryHit' : True, # bool
    'SingleHitPerSector' : False, # bool
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackTuple, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackTuple'
  pass # class TrackTuple

class TrackTune( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'DefaultName', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'DefaultName', # str
    'ParticleLocation' : '/Event/Dimuon/Phys/SelDiMuonInciLoose/Particles', # str
    'TrackLocation' : 'Rec/Track/Best', # str
    'resonanceName' : 'J/psi(1S)', # str
    'minPurityCut' : 0.70000000, # float
    'selectBest' : True, # bool
    'resonance' : 110.00000, # float
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackTune, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackTune'
  pass # class TrackTune

class TrackTimingMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'DefaultName', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'DefaultName', # str
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackTimingMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackTimingMonitor'
  pass # class TrackTimingMonitor

class TrackPV2HalfAlignMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TrackContainer' : 'Rec/Track/Best', # str
    'MinNumTrPerPV' : 5, # int
    'limPx' : 1.0000000, # float
    'limPy' : 1.0000000, # float
    'limPz' : 150.00000, # float
    'limDPx' : 0.50000000, # float
    'limDPy' : 0.50000000, # float
    'limDPz' : 1.0000000, # float
    'limChi2' : 10.000000, # float
    'MinZPV' : -200.00000, # float
    'MaxZPV' : 200.00000, # float
    'NumProfileBins' : 20, # int
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackPV2HalfAlignMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackPV2HalfAlignMonitor'
  pass # class TrackPV2HalfAlignMonitor

class TrackParticleMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'InputLocation' : '', # str
    'MinMass' : 0.0000000, # float
    'MaxMass' : 120000.00, # float
    'BinsMass' : 50, # int
    'MaxMom' : 0.0000000, # float
    'ThreshMom' : 0.0000000, # float
    'RiseMom' : 0.0000000, # float
    'FallMom' : 0.0000000, # float
    'BinsMom' : 20, # int
    'MaxPt' : 0.0000000, # float
    'ThreshPt' : 0.0000000, # float
    'RisePt' : 0.0000000, # float
    'FallPt' : 0.0000000, # float
    'BinsPt' : 20, # int
    'MaxMomDif' : 0.0000000, # float
    'FallMomDif' : 0.0000000, # float
    'BinsMomDif' : 5, # int
    'PowMomAsym' : False, # bool
    'BinsMomAsym' : 5, # int
    'MinEta' : 2.0000000, # float
    'MaxEta' : 7.0000000, # float
    'KEta' : 1.0000000, # float
    'FallEta' : 0.0000000, # float
    'BinsEta' : 10, # int
    'MaxTx' : 0.20000000, # float
    'FallTx' : 0.0000000, # float
    'BinsTx' : 20, # int
    'MaxTy' : 0.20000000, # float
    'FallTy' : 0.0000000, # float
    'BinsTy' : 20, # int
    'BinsPhiMatt' : 20, # int
    'BinsPhiAngle' : 12, # int
    'MinOpenAngle' : 0.0000000, # float
    'MaxOpenAngle' : 0.30000000, # float
    'KOpenAngle' : 1.0000000, # float
    'FallOpenAngle' : 0.0000000, # float
    'BinsOpenAngle' : 10, # int
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'BinsPt' : """ # transverse momentum bins in 2D histo (default: 20) """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'MaxOpenAngle' : """ Max opening angle (default: 0.3) """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'MaxMomDif' : """ Max (p+ - p-) magnitude in MeV for all histos (default: particle dependent) """,
    'BinsPhiMatt' : """ # 'Matt's phi' (decay plane angle w.r.t. B) bins (default: 20) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'FallPt' : """ exp fall rate in 1/MeV (optional) """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'ThreshPt' : """ threshold transverse momentum in MeV (optional) """,
    'BinsMomDif' : """ # (p+ - p-) bins (pos/neg each) in 2D histo (default: 5) """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'MinMass' : """ Mass window min in MeV (default: 0) """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'ThreshMom' : """ threshold momentum in MeV (optional) """,
    'RiseMom' : """ exp rise rate from threshold in 1/MeV (optional) """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'BinsMass' : """ # mass bins in all 2D histos (default: 50) """,
    'BinsOpenAngle' : """ # eta bins in 2D histo (default: 10) """,
    'BinsMom' : """ # momentum bins in M vs. p (default: 20) """,
    'PowMomAsym' : """ power of (p+ - p-)/(p+ + p-) shape """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'MaxMass' : """ Mass window max in MeV (default: 120GeV """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'FallOpenAngle' : """ exp fall rate (optional) """,
    'MaxTy' : """ Max ty (horizontal slope) for all histos (default: 0.2) """,
    'BinsMomAsym' : """ # (p+ - p-)/(p+ + p-) bins (pos/neg each) in 2D histo (default: 5) """,
    'BinsPhiAngle' : """ # 'phi' (decay plane azimuthal angle) bins (default: 12) """,
    'MaxTx' : """ Max tx (vertical slope) for all histos (default: 0.2) """,
    'MaxMom' : """ Max momentum in MeV for all histos (default: particle dependent) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'BinsEta' : """ # eta bins in 2D histo (default: 10) """,
    'BinsTx' : """ # tx (vertical slope) bins (pos/neg each) in 2D histo (default: 40) """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'BinsTy' : """ # ty (horizontal slope) bins (pos/neg each) in 2D histo (default: 40) """,
    'FallMom' : """ exp fall rate in 1/MeV (optional) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'MinOpenAngle' : """ Min opening angle (default: 0) """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxEta' : """ Max eta (default: 7) """,
    'MinEta' : """ Min eta (default: 2) """,
    'FallTx' : """ exp fall rate (optional) """,
    'FallEta' : """ exp fall rate (optional) """,
    'FallMomDif' : """ exp fall rate in 1/MeV (optional) """,
    'FallTy' : """ exp fall rate (optional) """,
    'KOpenAngle' : """ rise power (optional) """,
    'KEta' : """ rise power (optional) """,
    'RisePt' : """ exp rise rate from threshold in 1/MeV (optional) """,
    'MaxPt' : """ Max transverse momentum in MeV for all histos (default: particle dependent) """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackParticleMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackParticleMonitor'
  pass # class TrackParticleMonitor

class TrackMuonMatchMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TracksLocation' : 'Rec/Track/Best', # str
    'Extrapolator' : 'TrackLinearExtrapolator', # str
    'WhichStation' : 0, # int
    'MaxErrX' : 5.0000000, # float
    'MaxErrY' : 20.000000, # float
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackMuonMatchMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackMuonMatchMonitor'
  pass # class TrackMuonMatchMonitor

class TrackMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TracksInContainer' : 'Rec/Track/Best', # str
    'Extrapolator' : 'TrackMasterExtrapolator', # str
    'SplitByAlgorithm' : False, # bool
    'SplitByType' : True, # bool
    'UseUT' : False, # bool
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackMonitor'
  pass # class TrackMonitor

class TrackMonitorNT( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'DefaultName', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'DefaultName', # str
    'TracksInContainer' : 'Rec/Track/Best', # str
    'SplitByAlgorithm' : False, # bool
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackMonitorNT, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackMonitorNT'
  pass # class TrackMonitorNT

class TrackITOverlapMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TrackLocation' : 'Rec/Track/Best', # str
    'MaxTolY' : 50.000000, # float
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackITOverlapMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackITOverlapMonitor'
  pass # class TrackITOverlapMonitor

class TrackFitMatchMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TrackContainer' : 'Rec/Track/Best', # str
    'ConstrainMethod' : 2, # int
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackFitMatchMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackFitMatchMonitor'
  pass # class TrackFitMatchMonitor

class TrackExpectedHitsXYZTool( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'TolX' : 30.000000, # float
    'TolY' : 150.00000, # float
    'nSigma' : 5.0000000, # float
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'StatPrint' : """ Print the table of counters """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackExpectedHitsXYZTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackExpectedHitsXYZTool'
  pass # class TrackExpectedHitsXYZTool

class TrackDiMuonMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TrackLocation' : 'Rec/Track/Muon', # str
    'DiMuonLocation' : 'Rec/Vertex/DiMuon', # str
    'MaxChi2TwoProngVertex' : 25.000000, # float
    'MinMass' : 2600.0000, # float
    'MaxMass' : 4000.0000, # float
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackDiMuonMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackDiMuonMonitor'
  pass # class TrackDiMuonMonitor

class TrackCaloMatchMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TrackLocation' : 'Rec/Track/Best', # str
    'CaloSystem' : 'Ecal', # str
    'UseClusters' : True, # bool
    'UseGeometricZ' : True, # bool
    'ClusterZCorrection' : 0.0000000, # float
    'RequireTHits' : True, # bool
    'Extrapolator' : PrivateToolHandle('TrackMasterExtrapolator'), # GaudiHandle
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackCaloMatchMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackCaloMatchMonitor'
  pass # class TrackCaloMatchMonitor

class TrackAlignMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TrackLocation' : 'Rec/Track/Best', # str
    'UseLocalFrame' : True, # bool
    'MaxTrackChi2PerDoF' : 10.000000, # float
    'VeloDofs' : 'TxTyRz', # str
    'TTDofs' : 'TxRz', # str
    'ITDofs' : 'TxRz', # str
    'OTDofs' : 'TxRz', # str
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackAlignMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'TrackAlignMonitor'
  pass # class TrackAlignMonitor

class STYAlignMagOff( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TracksInContainer' : 'Rec/Track/Best', # str
    'Extrapolator' : 'TrackMasterExtrapolator', # str
    'SplitByAlgorithm' : False, # bool
    'SplitByType' : True, # bool
    'DetType' : 'IT', # str
    'XTol' : 1.0000000, # float
    'YTol' : 10.000000, # float
    'Global' : False, # bool
    'XY' : False, # bool
    'Expected' : False, # bool
    'PrintSectorInfo' : False, # bool
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(STYAlignMagOff, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'STYAlignMagOff'
  pass # class STYAlignMagOff

class STEfficiency( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'DefaultName', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'DefaultName', # str
    'TracksInContainer' : 'Rec/Track/Best', # str
    'Extrapolator' : 'TrackMasterExtrapolator', # str
    'SplitByAlgorithm' : False, # bool
    'SplitByType' : True, # bool
    'DetType' : 'IT', # str
    'ClusterCollector' : 'ITClusterCollector', # str
    'HitExpectation' : 'ITHitExpectation', # str
    'Cuts' : [ 0.30000000 ], # list
    'XLayerCut' : 0.30000000, # float
    'StereoLayerCut' : 0.30000000, # float
    'MinExpectedSectors' : 1, # int
    'MinNbResSectors' : -10, # int
    'MaxNbResSectors' : 10, # int
    'MinDistToEdgeX' : -1.0000000, # float
    'MinDistToEdgeY' : -1.0000000, # float
    'MinStationPassed' : 1, # int
    'MinCharge' : 0.0000000, # float
    'EfficiencyPlot' : True, # bool
    'ResidualsPlot' : False, # bool
    'TakeEveryHit' : True, # bool
    'SingleHitPerSector' : False, # bool
    'TestProperty' : True, # bool
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(STEfficiency, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'STEfficiency'
  pass # class STEfficiency

class STCoordinates( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TracksInContainer' : 'Rec/Track/Best', # str
    'Extrapolator' : 'TrackMasterExtrapolator', # str
    'SplitByAlgorithm' : False, # bool
    'SplitByType' : True, # bool
    'DetType' : 'IT', # str
    'PrintSectorInfo' : True, # bool
    'AlignmentTag' : 'v4_2', # str
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(STCoordinates, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'STCoordinates'
  pass # class STCoordinates

class PVSplit( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'InputVerticesLocation' : 'Rec/Vertex/Primary', # str
    'OutputVerticesLocation' : 'Rec/Vertex/Split', # str
    'RandomShuffle' : True, # bool
    'SplitMethod' : 'middle', # str
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(PVSplit, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'PVSplit'
  pass # class PVSplit

class PVResMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'DefaultName', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'DefaultName', # str
    'nTracksToBeRecble' : 5, # int
    'produceNtuple' : True, # bool
    'produceHistogram' : True, # bool
    'dzIsolated' : 10.000000, # float
    'inputTracksName' : 'Rec/Track/Best', # str
    'inputVerticesName' : 'Rec/Vertex/Primary', # str
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(PVResMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'PVResMonitor'
  pass # class PVResMonitor

class PitchResTool( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'TrackExtrapolatorName' : 'TrackMasterExtrapolator', # str
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'StatPrint' : """ Print the table of counters """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(PitchResTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'PitchResTool'
  pass # class PitchResTool

class OTYAlignMagOff( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TracksInContainer' : 'Rec/Track/Best', # str
    'Extrapolator' : 'TrackMasterExtrapolator', # str
    'SplitByAlgorithm' : False, # bool
    'SplitByType' : True, # bool
    'XTol' : 1.0000000, # float
    'YTol' : 10.000000, # float
    'Global' : False, # bool
    'Expected' : False, # bool
    'PrintModuleInfo' : False, # bool
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(OTYAlignMagOff, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'OTYAlignMagOff'
  pass # class OTYAlignMagOff

class OTTrackMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TrackLocation' : 'Rec/Track/Best', # str
    'Projector' : PublicToolHandle('TrajOTProjector'), # GaudiHandle
    'MaxUnbiasedChisqPerDofGoodTracks' : 2.0000000, # float
    'Granularity' : 1, # int
    'RawBankDecoder' : PublicToolHandle('OTRawBankDecoder'), # GaudiHandle
    'Online' : False, # bool
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(OTTrackMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'OTTrackMonitor'
  pass # class OTTrackMonitor

class OTHitEfficiencyMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TrackLocation' : 'Rec/Track/Best', # str
    'MinOTHits' : 21, # int
    'MaxChi2PerDoF' : 2.0000000, # float
    'MaxDistError' : 0.20000000, # float
    'RawBankDecoder' : PublicToolHandle('OTRawBankDecoder'), # GaudiHandle
    'Online' : False, # bool
    'MaxTracks' : 1000000, # int
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(OTHitEfficiencyMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'OTHitEfficiencyMonitor'
  pass # class OTHitEfficiencyMonitor

class OTCoordinates( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TracksInContainer' : 'Rec/Track/Best', # str
    'Extrapolator' : 'TrackMasterExtrapolator', # str
    'SplitByAlgorithm' : False, # bool
    'SplitByType' : True, # bool
    'PrintModuleInfo' : True, # bool
    'AlignmentTag' : 'v4_2', # str
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(OTCoordinates, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'OTCoordinates'
  pass # class OTCoordinates

class ITTrackMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TracksInContainer' : 'Rec/Track/Best', # str
    'Extrapolator' : 'TrackMasterExtrapolator', # str
    'SplitByAlgorithm' : False, # bool
    'SplitByType' : False, # bool
    'ReferenceZ' : 7500.0000, # float
    'splitByITType' : True, # bool
    'plotsByLayer' : True, # bool
    'minNumITHits' : 6, # int
    'InputData' : 'Raw/IT/Clusters', # str
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(ITTrackMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'ITTrackMonitor'
  pass # class ITTrackMonitor

class HitEffPlotter( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'InputCollection' : 'Rec/Track/Best', # str
    'UseUT' : False, # bool
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HitEffPlotter, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'HitEffPlotter'
  pass # class HitEffPlotter

class AlignmentOnlineMonitor( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'DefaultName', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'TrackLocation' : 'Rec/Track/Best', # str
    'VeloMode' : 'side', # str
    'OTMode' : 'all', # str
    'ITMode' : 'all', # str
    'TTMode' : 'all', # str
  }
  _propertyDocDct = { 
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'VetoObjects' : """ Skip execute if one or more of these TES objects exists """,
    'HistoDir' : """ Histogram Directory """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'RequireObjects' : """ Execute only if one or more of these TES objects exists """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(AlignmentOnlineMonitor, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackMonitors'
  def getType( self ):
      return 'AlignmentOnlineMonitor'
  pass # class AlignmentOnlineMonitor
