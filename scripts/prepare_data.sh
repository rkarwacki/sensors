#!/bin/bash
tail -n 720 ~/projects/sensors/data/sensors.csv > last_12_hours.csv && python csv_to_json.py last_12_hours.csv ../data/data_12h.js
rm last_12_hours.csv
