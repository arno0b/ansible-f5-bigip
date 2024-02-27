#!/bin/bash

cd /export/saasprodsftp/bk/prod/Payment/SEBL/RTGS/inbound
/usr/bin/scp -r *.xlsx seblsftp@10.96.7.120:/export/seblsftp/daily_oracletosebl_report
/usr/bin/scp -r *.xlsx seblsftp@10.82.8.89:/export/seblsftp/daily_oracletosebl_report
sleep 5
mv *.xlsx archive/
