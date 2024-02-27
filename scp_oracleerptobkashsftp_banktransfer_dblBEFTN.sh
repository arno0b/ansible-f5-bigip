#!/usr/bin/bash

cd /export/saasprodsftp/bk/prod/BankTransfer/DBL/BEFTN/inbound
/usr/bin/scp -r *.xlsx dblsftp@10.96.7.120:/export/dblsftp/daily_oracletodbl_report
/usr/bin/scp -r *.xlsx dblsftp@10.82.8.89:/export/dblsftp/daily_oracletodbl_report
sleep 5
mv *.xlsx archive/


