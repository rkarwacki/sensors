#!/bin/bash
cd /home/radek/sensors/scripts
tail -n 720 ~/projects/sensors/data/sensors.csv > last_12_hours.csv && python csv_to_json.py last_12_hours.csv ../data/data_12h.js
awk 'NR % 2 == 0' ~/projects/sensors/data/sensors.csv | tail -n 720 > last_24_hours.csv && python csv_to_json.py last_24_hours.csv ../data/data_24h.js
awk 'NR % 15 == 0' ~/projects/sensors/data/sensors.csv | tail -n 672 > last_7_days.csv && python csv_to_json.py last_7_days.csv ../data/data_7d.js
rm last_12_hours.csv
rm last_24_hours.csv
rm last_7_days.csv
