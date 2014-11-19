
#-- start of constituents_header ------

include ${CMTROOT}/src/Makefile.core

ifdef tag
CMTEXTRATAGS = $(tag)
else
tag       = $(CMTCONFIG)
endif

tags      = $(tag),$(CMTEXTRATAGS)

TrackMonitors_tag = $(tag)

#cmt_local_tagfile = $(TrackMonitors_tag).make
cmt_local_tagfile = $(bin)$(TrackMonitors_tag).make

#-include $(cmt_local_tagfile)
include $(cmt_local_tagfile)

#cmt_local_setup = $(bin)setup$$$$.make
#cmt_local_setup = $(bin)$(package)setup$$$$.make
#cmt_final_setup = $(bin)TrackMonitorssetup.make
cmt_final_setup = $(bin)setup.make
#cmt_final_setup = $(bin)$(package)setup.make

#--------------------------------------------------------

#cmt_lock_setup = /tmp/lock$(cmt_lock_pid).make
#cmt_temp_tag = /tmp/tag$(cmt_lock_pid).make

#first :: $(cmt_local_tagfile)
#	@echo $(cmt_local_tagfile) ok
#ifndef QUICK
#first :: $(cmt_final_setup) ;
#else
#first :: ;
#endif

##	@bin=`$(cmtexe) show macro_value bin`

#$(cmt_local_tagfile) : $(cmt_lock_setup)
#	@echo "#CMT> Error: $@: No such file" >&2; exit 1
#$(cmt_local_tagfile) :
#	@echo "#CMT> Warning: $@: No such file" >&2; exit
#	@echo "#CMT> Info: $@: No need to rebuild file" >&2; exit

#$(cmt_final_setup) : $(cmt_local_tagfile) 
#	$(echo) "(constituents.make) Rebuilding $@"
#	@if test ! -d $(@D); then $(mkdir) -p $(@D); fi; \
#	  if test -f $(cmt_local_setup); then /bin/rm -f $(cmt_local_setup); fi; \
#	  trap '/bin/rm -f $(cmt_local_setup)' 0 1 2 15; \
#	  $(cmtexe) -tag=$(tags) show setup >>$(cmt_local_setup); \
#	  if test ! -f $@; then \
#	    mv $(cmt_local_setup) $@; \
#	  else \
#	    if /usr/bin/diff $(cmt_local_setup) $@ >/dev/null ; then \
#	      : ; \
#	    else \
#	      mv $(cmt_local_setup) $@; \
#	    fi; \
#	  fi

#	@/bin/echo $@ ok   

#config :: checkuses
#	@exit 0
#checkuses : ;

env.make ::
	printenv >env.make.tmp; $(cmtexe) check files env.make.tmp env.make

ifndef QUICK
all :: build_library_links
	$(echo) "(constituents.make) all done"
endif

javadirs ::
	@if test ! -d $(javabin) ; then $(mkdir) -p $(javabin) ; fi

srcdirs ::
	@if test ! -d $(src) ; then $(mkdir) -p $(src) ; fi

dirs :: requirements
	@if test ! -d $(bin) ; then $(mkdir) -p $(bin) ; fi
#	@if test ! -r requirements ; then echo "No requirements file" ; fi; \
#	  if test ! -d $(bin) ; then $(mkdir) -p $(bin) ; fi

requirements :
	@if test ! -r requirements ; then echo "No requirements file" ; fi

build_library_links : dirs
	$(echo) "(constituents.make) Rebuilding library links"; \
	 $(build_library_links)
#	if test ! -d $(bin) ; then $(mkdir) -p $(bin) ; fi; \
#	$(build_library_links)

makefiles : ;

.DEFAULT ::
	$(echo) "(constituents.make) $@: No rule for such target" >&2
#	@echo "#CMT> Warning: $@: Using default commands" >&2; exit

#	@if test "$@" = "$(cmt_lock_setup)"; then \
	#  /bin/rm -f $(cmt_lock_setup); \
	 # touch $(cmt_lock_setup); \
	#fi

#-- end of constituents_header ------
#-- start of group ------

all_groups :: all

all :: $(all_dependencies)  $(all_pre_constituents) $(all_constituents)  $(all_post_constituents)
	$(echo) "all ok."

#	@/bin/echo " all ok."

clean :: allclean

allclean ::  $(all_constituentsclean)
	$(echo) $(all_constituentsclean)
	$(echo) "allclean ok."

#	@echo $(all_constituentsclean)
#	@/bin/echo " allclean ok."

allclean :: makefilesclean

#-- end of group ------
#-- start of group ------

all_groups :: cmt_actions

cmt_actions :: $(cmt_actions_dependencies)  $(cmt_actions_pre_constituents) $(cmt_actions_constituents)  $(cmt_actions_post_constituents)
	$(echo) "cmt_actions ok."

#	@/bin/echo " cmt_actions ok."

clean :: allclean

cmt_actionsclean ::  $(cmt_actions_constituentsclean)
	$(echo) $(cmt_actions_constituentsclean)
	$(echo) "cmt_actionsclean ok."

#	@echo $(cmt_actions_constituentsclean)
#	@/bin/echo " cmt_actionsclean ok."

cmt_actionsclean :: makefilesclean

#-- end of group ------
#-- start of constituent ------

cmt_TrackMonitors_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitors_has_target_tag

#cmt_local_tagfile_TrackMonitors = $(TrackMonitors_tag)_TrackMonitors.make
cmt_local_tagfile_TrackMonitors = $(bin)$(TrackMonitors_tag)_TrackMonitors.make
cmt_local_setup_TrackMonitors = $(bin)setup_TrackMonitors$$$$.make
cmt_final_setup_TrackMonitors = $(bin)setup_TrackMonitors.make
#cmt_final_setup_TrackMonitors = $(bin)TrackMonitors_TrackMonitorssetup.make
cmt_local_TrackMonitors_makefile = $(bin)TrackMonitors.make

TrackMonitors_extratags = -tag_add=target_TrackMonitors

#$(cmt_local_tagfile_TrackMonitors) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_TrackMonitors) ::
else
$(cmt_local_tagfile_TrackMonitors) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_TrackMonitors); then /bin/rm -f $(cmt_local_tagfile_TrackMonitors); fi ; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitors_extratags) build tag_makefile >>$(cmt_local_tagfile_TrackMonitors)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_TrackMonitors)"; \
	  test ! -f $(cmt_local_setup_TrackMonitors) || \rm -f $(cmt_local_setup_TrackMonitors); \
	  trap '\rm -f $(cmt_local_setup_TrackMonitors)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitors_extratags) show setup >$(cmt_local_setup_TrackMonitors) && \
	  if [ -f $(cmt_final_setup_TrackMonitors) ] && \
	    \cmp -s $(cmt_final_setup_TrackMonitors) $(cmt_local_setup_TrackMonitors); then \
	    \rm $(cmt_local_setup_TrackMonitors); else \
	    \mv -f $(cmt_local_setup_TrackMonitors) $(cmt_final_setup_TrackMonitors); fi

else

#cmt_local_tagfile_TrackMonitors = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitors = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_TrackMonitors = $(bin)setup.make
#cmt_final_setup_TrackMonitors = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitors_makefile = $(bin)TrackMonitors.make

endif

ifdef STRUCTURED_OUTPUT
TrackMonitorsdirs :
	@if test ! -d $(bin)TrackMonitors; then $(mkdir) -p $(bin)TrackMonitors; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitors
else
TrackMonitorsdirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# TrackMonitorsdirs ::
#	@if test ! -d $(bin)TrackMonitors; then $(mkdir) -p $(bin)TrackMonitors; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitors
#
#$(cmt_local_TrackMonitors_makefile) :: $(TrackMonitors_dependencies) $(cmt_local_tagfile_TrackMonitors) build_library_links dirs TrackMonitorsdirs
#else
#$(cmt_local_TrackMonitors_makefile) :: $(TrackMonitors_dependencies) $(cmt_local_tagfile_TrackMonitors) build_library_links dirs
#endif
#else
#$(cmt_local_TrackMonitors_makefile) :: $(cmt_local_tagfile_TrackMonitors)
#endif

makefiles : $(cmt_local_TrackMonitors_makefile)

ifndef QUICK
$(cmt_local_TrackMonitors_makefile) : $(TrackMonitors_dependencies) $(cmt_local_tagfile_TrackMonitors) build_library_links
else
$(cmt_local_TrackMonitors_makefile) : $(cmt_local_tagfile_TrackMonitors)
endif
	$(echo) "(constituents.make) Building TrackMonitors.make"; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitors_extratags) build constituent_makefile -out=$(cmt_local_TrackMonitors_makefile) TrackMonitors

TrackMonitors :: $(TrackMonitors_dependencies) $(cmt_local_TrackMonitors_makefile) dirs TrackMonitorsdirs
	$(echo) "(constituents.make) Starting TrackMonitors"
	@$(MAKE) -f $(cmt_local_TrackMonitors_makefile) TrackMonitors
	$(echo) "(constituents.make) TrackMonitors done"

clean :: TrackMonitorsclean

TrackMonitorsclean :: $(TrackMonitorsclean_dependencies) ##$(cmt_local_TrackMonitors_makefile)
	$(echo) "(constituents.make) Starting TrackMonitorsclean"
	@-if test -f $(cmt_local_TrackMonitors_makefile); then \
	  $(MAKE) -f $(cmt_local_TrackMonitors_makefile) TrackMonitorsclean; \
	fi
	$(echo) "(constituents.make) TrackMonitorsclean done"
#	@-$(MAKE) -f $(cmt_local_TrackMonitors_makefile) TrackMonitorsclean

##	  /bin/rm -f $(cmt_local_TrackMonitors_makefile) $(bin)TrackMonitors_dependencies.make

install :: TrackMonitorsinstall

TrackMonitorsinstall :: $(TrackMonitors_dependencies) $(cmt_local_TrackMonitors_makefile)
	$(echo) "(constituents.make) Starting install TrackMonitors"
	@-$(MAKE) -f $(cmt_local_TrackMonitors_makefile) install
	$(echo) "(constituents.make) install TrackMonitors done"

uninstall :: TrackMonitorsuninstall

$(foreach d,$(TrackMonitors_dependencies),$(eval $(d)uninstall_dependencies += TrackMonitorsuninstall))

TrackMonitorsuninstall :: $(TrackMonitorsuninstall_dependencies) $(cmt_local_TrackMonitors_makefile)
	$(echo) "(constituents.make) Starting uninstall TrackMonitors"
	@$(MAKE) -f $(cmt_local_TrackMonitors_makefile) uninstall
	$(echo) "(constituents.make) uninstall TrackMonitors done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ TrackMonitors"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ TrackMonitors done"
endif

#-- end of constituent ------
#-- start of constituent_lock ------

cmt_TrackMonitorsRootMap_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitorsRootMap_has_target_tag

#cmt_local_tagfile_TrackMonitorsRootMap = $(TrackMonitors_tag)_TrackMonitorsRootMap.make
cmt_local_tagfile_TrackMonitorsRootMap = $(bin)$(TrackMonitors_tag)_TrackMonitorsRootMap.make
cmt_local_setup_TrackMonitorsRootMap = $(bin)setup_TrackMonitorsRootMap$$$$.make
cmt_final_setup_TrackMonitorsRootMap = $(bin)setup_TrackMonitorsRootMap.make
#cmt_final_setup_TrackMonitorsRootMap = $(bin)TrackMonitors_TrackMonitorsRootMapsetup.make
cmt_local_TrackMonitorsRootMap_makefile = $(bin)TrackMonitorsRootMap.make

TrackMonitorsRootMap_extratags = -tag_add=target_TrackMonitorsRootMap

#$(cmt_local_tagfile_TrackMonitorsRootMap) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_TrackMonitorsRootMap) ::
else
$(cmt_local_tagfile_TrackMonitorsRootMap) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_TrackMonitorsRootMap); then /bin/rm -f $(cmt_local_tagfile_TrackMonitorsRootMap); fi ; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsRootMap_extratags) build tag_makefile >>$(cmt_local_tagfile_TrackMonitorsRootMap)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_TrackMonitorsRootMap)"; \
	  test ! -f $(cmt_local_setup_TrackMonitorsRootMap) || \rm -f $(cmt_local_setup_TrackMonitorsRootMap); \
	  trap '\rm -f $(cmt_local_setup_TrackMonitorsRootMap)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsRootMap_extratags) show setup >$(cmt_local_setup_TrackMonitorsRootMap) && \
	  if [ -f $(cmt_final_setup_TrackMonitorsRootMap) ] && \
	    \cmp -s $(cmt_final_setup_TrackMonitorsRootMap) $(cmt_local_setup_TrackMonitorsRootMap); then \
	    \rm $(cmt_local_setup_TrackMonitorsRootMap); else \
	    \mv -f $(cmt_local_setup_TrackMonitorsRootMap) $(cmt_final_setup_TrackMonitorsRootMap); fi

else

#cmt_local_tagfile_TrackMonitorsRootMap = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitorsRootMap = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_TrackMonitorsRootMap = $(bin)setup.make
#cmt_final_setup_TrackMonitorsRootMap = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitorsRootMap_makefile = $(bin)TrackMonitorsRootMap.make

endif

ifdef STRUCTURED_OUTPUT
TrackMonitorsRootMapdirs :
	@if test ! -d $(bin)TrackMonitorsRootMap; then $(mkdir) -p $(bin)TrackMonitorsRootMap; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsRootMap
else
TrackMonitorsRootMapdirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# TrackMonitorsRootMapdirs ::
#	@if test ! -d $(bin)TrackMonitorsRootMap; then $(mkdir) -p $(bin)TrackMonitorsRootMap; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsRootMap
#
#$(cmt_local_TrackMonitorsRootMap_makefile) :: $(TrackMonitorsRootMap_dependencies) $(cmt_local_tagfile_TrackMonitorsRootMap) build_library_links dirs TrackMonitorsRootMapdirs
#else
#$(cmt_local_TrackMonitorsRootMap_makefile) :: $(TrackMonitorsRootMap_dependencies) $(cmt_local_tagfile_TrackMonitorsRootMap) build_library_links dirs
#endif
#else
#$(cmt_local_TrackMonitorsRootMap_makefile) :: $(cmt_local_tagfile_TrackMonitorsRootMap)
#endif

makefiles : $(cmt_local_TrackMonitorsRootMap_makefile)

