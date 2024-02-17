#!/bin/bash
cd /home/radek/sensors/scripts
current_datetime=$(date +"%Y-%m-%d %H:%M:%S")
git add ../data/data_12h.js
git add ../data/data_24h.js
git add ../data/data_7d.js
git commit -m "Update: $current_datetime"
git push origin gh-pages
