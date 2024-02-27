#!/bin/bash

cd /export/saasprodsftp/bk/prod/BankTransfer/PRIME/RTGS/inbound
/usr/bin/scp -r *.xlsx primesftp@10.96.7.120:/export/primesftp/daily_oracletoprimebl_report
/usr/bin/scp -r *.xlsx primesftp@10.82.8.89:/export/primesftp/daily_oracletoprimebl_report
sleep 5
mv *.xlsx archive/
