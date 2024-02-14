# when the device is off (e.g. power out) data is not collected
# this script detects places where the data is missing

import sys
from datetime import datetime, timedelta

def detect_missing_entries(data):
    date_format = "%d/%m/%Y %H:%M"

    missing_entries = []
    log_frequency = 10000

    for i in range(len(data) - 1):
        current_line = data[i].strip().split('|')
        next_line = data[i + 1].strip().split('|')

        current_timestamp = datetime.strptime(current_line[0], date_format)
        next_expected_timestamp = current_timestamp + timedelta(minutes=1)

        next_timestamp = datetime.strptime(next_line[0], date_format)

        while next_timestamp != next_expected_timestamp:
            missing_entries.append(next_expected_timestamp.strftime("%d/%m/%Y %H:%M"))
            next_expected_timestamp += timedelta(minutes=1)

        # Print progress to the console
        if i % log_frequency == 0:
            print(f"Processed {i}/{len(data)} entries")

    return missing_entries

if len(sys.argv) != 2:
    print("Usage: python script.py data.csv")
    sys.exit(1)

data_file_path = sys.argv[1]

try:
    with open(data_file_path, 'r') as file:
        your_data = file.readlines()

    missing_timestamps = detect_missing_entries(your_data)

    if missing_timestamps:
        print("Missing entries found at the following timestamps:")
        for timestamp in missing_timestamps:
            print(timestamp)
    else:
        print("No missing entries found.")
except FileNotFoundError:
    print(f"Error: File not found at {data_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
