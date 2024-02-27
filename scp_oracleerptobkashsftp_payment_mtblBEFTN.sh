#!/bin/bash

cd /export/saasprodsftp/bk/prod/Payment/MTB/BEFTN/inbound
/usr/bin/scp -r *.xlsx mtblsftp@10.96.7.120:/export/mtblsftp/daily_oracletomtbl_report
/usr/bin/scp -r *.xlsx mtblsftp@10.82.8.89:/export/mtblsftp/daily_oracletomtbl_report
sleep 5
mv *.xlsx archive/
