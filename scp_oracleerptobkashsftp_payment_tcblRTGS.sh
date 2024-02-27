#!/bin/bash

cd /export/saasprodsftp/bk/prod/Payment/TCBL/RTGS/inbound
/usr/bin/scp -r *.xlsx cblsftp@10.96.7.120:/export/cblsftp/daily_oracletocbl_report
/usr/bin/scp -r *.xlsx cblsftp@10.82.8.89:/export/cblsftp/daily_oracletocbl_report
sleep 5
mv *.xlsx archive/
