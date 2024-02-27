#!/bin/bash

cd /export/saasprodsftp/bk/prod/BankTransfer/EBL/A2A/inbound
/usr/bin/scp -r *.xlsx eblsftp@10.96.7.120:/export/eblsftp/daily_oracletoebl_report
/usr/bin/scp -r *.xlsx eblsftp@10.82.8.89:/export/eblsftp/daily_oracletoebl_report
sleep 5
mv *.xlsx archive/
