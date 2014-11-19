#-- start of make_header -----------------

#====================================
#  Library TrackMonitors
#
#   Generated Wed Nov 12 13:48:53 2014  by ikomarov
#
#====================================

include ${CMTROOT}/src/Makefile.core

ifdef tag
CMTEXTRATAGS = $(tag)
else
tag       = $(CMTCONFIG)
endif

cmt_TrackMonitors_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitors_has_target_tag

tags      = $(tag),$(CMTEXTRATAGS),target_TrackMonitors

TrackMonitors_tag = $(tag)

#cmt_local_tagfile_TrackMonitors = $(TrackMonitors_tag)_TrackMonitors.make
cmt_local_tagfile_TrackMonitors = $(bin)$(TrackMonitors_tag)_TrackMonitors.make

else

tags      = $(tag),$(CMTEXTRATAGS)

TrackMonitors_tag = $(tag)

#cmt_local_tagfile_TrackMonitors = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitors = $(bin)$(TrackMonitors_tag).make

endif

include $(cmt_local_tagfile_TrackMonitors)
#-include $(cmt_local_tagfile_TrackMonitors)

ifdef cmt_TrackMonitors_has_target_tag

cmt_final_setup_TrackMonitors = $(bin)setup_TrackMonitors.make
#cmt_final_setup_TrackMonitors = $(bin)TrackMonitors_TrackMonitorssetup.make
cmt_local_TrackMonitors_makefile = $(bin)TrackMonitors.make

else

cmt_final_setup_TrackMonitors = $(bin)setup.make
#cmt_final_setup_TrackMonitors = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitors_makefile = $(bin)TrackMonitors.make

endif

cmt_final_setup = $(bin)setup.make
#cmt_final_setup = $(bin)TrackMonitorssetup.make

#TrackMonitors :: ;

dirs ::
	@if test ! -r requirements ; then echo "No requirements file" ; fi; \
	  if test ! -d $(bin) ; then $(mkdir) -p $(bin) ; fi

javadirs ::
	@if test ! -d $(javabin) ; then $(mkdir) -p $(javabin) ; fi

srcdirs ::
	@if test ! -d $(src) ; then $(mkdir) -p $(src) ; fi

help ::
	$(echo) 'TrackMonitors'

binobj = 
ifdef STRUCTURED_OUTPUT
binobj = TrackMonitors/
#TrackMonitors::
#	@if test ! -d $(bin)$(binobj) ; then $(mkdir) -p $(bin)$(binobj) ; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)$(binobj)
endif

ifdef use_requirements
$(use_requirements) : ;
endif

#-- end of make_header ------------------
#-- start of libary_header ---------------

TrackMonitorslibname   = $(bin)$(library_prefix)TrackMonitors$(library_suffix)
TrackMonitorslib       = $(TrackMonitorslibname).a
TrackMonitorsstamp     = $(bin)TrackMonitors.stamp
TrackMonitorsshstamp   = $(bin)TrackMonitors.shstamp

TrackMonitors :: dirs  TrackMonitorsLIB
	$(echo) "TrackMonitors ok"

#-- end of libary_header ----------------
#-- start of libary ----------------------

TrackMonitorsLIB :: $(TrackMonitorslib) $(TrackMonitorsshstamp)
	$(echo) "TrackMonitors : library ok"

$(TrackMonitorslib) :: $(bin)TrackTuple.o $(bin)TrackPV2HalfMonitor.o $(bin)TrackParticleMonitor.o $(bin)PVSplit.o $(bin)TrackMonitorBase.o $(bin)TrackVertexMonitor.o $(bin)OTCoordinates.o $(bin)TrackMonitorNT.o $(bin)STCoordinates.o $(bin)TTTrackMonitor.o $(bin)AlignmentOnlineMonitor.o $(bin)TrackTune.o $(bin)TrackITOverlapMonitor.o $(bin)OTYAlignMagOff.o $(bin)PVResMonitor.o $(bin)ITTrackMonitor.o $(bin)STYAlignMagOff.o $(bin)STEfficiency.o $(bin)TrackMonitor.o $(bin)Map.o $(bin)PitchResTool.o $(bin)HitEffPlotter.o $(bin)OTTrackMonitor.o $(bin)TrackV0Monitor.o $(bin)OTHitEfficiencyMonitor.o $(bin)TrackTimingMonitor.o $(bin)VertexCompare.o $(bin)UTTrackMonitor.o $(bin)TrackExpectedHitsXYZTool.o $(bin)TrackAlignMonitor.o $(bin)TrackDiMuonMonitor.o $(bin)TrackCaloMatchMonitor.o $(bin)TrackMuonMatchMonitor.o $(bin)TrackVeloOverlapMonitor.o $(bin)TrackFitMatchMonitor.o $(bin)TrackMonitorTupleBase.o
	$(lib_echo) "static library $@"
	$(lib_silent) [ ! -f $@ ] || \rm -f $@
	$(lib_silent) $(ar) $(TrackMonitorslib) $(bin)TrackTuple.o $(bin)TrackPV2HalfMonitor.o $(bin)TrackParticleMonitor.o $(bin)PVSplit.o $(bin)TrackMonitorBase.o $(bin)TrackVertexMonitor.o $(bin)OTCoordinates.o $(bin)TrackMonitorNT.o $(bin)STCoordinates.o $(bin)TTTrackMonitor.o $(bin)AlignmentOnlineMonitor.o $(bin)TrackTune.o $(bin)TrackITOverlapMonitor.o $(bin)OTYAlignMagOff.o $(bin)PVResMonitor.o $(bin)ITTrackMonitor.o $(bin)STYAlignMagOff.o $(bin)STEfficiency.o $(bin)TrackMonitor.o $(bin)Map.o $(bin)PitchResTool.o $(bin)HitEffPlotter.o $(bin)OTTrackMonitor.o $(bin)TrackV0Monitor.o $(bin)OTHitEfficiencyMonitor.o $(bin)TrackTimingMonitor.o $(bin)VertexCompare.o $(bin)UTTrackMonitor.o $(bin)TrackExpectedHitsXYZTool.o $(bin)TrackAlignMonitor.o $(bin)TrackDiMuonMonitor.o $(bin)TrackCaloMatchMonitor.o $(bin)TrackMuonMatchMonitor.o $(bin)TrackVeloOverlapMonitor.o $(bin)TrackFitMatchMonitor.o $(bin)TrackMonitorTupleBase.o
	$(lib_silent) $(ranlib) $(TrackMonitorslib)
	$(lib_silent) cat /dev/null >$(TrackMonitorsstamp)

