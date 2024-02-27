#!/bin/bash

cd /export/saasprodsftp/bk/prod/BankTransfer/UCB/A2A/inbound
/usr/bin/scp -r *.xlsx ucbsftp@10.96.7.120:/export/ucbsftp/daily_oracletoucbl_report
/usr/bin/scp -r *.xlsx ucbsftp@10.82.8.89:/export/ucbsftp/daily_oracletoucbl_report
sleep 5
mv *.xlsx archive/
