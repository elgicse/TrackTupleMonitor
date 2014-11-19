#!/bin/bash
#for J in `seq 0 32`;do for i in `seq 0 200`; do rfcp $CASTOR_HOME/ganga/$J/$i/RDForBs2PhiMuMu_Tuples_new.root $J/$i.root; done; done;
#for i in `seq 0 200`; do stager_qry -M $CASTOR_HOME/ganga/$J/$i/RDForBs2PhiMuMu_Tuples_new.root; done;

#ask status of data
#for J in `seq 24 32`;do for i in `seq 0 200`; do stager_qry -M $CASTOR_HOME/ganga/$J/$i/RDForBs2PhiMuMu_Tuples_new.root; done; done;
#for J in `seq 0 17`;do for i in `seq 0 200`; do stager_qry -M $CASTOR_HOME/ganga/$J/$i/Bs2PhiMuMu_Tuples.root; done; done;

#move data from tape store to hdd
#for J in `seq 24 32`;do for i in `seq 0 200`; do stager_get -S default -M $CASTOR_HOME/ganga/$J/$i/RDForBs2PhiMuMu_Tuples_new.root; done; done;
#for J in `seq 0 17`;do for i in `seq 0 200`; do stager_get -S default -M $CASTOR_HOME/ganga/$J/$i/Bs2PhiMuMu_Tuples.root; done; done;

#Replicate data
#for J in `seq 0 32`; do mkdir $J; done;
#for J in `seq 24 32`;do for i in `seq 0 200`; do rfcp $CASTOR_HOME/ganga/$J/$i/RDForBs2PhiMuMu_Tuples_new.root $J/$i.root; done; done;
#for J in `seq 0 17`;do for i in `seq 0 200`; do rfcp $CASTOR_HOME/ganga/$J/$i/Bs2PhiMuMu_Tuples.root $J/$i.root; done; done;

do for i in `seq 0 200`; do rfcp $CASTOR_HOME/ganga/$J/$i/RDForBs2PhiMuMu_Tuples_new.root 130/$i.root; done;

