import sys
from datetime import datetime

def filter_timestamp_order_issues(data):
    date_format = "%d/%m/%Y %H:%M"

    filtered_data = [data[0]]  # Keep the first line

    for i in range(len(data) - 1):
        current_line = data[i].strip().split('|')
        next_line = data[i + 1].strip().split('|')

        current_timestamp = datetime.strptime(current_line[0], date_format)
        next_timestamp = datetime.strptime(next_line[0], date_format)

        if current_timestamp <= next_timestamp:
            filtered_data.append(data[i + 1])

    return filtered_data

if len(sys.argv) != 3:
    print("Usage: python fix-misaligned-timestamps.py input_file.csv output_file.csv")
    sys.exit(1)

data_file_path = sys.argv[1]
output_file_path = sys.argv[2]

try:
    with open(data_file_path, 'r') as file:
        your_data = file.readlines()

    filtered_data = filter_timestamp_order_issues(your_data)

    with open(output_file_path, 'w') as output_file:
        output_file.writelines(filtered_data)

    print(f"Filtered data written to '{output_file_path}'")
except FileNotFoundError:
    print(f"Error: File not found at {data_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
