#!/usr/bin/bash

cd /export/saasprodsftp/bk/prod/Payment/BRAC/RTGS/inbound
/usr/bin/scp -r *.xlsx bblsftp@10.96.7.120:/export/bblsftp/daily_oracletobbl_report
/usr/bin/scp -r *.xlsx bblsftp@10.82.8.89:/export/bblsftp/daily_oracletobbl_report
sleep 5
mv *.xlsx archive/



