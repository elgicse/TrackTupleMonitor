#-- start of make_header -----------------

#====================================
#  Document TrackMonitorsConfDbMerge
#
#   Generated Wed Nov 12 13:49:11 2014  by ikomarov
#
#====================================

include ${CMTROOT}/src/Makefile.core

ifdef tag
CMTEXTRATAGS = $(tag)
else
tag       = $(CMTCONFIG)
endif

cmt_TrackMonitorsConfDbMerge_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitorsConfDbMerge_has_target_tag

tags      = $(tag),$(CMTEXTRATAGS),target_TrackMonitorsConfDbMerge

TrackMonitors_tag = $(tag)

#cmt_local_tagfile_TrackMonitorsConfDbMerge = $(TrackMonitors_tag)_TrackMonitorsConfDbMerge.make
cmt_local_tagfile_TrackMonitorsConfDbMerge = $(bin)$(TrackMonitors_tag)_TrackMonitorsConfDbMerge.make

else

tags      = $(tag),$(CMTEXTRATAGS)

TrackMonitors_tag = $(tag)

#cmt_local_tagfile_TrackMonitorsConfDbMerge = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitorsConfDbMerge = $(bin)$(TrackMonitors_tag).make

endif

include $(cmt_local_tagfile_TrackMonitorsConfDbMerge)
#-include $(cmt_local_tagfile_TrackMonitorsConfDbMerge)

ifdef cmt_TrackMonitorsConfDbMerge_has_target_tag

cmt_final_setup_TrackMonitorsConfDbMerge = $(bin)setup_TrackMonitorsConfDbMerge.make
#cmt_final_setup_TrackMonitorsConfDbMerge = $(bin)TrackMonitors_TrackMonitorsConfDbMergesetup.make
cmt_local_TrackMonitorsConfDbMerge_makefile = $(bin)TrackMonitorsConfDbMerge.make

else

cmt_final_setup_TrackMonitorsConfDbMerge = $(bin)setup.make
#cmt_final_setup_TrackMonitorsConfDbMerge = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitorsConfDbMerge_makefile = $(bin)TrackMonitorsConfDbMerge.make

endif

cmt_final_setup = $(bin)setup.make
#cmt_final_setup = $(bin)TrackMonitorssetup.make

#TrackMonitorsConfDbMerge :: ;

dirs ::
	@if test ! -r requirements ; then echo "No requirements file" ; fi; \
	  if test ! -d $(bin) ; then $(mkdir) -p $(bin) ; fi

javadirs ::
	@if test ! -d $(javabin) ; then $(mkdir) -p $(javabin) ; fi

srcdirs ::
	@if test ! -d $(src) ; then $(mkdir) -p $(src) ; fi

help ::
	$(echo) 'TrackMonitorsConfDbMerge'

binobj = 
ifdef STRUCTURED_OUTPUT
binobj = TrackMonitorsConfDbMerge/
#TrackMonitorsConfDbMerge::
#	@if test ! -d $(bin)$(binobj) ; then $(mkdir) -p $(bin)$(binobj) ; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)$(binobj)
endif

ifdef use_requirements
$(use_requirements) : ;
endif

#-- end of make_header ------------------
# File: cmt/fragments/merge_genconfDb_header
# Author: Sebastien Binet (binet@cern.ch)

# Makefile fragment to merge a <library>_confDb.py file into a single
# <project>_merged_confDb.py file in the (python) install area
# Note that <project> is massaged to get a valid python module name
# (ie: remove dots and dashes)

.PHONY: TrackMonitorsConfDbMerge TrackMonitorsConfDbMergeclean

# default is already '#'
#genconfDb_comment_char := "'#'"

instdir      := ${CMTINSTALLAREA}$(shared_install_subdir)
confDbRef    := /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr/TrackMonitors/x86_64-slc6-gcc48-opt/genConf/TrackMonitors/TrackMonitors_confDb.py
stampConfDb  := $(confDbRef).stamp
mergedConfDb := $(instdir)/python/$(subst .,_,$(subst -,_,$(project)))_merged_confDb.py

TrackMonitorsConfDbMerge :: $(stampConfDb) $(mergedConfDb)
	@:

.NOTPARALLEL : $(stampConfDb) $(mergedConfDb)

$(stampConfDb) $(mergedConfDb) :: $(confDbRef)
	@echo "Running merge_genconfDb  TrackMonitorsConfDbMerge"
	$(merge_genconfDb_cmd) \
          --do-merge \
          --input-file $(confDbRef) \
          --merged-file $(mergedConfDb)

TrackMonitorsConfDbMergeclean ::
	$(cleanup_silent) $(merge_genconfDb_cmd) \
          --un-merge \
          --input-file $(confDbRef) \
          --merged-file $(mergedConfDb)	;
	$(cleanup_silent) $(remove_command) $(stampConfDb)
libTrackMonitors_so_dependencies = ../x86_64-slc6-gcc48-opt/libTrackMonitors.so
#-- start of cleanup_header --------------

clean :: TrackMonitorsConfDbMergeclean ;
#	@cd .

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(TrackMonitorsConfDbMerge.make) $@: No rule for such target" >&2
#	@echo "#CMT> Warning: $@: No rule for such target" >&2; exit
	if echo $@ | grep '$(package)setup\.make$$' >/dev/null; then\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsConfDbMerge.make): $@: File no longer generated" >&2; exit 0; fi
else
.DEFAULT::
	$(echo) "(TrackMonitorsConfDbMerge.make) PEDANTIC: $@: No rule for such target" >&2
	if echo $@ | grep '$(package)setup\.make$$' >/dev/null; then\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsConfDbMerge.make): $@: File no longer generated" >&2; exit 0;\
	 elif test $@ = "$(cmt_final_setup)" -o\
	 $@ = "$(cmt_final_setup_TrackMonitorsConfDbMerge)" ; then\
	 found=n; for s in 1 2 3 4 5; do\
	 sleep $$s; test ! -f $@ || { found=y; break; }\
	 done; if test $$found = n; then\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsConfDbMerge.make) PEDANTIC: $@: Seems to be missing. Ignore it for now" >&2; exit 0 ; fi;\
	 elif test `expr $@ : '.*/'` -ne 0 ; then\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsConfDbMerge.make) PEDANTIC: $@: Seems to be a missing file. Please check" >&2; exit 2 ; \
	 else\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsConfDbMerge.make) PEDANTIC: $@: Seems to be a fake target due to some pattern. Just ignore it" >&2 ; exit 0; fi
endif

TrackMonitorsConfDbMergeclean ::
#-- end of cleanup_header ---------------