#------------------------------------------------------------------
#  Future improvement? to empty the object files after
#  storing in the library
#
##	  for f in $?; do \
##	    rm $${f}; touch $${f}; \
##	  done
#------------------------------------------------------------------

#
# We add one level of dependency upon the true shared library 
# (rather than simply upon the stamp file)
# this is for cases where the shared library has not been built
# while the stamp was created (error??) 
#

$(TrackMonitorslibname).$(shlibsuffix) :: $(TrackMonitorslib) requirements $(use_requirements) $(TrackMonitorsstamps)
	$(lib_echo) "shared library $@"
	$(lib_silent) if test "$(makecmd)"; then QUIET=; else QUIET=1; fi; QUIET=$${QUIET} bin=$(bin) $(make_shlib) "$(tags)" TrackMonitors $(TrackMonitors_shlibflags)

$(TrackMonitorsshstamp) :: $(TrackMonitorslibname).$(shlibsuffix)
	$(lib_silent) if test -f $(TrackMonitorslibname).$(shlibsuffix) ; then cat /dev/null >$(TrackMonitorsshstamp) ; fi

TrackMonitorsclean ::
	$(cleanup_echo) objects TrackMonitors
	$(cleanup_silent) /bin/rm -f $(bin)TrackTuple.o $(bin)TrackPV2HalfMonitor.o $(bin)TrackParticleMonitor.o $(bin)PVSplit.o $(bin)TrackMonitorBase.o $(bin)TrackVertexMonitor.o $(bin)OTCoordinates.o $(bin)TrackMonitorNT.o $(bin)STCoordinates.o $(bin)TTTrackMonitor.o $(bin)AlignmentOnlineMonitor.o $(bin)TrackTune.o $(bin)TrackITOverlapMonitor.o $(bin)OTYAlignMagOff.o $(bin)PVResMonitor.o $(bin)ITTrackMonitor.o $(bin)STYAlignMagOff.o $(bin)STEfficiency.o $(bin)TrackMonitor.o $(bin)Map.o $(bin)PitchResTool.o $(bin)HitEffPlotter.o $(bin)OTTrackMonitor.o $(bin)TrackV0Monitor.o $(bin)OTHitEfficiencyMonitor.o $(bin)TrackTimingMonitor.o $(bin)VertexCompare.o $(bin)UTTrackMonitor.o $(bin)TrackExpectedHitsXYZTool.o $(bin)TrackAlignMonitor.o $(bin)TrackDiMuonMonitor.o $(bin)TrackCaloMatchMonitor.o $(bin)TrackMuonMatchMonitor.o $(bin)TrackVeloOverlapMonitor.o $(bin)TrackFitMatchMonitor.o $(bin)TrackMonitorTupleBase.o
	$(cleanup_silent) /bin/rm -f $(patsubst %.o,%.d,$(bin)TrackTuple.o $(bin)TrackPV2HalfMonitor.o $(bin)TrackParticleMonitor.o $(bin)PVSplit.o $(bin)TrackMonitorBase.o $(bin)TrackVertexMonitor.o $(bin)OTCoordinates.o $(bin)TrackMonitorNT.o $(bin)STCoordinates.o $(bin)TTTrackMonitor.o $(bin)AlignmentOnlineMonitor.o $(bin)TrackTune.o $(bin)TrackITOverlapMonitor.o $(bin)OTYAlignMagOff.o $(bin)PVResMonitor.o $(bin)ITTrackMonitor.o $(bin)STYAlignMagOff.o $(bin)STEfficiency.o $(bin)TrackMonitor.o $(bin)Map.o $(bin)PitchResTool.o $(bin)HitEffPlotter.o $(bin)OTTrackMonitor.o $(bin)TrackV0Monitor.o $(bin)OTHitEfficiencyMonitor.o $(bin)TrackTimingMonitor.o $(bin)VertexCompare.o $(bin)UTTrackMonitor.o $(bin)TrackExpectedHitsXYZTool.o $(bin)TrackAlignMonitor.o $(bin)TrackDiMuonMonitor.o $(bin)TrackCaloMatchMonitor.o $(bin)TrackMuonMatchMonitor.o $(bin)TrackVeloOverlapMonitor.o $(bin)TrackFitMatchMonitor.o $(bin)TrackMonitorTupleBase.o) $(patsubst %.o,%.dep,$(bin)TrackTuple.o $(bin)TrackPV2HalfMonitor.o $(bin)TrackParticleMonitor.o $(bin)PVSplit.o $(bin)TrackMonitorBase.o $(bin)TrackVertexMonitor.o $(bin)OTCoordinates.o $(bin)TrackMonitorNT.o $(bin)STCoordinates.o $(bin)TTTrackMonitor.o $(bin)AlignmentOnlineMonitor.o $(bin)TrackTune.o $(bin)TrackITOverlapMonitor.o $(bin)OTYAlignMagOff.o $(bin)PVResMonitor.o $(bin)ITTrackMonitor.o $(bin)STYAlignMagOff.o $(bin)STEfficiency.o $(bin)TrackMonitor.o $(bin)Map.o $(bin)PitchResTool.o $(bin)HitEffPlotter.o $(bin)OTTrackMonitor.o $(bin)TrackV0Monitor.o $(bin)OTHitEfficiencyMonitor.o $(bin)TrackTimingMonitor.o $(bin)VertexCompare.o $(bin)UTTrackMonitor.o $(bin)TrackExpectedHitsXYZTool.o $(bin)TrackAlignMonitor.o $(bin)TrackDiMuonMonitor.o $(bin)TrackCaloMatchMonitor.o $(bin)TrackMuonMatchMonitor.o $(bin)TrackVeloOverlapMonitor.o $(bin)TrackFitMatchMonitor.o $(bin)TrackMonitorTupleBase.o) $(patsubst %.o,%.d.stamp,$(bin)TrackTuple.o $(bin)TrackPV2HalfMonitor.o $(bin)TrackParticleMonitor.o $(bin)PVSplit.o $(bin)TrackMonitorBase.o $(bin)TrackVertexMonitor.o $(bin)OTCoordinates.o $(bin)TrackMonitorNT.o $(bin)STCoordinates.o $(bin)TTTrackMonitor.o $(bin)AlignmentOnlineMonitor.o $(bin)TrackTune.o $(bin)TrackITOverlapMonitor.o $(bin)OTYAlignMagOff.o $(bin)PVResMonitor.o $(bin)ITTrackMonitor.o $(bin)STYAlignMagOff.o $(bin)STEfficiency.o $(bin)TrackMonitor.o $(bin)Map.o $(bin)PitchResTool.o $(bin)HitEffPlotter.o $(bin)OTTrackMonitor.o $(bin)TrackV0Monitor.o $(bin)OTHitEfficiencyMonitor.o $(bin)TrackTimingMonitor.o $(bin)VertexCompare.o $(bin)UTTrackMonitor.o $(bin)TrackExpectedHitsXYZTool.o $(bin)TrackAlignMonitor.o $(bin)TrackDiMuonMonitor.o $(bin)TrackCaloMatchMonitor.o $(bin)TrackMuonMatchMonitor.o $(bin)TrackVeloOverlapMonitor.o $(bin)TrackFitMatchMonitor.o $(bin)TrackMonitorTupleBase.o)
	$(cleanup_silent) cd $(bin); /bin/rm -rf TrackMonitors_deps TrackMonitors_dependencies.make

