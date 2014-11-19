#-- start of make_header -----------------

#====================================
#  Document TrackMonitorsConf
#
#   Generated Wed Nov 12 13:49:01 2014  by ikomarov
#
#====================================

include ${CMTROOT}/src/Makefile.core

ifdef tag
CMTEXTRATAGS = $(tag)
else
tag       = $(CMTCONFIG)
endif

cmt_TrackMonitorsConf_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitorsConf_has_target_tag

tags      = $(tag),$(CMTEXTRATAGS),target_TrackMonitorsConf

TrackMonitors_tag = $(tag)

#cmt_local_tagfile_TrackMonitorsConf = $(TrackMonitors_tag)_TrackMonitorsConf.make
cmt_local_tagfile_TrackMonitorsConf = $(bin)$(TrackMonitors_tag)_TrackMonitorsConf.make

else

tags      = $(tag),$(CMTEXTRATAGS)

TrackMonitors_tag = $(tag)

#cmt_local_tagfile_TrackMonitorsConf = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitorsConf = $(bin)$(TrackMonitors_tag).make

endif

include $(cmt_local_tagfile_TrackMonitorsConf)
#-include $(cmt_local_tagfile_TrackMonitorsConf)

ifdef cmt_TrackMonitorsConf_has_target_tag

cmt_final_setup_TrackMonitorsConf = $(bin)setup_TrackMonitorsConf.make
#cmt_final_setup_TrackMonitorsConf = $(bin)TrackMonitors_TrackMonitorsConfsetup.make
cmt_local_TrackMonitorsConf_makefile = $(bin)TrackMonitorsConf.make

else

cmt_final_setup_TrackMonitorsConf = $(bin)setup.make
#cmt_final_setup_TrackMonitorsConf = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitorsConf_makefile = $(bin)TrackMonitorsConf.make

endif

cmt_final_setup = $(bin)setup.make
#cmt_final_setup = $(bin)TrackMonitorssetup.make

#TrackMonitorsConf :: ;

dirs ::
	@if test ! -r requirements ; then echo "No requirements file" ; fi; \
	  if test ! -d $(bin) ; then $(mkdir) -p $(bin) ; fi

javadirs ::
	@if test ! -d $(javabin) ; then $(mkdir) -p $(javabin) ; fi

srcdirs ::
	@if test ! -d $(src) ; then $(mkdir) -p $(src) ; fi

help ::
	$(echo) 'TrackMonitorsConf'

binobj = 
ifdef STRUCTURED_OUTPUT
binobj = TrackMonitorsConf/
#TrackMonitorsConf::
#	@if test ! -d $(bin)$(binobj) ; then $(mkdir) -p $(bin)$(binobj) ; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)$(binobj)
endif

ifdef use_requirements
$(use_requirements) : ;
endif

#-- end of make_header ------------------
# File: cmt/fragments/genconfig_header
# Author: Wim Lavrijsen (WLavrijsen@lbl.gov)

# Use genconf.exe to create configurables python modules, then have the
# normal python install procedure take over.

.PHONY: TrackMonitorsConf TrackMonitorsConfclean

confpy  := TrackMonitorsConf.py
conflib := $(bin)$(library_prefix)TrackMonitors.$(shlibsuffix)
dbpy    := TrackMonitors_confDb.py
instdir := $(CMTINSTALLAREA)$(shared_install_subdir)/python/$(package)
product := $(instdir)/$(confpy)
initpy  := $(instdir)/__init__.py

ifdef GENCONF_ECHO
genconf_silent =
else
genconf_silent = $(silent)
endif

TrackMonitorsConf :: TrackMonitorsConfinstall

install :: TrackMonitorsConfinstall

TrackMonitorsConfinstall : /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors/$(confpy)
	@echo "Installing /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors in /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/InstallArea/x86_64-slc6-gcc48-opt/python" ; \
	 $(install_command) --exclude="*.py?" --exclude="__init__.py" /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/InstallArea/x86_64-slc6-gcc48-opt/python ; \

/afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors/$(confpy) : $(conflib) /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors
	$(genconf_silent) $(genconfig_cmd)   -o /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors -p $(package) \
	  --configurable-module=GaudiKernel.Proxy \
	  --configurable-default-name=Configurable.DefaultName \
	  --configurable-algorithm=ConfigurableAlgorithm \
	  --configurable-algtool=ConfigurableAlgTool \
	  --configurable-auditor=ConfigurableAuditor \
          --configurable-service=ConfigurableService \
	  -i ../$(tag)/$(library_prefix)TrackMonitors.$(shlibsuffix)

/afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors:
	@ if [ ! -d /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors ] ; then mkdir -p /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors ; fi ;

TrackMonitorsConfclean :: TrackMonitorsConfuninstall
	$(cleanup_silent) $(remove_command) /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors/$(confpy) /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors/$(dbpy)

uninstall :: TrackMonitorsConfuninstall

TrackMonitorsConfuninstall ::
	@$(uninstall_command) /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/InstallArea/x86_64-slc6-gcc48-opt/python
libTrackMonitors_so_dependencies = ../x86_64-slc6-gcc48-opt/libTrackMonitors.so
#-- start of cleanup_header --------------

clean :: TrackMonitorsConfclean ;
#	@cd .

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(TrackMonitorsConf.make) $@: No rule for such target" >&2
#	@echo "#CMT> Warning: $@: No rule for such target" >&2; exit
	if echo $@ | grep '$(package)setup\.make$$' >/dev/null; then\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsConf.make): $@: File no longer generated" >&2; exit 0; fi
else
.DEFAULT::
	$(echo) "(TrackMonitorsConf.make) PEDANTIC: $@: No rule for such target" >&2
	if echo $@ | grep '$(package)setup\.make$$' >/dev/null; then\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsConf.make): $@: File no longer generated" >&2; exit 0;\
	 elif test $@ = "$(cmt_final_setup)" -o\
	 $@ = "$(cmt_final_setup_TrackMonitorsConf)" ; then\
	 found=n; for s in 1 2 3 4 5; do\
	 sleep $$s; test ! -f $@ || { found=y; break; }\
	 done; if test $$found = n; then\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsConf.make) PEDANTIC: $@: Seems to be missing. Ignore it for now" >&2; exit 0 ; fi;\
	 elif test `expr $@ : '.*/'` -ne 0 ; then\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsConf.make) PEDANTIC: $@: Seems to be a missing file. Please check" >&2; exit 2 ; \
	 else\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsConf.make) PEDANTIC: $@: Seems to be a fake target due to some pattern. Just ignore it" >&2 ; exit 0; fi
endif

TrackMonitorsConfclean ::
#-- end of cleanup_header ---------------
