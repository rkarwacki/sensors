# this script checks the data for potential chronology issues
# for some reason, the device writes data with a timestamp from the near future
# but also, daylight savings time causes issues

# -r will try to remove the problematic lines, it does not work perfectly, but gets rid of most of the issues

import sys
from datetime import datetime

def detect_timestamp_order_issues(data):
    date_format = "%d/%m/%Y %H:%M"

    issues = []

    for i in range(len(data) - 1):
        current_line = data[i].strip().split('|')
        next_line = data[i + 1].strip().split('|')

        current_timestamp = datetime.strptime(current_line[0], date_format)
        next_timestamp = datetime.strptime(next_line[0], date_format)

        if current_timestamp >= next_timestamp:
            issues.append(f"Timestamp order issue: {current_line[0]} >= {next_line[0]}")

    return issues

def remove_timestamp_order_issues(data):
    date_format = "%d/%m/%Y %H:%M"

    new_data = [data[0]]  # Keep the header

    for i in range(1, len(data)):
        current_line = data[i].strip().split('|')
        prev_line = data[i - 1].strip().split('|')

        current_timestamp = datetime.strptime(current_line[0], date_format)
        prev_timestamp = datetime.strptime(prev_line[0], date_format)

        if current_timestamp > prev_timestamp:
            new_data.append(data[i])

    return new_data

if len(sys.argv) not in [2, 3]:
    print("Usage: python script.py data.csv [-r]")
    sys.exit(1)

data_file_path = sys.argv[1]
remove_issues = "-r" in sys.argv

try:
    with open(data_file_path, 'r') as file:
        your_data = file.readlines()

    order_issues = detect_timestamp_order_issues(your_data)

    if order_issues:
        print("Timestamp order issues found:")
        for issue in order_issues:
            print(issue)

        if remove_issues:
            print("Removing problematic lines...")
            your_data = remove_timestamp_order_issues(your_data)

            with open(data_file_path, 'w') as file:
                file.writelines(your_data)

            print("Removed problematic lines.")
    else:
        print("No timestamp order issues found.")
except FileNotFoundError:
    print(f"Error: File not found at {data_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