#-----------------------------------------------------------------
#
#  New section for automatic installation
#
#-----------------------------------------------------------------

install_dir = ${CMTINSTALLAREA}/$(tag)/lib
TrackMonitorsinstallname = $(library_prefix)TrackMonitors$(library_suffix).$(shlibsuffix)

TrackMonitors :: TrackMonitorsinstall

install :: TrackMonitorsinstall

TrackMonitorsinstall :: $(install_dir)/$(TrackMonitorsinstallname)
ifdef CMTINSTALLAREA
	$(echo) "installation done"
endif

$(install_dir)/$(TrackMonitorsinstallname) :: $(bin)$(TrackMonitorsinstallname)
ifdef CMTINSTALLAREA
	$(install_silent) $(cmt_install_action) \
	    -source "`(cd $(bin); pwd)`" \
	    -name "$(TrackMonitorsinstallname)" \
	    -out "$(install_dir)" \
	    -cmd "$(cmt_installarea_command)" \
	    -cmtpath "$($(package)_cmtpath)"
endif

##TrackMonitorsclean :: TrackMonitorsuninstall

uninstall :: TrackMonitorsuninstall

TrackMonitorsuninstall ::
ifdef CMTINSTALLAREA
	$(cleanup_silent) $(cmt_uninstall_action) \
	    -source "`(cd $(bin); pwd)`" \
	    -name "$(TrackMonitorsinstallname)" \
	    -out "$(install_dir)" \
	    -cmtpath "$($(package)_cmtpath)"
endif

#-- end of libary -----------------------
#-- start of dependency ------------------
ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)

#$(bin)TrackMonitors_dependencies.make :: dirs