ifndef QUICK
$(cmt_local_TrackMonitorsRootMap_makefile) : $(TrackMonitorsRootMap_dependencies) $(cmt_local_tagfile_TrackMonitorsRootMap) build_library_links
else
$(cmt_local_TrackMonitorsRootMap_makefile) : $(cmt_local_tagfile_TrackMonitorsRootMap)
endif
	$(echo) "(constituents.make) Building TrackMonitorsRootMap.make"; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsRootMap_extratags) build constituent_makefile -out=$(cmt_local_TrackMonitorsRootMap_makefile) TrackMonitorsRootMap

TrackMonitorsRootMap :: $(TrackMonitorsRootMap_dependencies) $(cmt_local_TrackMonitorsRootMap_makefile) dirs TrackMonitorsRootMapdirs
	$(echo) "(constituents.make) Creating TrackMonitorsRootMap${lock_suffix} and Starting TrackMonitorsRootMap"
	@${lock_command} TrackMonitorsRootMap${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} TrackMonitorsRootMap${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_TrackMonitorsRootMap_makefile) TrackMonitorsRootMap; \
	  retval=$$?; ${unlock_command} TrackMonitorsRootMap${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) TrackMonitorsRootMap done"

clean :: TrackMonitorsRootMapclean

TrackMonitorsRootMapclean :: $(TrackMonitorsRootMapclean_dependencies) ##$(cmt_local_TrackMonitorsRootMap_makefile)
	$(echo) "(constituents.make) Starting TrackMonitorsRootMapclean"
	@-if test -f $(cmt_local_TrackMonitorsRootMap_makefile); then \
	  $(MAKE) -f $(cmt_local_TrackMonitorsRootMap_makefile) TrackMonitorsRootMapclean; \
	fi
	$(echo) "(constituents.make) TrackMonitorsRootMapclean done"
#	@-$(MAKE) -f $(cmt_local_TrackMonitorsRootMap_makefile) TrackMonitorsRootMapclean

##	  /bin/rm -f $(cmt_local_TrackMonitorsRootMap_makefile) $(bin)TrackMonitorsRootMap_dependencies.make

install :: TrackMonitorsRootMapinstall

TrackMonitorsRootMapinstall :: $(TrackMonitorsRootMap_dependencies) $(cmt_local_TrackMonitorsRootMap_makefile)
	$(echo) "(constituents.make) Starting install TrackMonitorsRootMap"
	@-$(MAKE) -f $(cmt_local_TrackMonitorsRootMap_makefile) install
	$(echo) "(constituents.make) install TrackMonitorsRootMap done"

uninstall :: TrackMonitorsRootMapuninstall

$(foreach d,$(TrackMonitorsRootMap_dependencies),$(eval $(d)uninstall_dependencies += TrackMonitorsRootMapuninstall))

TrackMonitorsRootMapuninstall :: $(TrackMonitorsRootMapuninstall_dependencies) $(cmt_local_TrackMonitorsRootMap_makefile)
	$(echo) "(constituents.make) Starting uninstall TrackMonitorsRootMap"
	@$(MAKE) -f $(cmt_local_TrackMonitorsRootMap_makefile) uninstall
	$(echo) "(constituents.make) uninstall TrackMonitorsRootMap done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ TrackMonitorsRootMap"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ TrackMonitorsRootMap done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_TrackMonitorsMergeMap_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitorsMergeMap_has_target_tag

#cmt_local_tagfile_TrackMonitorsMergeMap = $(TrackMonitors_tag)_TrackMonitorsMergeMap.make
cmt_local_tagfile_TrackMonitorsMergeMap = $(bin)$(TrackMonitors_tag)_TrackMonitorsMergeMap.make
cmt_local_setup_TrackMonitorsMergeMap = $(bin)setup_TrackMonitorsMergeMap$$$$.make
cmt_final_setup_TrackMonitorsMergeMap = $(bin)setup_TrackMonitorsMergeMap.make
#cmt_final_setup_TrackMonitorsMergeMap = $(bin)TrackMonitors_TrackMonitorsMergeMapsetup.make
cmt_local_TrackMonitorsMergeMap_makefile = $(bin)TrackMonitorsMergeMap.make

TrackMonitorsMergeMap_extratags = -tag_add=target_TrackMonitorsMergeMap

#$(cmt_local_tagfile_TrackMonitorsMergeMap) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_TrackMonitorsMergeMap) ::
else
$(cmt_local_tagfile_TrackMonitorsMergeMap) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_TrackMonitorsMergeMap); then /bin/rm -f $(cmt_local_tagfile_TrackMonitorsMergeMap); fi ; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsMergeMap_extratags) build tag_makefile >>$(cmt_local_tagfile_TrackMonitorsMergeMap)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_TrackMonitorsMergeMap)"; \
	  test ! -f $(cmt_local_setup_TrackMonitorsMergeMap) || \rm -f $(cmt_local_setup_TrackMonitorsMergeMap); \
	  trap '\rm -f $(cmt_local_setup_TrackMonitorsMergeMap)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsMergeMap_extratags) show setup >$(cmt_local_setup_TrackMonitorsMergeMap) && \
	  if [ -f $(cmt_final_setup_TrackMonitorsMergeMap) ] && \
	    \cmp -s $(cmt_final_setup_TrackMonitorsMergeMap) $(cmt_local_setup_TrackMonitorsMergeMap); then \
	    \rm $(cmt_local_setup_TrackMonitorsMergeMap); else \
	    \mv -f $(cmt_local_setup_TrackMonitorsMergeMap) $(cmt_final_setup_TrackMonitorsMergeMap); fi

else

#cmt_local_tagfile_TrackMonitorsMergeMap = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitorsMergeMap = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_TrackMonitorsMergeMap = $(bin)setup.make
#cmt_final_setup_TrackMonitorsMergeMap = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitorsMergeMap_makefile = $(bin)TrackMonitorsMergeMap.make

endif

ifdef STRUCTURED_OUTPUT
TrackMonitorsMergeMapdirs :
	@if test ! -d $(bin)TrackMonitorsMergeMap; then $(mkdir) -p $(bin)TrackMonitorsMergeMap; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsMergeMap
else
TrackMonitorsMergeMapdirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# TrackMonitorsMergeMapdirs ::
#	@if test ! -d $(bin)TrackMonitorsMergeMap; then $(mkdir) -p $(bin)TrackMonitorsMergeMap; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsMergeMap
#
#$(cmt_local_TrackMonitorsMergeMap_makefile) :: $(TrackMonitorsMergeMap_dependencies) $(cmt_local_tagfile_TrackMonitorsMergeMap) build_library_links dirs TrackMonitorsMergeMapdirs
#else
#$(cmt_local_TrackMonitorsMergeMap_makefile) :: $(TrackMonitorsMergeMap_dependencies) $(cmt_local_tagfile_TrackMonitorsMergeMap) build_library_links dirs
#endif
#else
#$(cmt_local_TrackMonitorsMergeMap_makefile) :: $(cmt_local_tagfile_TrackMonitorsMergeMap)
#endif

makefiles : $(cmt_local_TrackMonitorsMergeMap_makefile)

ifndef QUICK
$(cmt_local_TrackMonitorsMergeMap_makefile) : $(TrackMonitorsMergeMap_dependencies) $(cmt_local_tagfile_TrackMonitorsMergeMap) build_library_links
else
$(cmt_local_TrackMonitorsMergeMap_makefile) : $(cmt_local_tagfile_TrackMonitorsMergeMap)
endif
	$(echo) "(constituents.make) Building TrackMonitorsMergeMap.make"; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsMergeMap_extratags) build constituent_makefile -out=$(cmt_local_TrackMonitorsMergeMap_makefile) TrackMonitorsMergeMap

TrackMonitorsMergeMap :: $(TrackMonitorsMergeMap_dependencies) $(cmt_local_TrackMonitorsMergeMap_makefile) dirs TrackMonitorsMergeMapdirs
	$(echo) "(constituents.make) Creating TrackMonitorsMergeMap${lock_suffix} and Starting TrackMonitorsMergeMap"
	@${lock_command} TrackMonitorsMergeMap${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} TrackMonitorsMergeMap${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_TrackMonitorsMergeMap_makefile) TrackMonitorsMergeMap; \
	  retval=$$?; ${unlock_command} TrackMonitorsMergeMap${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) TrackMonitorsMergeMap done"

clean :: TrackMonitorsMergeMapclean

TrackMonitorsMergeMapclean :: $(TrackMonitorsMergeMapclean_dependencies) ##$(cmt_local_TrackMonitorsMergeMap_makefile)
	$(echo) "(constituents.make) Starting TrackMonitorsMergeMapclean"
	@-if test -f $(cmt_local_TrackMonitorsMergeMap_makefile); then \
	  $(MAKE) -f $(cmt_local_TrackMonitorsMergeMap_makefile) TrackMonitorsMergeMapclean; \
	fi
	$(echo) "(constituents.make) TrackMonitorsMergeMapclean done"
#	@-$(MAKE) -f $(cmt_local_TrackMonitorsMergeMap_makefile) TrackMonitorsMergeMapclean

##	  /bin/rm -f $(cmt_local_TrackMonitorsMergeMap_makefile) $(bin)TrackMonitorsMergeMap_dependencies.make

install :: TrackMonitorsMergeMapinstall

TrackMonitorsMergeMapinstall :: $(TrackMonitorsMergeMap_dependencies) $(cmt_local_TrackMonitorsMergeMap_makefile)
	$(echo) "(constituents.make) Starting install TrackMonitorsMergeMap"
	@-$(MAKE) -f $(cmt_local_TrackMonitorsMergeMap_makefile) install
	$(echo) "(constituents.make) install TrackMonitorsMergeMap done"

uninstall :: TrackMonitorsMergeMapuninstall

$(foreach d,$(TrackMonitorsMergeMap_dependencies),$(eval $(d)uninstall_dependencies += TrackMonitorsMergeMapuninstall))

TrackMonitorsMergeMapuninstall :: $(TrackMonitorsMergeMapuninstall_dependencies) $(cmt_local_TrackMonitorsMergeMap_makefile)
	$(echo) "(constituents.make) Starting uninstall TrackMonitorsMergeMap"
	@$(MAKE) -f $(cmt_local_TrackMonitorsMergeMap_makefile) uninstall
	$(echo) "(constituents.make) uninstall TrackMonitorsMergeMap done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ TrackMonitorsMergeMap"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ TrackMonitorsMergeMap done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_TrackMonitorsConf_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitorsConf_has_target_tag

#cmt_local_tagfile_TrackMonitorsConf = $(TrackMonitors_tag)_TrackMonitorsConf.make
cmt_local_tagfile_TrackMonitorsConf = $(bin)$(TrackMonitors_tag)_TrackMonitorsConf.make
cmt_local_setup_TrackMonitorsConf = $(bin)setup_TrackMonitorsConf$$$$.make
cmt_final_setup_TrackMonitorsConf = $(bin)setup_TrackMonitorsConf.make
#cmt_final_setup_TrackMonitorsConf = $(bin)TrackMonitors_TrackMonitorsConfsetup.make
cmt_local_TrackMonitorsConf_makefile = $(bin)TrackMonitorsConf.make

TrackMonitorsConf_extratags = -tag_add=target_TrackMonitorsConf

#$(cmt_local_tagfile_TrackMonitorsConf) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_TrackMonitorsConf) ::
else
$(cmt_local_tagfile_TrackMonitorsConf) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_TrackMonitorsConf); then /bin/rm -f $(cmt_local_tagfile_TrackMonitorsConf); fi ; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsConf_extratags) build tag_makefile >>$(cmt_local_tagfile_TrackMonitorsConf)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_TrackMonitorsConf)"; \
	  test ! -f $(cmt_local_setup_TrackMonitorsConf) || \rm -f $(cmt_local_setup_TrackMonitorsConf); \
	  trap '\rm -f $(cmt_local_setup_TrackMonitorsConf)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsConf_extratags) show setup >$(cmt_local_setup_TrackMonitorsConf) && \
	  if [ -f $(cmt_final_setup_TrackMonitorsConf) ] && \
	    \cmp -s $(cmt_final_setup_TrackMonitorsConf) $(cmt_local_setup_TrackMonitorsConf); then \
	    \rm $(cmt_local_setup_TrackMonitorsConf); else \
	    \mv -f $(cmt_local_setup_TrackMonitorsConf) $(cmt_final_setup_TrackMonitorsConf); fi

else

#cmt_local_tagfile_TrackMonitorsConf = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitorsConf = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_TrackMonitorsConf = $(bin)setup.make
#cmt_final_setup_TrackMonitorsConf = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitorsConf_makefile = $(bin)TrackMonitorsConf.make

endif

ifdef STRUCTURED_OUTPUT
TrackMonitorsConfdirs :
	@if test ! -d $(bin)TrackMonitorsConf; then $(mkdir) -p $(bin)TrackMonitorsConf; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsConf
else
TrackMonitorsConfdirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# TrackMonitorsConfdirs ::
#	@if test ! -d $(bin)TrackMonitorsConf; then $(mkdir) -p $(bin)TrackMonitorsConf; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsConf
#
#$(cmt_local_TrackMonitorsConf_makefile) :: $(TrackMonitorsConf_dependencies) $(cmt_local_tagfile_TrackMonitorsConf) build_library_links dirs TrackMonitorsConfdirs
#else
#$(cmt_local_TrackMonitorsConf_makefile) :: $(TrackMonitorsConf_dependencies) $(cmt_local_tagfile_TrackMonitorsConf) build_library_links dirs
#endif
#else
#$(cmt_local_TrackMonitorsConf_makefile) :: $(cmt_local_tagfile_TrackMonitorsConf)
#endif

makefiles : $(cmt_local_TrackMonitorsConf_makefile)

ifndef QUICK
$(cmt_local_TrackMonitorsConf_makefile) : $(TrackMonitorsConf_dependencies) $(cmt_local_tagfile_TrackMonitorsConf) build_library_links
else
$(cmt_local_TrackMonitorsConf_makefile) : $(cmt_local_tagfile_TrackMonitorsConf)
endif
	$(echo) "(constituents.make) Building TrackMonitorsConf.make"; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsConf_extratags) build constituent_makefile -out=$(cmt_local_TrackMonitorsConf_makefile) TrackMonitorsConf

