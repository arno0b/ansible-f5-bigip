#!/bin/bash

cd /export/saasprodsftp/bk/prod/BankTransfer/JBL/BEFTN/inbound
/usr/bin/scp -r *.xlsx jamunabsftp@10.96.7.120:/export/jamunabsftp/daily_oracletojbl_report
/usr/bin/scp -r *.xlsx jamunabsftp@10.82.8.89:/export/jamunabsftp/daily_oracletojbl_report
sleep 5
mv *.xlsx archive/