ifndef QUICK
$(bin)TrackMonitors_dependencies.make : $(src)TrackTuple.cpp $(src)TrackPV2HalfMonitor.cpp $(src)TrackParticleMonitor.cpp $(src)PVSplit.cpp $(src)TrackMonitorBase.cpp $(src)TrackVertexMonitor.cpp $(src)OTCoordinates.cpp $(src)TrackMonitorNT.cpp $(src)STCoordinates.cpp $(src)TTTrackMonitor.cpp $(src)AlignmentOnlineMonitor.cpp $(src)TrackTune.cpp $(src)TrackITOverlapMonitor.cpp $(src)OTYAlignMagOff.cpp $(src)PVResMonitor.cpp $(src)ITTrackMonitor.cpp $(src)STYAlignMagOff.cpp $(src)STEfficiency.cpp $(src)TrackMonitor.cpp $(src)Map.cpp $(src)PitchResTool.cpp $(src)HitEffPlotter.cpp $(src)OTTrackMonitor.cpp $(src)TrackV0Monitor.cpp $(src)OTHitEfficiencyMonitor.cpp $(src)TrackTimingMonitor.cpp $(src)VertexCompare.cpp $(src)UTTrackMonitor.cpp $(src)TrackExpectedHitsXYZTool.cpp $(src)TrackAlignMonitor.cpp $(src)TrackDiMuonMonitor.cpp $(src)TrackCaloMatchMonitor.cpp $(src)TrackMuonMatchMonitor.cpp $(src)TrackVeloOverlapMonitor.cpp $(src)TrackFitMatchMonitor.cpp $(src)TrackMonitorTupleBase.cpp $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(echo) "(TrackMonitors.make) Rebuilding $@"; \
	  $(build_dependencies) TrackMonitors -all_sources -out=$@ $(src)TrackTuple.cpp $(src)TrackPV2HalfMonitor.cpp $(src)TrackParticleMonitor.cpp $(src)PVSplit.cpp $(src)TrackMonitorBase.cpp $(src)TrackVertexMonitor.cpp $(src)OTCoordinates.cpp $(src)TrackMonitorNT.cpp $(src)STCoordinates.cpp $(src)TTTrackMonitor.cpp $(src)AlignmentOnlineMonitor.cpp $(src)TrackTune.cpp $(src)TrackITOverlapMonitor.cpp $(src)OTYAlignMagOff.cpp $(src)PVResMonitor.cpp $(src)ITTrackMonitor.cpp $(src)STYAlignMagOff.cpp $(src)STEfficiency.cpp $(src)TrackMonitor.cpp $(src)Map.cpp $(src)PitchResTool.cpp $(src)HitEffPlotter.cpp $(src)OTTrackMonitor.cpp $(src)TrackV0Monitor.cpp $(src)OTHitEfficiencyMonitor.cpp $(src)TrackTimingMonitor.cpp $(src)VertexCompare.cpp $(src)UTTrackMonitor.cpp $(src)TrackExpectedHitsXYZTool.cpp $(src)TrackAlignMonitor.cpp $(src)TrackDiMuonMonitor.cpp $(src)TrackCaloMatchMonitor.cpp $(src)TrackMuonMatchMonitor.cpp $(src)TrackVeloOverlapMonitor.cpp $(src)TrackFitMatchMonitor.cpp $(src)TrackMonitorTupleBase.cpp
endif

#$(TrackMonitors_dependencies)

-include $(bin)TrackMonitors_dependencies.make

endif
endif
#-- end of dependency -------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackTuple.d
endif
endif


$(bin)$(binobj)TrackTuple.o $(bin)$(binobj)TrackTuple.d : $(src)TrackTuple.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackTuple.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackTuple_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackTuple_cppflags) $(TrackTuple_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackTuple.o -MT $(bin)$(binobj)TrackTuple.d -MF $(bin)$(binobj)TrackTuple.d -o $(bin)$(binobj)TrackTuple.o $(src)TrackTuple.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackPV2HalfMonitor.d
endif
endif


$(bin)$(binobj)TrackPV2HalfMonitor.o $(bin)$(binobj)TrackPV2HalfMonitor.d : $(src)TrackPV2HalfMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackPV2HalfMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackPV2HalfMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackPV2HalfMonitor_cppflags) $(TrackPV2HalfMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackPV2HalfMonitor.o -MT $(bin)$(binobj)TrackPV2HalfMonitor.d -MF $(bin)$(binobj)TrackPV2HalfMonitor.d -o $(bin)$(binobj)TrackPV2HalfMonitor.o $(src)TrackPV2HalfMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackParticleMonitor.d
endif
endif


$(bin)$(binobj)TrackParticleMonitor.o $(bin)$(binobj)TrackParticleMonitor.d : $(src)TrackParticleMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackParticleMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackParticleMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackParticleMonitor_cppflags) $(TrackParticleMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackParticleMonitor.o -MT $(bin)$(binobj)TrackParticleMonitor.d -MF $(bin)$(binobj)TrackParticleMonitor.d -o $(bin)$(binobj)TrackParticleMonitor.o $(src)TrackParticleMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)PVSplit.d
endif
endif


