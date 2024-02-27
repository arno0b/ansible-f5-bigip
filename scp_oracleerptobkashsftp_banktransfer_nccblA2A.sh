#!/bin/bash

cd /export/saasprodsftp/bk/prod/BankTransfer/NCC/A2A/inbound
/usr/bin/scp -r *.xlsx nccblsftp@10.96.7.120:/export/nccblsftp/daily_oracletonccbl_report
/usr/bin/scp -r *.xlsx nccblsftp@10.82.8.89:/export/nccblsftp/daily_oracletonccbl_report
sleep 5
mv *.xlsx archive/
