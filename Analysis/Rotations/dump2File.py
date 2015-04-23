#!/usr/bin/env python
import os, time

time1 = '28/02/2012 14.33'
time2 = '10/04/2012 14.33'

def getTimeStr(t0):
    return str(int(time.mktime(time.strptime(t0, '%d/%m/%Y %H.%M'))))+'0'*9

os.system(os.path.expandvars('dump_db_to_files.py -c sqlite_file:$SQLITEDBPATH/LHCBCOND.db/LHCBCOND -s /Conditions/TT/Alignment -d dir1 -t '+getTimeStr(time1)))

os.system(os.path.expandvars('dump_db_to_files.py -c sqlite_file:$SQLITEDBPATH/LHCBCOND.db/LHCBCOND -s /Conditions/TT/Alignment -d dir2 -t '+getTimeStr(time2)))

#os.system(os.path.expandvars('dump_db_to_files.py -c sqlite_file:$SQLITEDBPATH/LHCBCOND.db/LHCBCOND -s /Conditions/TT/Alignment -d dir1'))