$(bin)$(binobj)PVSplit.o $(bin)$(binobj)PVSplit.d : $(src)PVSplit.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)PVSplit.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(PVSplit_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(PVSplit_cppflags) $(PVSplit_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)PVSplit.o -MT $(bin)$(binobj)PVSplit.d -MF $(bin)$(binobj)PVSplit.d -o $(bin)$(binobj)PVSplit.o $(src)PVSplit.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackMonitorBase.d
endif
endif


$(bin)$(binobj)TrackMonitorBase.o $(bin)$(binobj)TrackMonitorBase.d : $(src)TrackMonitorBase.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackMonitorBase.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackMonitorBase_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackMonitorBase_cppflags) $(TrackMonitorBase_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackMonitorBase.o -MT $(bin)$(binobj)TrackMonitorBase.d -MF $(bin)$(binobj)TrackMonitorBase.d -o $(bin)$(binobj)TrackMonitorBase.o $(src)TrackMonitorBase.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackVertexMonitor.d
endif
endif


$(bin)$(binobj)TrackVertexMonitor.o $(bin)$(binobj)TrackVertexMonitor.d : $(src)TrackVertexMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackVertexMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackVertexMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackVertexMonitor_cppflags) $(TrackVertexMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackVertexMonitor.o -MT $(bin)$(binobj)TrackVertexMonitor.d -MF $(bin)$(binobj)TrackVertexMonitor.d -o $(bin)$(binobj)TrackVertexMonitor.o $(src)TrackVertexMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)OTCoordinates.d
endif
endif


$(bin)$(binobj)OTCoordinates.o $(bin)$(binobj)OTCoordinates.d : $(src)OTCoordinates.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)OTCoordinates.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(OTCoordinates_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(OTCoordinates_cppflags) $(OTCoordinates_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)OTCoordinates.o -MT $(bin)$(binobj)OTCoordinates.d -MF $(bin)$(binobj)OTCoordinates.d -o $(bin)$(binobj)OTCoordinates.o $(src)OTCoordinates.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackMonitorNT.d
endif
endif


$(bin)$(binobj)TrackMonitorNT.o $(bin)$(binobj)TrackMonitorNT.d : $(src)TrackMonitorNT.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackMonitorNT.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackMonitorNT_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackMonitorNT_cppflags) $(TrackMonitorNT_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackMonitorNT.o -MT $(bin)$(binobj)TrackMonitorNT.d -MF $(bin)$(binobj)TrackMonitorNT.d -o $(bin)$(binobj)TrackMonitorNT.o $(src)TrackMonitorNT.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)STCoordinates.d
endif
endif


$(bin)$(binobj)STCoordinates.o $(bin)$(binobj)STCoordinates.d : $(src)STCoordinates.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)STCoordinates.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(STCoordinates_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(STCoordinates_cppflags) $(STCoordinates_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)STCoordinates.o -MT $(bin)$(binobj)STCoordinates.d -MF $(bin)$(binobj)STCoordinates.d -o $(bin)$(binobj)STCoordinates.o $(src)STCoordinates.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TTTrackMonitor.d
endif
endif


$(bin)$(binobj)TTTrackMonitor.o $(bin)$(binobj)TTTrackMonitor.d : $(src)TTTrackMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TTTrackMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TTTrackMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TTTrackMonitor_cppflags) $(TTTrackMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TTTrackMonitor.o -MT $(bin)$(binobj)TTTrackMonitor.d -MF $(bin)$(binobj)TTTrackMonitor.d -o $(bin)$(binobj)TTTrackMonitor.o $(src)TTTrackMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)AlignmentOnlineMonitor.d
endif
endif


$(bin)$(binobj)AlignmentOnlineMonitor.o $(bin)$(binobj)AlignmentOnlineMonitor.d : $(src)AlignmentOnlineMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)AlignmentOnlineMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(AlignmentOnlineMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(AlignmentOnlineMonitor_cppflags) $(AlignmentOnlineMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)AlignmentOnlineMonitor.o -MT $(bin)$(binobj)AlignmentOnlineMonitor.d -MF $(bin)$(binobj)AlignmentOnlineMonitor.d -o $(bin)$(binobj)AlignmentOnlineMonitor.o $(src)AlignmentOnlineMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackTune.d
endif
endif


$(bin)$(binobj)TrackTune.o $(bin)$(binobj)TrackTune.d : $(src)TrackTune.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackTune.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackTune_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackTune_cppflags) $(TrackTune_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackTune.o -MT $(bin)$(binobj)TrackTune.d -MF $(bin)$(binobj)TrackTune.d -o $(bin)$(binobj)TrackTune.o $(src)TrackTune.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackITOverlapMonitor.d
endif
endif


$(bin)$(binobj)TrackITOverlapMonitor.o $(bin)$(binobj)TrackITOverlapMonitor.d : $(src)TrackITOverlapMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackITOverlapMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackITOverlapMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackITOverlapMonitor_cppflags) $(TrackITOverlapMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackITOverlapMonitor.o -MT $(bin)$(binobj)TrackITOverlapMonitor.d -MF $(bin)$(binobj)TrackITOverlapMonitor.d -o $(bin)$(binobj)TrackITOverlapMonitor.o $(src)TrackITOverlapMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)OTYAlignMagOff.d
endif
endif


