#!/usr/bin/bash

cd /export/saasprodsftp/bk/prod/Payment/TRUST/RTGS/inbound
/usr/bin/scp -r *.xlsx trstsftp@10.96.7.120:/export/trstsftp/daily_oracletotrst_report
/usr/bin/scp -r *.xlsx trstsftp@10.82.8.89:/export/trstsftp/daily_oracletotrst_report
sleep 5
mv *.xlsx archive/