TrackMonitorsConf :: $(TrackMonitorsConf_dependencies) $(cmt_local_TrackMonitorsConf_makefile) dirs TrackMonitorsConfdirs
	$(echo) "(constituents.make) Creating TrackMonitorsConf${lock_suffix} and Starting TrackMonitorsConf"
	@${lock_command} TrackMonitorsConf${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} TrackMonitorsConf${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_TrackMonitorsConf_makefile) TrackMonitorsConf; \
	  retval=$$?; ${unlock_command} TrackMonitorsConf${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) TrackMonitorsConf done"

clean :: TrackMonitorsConfclean

TrackMonitorsConfclean :: $(TrackMonitorsConfclean_dependencies) ##$(cmt_local_TrackMonitorsConf_makefile)
	$(echo) "(constituents.make) Starting TrackMonitorsConfclean"
	@-if test -f $(cmt_local_TrackMonitorsConf_makefile); then \
	  $(MAKE) -f $(cmt_local_TrackMonitorsConf_makefile) TrackMonitorsConfclean; \
	fi
	$(echo) "(constituents.make) TrackMonitorsConfclean done"
#	@-$(MAKE) -f $(cmt_local_TrackMonitorsConf_makefile) TrackMonitorsConfclean

##	  /bin/rm -f $(cmt_local_TrackMonitorsConf_makefile) $(bin)TrackMonitorsConf_dependencies.make

install :: TrackMonitorsConfinstall

TrackMonitorsConfinstall :: $(TrackMonitorsConf_dependencies) $(cmt_local_TrackMonitorsConf_makefile)
	$(echo) "(constituents.make) Starting install TrackMonitorsConf"
	@-$(MAKE) -f $(cmt_local_TrackMonitorsConf_makefile) install
	$(echo) "(constituents.make) install TrackMonitorsConf done"

uninstall :: TrackMonitorsConfuninstall

$(foreach d,$(TrackMonitorsConf_dependencies),$(eval $(d)uninstall_dependencies += TrackMonitorsConfuninstall))

TrackMonitorsConfuninstall :: $(TrackMonitorsConfuninstall_dependencies) $(cmt_local_TrackMonitorsConf_makefile)
	$(echo) "(constituents.make) Starting uninstall TrackMonitorsConf"
	@$(MAKE) -f $(cmt_local_TrackMonitorsConf_makefile) uninstall
	$(echo) "(constituents.make) uninstall TrackMonitorsConf done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ TrackMonitorsConf"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ TrackMonitorsConf done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_TrackMonitors_python_init_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitors_python_init_has_target_tag

#cmt_local_tagfile_TrackMonitors_python_init = $(TrackMonitors_tag)_TrackMonitors_python_init.make
cmt_local_tagfile_TrackMonitors_python_init = $(bin)$(TrackMonitors_tag)_TrackMonitors_python_init.make
cmt_local_setup_TrackMonitors_python_init = $(bin)setup_TrackMonitors_python_init$$$$.make
cmt_final_setup_TrackMonitors_python_init = $(bin)setup_TrackMonitors_python_init.make
#cmt_final_setup_TrackMonitors_python_init = $(bin)TrackMonitors_TrackMonitors_python_initsetup.make
cmt_local_TrackMonitors_python_init_makefile = $(bin)TrackMonitors_python_init.make

TrackMonitors_python_init_extratags = -tag_add=target_TrackMonitors_python_init

#$(cmt_local_tagfile_TrackMonitors_python_init) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_TrackMonitors_python_init) ::
else
$(cmt_local_tagfile_TrackMonitors_python_init) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_TrackMonitors_python_init); then /bin/rm -f $(cmt_local_tagfile_TrackMonitors_python_init); fi ; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitors_python_init_extratags) build tag_makefile >>$(cmt_local_tagfile_TrackMonitors_python_init)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_TrackMonitors_python_init)"; \
	  test ! -f $(cmt_local_setup_TrackMonitors_python_init) || \rm -f $(cmt_local_setup_TrackMonitors_python_init); \
	  trap '\rm -f $(cmt_local_setup_TrackMonitors_python_init)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitors_python_init_extratags) show setup >$(cmt_local_setup_TrackMonitors_python_init) && \
	  if [ -f $(cmt_final_setup_TrackMonitors_python_init) ] && \
	    \cmp -s $(cmt_final_setup_TrackMonitors_python_init) $(cmt_local_setup_TrackMonitors_python_init); then \
	    \rm $(cmt_local_setup_TrackMonitors_python_init); else \
	    \mv -f $(cmt_local_setup_TrackMonitors_python_init) $(cmt_final_setup_TrackMonitors_python_init); fi

else

#cmt_local_tagfile_TrackMonitors_python_init = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitors_python_init = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_TrackMonitors_python_init = $(bin)setup.make
#cmt_final_setup_TrackMonitors_python_init = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitors_python_init_makefile = $(bin)TrackMonitors_python_init.make

endif

ifdef STRUCTURED_OUTPUT
TrackMonitors_python_initdirs :
	@if test ! -d $(bin)TrackMonitors_python_init; then $(mkdir) -p $(bin)TrackMonitors_python_init; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitors_python_init
else
TrackMonitors_python_initdirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# TrackMonitors_python_initdirs ::
#	@if test ! -d $(bin)TrackMonitors_python_init; then $(mkdir) -p $(bin)TrackMonitors_python_init; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitors_python_init
#
#$(cmt_local_TrackMonitors_python_init_makefile) :: $(TrackMonitors_python_init_dependencies) $(cmt_local_tagfile_TrackMonitors_python_init) build_library_links dirs TrackMonitors_python_initdirs
#else
#$(cmt_local_TrackMonitors_python_init_makefile) :: $(TrackMonitors_python_init_dependencies) $(cmt_local_tagfile_TrackMonitors_python_init) build_library_links dirs
#endif
#else
#$(cmt_local_TrackMonitors_python_init_makefile) :: $(cmt_local_tagfile_TrackMonitors_python_init)
#endif

makefiles : $(cmt_local_TrackMonitors_python_init_makefile)

ifndef QUICK
$(cmt_local_TrackMonitors_python_init_makefile) : $(TrackMonitors_python_init_dependencies) $(cmt_local_tagfile_TrackMonitors_python_init) build_library_links
else
$(cmt_local_TrackMonitors_python_init_makefile) : $(cmt_local_tagfile_TrackMonitors_python_init)
endif
	$(echo) "(constituents.make) Building TrackMonitors_python_init.make"; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitors_python_init_extratags) build constituent_makefile -out=$(cmt_local_TrackMonitors_python_init_makefile) TrackMonitors_python_init

TrackMonitors_python_init :: $(TrackMonitors_python_init_dependencies) $(cmt_local_TrackMonitors_python_init_makefile) dirs TrackMonitors_python_initdirs
	$(echo) "(constituents.make) Creating TrackMonitors_python_init${lock_suffix} and Starting TrackMonitors_python_init"
	@${lock_command} TrackMonitors_python_init${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} TrackMonitors_python_init${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_TrackMonitors_python_init_makefile) TrackMonitors_python_init; \
	  retval=$$?; ${unlock_command} TrackMonitors_python_init${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) TrackMonitors_python_init done"

clean :: TrackMonitors_python_initclean

TrackMonitors_python_initclean :: $(TrackMonitors_python_initclean_dependencies) ##$(cmt_local_TrackMonitors_python_init_makefile)
	$(echo) "(constituents.make) Starting TrackMonitors_python_initclean"
	@-if test -f $(cmt_local_TrackMonitors_python_init_makefile); then \
	  $(MAKE) -f $(cmt_local_TrackMonitors_python_init_makefile) TrackMonitors_python_initclean; \
	fi
	$(echo) "(constituents.make) TrackMonitors_python_initclean done"
#	@-$(MAKE) -f $(cmt_local_TrackMonitors_python_init_makefile) TrackMonitors_python_initclean

##	  /bin/rm -f $(cmt_local_TrackMonitors_python_init_makefile) $(bin)TrackMonitors_python_init_dependencies.make

install :: TrackMonitors_python_initinstall

TrackMonitors_python_initinstall :: $(TrackMonitors_python_init_dependencies) $(cmt_local_TrackMonitors_python_init_makefile)
	$(echo) "(constituents.make) Starting install TrackMonitors_python_init"
	@-$(MAKE) -f $(cmt_local_TrackMonitors_python_init_makefile) install
	$(echo) "(constituents.make) install TrackMonitors_python_init done"

uninstall :: TrackMonitors_python_inituninstall

$(foreach d,$(TrackMonitors_python_init_dependencies),$(eval $(d)uninstall_dependencies += TrackMonitors_python_inituninstall))

TrackMonitors_python_inituninstall :: $(TrackMonitors_python_inituninstall_dependencies) $(cmt_local_TrackMonitors_python_init_makefile)
	$(echo) "(constituents.make) Starting uninstall TrackMonitors_python_init"
	@$(MAKE) -f $(cmt_local_TrackMonitors_python_init_makefile) uninstall
	$(echo) "(constituents.make) uninstall TrackMonitors_python_init done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ TrackMonitors_python_init"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ TrackMonitors_python_init done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_zip_TrackMonitors_python_modules_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_zip_TrackMonitors_python_modules_has_target_tag

#cmt_local_tagfile_zip_TrackMonitors_python_modules = $(TrackMonitors_tag)_zip_TrackMonitors_python_modules.make
cmt_local_tagfile_zip_TrackMonitors_python_modules = $(bin)$(TrackMonitors_tag)_zip_TrackMonitors_python_modules.make
cmt_local_setup_zip_TrackMonitors_python_modules = $(bin)setup_zip_TrackMonitors_python_modules$$$$.make
cmt_final_setup_zip_TrackMonitors_python_modules = $(bin)setup_zip_TrackMonitors_python_modules.make
#cmt_final_setup_zip_TrackMonitors_python_modules = $(bin)TrackMonitors_zip_TrackMonitors_python_modulessetup.make
cmt_local_zip_TrackMonitors_python_modules_makefile = $(bin)zip_TrackMonitors_python_modules.make

zip_TrackMonitors_python_modules_extratags = -tag_add=target_zip_TrackMonitors_python_modules

#$(cmt_local_tagfile_zip_TrackMonitors_python_modules) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_zip_TrackMonitors_python_modules) ::
else
$(cmt_local_tagfile_zip_TrackMonitors_python_modules) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_zip_TrackMonitors_python_modules); then /bin/rm -f $(cmt_local_tagfile_zip_TrackMonitors_python_modules); fi ; \
	  $(cmtexe) -tag=$(tags) $(zip_TrackMonitors_python_modules_extratags) build tag_makefile >>$(cmt_local_tagfile_zip_TrackMonitors_python_modules)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_zip_TrackMonitors_python_modules)"; \
	  test ! -f $(cmt_local_setup_zip_TrackMonitors_python_modules) || \rm -f $(cmt_local_setup_zip_TrackMonitors_python_modules); \
	  trap '\rm -f $(cmt_local_setup_zip_TrackMonitors_python_modules)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(zip_TrackMonitors_python_modules_extratags) show setup >$(cmt_local_setup_zip_TrackMonitors_python_modules) && \
	  if [ -f $(cmt_final_setup_zip_TrackMonitors_python_modules) ] && \
	    \cmp -s $(cmt_final_setup_zip_TrackMonitors_python_modules) $(cmt_local_setup_zip_TrackMonitors_python_modules); then \
	    \rm $(cmt_local_setup_zip_TrackMonitors_python_modules); else \
	    \mv -f $(cmt_local_setup_zip_TrackMonitors_python_modules) $(cmt_final_setup_zip_TrackMonitors_python_modules); fi

else

#cmt_local_tagfile_zip_TrackMonitors_python_modules = $(TrackMonitors_tag).make
cmt_local_tagfile_zip_TrackMonitors_python_modules = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_zip_TrackMonitors_python_modules = $(bin)setup.make
#cmt_final_setup_zip_TrackMonitors_python_modules = $(bin)TrackMonitorssetup.make
cmt_local_zip_TrackMonitors_python_modules_makefile = $(bin)zip_TrackMonitors_python_modules.make

endif

ifdef STRUCTURED_OUTPUT
zip_TrackMonitors_python_modulesdirs :
	@if test ! -d $(bin)zip_TrackMonitors_python_modules; then $(mkdir) -p $(bin)zip_TrackMonitors_python_modules; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)zip_TrackMonitors_python_modules
else
zip_TrackMonitors_python_modulesdirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# zip_TrackMonitors_python_modulesdirs ::
#	@if test ! -d $(bin)zip_TrackMonitors_python_modules; then $(mkdir) -p $(bin)zip_TrackMonitors_python_modules; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)zip_TrackMonitors_python_modules
#
#$(cmt_local_zip_TrackMonitors_python_modules_makefile) :: $(zip_TrackMonitors_python_modules_dependencies) $(cmt_local_tagfile_zip_TrackMonitors_python_modules) build_library_links dirs zip_TrackMonitors_python_modulesdirs
#else
#$(cmt_local_zip_TrackMonitors_python_modules_makefile) :: $(zip_TrackMonitors_python_modules_dependencies) $(cmt_local_tagfile_zip_TrackMonitors_python_modules) build_library_links dirs
#endif
#else
#$(cmt_local_zip_TrackMonitors_python_modules_makefile) :: $(cmt_local_tagfile_zip_TrackMonitors_python_modules)
#endif

makefiles : $(cmt_local_zip_TrackMonitors_python_modules_makefile)

ifndef QUICK
$(cmt_local_zip_TrackMonitors_python_modules_makefile) : $(zip_TrackMonitors_python_modules_dependencies) $(cmt_local_tagfile_zip_TrackMonitors_python_modules) build_library_links
else
$(cmt_local_zip_TrackMonitors_python_modules_makefile) : $(cmt_local_tagfile_zip_TrackMonitors_python_modules)
endif
	$(echo) "(constituents.make) Building zip_TrackMonitors_python_modules.make"; \
	  $(cmtexe) -tag=$(tags) $(zip_TrackMonitors_python_modules_extratags) build constituent_makefile -out=$(cmt_local_zip_TrackMonitors_python_modules_makefile) zip_TrackMonitors_python_modules