$(bin)$(binobj)OTYAlignMagOff.o $(bin)$(binobj)OTYAlignMagOff.d : $(src)OTYAlignMagOff.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)OTYAlignMagOff.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(OTYAlignMagOff_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(OTYAlignMagOff_cppflags) $(OTYAlignMagOff_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)OTYAlignMagOff.o -MT $(bin)$(binobj)OTYAlignMagOff.d -MF $(bin)$(binobj)OTYAlignMagOff.d -o $(bin)$(binobj)OTYAlignMagOff.o $(src)OTYAlignMagOff.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)PVResMonitor.d
endif
endif


$(bin)$(binobj)PVResMonitor.o $(bin)$(binobj)PVResMonitor.d : $(src)PVResMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)PVResMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(PVResMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(PVResMonitor_cppflags) $(PVResMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)PVResMonitor.o -MT $(bin)$(binobj)PVResMonitor.d -MF $(bin)$(binobj)PVResMonitor.d -o $(bin)$(binobj)PVResMonitor.o $(src)PVResMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)ITTrackMonitor.d
endif
endif


$(bin)$(binobj)ITTrackMonitor.o $(bin)$(binobj)ITTrackMonitor.d : $(src)ITTrackMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)ITTrackMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(ITTrackMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(ITTrackMonitor_cppflags) $(ITTrackMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)ITTrackMonitor.o -MT $(bin)$(binobj)ITTrackMonitor.d -MF $(bin)$(binobj)ITTrackMonitor.d -o $(bin)$(binobj)ITTrackMonitor.o $(src)ITTrackMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)STYAlignMagOff.d
endif
endif


$(bin)$(binobj)STYAlignMagOff.o $(bin)$(binobj)STYAlignMagOff.d : $(src)STYAlignMagOff.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)STYAlignMagOff.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(STYAlignMagOff_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(STYAlignMagOff_cppflags) $(STYAlignMagOff_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)STYAlignMagOff.o -MT $(bin)$(binobj)STYAlignMagOff.d -MF $(bin)$(binobj)STYAlignMagOff.d -o $(bin)$(binobj)STYAlignMagOff.o $(src)STYAlignMagOff.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)STEfficiency.d
endif
endif


$(bin)$(binobj)STEfficiency.o $(bin)$(binobj)STEfficiency.d : $(src)STEfficiency.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)STEfficiency.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(STEfficiency_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(STEfficiency_cppflags) $(STEfficiency_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)STEfficiency.o -MT $(bin)$(binobj)STEfficiency.d -MF $(bin)$(binobj)STEfficiency.d -o $(bin)$(binobj)STEfficiency.o $(src)STEfficiency.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackMonitor.d
endif
endif


$(bin)$(binobj)TrackMonitor.o $(bin)$(binobj)TrackMonitor.d : $(src)TrackMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackMonitor_cppflags) $(TrackMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackMonitor.o -MT $(bin)$(binobj)TrackMonitor.d -MF $(bin)$(binobj)TrackMonitor.d -o $(bin)$(binobj)TrackMonitor.o $(src)TrackMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)Map.d
endif
endif


$(bin)$(binobj)Map.o $(bin)$(binobj)Map.d : $(src)Map.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)Map.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(Map_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(Map_cppflags) $(Map_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)Map.o -MT $(bin)$(binobj)Map.d -MF $(bin)$(binobj)Map.d -o $(bin)$(binobj)Map.o $(src)Map.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)PitchResTool.d
endif
endif


$(bin)$(binobj)PitchResTool.o $(bin)$(binobj)PitchResTool.d : $(src)PitchResTool.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)PitchResTool.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(PitchResTool_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(PitchResTool_cppflags) $(PitchResTool_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)PitchResTool.o -MT $(bin)$(binobj)PitchResTool.d -MF $(bin)$(binobj)PitchResTool.d -o $(bin)$(binobj)PitchResTool.o $(src)PitchResTool.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)HitEffPlotter.d
endif
endif


$(bin)$(binobj)HitEffPlotter.o $(bin)$(binobj)HitEffPlotter.d : $(src)HitEffPlotter.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)HitEffPlotter.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(HitEffPlotter_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(HitEffPlotter_cppflags) $(HitEffPlotter_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)HitEffPlotter.o -MT $(bin)$(binobj)HitEffPlotter.d -MF $(bin)$(binobj)HitEffPlotter.d -o $(bin)$(binobj)HitEffPlotter.o $(src)HitEffPlotter.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)OTTrackMonitor.d
endif
endif


$(bin)$(binobj)OTTrackMonitor.o $(bin)$(binobj)OTTrackMonitor.d : $(src)OTTrackMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)OTTrackMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(OTTrackMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(OTTrackMonitor_cppflags) $(OTTrackMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)OTTrackMonitor.o -MT $(bin)$(binobj)OTTrackMonitor.d -MF $(bin)$(binobj)OTTrackMonitor.d -o $(bin)$(binobj)OTTrackMonitor.o $(src)OTTrackMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackV0Monitor.d
endif
endif


$(bin)$(binobj)TrackV0Monitor.o $(bin)$(binobj)TrackV0Monitor.d : $(src)TrackV0Monitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackV0Monitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackV0Monitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackV0Monitor_cppflags) $(TrackV0Monitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackV0Monitor.o -MT $(bin)$(binobj)TrackV0Monitor.d -MF $(bin)$(binobj)TrackV0Monitor.d -o $(bin)$(binobj)TrackV0Monitor.o $(src)TrackV0Monitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)OTHitEfficiencyMonitor.d
endif
endif


