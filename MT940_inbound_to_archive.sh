#!/bin/bash

base_dir="/export/saasprodsftp/bk/prod/MT940"

for bank_dir in "$base_dir"/*; do
    if [[ -d "$bank_dir/inbound" ]]; then 
        archive_dir="$bank_dir/inbound/archive"
        mkdir -p "$archive_dir"  
        find "$bank_dir/inbound" -maxdepth 1 -type f -mtime +29 -exec mv {} "$archive_dir" \;
        echo "Files older than 30 days in $bank_dir/inbound have been moved to $archive_dir"
    fi
done