zip_TrackMonitors_python_modules :: $(zip_TrackMonitors_python_modules_dependencies) $(cmt_local_zip_TrackMonitors_python_modules_makefile) dirs zip_TrackMonitors_python_modulesdirs
	$(echo) "(constituents.make) Creating zip_TrackMonitors_python_modules${lock_suffix} and Starting zip_TrackMonitors_python_modules"
	@${lock_command} zip_TrackMonitors_python_modules${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} zip_TrackMonitors_python_modules${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_zip_TrackMonitors_python_modules_makefile) zip_TrackMonitors_python_modules; \
	  retval=$$?; ${unlock_command} zip_TrackMonitors_python_modules${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) zip_TrackMonitors_python_modules done"

clean :: zip_TrackMonitors_python_modulesclean

zip_TrackMonitors_python_modulesclean :: $(zip_TrackMonitors_python_modulesclean_dependencies) ##$(cmt_local_zip_TrackMonitors_python_modules_makefile)
	$(echo) "(constituents.make) Starting zip_TrackMonitors_python_modulesclean"
	@-if test -f $(cmt_local_zip_TrackMonitors_python_modules_makefile); then \
	  $(MAKE) -f $(cmt_local_zip_TrackMonitors_python_modules_makefile) zip_TrackMonitors_python_modulesclean; \
	fi
	$(echo) "(constituents.make) zip_TrackMonitors_python_modulesclean done"
#	@-$(MAKE) -f $(cmt_local_zip_TrackMonitors_python_modules_makefile) zip_TrackMonitors_python_modulesclean

##	  /bin/rm -f $(cmt_local_zip_TrackMonitors_python_modules_makefile) $(bin)zip_TrackMonitors_python_modules_dependencies.make

install :: zip_TrackMonitors_python_modulesinstall

zip_TrackMonitors_python_modulesinstall :: $(zip_TrackMonitors_python_modules_dependencies) $(cmt_local_zip_TrackMonitors_python_modules_makefile)
	$(echo) "(constituents.make) Starting install zip_TrackMonitors_python_modules"
	@-$(MAKE) -f $(cmt_local_zip_TrackMonitors_python_modules_makefile) install
	$(echo) "(constituents.make) install zip_TrackMonitors_python_modules done"

uninstall :: zip_TrackMonitors_python_modulesuninstall

$(foreach d,$(zip_TrackMonitors_python_modules_dependencies),$(eval $(d)uninstall_dependencies += zip_TrackMonitors_python_modulesuninstall))

zip_TrackMonitors_python_modulesuninstall :: $(zip_TrackMonitors_python_modulesuninstall_dependencies) $(cmt_local_zip_TrackMonitors_python_modules_makefile)
	$(echo) "(constituents.make) Starting uninstall zip_TrackMonitors_python_modules"
	@$(MAKE) -f $(cmt_local_zip_TrackMonitors_python_modules_makefile) uninstall
	$(echo) "(constituents.make) uninstall zip_TrackMonitors_python_modules done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ zip_TrackMonitors_python_modules"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ zip_TrackMonitors_python_modules done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_TrackMonitorsConfDbMerge_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitorsConfDbMerge_has_target_tag

#cmt_local_tagfile_TrackMonitorsConfDbMerge = $(TrackMonitors_tag)_TrackMonitorsConfDbMerge.make
cmt_local_tagfile_TrackMonitorsConfDbMerge = $(bin)$(TrackMonitors_tag)_TrackMonitorsConfDbMerge.make
cmt_local_setup_TrackMonitorsConfDbMerge = $(bin)setup_TrackMonitorsConfDbMerge$$$$.make
cmt_final_setup_TrackMonitorsConfDbMerge = $(bin)setup_TrackMonitorsConfDbMerge.make
#cmt_final_setup_TrackMonitorsConfDbMerge = $(bin)TrackMonitors_TrackMonitorsConfDbMergesetup.make
cmt_local_TrackMonitorsConfDbMerge_makefile = $(bin)TrackMonitorsConfDbMerge.make

TrackMonitorsConfDbMerge_extratags = -tag_add=target_TrackMonitorsConfDbMerge

#$(cmt_local_tagfile_TrackMonitorsConfDbMerge) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_TrackMonitorsConfDbMerge) ::
else
$(cmt_local_tagfile_TrackMonitorsConfDbMerge) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_TrackMonitorsConfDbMerge); then /bin/rm -f $(cmt_local_tagfile_TrackMonitorsConfDbMerge); fi ; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsConfDbMerge_extratags) build tag_makefile >>$(cmt_local_tagfile_TrackMonitorsConfDbMerge)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_TrackMonitorsConfDbMerge)"; \
	  test ! -f $(cmt_local_setup_TrackMonitorsConfDbMerge) || \rm -f $(cmt_local_setup_TrackMonitorsConfDbMerge); \
	  trap '\rm -f $(cmt_local_setup_TrackMonitorsConfDbMerge)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsConfDbMerge_extratags) show setup >$(cmt_local_setup_TrackMonitorsConfDbMerge) && \
	  if [ -f $(cmt_final_setup_TrackMonitorsConfDbMerge) ] && \
	    \cmp -s $(cmt_final_setup_TrackMonitorsConfDbMerge) $(cmt_local_setup_TrackMonitorsConfDbMerge); then \
	    \rm $(cmt_local_setup_TrackMonitorsConfDbMerge); else \
	    \mv -f $(cmt_local_setup_TrackMonitorsConfDbMerge) $(cmt_final_setup_TrackMonitorsConfDbMerge); fi

else

#cmt_local_tagfile_TrackMonitorsConfDbMerge = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitorsConfDbMerge = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_TrackMonitorsConfDbMerge = $(bin)setup.make
#cmt_final_setup_TrackMonitorsConfDbMerge = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitorsConfDbMerge_makefile = $(bin)TrackMonitorsConfDbMerge.make

endif

ifdef STRUCTURED_OUTPUT
TrackMonitorsConfDbMergedirs :
	@if test ! -d $(bin)TrackMonitorsConfDbMerge; then $(mkdir) -p $(bin)TrackMonitorsConfDbMerge; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsConfDbMerge
else
TrackMonitorsConfDbMergedirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# TrackMonitorsConfDbMergedirs ::
#	@if test ! -d $(bin)TrackMonitorsConfDbMerge; then $(mkdir) -p $(bin)TrackMonitorsConfDbMerge; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsConfDbMerge
#
#$(cmt_local_TrackMonitorsConfDbMerge_makefile) :: $(TrackMonitorsConfDbMerge_dependencies) $(cmt_local_tagfile_TrackMonitorsConfDbMerge) build_library_links dirs TrackMonitorsConfDbMergedirs
#else
#$(cmt_local_TrackMonitorsConfDbMerge_makefile) :: $(TrackMonitorsConfDbMerge_dependencies) $(cmt_local_tagfile_TrackMonitorsConfDbMerge) build_library_links dirs
#endif
#else
#$(cmt_local_TrackMonitorsConfDbMerge_makefile) :: $(cmt_local_tagfile_TrackMonitorsConfDbMerge)
#endif

makefiles : $(cmt_local_TrackMonitorsConfDbMerge_makefile)

ifndef QUICK
$(cmt_local_TrackMonitorsConfDbMerge_makefile) : $(TrackMonitorsConfDbMerge_dependencies) $(cmt_local_tagfile_TrackMonitorsConfDbMerge) build_library_links
else
$(cmt_local_TrackMonitorsConfDbMerge_makefile) : $(cmt_local_tagfile_TrackMonitorsConfDbMerge)
endif
	$(echo) "(constituents.make) Building TrackMonitorsConfDbMerge.make"; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsConfDbMerge_extratags) build constituent_makefile -out=$(cmt_local_TrackMonitorsConfDbMerge_makefile) TrackMonitorsConfDbMerge

TrackMonitorsConfDbMerge :: $(TrackMonitorsConfDbMerge_dependencies) $(cmt_local_TrackMonitorsConfDbMerge_makefile) dirs TrackMonitorsConfDbMergedirs
	$(echo) "(constituents.make) Creating TrackMonitorsConfDbMerge${lock_suffix} and Starting TrackMonitorsConfDbMerge"
	@${lock_command} TrackMonitorsConfDbMerge${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} TrackMonitorsConfDbMerge${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_TrackMonitorsConfDbMerge_makefile) TrackMonitorsConfDbMerge; \
	  retval=$$?; ${unlock_command} TrackMonitorsConfDbMerge${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) TrackMonitorsConfDbMerge done"

clean :: TrackMonitorsConfDbMergeclean

TrackMonitorsConfDbMergeclean :: $(TrackMonitorsConfDbMergeclean_dependencies) ##$(cmt_local_TrackMonitorsConfDbMerge_makefile)
	$(echo) "(constituents.make) Starting TrackMonitorsConfDbMergeclean"
	@-if test -f $(cmt_local_TrackMonitorsConfDbMerge_makefile); then \
	  $(MAKE) -f $(cmt_local_TrackMonitorsConfDbMerge_makefile) TrackMonitorsConfDbMergeclean; \
	fi
	$(echo) "(constituents.make) TrackMonitorsConfDbMergeclean done"
#	@-$(MAKE) -f $(cmt_local_TrackMonitorsConfDbMerge_makefile) TrackMonitorsConfDbMergeclean

##	  /bin/rm -f $(cmt_local_TrackMonitorsConfDbMerge_makefile) $(bin)TrackMonitorsConfDbMerge_dependencies.make

install :: TrackMonitorsConfDbMergeinstall

TrackMonitorsConfDbMergeinstall :: $(TrackMonitorsConfDbMerge_dependencies) $(cmt_local_TrackMonitorsConfDbMerge_makefile)
	$(echo) "(constituents.make) Starting install TrackMonitorsConfDbMerge"
	@-$(MAKE) -f $(cmt_local_TrackMonitorsConfDbMerge_makefile) install
	$(echo) "(constituents.make) install TrackMonitorsConfDbMerge done"

uninstall :: TrackMonitorsConfDbMergeuninstall

$(foreach d,$(TrackMonitorsConfDbMerge_dependencies),$(eval $(d)uninstall_dependencies += TrackMonitorsConfDbMergeuninstall))

TrackMonitorsConfDbMergeuninstall :: $(TrackMonitorsConfDbMergeuninstall_dependencies) $(cmt_local_TrackMonitorsConfDbMerge_makefile)
	$(echo) "(constituents.make) Starting uninstall TrackMonitorsConfDbMerge"
	@$(MAKE) -f $(cmt_local_TrackMonitorsConfDbMerge_makefile) uninstall
	$(echo) "(constituents.make) uninstall TrackMonitorsConfDbMerge done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ TrackMonitorsConfDbMerge"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ TrackMonitorsConfDbMerge done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_TrackMonitors_python_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitors_python_has_target_tag

#cmt_local_tagfile_TrackMonitors_python = $(TrackMonitors_tag)_TrackMonitors_python.make
cmt_local_tagfile_TrackMonitors_python = $(bin)$(TrackMonitors_tag)_TrackMonitors_python.make
cmt_local_setup_TrackMonitors_python = $(bin)setup_TrackMonitors_python$$$$.make
cmt_final_setup_TrackMonitors_python = $(bin)setup_TrackMonitors_python.make
#cmt_final_setup_TrackMonitors_python = $(bin)TrackMonitors_TrackMonitors_pythonsetup.make
cmt_local_TrackMonitors_python_makefile = $(bin)TrackMonitors_python.make

TrackMonitors_python_extratags = -tag_add=target_TrackMonitors_python

#$(cmt_local_tagfile_TrackMonitors_python) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_TrackMonitors_python) ::
else
$(cmt_local_tagfile_TrackMonitors_python) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_TrackMonitors_python); then /bin/rm -f $(cmt_local_tagfile_TrackMonitors_python); fi ; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitors_python_extratags) build tag_makefile >>$(cmt_local_tagfile_TrackMonitors_python)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_TrackMonitors_python)"; \
	  test ! -f $(cmt_local_setup_TrackMonitors_python) || \rm -f $(cmt_local_setup_TrackMonitors_python); \
	  trap '\rm -f $(cmt_local_setup_TrackMonitors_python)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitors_python_extratags) show setup >$(cmt_local_setup_TrackMonitors_python) && \
	  if [ -f $(cmt_final_setup_TrackMonitors_python) ] && \
	    \cmp -s $(cmt_final_setup_TrackMonitors_python) $(cmt_local_setup_TrackMonitors_python); then \
	    \rm $(cmt_local_setup_TrackMonitors_python); else \
	    \mv -f $(cmt_local_setup_TrackMonitors_python) $(cmt_final_setup_TrackMonitors_python); fi

else

#cmt_local_tagfile_TrackMonitors_python = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitors_python = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_TrackMonitors_python = $(bin)setup.make
#cmt_final_setup_TrackMonitors_python = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitors_python_makefile = $(bin)TrackMonitors_python.make

endif

ifdef STRUCTURED_OUTPUT
TrackMonitors_pythondirs :
	@if test ! -d $(bin)TrackMonitors_python; then $(mkdir) -p $(bin)TrackMonitors_python; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitors_python
else
TrackMonitors_pythondirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# TrackMonitors_pythondirs ::
#	@if test ! -d $(bin)TrackMonitors_python; then $(mkdir) -p $(bin)TrackMonitors_python; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitors_python
#
#$(cmt_local_TrackMonitors_python_makefile) :: $(TrackMonitors_python_dependencies) $(cmt_local_tagfile_TrackMonitors_python) build_library_links dirs TrackMonitors_pythondirs
#else
#$(cmt_local_TrackMonitors_python_makefile) :: $(TrackMonitors_python_dependencies) $(cmt_local_tagfile_TrackMonitors_python) build_library_links dirs
#endif
#else
#$(cmt_local_TrackMonitors_python_makefile) :: $(cmt_local_tagfile_TrackMonitors_python)
#endif

makefiles : $(cmt_local_TrackMonitors_python_makefile)

ifndef QUICK
$(cmt_local_TrackMonitors_python_makefile) : $(TrackMonitors_python_dependencies) $(cmt_local_tagfile_TrackMonitors_python) build_library_links
else
$(cmt_local_TrackMonitors_python_makefile) : $(cmt_local_tagfile_TrackMonitors_python)
endif
	$(echo) "(constituents.make) Building TrackMonitors_python.make"; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitors_python_extratags) build constituent_makefile -out=$(cmt_local_TrackMonitors_python_makefile) TrackMonitors_python