$(bin)$(binobj)OTHitEfficiencyMonitor.o $(bin)$(binobj)OTHitEfficiencyMonitor.d : $(src)OTHitEfficiencyMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)OTHitEfficiencyMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(OTHitEfficiencyMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(OTHitEfficiencyMonitor_cppflags) $(OTHitEfficiencyMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)OTHitEfficiencyMonitor.o -MT $(bin)$(binobj)OTHitEfficiencyMonitor.d -MF $(bin)$(binobj)OTHitEfficiencyMonitor.d -o $(bin)$(binobj)OTHitEfficiencyMonitor.o $(src)OTHitEfficiencyMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackTimingMonitor.d
endif
endif


$(bin)$(binobj)TrackTimingMonitor.o $(bin)$(binobj)TrackTimingMonitor.d : $(src)TrackTimingMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackTimingMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackTimingMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackTimingMonitor_cppflags) $(TrackTimingMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackTimingMonitor.o -MT $(bin)$(binobj)TrackTimingMonitor.d -MF $(bin)$(binobj)TrackTimingMonitor.d -o $(bin)$(binobj)TrackTimingMonitor.o $(src)TrackTimingMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)VertexCompare.d
endif
endif


$(bin)$(binobj)VertexCompare.o $(bin)$(binobj)VertexCompare.d : $(src)VertexCompare.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)VertexCompare.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(VertexCompare_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(VertexCompare_cppflags) $(VertexCompare_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)VertexCompare.o -MT $(bin)$(binobj)VertexCompare.d -MF $(bin)$(binobj)VertexCompare.d -o $(bin)$(binobj)VertexCompare.o $(src)VertexCompare.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)UTTrackMonitor.d
endif
endif


