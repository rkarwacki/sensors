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

        if current_timestamp > next_timestamp:
            issues.append(f"Timestamp order issue: {current_line[0]} > {next_line[0]}")

    return issues

if len(sys.argv) != 2:
    print("Usage: python script.py data.csv")
    sys.exit(1)

data_file_path = sys.argv[1]

try:
    with open(data_file_path, 'r') as file:
        your_data = file.readlines()

    order_issues = detect_timestamp_order_issues(your_data)

    if order_issues:
        print("Timestamp order issues found:")
        for issue in order_issues:
            print(issue)
    else:
        print("No timestamp order issues found.")
except FileNotFoundError:
    print(f"Error: File not found at {data_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