TrackMonitors_python :: $(TrackMonitors_python_dependencies) $(cmt_local_TrackMonitors_python_makefile) dirs TrackMonitors_pythondirs
	$(echo) "(constituents.make) Creating TrackMonitors_python${lock_suffix} and Starting TrackMonitors_python"
	@${lock_command} TrackMonitors_python${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} TrackMonitors_python${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_TrackMonitors_python_makefile) TrackMonitors_python; \
	  retval=$$?; ${unlock_command} TrackMonitors_python${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) TrackMonitors_python done"

clean :: TrackMonitors_pythonclean

TrackMonitors_pythonclean :: $(TrackMonitors_pythonclean_dependencies) ##$(cmt_local_TrackMonitors_python_makefile)
	$(echo) "(constituents.make) Starting TrackMonitors_pythonclean"
	@-if test -f $(cmt_local_TrackMonitors_python_makefile); then \
	  $(MAKE) -f $(cmt_local_TrackMonitors_python_makefile) TrackMonitors_pythonclean; \
	fi
	$(echo) "(constituents.make) TrackMonitors_pythonclean done"
#	@-$(MAKE) -f $(cmt_local_TrackMonitors_python_makefile) TrackMonitors_pythonclean

##	  /bin/rm -f $(cmt_local_TrackMonitors_python_makefile) $(bin)TrackMonitors_python_dependencies.make

install :: TrackMonitors_pythoninstall

TrackMonitors_pythoninstall :: $(TrackMonitors_python_dependencies) $(cmt_local_TrackMonitors_python_makefile)
	$(echo) "(constituents.make) Starting install TrackMonitors_python"
	@-$(MAKE) -f $(cmt_local_TrackMonitors_python_makefile) install
	$(echo) "(constituents.make) install TrackMonitors_python done"

uninstall :: TrackMonitors_pythonuninstall

$(foreach d,$(TrackMonitors_python_dependencies),$(eval $(d)uninstall_dependencies += TrackMonitors_pythonuninstall))

TrackMonitors_pythonuninstall :: $(TrackMonitors_pythonuninstall_dependencies) $(cmt_local_TrackMonitors_python_makefile)
	$(echo) "(constituents.make) Starting uninstall TrackMonitors_python"
	@$(MAKE) -f $(cmt_local_TrackMonitors_python_makefile) uninstall
	$(echo) "(constituents.make) uninstall TrackMonitors_python done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ TrackMonitors_python"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ TrackMonitors_python done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_TrackMonitorsGenConfUser_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitorsGenConfUser_has_target_tag

#cmt_local_tagfile_TrackMonitorsGenConfUser = $(TrackMonitors_tag)_TrackMonitorsGenConfUser.make
cmt_local_tagfile_TrackMonitorsGenConfUser = $(bin)$(TrackMonitors_tag)_TrackMonitorsGenConfUser.make
cmt_local_setup_TrackMonitorsGenConfUser = $(bin)setup_TrackMonitorsGenConfUser$$$$.make
cmt_final_setup_TrackMonitorsGenConfUser = $(bin)setup_TrackMonitorsGenConfUser.make
#cmt_final_setup_TrackMonitorsGenConfUser = $(bin)TrackMonitors_TrackMonitorsGenConfUsersetup.make
cmt_local_TrackMonitorsGenConfUser_makefile = $(bin)TrackMonitorsGenConfUser.make

TrackMonitorsGenConfUser_extratags = -tag_add=target_TrackMonitorsGenConfUser

#$(cmt_local_tagfile_TrackMonitorsGenConfUser) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_TrackMonitorsGenConfUser) ::
else
$(cmt_local_tagfile_TrackMonitorsGenConfUser) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_TrackMonitorsGenConfUser); then /bin/rm -f $(cmt_local_tagfile_TrackMonitorsGenConfUser); fi ; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsGenConfUser_extratags) build tag_makefile >>$(cmt_local_tagfile_TrackMonitorsGenConfUser)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_TrackMonitorsGenConfUser)"; \
	  test ! -f $(cmt_local_setup_TrackMonitorsGenConfUser) || \rm -f $(cmt_local_setup_TrackMonitorsGenConfUser); \
	  trap '\rm -f $(cmt_local_setup_TrackMonitorsGenConfUser)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsGenConfUser_extratags) show setup >$(cmt_local_setup_TrackMonitorsGenConfUser) && \
	  if [ -f $(cmt_final_setup_TrackMonitorsGenConfUser) ] && \
	    \cmp -s $(cmt_final_setup_TrackMonitorsGenConfUser) $(cmt_local_setup_TrackMonitorsGenConfUser); then \
	    \rm $(cmt_local_setup_TrackMonitorsGenConfUser); else \
	    \mv -f $(cmt_local_setup_TrackMonitorsGenConfUser) $(cmt_final_setup_TrackMonitorsGenConfUser); fi

else

#cmt_local_tagfile_TrackMonitorsGenConfUser = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitorsGenConfUser = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_TrackMonitorsGenConfUser = $(bin)setup.make
#cmt_final_setup_TrackMonitorsGenConfUser = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitorsGenConfUser_makefile = $(bin)TrackMonitorsGenConfUser.make

endif

ifdef STRUCTURED_OUTPUT
TrackMonitorsGenConfUserdirs :
	@if test ! -d $(bin)TrackMonitorsGenConfUser; then $(mkdir) -p $(bin)TrackMonitorsGenConfUser; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsGenConfUser
else
TrackMonitorsGenConfUserdirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# TrackMonitorsGenConfUserdirs ::
#	@if test ! -d $(bin)TrackMonitorsGenConfUser; then $(mkdir) -p $(bin)TrackMonitorsGenConfUser; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsGenConfUser
#
#$(cmt_local_TrackMonitorsGenConfUser_makefile) :: $(TrackMonitorsGenConfUser_dependencies) $(cmt_local_tagfile_TrackMonitorsGenConfUser) build_library_links dirs TrackMonitorsGenConfUserdirs
#else
#$(cmt_local_TrackMonitorsGenConfUser_makefile) :: $(TrackMonitorsGenConfUser_dependencies) $(cmt_local_tagfile_TrackMonitorsGenConfUser) build_library_links dirs
#endif
#else
#$(cmt_local_TrackMonitorsGenConfUser_makefile) :: $(cmt_local_tagfile_TrackMonitorsGenConfUser)
#endif

makefiles : $(cmt_local_TrackMonitorsGenConfUser_makefile)

ifndef QUICK
$(cmt_local_TrackMonitorsGenConfUser_makefile) : $(TrackMonitorsGenConfUser_dependencies) $(cmt_local_tagfile_TrackMonitorsGenConfUser) build_library_links
else
$(cmt_local_TrackMonitorsGenConfUser_makefile) : $(cmt_local_tagfile_TrackMonitorsGenConfUser)
endif
	$(echo) "(constituents.make) Building TrackMonitorsGenConfUser.make"; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsGenConfUser_extratags) build constituent_makefile -out=$(cmt_local_TrackMonitorsGenConfUser_makefile) TrackMonitorsGenConfUser

TrackMonitorsGenConfUser :: $(TrackMonitorsGenConfUser_dependencies) $(cmt_local_TrackMonitorsGenConfUser_makefile) dirs TrackMonitorsGenConfUserdirs
	$(echo) "(constituents.make) Creating TrackMonitorsGenConfUser${lock_suffix} and Starting TrackMonitorsGenConfUser"
	@${lock_command} TrackMonitorsGenConfUser${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} TrackMonitorsGenConfUser${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_TrackMonitorsGenConfUser_makefile) TrackMonitorsGenConfUser; \
	  retval=$$?; ${unlock_command} TrackMonitorsGenConfUser${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) TrackMonitorsGenConfUser done"

clean :: TrackMonitorsGenConfUserclean

TrackMonitorsGenConfUserclean :: $(TrackMonitorsGenConfUserclean_dependencies) ##$(cmt_local_TrackMonitorsGenConfUser_makefile)
	$(echo) "(constituents.make) Starting TrackMonitorsGenConfUserclean"
	@-if test -f $(cmt_local_TrackMonitorsGenConfUser_makefile); then \
	  $(MAKE) -f $(cmt_local_TrackMonitorsGenConfUser_makefile) TrackMonitorsGenConfUserclean; \
	fi
	$(echo) "(constituents.make) TrackMonitorsGenConfUserclean done"
#	@-$(MAKE) -f $(cmt_local_TrackMonitorsGenConfUser_makefile) TrackMonitorsGenConfUserclean

##	  /bin/rm -f $(cmt_local_TrackMonitorsGenConfUser_makefile) $(bin)TrackMonitorsGenConfUser_dependencies.make

install :: TrackMonitorsGenConfUserinstall

TrackMonitorsGenConfUserinstall :: $(TrackMonitorsGenConfUser_dependencies) $(cmt_local_TrackMonitorsGenConfUser_makefile)
	$(echo) "(constituents.make) Starting install TrackMonitorsGenConfUser"
	@-$(MAKE) -f $(cmt_local_TrackMonitorsGenConfUser_makefile) install
	$(echo) "(constituents.make) install TrackMonitorsGenConfUser done"

uninstall :: TrackMonitorsGenConfUseruninstall

$(foreach d,$(TrackMonitorsGenConfUser_dependencies),$(eval $(d)uninstall_dependencies += TrackMonitorsGenConfUseruninstall))

TrackMonitorsGenConfUseruninstall :: $(TrackMonitorsGenConfUseruninstall_dependencies) $(cmt_local_TrackMonitorsGenConfUser_makefile)
	$(echo) "(constituents.make) Starting uninstall TrackMonitorsGenConfUser"
	@$(MAKE) -f $(cmt_local_TrackMonitorsGenConfUser_makefile) uninstall
	$(echo) "(constituents.make) uninstall TrackMonitorsGenConfUser done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ TrackMonitorsGenConfUser"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ TrackMonitorsGenConfUser done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_TrackMonitorsConfUserDbMerge_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitorsConfUserDbMerge_has_target_tag

#cmt_local_tagfile_TrackMonitorsConfUserDbMerge = $(TrackMonitors_tag)_TrackMonitorsConfUserDbMerge.make
cmt_local_tagfile_TrackMonitorsConfUserDbMerge = $(bin)$(TrackMonitors_tag)_TrackMonitorsConfUserDbMerge.make
cmt_local_setup_TrackMonitorsConfUserDbMerge = $(bin)setup_TrackMonitorsConfUserDbMerge$$$$.make
cmt_final_setup_TrackMonitorsConfUserDbMerge = $(bin)setup_TrackMonitorsConfUserDbMerge.make
#cmt_final_setup_TrackMonitorsConfUserDbMerge = $(bin)TrackMonitors_TrackMonitorsConfUserDbMergesetup.make
cmt_local_TrackMonitorsConfUserDbMerge_makefile = $(bin)TrackMonitorsConfUserDbMerge.make

TrackMonitorsConfUserDbMerge_extratags = -tag_add=target_TrackMonitorsConfUserDbMerge

#$(cmt_local_tagfile_TrackMonitorsConfUserDbMerge) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_TrackMonitorsConfUserDbMerge) ::
else
$(cmt_local_tagfile_TrackMonitorsConfUserDbMerge) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_TrackMonitorsConfUserDbMerge); then /bin/rm -f $(cmt_local_tagfile_TrackMonitorsConfUserDbMerge); fi ; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsConfUserDbMerge_extratags) build tag_makefile >>$(cmt_local_tagfile_TrackMonitorsConfUserDbMerge)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_TrackMonitorsConfUserDbMerge)"; \
	  test ! -f $(cmt_local_setup_TrackMonitorsConfUserDbMerge) || \rm -f $(cmt_local_setup_TrackMonitorsConfUserDbMerge); \
	  trap '\rm -f $(cmt_local_setup_TrackMonitorsConfUserDbMerge)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsConfUserDbMerge_extratags) show setup >$(cmt_local_setup_TrackMonitorsConfUserDbMerge) && \
	  if [ -f $(cmt_final_setup_TrackMonitorsConfUserDbMerge) ] && \
	    \cmp -s $(cmt_final_setup_TrackMonitorsConfUserDbMerge) $(cmt_local_setup_TrackMonitorsConfUserDbMerge); then \
	    \rm $(cmt_local_setup_TrackMonitorsConfUserDbMerge); else \
	    \mv -f $(cmt_local_setup_TrackMonitorsConfUserDbMerge) $(cmt_final_setup_TrackMonitorsConfUserDbMerge); fi

else

#cmt_local_tagfile_TrackMonitorsConfUserDbMerge = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitorsConfUserDbMerge = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_TrackMonitorsConfUserDbMerge = $(bin)setup.make
#cmt_final_setup_TrackMonitorsConfUserDbMerge = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitorsConfUserDbMerge_makefile = $(bin)TrackMonitorsConfUserDbMerge.make

endif

ifdef STRUCTURED_OUTPUT
TrackMonitorsConfUserDbMergedirs :
	@if test ! -d $(bin)TrackMonitorsConfUserDbMerge; then $(mkdir) -p $(bin)TrackMonitorsConfUserDbMerge; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsConfUserDbMerge
else
TrackMonitorsConfUserDbMergedirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# TrackMonitorsConfUserDbMergedirs ::
#	@if test ! -d $(bin)TrackMonitorsConfUserDbMerge; then $(mkdir) -p $(bin)TrackMonitorsConfUserDbMerge; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)TrackMonitorsConfUserDbMerge
#
#$(cmt_local_TrackMonitorsConfUserDbMerge_makefile) :: $(TrackMonitorsConfUserDbMerge_dependencies) $(cmt_local_tagfile_TrackMonitorsConfUserDbMerge) build_library_links dirs TrackMonitorsConfUserDbMergedirs
#else
#$(cmt_local_TrackMonitorsConfUserDbMerge_makefile) :: $(TrackMonitorsConfUserDbMerge_dependencies) $(cmt_local_tagfile_TrackMonitorsConfUserDbMerge) build_library_links dirs
#endif
#else
#$(cmt_local_TrackMonitorsConfUserDbMerge_makefile) :: $(cmt_local_tagfile_TrackMonitorsConfUserDbMerge)
#endif

makefiles : $(cmt_local_TrackMonitorsConfUserDbMerge_makefile)

