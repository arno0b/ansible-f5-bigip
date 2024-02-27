#!/bin/bash

cd /export/saasprodsftp/bk/prod/BankTransfer/TBL/A2A/inbound
/usr/bin/scp -r *.xlsx trstsftp@10.82.8.89:/export/trstsftp/daily_oracletotrst_report
sleep 5
mv *.xlsx archive/
