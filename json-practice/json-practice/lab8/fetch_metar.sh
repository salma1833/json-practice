#!/bin/bash

# fetch metar data
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json 
metar_data=$(cat aviation.json)

# ReceiptTime values
receipt_times=$(echo "$metar_data" | jq -r '.[].receiptTime')

# Display first 6 values
echo "$receipt_times" | head -n 6
