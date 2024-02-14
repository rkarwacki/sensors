# sometimes the device writes garbage to the data, causing errors when processing
# this script reveals th

import sys
import re
from datetime import datetime

def verify_data(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                # Check for special characters using a regex pattern
                if re.search(r'[^\x20-\x7E]', line):
                    print(f"Line {line_number}: Special characters found.")
                    continue

                # Check for unexpected format (not matching the expected pattern)
                try:
                    timestamp, _, _, _, _ = line.split('|', maxsplit=4)
                    _ = datetime.strptime(timestamp, "%d/%m/%Y %H:%M")
                except (ValueError, IndexError):
                    print(f"Line {line_number}: Unexpected format or missing fields.")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) != 2:
    print("Usage: python verify_data.py data.csv")
    sys.exit(1)

data_file_path = sys.argv[1]

verify_data(data_file_path)
