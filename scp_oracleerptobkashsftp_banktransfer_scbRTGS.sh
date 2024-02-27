#!/bin/bash

cd /export/saasprodsftp/bk/prod/BankTransfer/SCB/RTGS/inbound/
/usr/bin/scp -r *RTGS_SCB* scbsftp@10.96.7.120:/export/scbsftp/daily_oracletoscb_report
/usr/bin/scp -r *RTGS_SCB* scbsftp@10.82.8.89:/export/scbsftp/daily_oracletoscb_report
sleep 5
mv *RTGS_SCB* archive/