ifndef QUICK
$(cmt_local_TrackMonitorsConfUserDbMerge_makefile) : $(TrackMonitorsConfUserDbMerge_dependencies) $(cmt_local_tagfile_TrackMonitorsConfUserDbMerge) build_library_links
else
$(cmt_local_TrackMonitorsConfUserDbMerge_makefile) : $(cmt_local_tagfile_TrackMonitorsConfUserDbMerge)
endif
	$(echo) "(constituents.make) Building TrackMonitorsConfUserDbMerge.make"; \
	  $(cmtexe) -tag=$(tags) $(TrackMonitorsConfUserDbMerge_extratags) build constituent_makefile -out=$(cmt_local_TrackMonitorsConfUserDbMerge_makefile) TrackMonitorsConfUserDbMerge

TrackMonitorsConfUserDbMerge :: $(TrackMonitorsConfUserDbMerge_dependencies) $(cmt_local_TrackMonitorsConfUserDbMerge_makefile) dirs TrackMonitorsConfUserDbMergedirs
	$(echo) "(constituents.make) Creating TrackMonitorsConfUserDbMerge${lock_suffix} and Starting TrackMonitorsConfUserDbMerge"
	@${lock_command} TrackMonitorsConfUserDbMerge${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} TrackMonitorsConfUserDbMerge${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_TrackMonitorsConfUserDbMerge_makefile) TrackMonitorsConfUserDbMerge; \
	  retval=$$?; ${unlock_command} TrackMonitorsConfUserDbMerge${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) TrackMonitorsConfUserDbMerge done"

clean :: TrackMonitorsConfUserDbMergeclean

TrackMonitorsConfUserDbMergeclean :: $(TrackMonitorsConfUserDbMergeclean_dependencies) ##$(cmt_local_TrackMonitorsConfUserDbMerge_makefile)
	$(echo) "(constituents.make) Starting TrackMonitorsConfUserDbMergeclean"
	@-if test -f $(cmt_local_TrackMonitorsConfUserDbMerge_makefile); then \
	  $(MAKE) -f $(cmt_local_TrackMonitorsConfUserDbMerge_makefile) TrackMonitorsConfUserDbMergeclean; \
	fi
	$(echo) "(constituents.make) TrackMonitorsConfUserDbMergeclean done"
#	@-$(MAKE) -f $(cmt_local_TrackMonitorsConfUserDbMerge_makefile) TrackMonitorsConfUserDbMergeclean

##	  /bin/rm -f $(cmt_local_TrackMonitorsConfUserDbMerge_makefile) $(bin)TrackMonitorsConfUserDbMerge_dependencies.make

install :: TrackMonitorsConfUserDbMergeinstall

TrackMonitorsConfUserDbMergeinstall :: $(TrackMonitorsConfUserDbMerge_dependencies) $(cmt_local_TrackMonitorsConfUserDbMerge_makefile)
	$(echo) "(constituents.make) Starting install TrackMonitorsConfUserDbMerge"
	@-$(MAKE) -f $(cmt_local_TrackMonitorsConfUserDbMerge_makefile) install
	$(echo) "(constituents.make) install TrackMonitorsConfUserDbMerge done"

uninstall :: TrackMonitorsConfUserDbMergeuninstall

$(foreach d,$(TrackMonitorsConfUserDbMerge_dependencies),$(eval $(d)uninstall_dependencies += TrackMonitorsConfUserDbMergeuninstall))

TrackMonitorsConfUserDbMergeuninstall :: $(TrackMonitorsConfUserDbMergeuninstall_dependencies) $(cmt_local_TrackMonitorsConfUserDbMerge_makefile)
	$(echo) "(constituents.make) Starting uninstall TrackMonitorsConfUserDbMerge"
	@$(MAKE) -f $(cmt_local_TrackMonitorsConfUserDbMerge_makefile) uninstall
	$(echo) "(constituents.make) uninstall TrackMonitorsConfUserDbMerge done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ TrackMonitorsConfUserDbMerge"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ TrackMonitorsConfUserDbMerge done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_make_has_target_tag = 1

#--------------------------------------------------------

ifdef cmt_make_has_target_tag

#cmt_local_tagfile_make = $(TrackMonitors_tag)_make.make
cmt_local_tagfile_make = $(bin)$(TrackMonitors_tag)_make.make
cmt_local_setup_make = $(bin)setup_make$$$$.make
cmt_final_setup_make = $(bin)setup_make.make
#cmt_final_setup_make = $(bin)TrackMonitors_makesetup.make
cmt_local_make_makefile = $(bin)make.make

make_extratags = -tag_add=target_make

#$(cmt_local_tagfile_make) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_make) ::
else
$(cmt_local_tagfile_make) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_make); then /bin/rm -f $(cmt_local_tagfile_make); fi ; \
	  $(cmtexe) -tag=$(tags) $(make_extratags) build tag_makefile >>$(cmt_local_tagfile_make)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_make)"; \
	  test ! -f $(cmt_local_setup_make) || \rm -f $(cmt_local_setup_make); \
	  trap '\rm -f $(cmt_local_setup_make)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(make_extratags) show setup >$(cmt_local_setup_make) && \
	  if [ -f $(cmt_final_setup_make) ] && \
	    \cmp -s $(cmt_final_setup_make) $(cmt_local_setup_make); then \
	    \rm $(cmt_local_setup_make); else \
	    \mv -f $(cmt_local_setup_make) $(cmt_final_setup_make); fi

else

#cmt_local_tagfile_make = $(TrackMonitors_tag).make
cmt_local_tagfile_make = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_make = $(bin)setup.make
#cmt_final_setup_make = $(bin)TrackMonitorssetup.make
cmt_local_make_makefile = $(bin)make.make

endif

ifdef STRUCTURED_OUTPUT
makedirs :
	@if test ! -d $(bin)make; then $(mkdir) -p $(bin)make; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)make
else
makedirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# makedirs ::
#	@if test ! -d $(bin)make; then $(mkdir) -p $(bin)make; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)make
#
#$(cmt_local_make_makefile) :: $(make_dependencies) $(cmt_local_tagfile_make) build_library_links dirs makedirs
#else
#$(cmt_local_make_makefile) :: $(make_dependencies) $(cmt_local_tagfile_make) build_library_links dirs
#endif
#else
#$(cmt_local_make_makefile) :: $(cmt_local_tagfile_make)
#endif

makefiles : $(cmt_local_make_makefile)

ifndef QUICK
$(cmt_local_make_makefile) : $(make_dependencies) $(cmt_local_tagfile_make) build_library_links
else
$(cmt_local_make_makefile) : $(cmt_local_tagfile_make)
endif
	$(echo) "(constituents.make) Building make.make"; \
	  $(cmtexe) -tag=$(tags) $(make_extratags) build constituent_makefile -out=$(cmt_local_make_makefile) make

make :: $(make_dependencies) $(cmt_local_make_makefile) dirs makedirs
	$(echo) "(constituents.make) Creating make${lock_suffix} and Starting make"
	@${lock_command} make${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} make${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_make_makefile) make; \
	  retval=$$?; ${unlock_command} make${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) make done"

clean :: makeclean

makeclean :: $(makeclean_dependencies) ##$(cmt_local_make_makefile)
	$(echo) "(constituents.make) Starting makeclean"
	@-if test -f $(cmt_local_make_makefile); then \
	  $(MAKE) -f $(cmt_local_make_makefile) makeclean; \
	fi
	$(echo) "(constituents.make) makeclean done"
#	@-$(MAKE) -f $(cmt_local_make_makefile) makeclean

##	  /bin/rm -f $(cmt_local_make_makefile) $(bin)make_dependencies.make

install :: makeinstall

makeinstall :: $(make_dependencies) $(cmt_local_make_makefile)
	$(echo) "(constituents.make) Starting install make"
	@-$(MAKE) -f $(cmt_local_make_makefile) install
	$(echo) "(constituents.make) install make done"

uninstall :: makeuninstall

$(foreach d,$(make_dependencies),$(eval $(d)uninstall_dependencies += makeuninstall))

makeuninstall :: $(makeuninstall_dependencies) $(cmt_local_make_makefile)
	$(echo) "(constituents.make) Starting uninstall make"
	@$(MAKE) -f $(cmt_local_make_makefile) uninstall
	$(echo) "(constituents.make) uninstall make done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ make"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ make done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_CompilePython_has_target_tag = 1

#--------------------------------------------------------

ifdef cmt_CompilePython_has_target_tag

#cmt_local_tagfile_CompilePython = $(TrackMonitors_tag)_CompilePython.make
cmt_local_tagfile_CompilePython = $(bin)$(TrackMonitors_tag)_CompilePython.make
cmt_local_setup_CompilePython = $(bin)setup_CompilePython$$$$.make
cmt_final_setup_CompilePython = $(bin)setup_CompilePython.make
#cmt_final_setup_CompilePython = $(bin)TrackMonitors_CompilePythonsetup.make
cmt_local_CompilePython_makefile = $(bin)CompilePython.make

CompilePython_extratags = -tag_add=target_CompilePython

#$(cmt_local_tagfile_CompilePython) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_CompilePython) ::
else
$(cmt_local_tagfile_CompilePython) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_CompilePython); then /bin/rm -f $(cmt_local_tagfile_CompilePython); fi ; \
	  $(cmtexe) -tag=$(tags) $(CompilePython_extratags) build tag_makefile >>$(cmt_local_tagfile_CompilePython)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_CompilePython)"; \
	  test ! -f $(cmt_local_setup_CompilePython) || \rm -f $(cmt_local_setup_CompilePython); \
	  trap '\rm -f $(cmt_local_setup_CompilePython)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(CompilePython_extratags) show setup >$(cmt_local_setup_CompilePython) && \
	  if [ -f $(cmt_final_setup_CompilePython) ] && \
	    \cmp -s $(cmt_final_setup_CompilePython) $(cmt_local_setup_CompilePython); then \
	    \rm $(cmt_local_setup_CompilePython); else \
	    \mv -f $(cmt_local_setup_CompilePython) $(cmt_final_setup_CompilePython); fi

else

#cmt_local_tagfile_CompilePython = $(TrackMonitors_tag).make
cmt_local_tagfile_CompilePython = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_CompilePython = $(bin)setup.make
#cmt_final_setup_CompilePython = $(bin)TrackMonitorssetup.make
cmt_local_CompilePython_makefile = $(bin)CompilePython.make

endif

ifdef STRUCTURED_OUTPUT
CompilePythondirs :
	@if test ! -d $(bin)CompilePython; then $(mkdir) -p $(bin)CompilePython; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)CompilePython
else
CompilePythondirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# CompilePythondirs ::
#	@if test ! -d $(bin)CompilePython; then $(mkdir) -p $(bin)CompilePython; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)CompilePython
#
#$(cmt_local_CompilePython_makefile) :: $(CompilePython_dependencies) $(cmt_local_tagfile_CompilePython) build_library_links dirs CompilePythondirs
#else
#$(cmt_local_CompilePython_makefile) :: $(CompilePython_dependencies) $(cmt_local_tagfile_CompilePython) build_library_links dirs
#endif
#else
#$(cmt_local_CompilePython_makefile) :: $(cmt_local_tagfile_CompilePython)
#endif

makefiles : $(cmt_local_CompilePython_makefile)

ifndef QUICK
$(cmt_local_CompilePython_makefile) : $(CompilePython_dependencies) $(cmt_local_tagfile_CompilePython) build_library_links
else
$(cmt_local_CompilePython_makefile) : $(cmt_local_tagfile_CompilePython)
endif
	$(echo) "(constituents.make) Building CompilePython.make"; \
	  $(cmtexe) -tag=$(tags) $(CompilePython_extratags) build constituent_makefile -out=$(cmt_local_CompilePython_makefile) CompilePython

CompilePython :: $(CompilePython_dependencies) $(cmt_local_CompilePython_makefile) dirs CompilePythondirs
	$(echo) "(constituents.make) Creating CompilePython${lock_suffix} and Starting CompilePython"
	@${lock_command} CompilePython${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} CompilePython${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_CompilePython_makefile) CompilePython; \
	  retval=$$?; ${unlock_command} CompilePython${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) CompilePython done"

clean :: CompilePythonclean

CompilePythonclean :: $(CompilePythonclean_dependencies) ##$(cmt_local_CompilePython_makefile)
	$(echo) "(constituents.make) Starting CompilePythonclean"
	@-if test -f $(cmt_local_CompilePython_makefile); then \
	  $(MAKE) -f $(cmt_local_CompilePython_makefile) CompilePythonclean; \
	fi
	$(echo) "(constituents.make) CompilePythonclean done"
#	@-$(MAKE) -f $(cmt_local_CompilePython_makefile) CompilePythonclean

##	  /bin/rm -f $(cmt_local_CompilePython_makefile) $(bin)CompilePython_dependencies.make

install :: CompilePythoninstall

CompilePythoninstall :: $(CompilePython_dependencies) $(cmt_local_CompilePython_makefile)
	$(echo) "(constituents.make) Starting install CompilePython"
	@-$(MAKE) -f $(cmt_local_CompilePython_makefile) install
	$(echo) "(constituents.make) install CompilePython done"

uninstall :: CompilePythonuninstall

$(foreach d,$(CompilePython_dependencies),$(eval $(d)uninstall_dependencies += CompilePythonuninstall))

CompilePythonuninstall :: $(CompilePythonuninstall_dependencies) $(cmt_local_CompilePython_makefile)
	$(echo) "(constituents.make) Starting uninstall CompilePython"
	@$(MAKE) -f $(cmt_local_CompilePython_makefile) uninstall
	$(echo) "(constituents.make) uninstall CompilePython done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ CompilePython"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ CompilePython done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_qmtest_run_has_target_tag = 1

#--------------------------------------------------------

ifdef cmt_qmtest_run_has_target_tag

#cmt_local_tagfile_qmtest_run = $(TrackMonitors_tag)_qmtest_run.make
cmt_local_tagfile_qmtest_run = $(bin)$(TrackMonitors_tag)_qmtest_run.make
cmt_local_setup_qmtest_run = $(bin)setup_qmtest_run$$$$.make
cmt_final_setup_qmtest_run = $(bin)setup_qmtest_run.make
#cmt_final_setup_qmtest_run = $(bin)TrackMonitors_qmtest_runsetup.make
cmt_local_qmtest_run_makefile = $(bin)qmtest_run.make

qmtest_run_extratags = -tag_add=target_qmtest_run

