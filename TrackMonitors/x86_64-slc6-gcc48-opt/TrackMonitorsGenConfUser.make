#-- start of make_header -----------------

#====================================
#  Document TrackMonitorsGenConfUser
#
#   Generated Wed Nov 12 13:49:04 2014  by ikomarov
#
#====================================

include ${CMTROOT}/src/Makefile.core

ifdef tag
CMTEXTRATAGS = $(tag)
else
tag       = $(CMTCONFIG)
endif

cmt_TrackMonitorsGenConfUser_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_TrackMonitorsGenConfUser_has_target_tag

tags      = $(tag),$(CMTEXTRATAGS),target_TrackMonitorsGenConfUser

TrackMonitors_tag = $(tag)

#cmt_local_tagfile_TrackMonitorsGenConfUser = $(TrackMonitors_tag)_TrackMonitorsGenConfUser.make
cmt_local_tagfile_TrackMonitorsGenConfUser = $(bin)$(TrackMonitors_tag)_TrackMonitorsGenConfUser.make

else

tags      = $(tag),$(CMTEXTRATAGS)

TrackMonitors_tag = $(tag)

#cmt_local_tagfile_TrackMonitorsGenConfUser = $(TrackMonitors_tag).make
cmt_local_tagfile_TrackMonitorsGenConfUser = $(bin)$(TrackMonitors_tag).make

endif

include $(cmt_local_tagfile_TrackMonitorsGenConfUser)
#-include $(cmt_local_tagfile_TrackMonitorsGenConfUser)

ifdef cmt_TrackMonitorsGenConfUser_has_target_tag

cmt_final_setup_TrackMonitorsGenConfUser = $(bin)setup_TrackMonitorsGenConfUser.make
#cmt_final_setup_TrackMonitorsGenConfUser = $(bin)TrackMonitors_TrackMonitorsGenConfUsersetup.make
cmt_local_TrackMonitorsGenConfUser_makefile = $(bin)TrackMonitorsGenConfUser.make

else

cmt_final_setup_TrackMonitorsGenConfUser = $(bin)setup.make
#cmt_final_setup_TrackMonitorsGenConfUser = $(bin)TrackMonitorssetup.make
cmt_local_TrackMonitorsGenConfUser_makefile = $(bin)TrackMonitorsGenConfUser.make

endif

cmt_final_setup = $(bin)setup.make
#cmt_final_setup = $(bin)TrackMonitorssetup.make

#TrackMonitorsGenConfUser :: ;

dirs ::
	@if test ! -r requirements ; then echo "No requirements file" ; fi; \
	  if test ! -d $(bin) ; then $(mkdir) -p $(bin) ; fi

javadirs ::
	@if test ! -d $(javabin) ; then $(mkdir) -p $(javabin) ; fi

srcdirs ::
	@if test ! -d $(src) ; then $(mkdir) -p $(src) ; fi

help ::
	$(echo) 'TrackMonitorsGenConfUser'

binobj = 
ifdef STRUCTURED_OUTPUT
binobj = TrackMonitorsGenConfUser/
#TrackMonitorsGenConfUser::
#	@if test ! -d $(bin)$(binobj) ; then $(mkdir) -p $(bin)$(binobj) ; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)$(binobj)
endif

ifdef use_requirements
$(use_requirements) : ;
endif

#-- end of make_header ------------------
# ============= call_command_header:begin =============
deps        = $(TrackMonitorsGenConfUser_deps)
command     = $(TrackMonitorsGenConfUser_command)
output      = $(TrackMonitorsGenConfUser_output)

.PHONY: TrackMonitorsGenConfUser TrackMonitorsGenConfUserclean

TrackMonitorsGenConfUser :: $(output)

TrackMonitorsGenConfUserclean ::
	$(cmt_uninstallarea_command) $(output)

$(output):: $(deps)
	$(command)

FORCE:
# ============= call_command_header:end =============
#-- start of cleanup_header --------------

clean :: TrackMonitorsGenConfUserclean ;
#	@cd .

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(TrackMonitorsGenConfUser.make) $@: No rule for such target" >&2
#	@echo "#CMT> Warning: $@: No rule for such target" >&2; exit
	if echo $@ | grep '$(package)setup\.make$$' >/dev/null; then\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsGenConfUser.make): $@: File no longer generated" >&2; exit 0; fi
else
.DEFAULT::
	$(echo) "(TrackMonitorsGenConfUser.make) PEDANTIC: $@: No rule for such target" >&2
	if echo $@ | grep '$(package)setup\.make$$' >/dev/null; then\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsGenConfUser.make): $@: File no longer generated" >&2; exit 0;\
	 elif test $@ = "$(cmt_final_setup)" -o\
	 $@ = "$(cmt_final_setup_TrackMonitorsGenConfUser)" ; then\
	 found=n; for s in 1 2 3 4 5; do\
	 sleep $$s; test ! -f $@ || { found=y; break; }\
	 done; if test $$found = n; then\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsGenConfUser.make) PEDANTIC: $@: Seems to be missing. Ignore it for now" >&2; exit 0 ; fi;\
	 elif test `expr $@ : '.*/'` -ne 0 ; then\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsGenConfUser.make) PEDANTIC: $@: Seems to be a missing file. Please check" >&2; exit 2 ; \
	 else\
	 test -z "$(cmtmsg)" ||\
	 echo "$(CMTMSGPREFIX)" "(TrackMonitorsGenConfUser.make) PEDANTIC: $@: Seems to be a fake target due to some pattern. Just ignore it" >&2 ; exit 0; fi
endif

TrackMonitorsGenConfUserclean ::
#-- end of cleanup_header ---------------
