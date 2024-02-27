#!/usr/bin/bash

cd /export/saasprodsftp/bk/prod/BankTransfer/BRAC/6001/BEFTN/inbound
/usr/bin/scp -r BK_FIN_BRAC_*.xlsx bblsftp@10.96.7.120:/export/bblsftp/daily_oracletobbl_report_AP
/usr/bin/scp -r BK_FIN_BRAC_*.xlsx bblsftp@10.82.8.89:/export/bblsftp/daily_oracletobbl_report_AP
sleep 5
mv *.xlsx archive/