#$(cmt_local_tagfile_qmtest_run) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_qmtest_run) ::
else
$(cmt_local_tagfile_qmtest_run) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_qmtest_run); then /bin/rm -f $(cmt_local_tagfile_qmtest_run); fi ; \
	  $(cmtexe) -tag=$(tags) $(qmtest_run_extratags) build tag_makefile >>$(cmt_local_tagfile_qmtest_run)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_qmtest_run)"; \
	  test ! -f $(cmt_local_setup_qmtest_run) || \rm -f $(cmt_local_setup_qmtest_run); \
	  trap '\rm -f $(cmt_local_setup_qmtest_run)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(qmtest_run_extratags) show setup >$(cmt_local_setup_qmtest_run) && \
	  if [ -f $(cmt_final_setup_qmtest_run) ] && \
	    \cmp -s $(cmt_final_setup_qmtest_run) $(cmt_local_setup_qmtest_run); then \
	    \rm $(cmt_local_setup_qmtest_run); else \
	    \mv -f $(cmt_local_setup_qmtest_run) $(cmt_final_setup_qmtest_run); fi

else

#cmt_local_tagfile_qmtest_run = $(TrackMonitors_tag).make
cmt_local_tagfile_qmtest_run = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_qmtest_run = $(bin)setup.make
#cmt_final_setup_qmtest_run = $(bin)TrackMonitorssetup.make
cmt_local_qmtest_run_makefile = $(bin)qmtest_run.make

endif

ifdef STRUCTURED_OUTPUT
qmtest_rundirs :
	@if test ! -d $(bin)qmtest_run; then $(mkdir) -p $(bin)qmtest_run; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)qmtest_run
else
qmtest_rundirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# qmtest_rundirs ::
#	@if test ! -d $(bin)qmtest_run; then $(mkdir) -p $(bin)qmtest_run; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)qmtest_run
#
#$(cmt_local_qmtest_run_makefile) :: $(qmtest_run_dependencies) $(cmt_local_tagfile_qmtest_run) build_library_links dirs qmtest_rundirs
#else
#$(cmt_local_qmtest_run_makefile) :: $(qmtest_run_dependencies) $(cmt_local_tagfile_qmtest_run) build_library_links dirs
#endif
#else
#$(cmt_local_qmtest_run_makefile) :: $(cmt_local_tagfile_qmtest_run)
#endif

makefiles : $(cmt_local_qmtest_run_makefile)

ifndef QUICK
$(cmt_local_qmtest_run_makefile) : $(qmtest_run_dependencies) $(cmt_local_tagfile_qmtest_run) build_library_links
else
$(cmt_local_qmtest_run_makefile) : $(cmt_local_tagfile_qmtest_run)
endif
	$(echo) "(constituents.make) Building qmtest_run.make"; \
	  $(cmtexe) -tag=$(tags) $(qmtest_run_extratags) build constituent_makefile -out=$(cmt_local_qmtest_run_makefile) qmtest_run

qmtest_run :: $(qmtest_run_dependencies) $(cmt_local_qmtest_run_makefile) dirs qmtest_rundirs
	$(echo) "(constituents.make) Creating qmtest_run${lock_suffix} and Starting qmtest_run"
	@${lock_command} qmtest_run${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} qmtest_run${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_qmtest_run_makefile) qmtest_run; \
	  retval=$$?; ${unlock_command} qmtest_run${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) qmtest_run done"

clean :: qmtest_runclean

qmtest_runclean :: $(qmtest_runclean_dependencies) ##$(cmt_local_qmtest_run_makefile)
	$(echo) "(constituents.make) Starting qmtest_runclean"
	@-if test -f $(cmt_local_qmtest_run_makefile); then \
	  $(MAKE) -f $(cmt_local_qmtest_run_makefile) qmtest_runclean; \
	fi
	$(echo) "(constituents.make) qmtest_runclean done"
#	@-$(MAKE) -f $(cmt_local_qmtest_run_makefile) qmtest_runclean

##	  /bin/rm -f $(cmt_local_qmtest_run_makefile) $(bin)qmtest_run_dependencies.make

install :: qmtest_runinstall

qmtest_runinstall :: $(qmtest_run_dependencies) $(cmt_local_qmtest_run_makefile)
	$(echo) "(constituents.make) Starting install qmtest_run"
	@-$(MAKE) -f $(cmt_local_qmtest_run_makefile) install
	$(echo) "(constituents.make) install qmtest_run done"

uninstall :: qmtest_rununinstall

$(foreach d,$(qmtest_run_dependencies),$(eval $(d)uninstall_dependencies += qmtest_rununinstall))

qmtest_rununinstall :: $(qmtest_rununinstall_dependencies) $(cmt_local_qmtest_run_makefile)
	$(echo) "(constituents.make) Starting uninstall qmtest_run"
	@$(MAKE) -f $(cmt_local_qmtest_run_makefile) uninstall
	$(echo) "(constituents.make) uninstall qmtest_run done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ qmtest_run"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ qmtest_run done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_qmtest_summarize_has_target_tag = 1

#--------------------------------------------------------

ifdef cmt_qmtest_summarize_has_target_tag

#cmt_local_tagfile_qmtest_summarize = $(TrackMonitors_tag)_qmtest_summarize.make
cmt_local_tagfile_qmtest_summarize = $(bin)$(TrackMonitors_tag)_qmtest_summarize.make
cmt_local_setup_qmtest_summarize = $(bin)setup_qmtest_summarize$$$$.make
cmt_final_setup_qmtest_summarize = $(bin)setup_qmtest_summarize.make
#cmt_final_setup_qmtest_summarize = $(bin)TrackMonitors_qmtest_summarizesetup.make
cmt_local_qmtest_summarize_makefile = $(bin)qmtest_summarize.make

qmtest_summarize_extratags = -tag_add=target_qmtest_summarize

#$(cmt_local_tagfile_qmtest_summarize) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_qmtest_summarize) ::
else
$(cmt_local_tagfile_qmtest_summarize) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_qmtest_summarize); then /bin/rm -f $(cmt_local_tagfile_qmtest_summarize); fi ; \
	  $(cmtexe) -tag=$(tags) $(qmtest_summarize_extratags) build tag_makefile >>$(cmt_local_tagfile_qmtest_summarize)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_qmtest_summarize)"; \
	  test ! -f $(cmt_local_setup_qmtest_summarize) || \rm -f $(cmt_local_setup_qmtest_summarize); \
	  trap '\rm -f $(cmt_local_setup_qmtest_summarize)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(qmtest_summarize_extratags) show setup >$(cmt_local_setup_qmtest_summarize) && \
	  if [ -f $(cmt_final_setup_qmtest_summarize) ] && \
	    \cmp -s $(cmt_final_setup_qmtest_summarize) $(cmt_local_setup_qmtest_summarize); then \
	    \rm $(cmt_local_setup_qmtest_summarize); else \
	    \mv -f $(cmt_local_setup_qmtest_summarize) $(cmt_final_setup_qmtest_summarize); fi

else

#cmt_local_tagfile_qmtest_summarize = $(TrackMonitors_tag).make
cmt_local_tagfile_qmtest_summarize = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_qmtest_summarize = $(bin)setup.make
#cmt_final_setup_qmtest_summarize = $(bin)TrackMonitorssetup.make
cmt_local_qmtest_summarize_makefile = $(bin)qmtest_summarize.make

endif

ifdef STRUCTURED_OUTPUT
qmtest_summarizedirs :
	@if test ! -d $(bin)qmtest_summarize; then $(mkdir) -p $(bin)qmtest_summarize; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)qmtest_summarize
else
qmtest_summarizedirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# qmtest_summarizedirs ::
#	@if test ! -d $(bin)qmtest_summarize; then $(mkdir) -p $(bin)qmtest_summarize; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)qmtest_summarize
#
#$(cmt_local_qmtest_summarize_makefile) :: $(qmtest_summarize_dependencies) $(cmt_local_tagfile_qmtest_summarize) build_library_links dirs qmtest_summarizedirs
#else
#$(cmt_local_qmtest_summarize_makefile) :: $(qmtest_summarize_dependencies) $(cmt_local_tagfile_qmtest_summarize) build_library_links dirs
#endif
#else
#$(cmt_local_qmtest_summarize_makefile) :: $(cmt_local_tagfile_qmtest_summarize)
#endif

makefiles : $(cmt_local_qmtest_summarize_makefile)

ifndef QUICK
$(cmt_local_qmtest_summarize_makefile) : $(qmtest_summarize_dependencies) $(cmt_local_tagfile_qmtest_summarize) build_library_links
else
$(cmt_local_qmtest_summarize_makefile) : $(cmt_local_tagfile_qmtest_summarize)
endif
	$(echo) "(constituents.make) Building qmtest_summarize.make"; \
	  $(cmtexe) -tag=$(tags) $(qmtest_summarize_extratags) build constituent_makefile -out=$(cmt_local_qmtest_summarize_makefile) qmtest_summarize

qmtest_summarize :: $(qmtest_summarize_dependencies) $(cmt_local_qmtest_summarize_makefile) dirs qmtest_summarizedirs
	$(echo) "(constituents.make) Creating qmtest_summarize${lock_suffix} and Starting qmtest_summarize"
	@${lock_command} qmtest_summarize${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} qmtest_summarize${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_qmtest_summarize_makefile) qmtest_summarize; \
	  retval=$$?; ${unlock_command} qmtest_summarize${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) qmtest_summarize done"

clean :: qmtest_summarizeclean

qmtest_summarizeclean :: $(qmtest_summarizeclean_dependencies) ##$(cmt_local_qmtest_summarize_makefile)
	$(echo) "(constituents.make) Starting qmtest_summarizeclean"
	@-if test -f $(cmt_local_qmtest_summarize_makefile); then \
	  $(MAKE) -f $(cmt_local_qmtest_summarize_makefile) qmtest_summarizeclean; \
	fi
	$(echo) "(constituents.make) qmtest_summarizeclean done"
#	@-$(MAKE) -f $(cmt_local_qmtest_summarize_makefile) qmtest_summarizeclean

##	  /bin/rm -f $(cmt_local_qmtest_summarize_makefile) $(bin)qmtest_summarize_dependencies.make

install :: qmtest_summarizeinstall

qmtest_summarizeinstall :: $(qmtest_summarize_dependencies) $(cmt_local_qmtest_summarize_makefile)
	$(echo) "(constituents.make) Starting install qmtest_summarize"
	@-$(MAKE) -f $(cmt_local_qmtest_summarize_makefile) install
	$(echo) "(constituents.make) install qmtest_summarize done"

uninstall :: qmtest_summarizeuninstall

$(foreach d,$(qmtest_summarize_dependencies),$(eval $(d)uninstall_dependencies += qmtest_summarizeuninstall))

qmtest_summarizeuninstall :: $(qmtest_summarizeuninstall_dependencies) $(cmt_local_qmtest_summarize_makefile)
	$(echo) "(constituents.make) Starting uninstall qmtest_summarize"
	@$(MAKE) -f $(cmt_local_qmtest_summarize_makefile) uninstall
	$(echo) "(constituents.make) uninstall qmtest_summarize done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ qmtest_summarize"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ qmtest_summarize done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_TestPackage_has_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TestPackage_has_target_tag

#cmt_local_tagfile_TestPackage = $(TrackMonitors_tag)_TestPackage.make
cmt_local_tagfile_TestPackage = $(bin)$(TrackMonitors_tag)_TestPackage.make
cmt_local_setup_TestPackage = $(bin)setup_TestPackage$$$$.make
cmt_final_setup_TestPackage = $(bin)setup_TestPackage.make
#cmt_final_setup_TestPackage = $(bin)TrackMonitors_TestPackagesetup.make
cmt_local_TestPackage_makefile = $(bin)TestPackage.make

TestPackage_extratags = -tag_add=target_TestPackage

#$(cmt_local_tagfile_TestPackage) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_TestPackage) ::
else
$(cmt_local_tagfile_TestPackage) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_TestPackage); then /bin/rm -f $(cmt_local_tagfile_TestPackage); fi ; \
	  $(cmtexe) -tag=$(tags) $(TestPackage_extratags) build tag_makefile >>$(cmt_local_tagfile_TestPackage)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_TestPackage)"; \
	  test ! -f $(cmt_local_setup_TestPackage) || \rm -f $(cmt_local_setup_TestPackage); \
	  trap '\rm -f $(cmt_local_setup_TestPackage)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(TestPackage_extratags) show setup >$(cmt_local_setup_TestPackage) && \
	  if [ -f $(cmt_final_setup_TestPackage) ] && \
	    \cmp -s $(cmt_final_setup_TestPackage) $(cmt_local_setup_TestPackage); then \
	    \rm $(cmt_local_setup_TestPackage); else \
	    \mv -f $(cmt_local_setup_TestPackage) $(cmt_final_setup_TestPackage); fi

else

#cmt_local_tagfile_TestPackage = $(TrackMonitors_tag).make
cmt_local_tagfile_TestPackage = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_TestPackage = $(bin)setup.make
#cmt_final_setup_TestPackage = $(bin)TrackMonitorssetup.make
cmt_local_TestPackage_makefile = $(bin)TestPackage.make

endif

ifdef STRUCTURED_OUTPUT
TestPackagedirs :
	@if test ! -d $(bin)TestPackage; then $(mkdir) -p $(bin)TestPackage; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)TestPackage
else
TestPackagedirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# TestPackagedirs ::
#	@if test ! -d $(bin)TestPackage; then $(mkdir) -p $(bin)TestPackage; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)TestPackage
#
#$(cmt_local_TestPackage_makefile) :: $(TestPackage_dependencies) $(cmt_local_tagfile_TestPackage) build_library_links dirs TestPackagedirs
#else
#$(cmt_local_TestPackage_makefile) :: $(TestPackage_dependencies) $(cmt_local_tagfile_TestPackage) build_library_links dirs
#endif
#else
#$(cmt_local_TestPackage_makefile) :: $(cmt_local_tagfile_TestPackage)
#endif

makefiles : $(cmt_local_TestPackage_makefile)

ifndef QUICK
$(cmt_local_TestPackage_makefile) : $(TestPackage_dependencies) $(cmt_local_tagfile_TestPackage) build_library_links
else
$(cmt_local_TestPackage_makefile) : $(cmt_local_tagfile_TestPackage)
endif
	$(echo) "(constituents.make) Building TestPackage.make"; \
	  $(cmtexe) -tag=$(tags) $(TestPackage_extratags) build constituent_makefile -out=$(cmt_local_TestPackage_makefile) TestPackage

