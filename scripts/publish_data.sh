#!/bin/bash
current_datetime=$(date +"%Y-%m-%d %H:%M:%S")
git add .
git commit -m "Update: $current_datetime"
git push origin gh-pages