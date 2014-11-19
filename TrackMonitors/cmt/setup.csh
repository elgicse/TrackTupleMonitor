# echo "Setting TrackMonitors v2r0 in /afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr"

if ( $?CMTROOT == 0 ) then
  setenv CMTROOT /afs/cern.ch/sw/contrib/CMT/v1r20p20090520
endif
source ${CMTROOT}/mgr/setup.csh

set tempfile=`${CMTROOT}/mgr/cmt -quiet build temporary_name`
if $status != 0 then
  set tempfile=/tmp/cmt.$$
endif
${CMTROOT}/mgr/cmt setup -csh -pack=TrackMonitors -version=v2r0 -path=/afs/cern.ch/user/i/ikomarov/cmtuser/DaVinci_v33r9/Tr  -no_cleanup $* >${tempfile}; source ${tempfile}
/bin/rm -f ${tempfile}