TestPackage :: $(TestPackage_dependencies) $(cmt_local_TestPackage_makefile) dirs TestPackagedirs
	$(echo) "(constituents.make) Creating TestPackage${lock_suffix} and Starting TestPackage"
	@${lock_command} TestPackage${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} TestPackage${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_TestPackage_makefile) TestPackage; \
	  retval=$$?; ${unlock_command} TestPackage${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) TestPackage done"

clean :: TestPackageclean

TestPackageclean :: $(TestPackageclean_dependencies) ##$(cmt_local_TestPackage_makefile)
	$(echo) "(constituents.make) Starting TestPackageclean"
	@-if test -f $(cmt_local_TestPackage_makefile); then \
	  $(MAKE) -f $(cmt_local_TestPackage_makefile) TestPackageclean; \
	fi
	$(echo) "(constituents.make) TestPackageclean done"
#	@-$(MAKE) -f $(cmt_local_TestPackage_makefile) TestPackageclean

##	  /bin/rm -f $(cmt_local_TestPackage_makefile) $(bin)TestPackage_dependencies.make

install :: TestPackageinstall

TestPackageinstall :: $(TestPackage_dependencies) $(cmt_local_TestPackage_makefile)
	$(echo) "(constituents.make) Starting install TestPackage"
	@-$(MAKE) -f $(cmt_local_TestPackage_makefile) install
	$(echo) "(constituents.make) install TestPackage done"

uninstall :: TestPackageuninstall

$(foreach d,$(TestPackage_dependencies),$(eval $(d)uninstall_dependencies += TestPackageuninstall))

TestPackageuninstall :: $(TestPackageuninstall_dependencies) $(cmt_local_TestPackage_makefile)
	$(echo) "(constituents.make) Starting uninstall TestPackage"
	@$(MAKE) -f $(cmt_local_TestPackage_makefile) uninstall
	$(echo) "(constituents.make) uninstall TestPackage done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ TestPackage"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ TestPackage done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_TestProject_has_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TestProject_has_target_tag

#cmt_local_tagfile_TestProject = $(TrackMonitors_tag)_TestProject.make
cmt_local_tagfile_TestProject = $(bin)$(TrackMonitors_tag)_TestProject.make
cmt_local_setup_TestProject = $(bin)setup_TestProject$$$$.make
cmt_final_setup_TestProject = $(bin)setup_TestProject.make
#cmt_final_setup_TestProject = $(bin)TrackMonitors_TestProjectsetup.make
cmt_local_TestProject_makefile = $(bin)TestProject.make

TestProject_extratags = -tag_add=target_TestProject

#$(cmt_local_tagfile_TestProject) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_TestProject) ::
else
$(cmt_local_tagfile_TestProject) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_TestProject); then /bin/rm -f $(cmt_local_tagfile_TestProject); fi ; \
	  $(cmtexe) -tag=$(tags) $(TestProject_extratags) build tag_makefile >>$(cmt_local_tagfile_TestProject)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_TestProject)"; \
	  test ! -f $(cmt_local_setup_TestProject) || \rm -f $(cmt_local_setup_TestProject); \
	  trap '\rm -f $(cmt_local_setup_TestProject)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(TestProject_extratags) show setup >$(cmt_local_setup_TestProject) && \
	  if [ -f $(cmt_final_setup_TestProject) ] && \
	    \cmp -s $(cmt_final_setup_TestProject) $(cmt_local_setup_TestProject); then \
	    \rm $(cmt_local_setup_TestProject); else \
	    \mv -f $(cmt_local_setup_TestProject) $(cmt_final_setup_TestProject); fi

else

#cmt_local_tagfile_TestProject = $(TrackMonitors_tag).make
cmt_local_tagfile_TestProject = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_TestProject = $(bin)setup.make
#cmt_final_setup_TestProject = $(bin)TrackMonitorssetup.make
cmt_local_TestProject_makefile = $(bin)TestProject.make

endif

ifdef STRUCTURED_OUTPUT
TestProjectdirs :
	@if test ! -d $(bin)TestProject; then $(mkdir) -p $(bin)TestProject; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)TestProject
else
TestProjectdirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# TestProjectdirs ::
#	@if test ! -d $(bin)TestProject; then $(mkdir) -p $(bin)TestProject; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)TestProject
#
#$(cmt_local_TestProject_makefile) :: $(TestProject_dependencies) $(cmt_local_tagfile_TestProject) build_library_links dirs TestProjectdirs
#else
#$(cmt_local_TestProject_makefile) :: $(TestProject_dependencies) $(cmt_local_tagfile_TestProject) build_library_links dirs
#endif
#else
#$(cmt_local_TestProject_makefile) :: $(cmt_local_tagfile_TestProject)
#endif

makefiles : $(cmt_local_TestProject_makefile)

ifndef QUICK
$(cmt_local_TestProject_makefile) : $(TestProject_dependencies) $(cmt_local_tagfile_TestProject) build_library_links
else
$(cmt_local_TestProject_makefile) : $(cmt_local_tagfile_TestProject)
endif
	$(echo) "(constituents.make) Building TestProject.make"; \
	  $(cmtexe) -tag=$(tags) $(TestProject_extratags) build constituent_makefile -out=$(cmt_local_TestProject_makefile) TestProject

TestProject :: $(TestProject_dependencies) $(cmt_local_TestProject_makefile) dirs TestProjectdirs
	$(echo) "(constituents.make) Creating TestProject${lock_suffix} and Starting TestProject"
	@${lock_command} TestProject${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} TestProject${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_TestProject_makefile) TestProject; \
	  retval=$$?; ${unlock_command} TestProject${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) TestProject done"

clean :: TestProjectclean

TestProjectclean :: $(TestProjectclean_dependencies) ##$(cmt_local_TestProject_makefile)
	$(echo) "(constituents.make) Starting TestProjectclean"
	@-if test -f $(cmt_local_TestProject_makefile); then \
	  $(MAKE) -f $(cmt_local_TestProject_makefile) TestProjectclean; \
	fi
	$(echo) "(constituents.make) TestProjectclean done"
#	@-$(MAKE) -f $(cmt_local_TestProject_makefile) TestProjectclean

##	  /bin/rm -f $(cmt_local_TestProject_makefile) $(bin)TestProject_dependencies.make

install :: TestProjectinstall

TestProjectinstall :: $(TestProject_dependencies) $(cmt_local_TestProject_makefile)
	$(echo) "(constituents.make) Starting install TestProject"
	@-$(MAKE) -f $(cmt_local_TestProject_makefile) install
	$(echo) "(constituents.make) install TestProject done"

uninstall :: TestProjectuninstall

$(foreach d,$(TestProject_dependencies),$(eval $(d)uninstall_dependencies += TestProjectuninstall))

TestProjectuninstall :: $(TestProjectuninstall_dependencies) $(cmt_local_TestProject_makefile)
	$(echo) "(constituents.make) Starting uninstall TestProject"
	@$(MAKE) -f $(cmt_local_TestProject_makefile) uninstall
	$(echo) "(constituents.make) uninstall TestProject done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ TestProject"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ TestProject done"
endif

#-- end of constituent_lock ------
#-- start of constituent_lock ------

cmt_new_rootsys_has_target_tag = 1

#--------------------------------------------------------

ifdef cmt_new_rootsys_has_target_tag

#cmt_local_tagfile_new_rootsys = $(TrackMonitors_tag)_new_rootsys.make
cmt_local_tagfile_new_rootsys = $(bin)$(TrackMonitors_tag)_new_rootsys.make
cmt_local_setup_new_rootsys = $(bin)setup_new_rootsys$$$$.make
cmt_final_setup_new_rootsys = $(bin)setup_new_rootsys.make
#cmt_final_setup_new_rootsys = $(bin)TrackMonitors_new_rootsyssetup.make
cmt_local_new_rootsys_makefile = $(bin)new_rootsys.make

new_rootsys_extratags = -tag_add=target_new_rootsys

#$(cmt_local_tagfile_new_rootsys) : $(cmt_lock_setup)
ifndef QUICK
$(cmt_local_tagfile_new_rootsys) ::
else
$(cmt_local_tagfile_new_rootsys) :
endif
	$(echo) "(constituents.make) Rebuilding $@"; \
	  if test -f $(cmt_local_tagfile_new_rootsys); then /bin/rm -f $(cmt_local_tagfile_new_rootsys); fi ; \
	  $(cmtexe) -tag=$(tags) $(new_rootsys_extratags) build tag_makefile >>$(cmt_local_tagfile_new_rootsys)
	$(echo) "(constituents.make) Rebuilding $(cmt_final_setup_new_rootsys)"; \
	  test ! -f $(cmt_local_setup_new_rootsys) || \rm -f $(cmt_local_setup_new_rootsys); \
	  trap '\rm -f $(cmt_local_setup_new_rootsys)' 0 1 2 15; \
	  $(cmtexe) -tag=$(tags) $(new_rootsys_extratags) show setup >$(cmt_local_setup_new_rootsys) && \
	  if [ -f $(cmt_final_setup_new_rootsys) ] && \
	    \cmp -s $(cmt_final_setup_new_rootsys) $(cmt_local_setup_new_rootsys); then \
	    \rm $(cmt_local_setup_new_rootsys); else \
	    \mv -f $(cmt_local_setup_new_rootsys) $(cmt_final_setup_new_rootsys); fi

else

#cmt_local_tagfile_new_rootsys = $(TrackMonitors_tag).make
cmt_local_tagfile_new_rootsys = $(bin)$(TrackMonitors_tag).make
cmt_final_setup_new_rootsys = $(bin)setup.make
#cmt_final_setup_new_rootsys = $(bin)TrackMonitorssetup.make
cmt_local_new_rootsys_makefile = $(bin)new_rootsys.make

endif

ifdef STRUCTURED_OUTPUT
new_rootsysdirs :
	@if test ! -d $(bin)new_rootsys; then $(mkdir) -p $(bin)new_rootsys; fi
	$(echo) "STRUCTURED_OUTPUT="$(bin)new_rootsys
else
new_rootsysdirs : ;
endif

#ifndef QUICK
#ifdef STRUCTURED_OUTPUT
# new_rootsysdirs ::
#	@if test ! -d $(bin)new_rootsys; then $(mkdir) -p $(bin)new_rootsys; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)new_rootsys
#
#$(cmt_local_new_rootsys_makefile) :: $(new_rootsys_dependencies) $(cmt_local_tagfile_new_rootsys) build_library_links dirs new_rootsysdirs
#else
#$(cmt_local_new_rootsys_makefile) :: $(new_rootsys_dependencies) $(cmt_local_tagfile_new_rootsys) build_library_links dirs
#endif
#else
#$(cmt_local_new_rootsys_makefile) :: $(cmt_local_tagfile_new_rootsys)
#endif

makefiles : $(cmt_local_new_rootsys_makefile)

ifndef QUICK
$(cmt_local_new_rootsys_makefile) : $(new_rootsys_dependencies) $(cmt_local_tagfile_new_rootsys) build_library_links
else
$(cmt_local_new_rootsys_makefile) : $(cmt_local_tagfile_new_rootsys)
endif
	$(echo) "(constituents.make) Building new_rootsys.make"; \
	  $(cmtexe) -tag=$(tags) $(new_rootsys_extratags) build constituent_makefile -out=$(cmt_local_new_rootsys_makefile) new_rootsys

new_rootsys :: $(new_rootsys_dependencies) $(cmt_local_new_rootsys_makefile) dirs new_rootsysdirs
	$(echo) "(constituents.make) Creating new_rootsys${lock_suffix} and Starting new_rootsys"
	@${lock_command} new_rootsys${lock_suffix} || exit $$?; \
	  retval=$$?; \
	  trap '${unlock_command} new_rootsys${lock_suffix}; exit $${retval}' 1 2 15; \
	  $(MAKE) -f $(cmt_local_new_rootsys_makefile) new_rootsys; \
	  retval=$$?; ${unlock_command} new_rootsys${lock_suffix}; exit $${retval}
	$(echo) "(constituents.make) new_rootsys done"

clean :: new_rootsysclean

new_rootsysclean :: $(new_rootsysclean_dependencies) ##$(cmt_local_new_rootsys_makefile)
	$(echo) "(constituents.make) Starting new_rootsysclean"
	@-if test -f $(cmt_local_new_rootsys_makefile); then \
	  $(MAKE) -f $(cmt_local_new_rootsys_makefile) new_rootsysclean; \
	fi
	$(echo) "(constituents.make) new_rootsysclean done"
#	@-$(MAKE) -f $(cmt_local_new_rootsys_makefile) new_rootsysclean

##	  /bin/rm -f $(cmt_local_new_rootsys_makefile) $(bin)new_rootsys_dependencies.make

install :: new_rootsysinstall

new_rootsysinstall :: $(new_rootsys_dependencies) $(cmt_local_new_rootsys_makefile)
	$(echo) "(constituents.make) Starting install new_rootsys"
	@-$(MAKE) -f $(cmt_local_new_rootsys_makefile) install
	$(echo) "(constituents.make) install new_rootsys done"

uninstall :: new_rootsysuninstall

$(foreach d,$(new_rootsys_dependencies),$(eval $(d)uninstall_dependencies += new_rootsysuninstall))

new_rootsysuninstall :: $(new_rootsysuninstall_dependencies) $(cmt_local_new_rootsys_makefile)
	$(echo) "(constituents.make) Starting uninstall new_rootsys"
	@$(MAKE) -f $(cmt_local_new_rootsys_makefile) uninstall
	$(echo) "(constituents.make) uninstall new_rootsys done"

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(constituents.make) Starting $@ new_rootsys"
	$(echo) Using default action for $@
	$(echo) "(constituents.make) $@ new_rootsys done"
endif

#-- end of constituent_lock ------
#-- start of constituents_trailer ------

clean :: remove_library_links

remove_library_links ::
	$(echo) "(constituents.make) Removing library links"; \
	  $(remove_library_links)

makefilesclean ::

###	@/bin/rm -f checkuses

###	/bin/rm -f *.make*

clean :: makefilesclean

binclean :: clean
	$(echo) "(constituents.make) Removing binary directory $(bin)"
	@if test ! "$(bin)" = "./"; then \
	  /bin/rm -rf $(bin); \
	fi

#-- end of constituents_trailer ------