$(bin)$(binobj)UTTrackMonitor.o $(bin)$(binobj)UTTrackMonitor.d : $(src)UTTrackMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)UTTrackMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(UTTrackMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(UTTrackMonitor_cppflags) $(UTTrackMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)UTTrackMonitor.o -MT $(bin)$(binobj)UTTrackMonitor.d -MF $(bin)$(binobj)UTTrackMonitor.d -o $(bin)$(binobj)UTTrackMonitor.o $(src)UTTrackMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackExpectedHitsXYZTool.d
endif
endif


$(bin)$(binobj)TrackExpectedHitsXYZTool.o $(bin)$(binobj)TrackExpectedHitsXYZTool.d : $(src)TrackExpectedHitsXYZTool.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackExpectedHitsXYZTool.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackExpectedHitsXYZTool_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackExpectedHitsXYZTool_cppflags) $(TrackExpectedHitsXYZTool_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackExpectedHitsXYZTool.o -MT $(bin)$(binobj)TrackExpectedHitsXYZTool.d -MF $(bin)$(binobj)TrackExpectedHitsXYZTool.d -o $(bin)$(binobj)TrackExpectedHitsXYZTool.o $(src)TrackExpectedHitsXYZTool.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackAlignMonitor.d
endif
endif


$(bin)$(binobj)TrackAlignMonitor.o $(bin)$(binobj)TrackAlignMonitor.d : $(src)TrackAlignMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackAlignMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackAlignMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackAlignMonitor_cppflags) $(TrackAlignMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackAlignMonitor.o -MT $(bin)$(binobj)TrackAlignMonitor.d -MF $(bin)$(binobj)TrackAlignMonitor.d -o $(bin)$(binobj)TrackAlignMonitor.o $(src)TrackAlignMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackDiMuonMonitor.d
endif
endif


$(bin)$(binobj)TrackDiMuonMonitor.o $(bin)$(binobj)TrackDiMuonMonitor.d : $(src)TrackDiMuonMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackDiMuonMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackDiMuonMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackDiMuonMonitor_cppflags) $(TrackDiMuonMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackDiMuonMonitor.o -MT $(bin)$(binobj)TrackDiMuonMonitor.d -MF $(bin)$(binobj)TrackDiMuonMonitor.d -o $(bin)$(binobj)TrackDiMuonMonitor.o $(src)TrackDiMuonMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackCaloMatchMonitor.d
endif
endif


$(bin)$(binobj)TrackCaloMatchMonitor.o $(bin)$(binobj)TrackCaloMatchMonitor.d : $(src)TrackCaloMatchMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackCaloMatchMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackCaloMatchMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackCaloMatchMonitor_cppflags) $(TrackCaloMatchMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackCaloMatchMonitor.o -MT $(bin)$(binobj)TrackCaloMatchMonitor.d -MF $(bin)$(binobj)TrackCaloMatchMonitor.d -o $(bin)$(binobj)TrackCaloMatchMonitor.o $(src)TrackCaloMatchMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackMuonMatchMonitor.d
endif
endif


$(bin)$(binobj)TrackMuonMatchMonitor.o $(bin)$(binobj)TrackMuonMatchMonitor.d : $(src)TrackMuonMatchMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackMuonMatchMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackMuonMatchMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackMuonMatchMonitor_cppflags) $(TrackMuonMatchMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackMuonMatchMonitor.o -MT $(bin)$(binobj)TrackMuonMatchMonitor.d -MF $(bin)$(binobj)TrackMuonMatchMonitor.d -o $(bin)$(binobj)TrackMuonMatchMonitor.o $(src)TrackMuonMatchMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackVeloOverlapMonitor.d
endif
endif


$(bin)$(binobj)TrackVeloOverlapMonitor.o $(bin)$(binobj)TrackVeloOverlapMonitor.d : $(src)TrackVeloOverlapMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackVeloOverlapMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackVeloOverlapMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackVeloOverlapMonitor_cppflags) $(TrackVeloOverlapMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackVeloOverlapMonitor.o -MT $(bin)$(binobj)TrackVeloOverlapMonitor.d -MF $(bin)$(binobj)TrackVeloOverlapMonitor.d -o $(bin)$(binobj)TrackVeloOverlapMonitor.o $(src)TrackVeloOverlapMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackFitMatchMonitor.d
endif
endif


$(bin)$(binobj)TrackFitMatchMonitor.o $(bin)$(binobj)TrackFitMatchMonitor.d : $(src)TrackFitMatchMonitor.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackFitMatchMonitor.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackFitMatchMonitor_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackFitMatchMonitor_cppflags) $(TrackFitMatchMonitor_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackFitMatchMonitor.o -MT $(bin)$(binobj)TrackFitMatchMonitor.d -MF $(bin)$(binobj)TrackFitMatchMonitor.d -o $(bin)$(binobj)TrackFitMatchMonitor.o $(src)TrackFitMatchMonitor.cpp


#-- end of cpp_library ------------------
#-- start of cpp_library -----------------

ifneq ($(MAKECMDGOALS),TrackMonitorsclean)
ifneq ($(MAKECMDGOALS),uninstall)
-include $(bin)$(binobj)TrackMonitorTupleBase.d
endif
endif


$(bin)$(binobj)TrackMonitorTupleBase.o $(bin)$(binobj)TrackMonitorTupleBase.d : $(src)TrackMonitorTupleBase.cpp  $(use_requirements) $(cmt_final_setup_TrackMonitors)
	$(cpp_echo) $(src)TrackMonitorTupleBase.cpp
	@mkdir -p $(@D)
	$(cpp_silent) $(cppcomp) $(use_pp_cppflags) $(TrackMonitors_pp_cppflags) $(app_TrackMonitors_pp_cppflags) $(TrackMonitorTupleBase_pp_cppflags) $(use_cppflags) $(TrackMonitors_cppflags) $(lib_TrackMonitors_cppflags) $(app_TrackMonitors_cppflags) $(TrackMonitorTupleBase_cppflags) $(TrackMonitorTupleBase_cpp_cppflags)  -MP -MMD -MT $(bin)$(binobj)TrackMonitorTupleBase.o -MT $(bin)$(binobj)TrackMonitorTupleBase.d -MF $(bin)$(binobj)TrackMonitorTupleBase.d -o $(bin)$(binobj)TrackMonitorTupleBase.o $(src)TrackMonitorTupleBase.cpp


#-- end of cpp_library ------------------
#-- start of cleanup_header --------------

clean :: TrackMonitorsclean ;
#	@cd .

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(TrackMonitors.make) $@: No rule for such target" >&2
#	@echo "#CMT> Warning: $@: No rule for such target" >&2; exit
	if echo $@ | grep '$(package)setup\.make$$' >/dev/null; then\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitors.make): $@: File no longer generated" >&2; exit 0; fi
else
.DEFAULT::
	$(echo) "(TrackMonitors.make) PEDANTIC: $@: No rule for such target" >&2
	if echo $@ | grep '$(package)setup\.make$$' >/dev/null; then\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitors.make): $@: File no longer generated" >&2; exit 0;\
	 elif test $@ = "$(cmt_final_setup)" -o\
	 $@ = "$(cmt_final_setup_TrackMonitors)" ; then\
	 found=n; for s in 1 2 3 4 5; do\
	 sleep $$s; test ! -f $@ || { found=y; break; }\
	 done; if test $$found = n; then\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitors.make) PEDANTIC: $@: Seems to be missing. Ignore it for now" >&2; exit 0 ; fi;\
	 elif test `expr $@ : '.*/'` -ne 0 ; then\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitors.make) PEDANTIC: $@: Seems to be a missing file. Please check" >&2; exit 2 ; \
	 else\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitors.make) PEDANTIC: $@: Seems to be a fake target due to some pattern. Just ignore it" >&2 ; exit 0; fi
endif

TrackMonitorsclean ::
#-- end of cleanup_header ---------------
#-- start of cleanup_library -------------
	$(cleanup_echo) library TrackMonitors
	-$(cleanup_silent) cd $(bin); /bin/rm -f $(library_prefix)TrackMonitors$(library_suffix).a $(library_prefix)TrackMonitors$(library_suffix).s? TrackMonitors.stamp TrackMonitors.shstamp
#-- end of cleanup_library ---------------
