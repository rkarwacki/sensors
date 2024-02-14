# this script checks if the sensor data is within given bounds
# it will also check if there are no illegal characters in the lines
# -r will remove the lines that are out of bonds or contain invalid characters

# -s will strip the last part of the time (seconds)

import sys
import os

def check_range(value, min_val, max_val, label):
    if min_val <= value <= max_val:
        return True
    else:
        print(f"Deviation: {label} out of range ({min_val} - {max_val}): {value}")
        return False

def check_valid_characters(line):
    allowed_characters = set("0123456789|./: ")
    if set(line) <= allowed_characters:
        return True
    else:
        invalid_chars = set(line) - allowed_characters
        print(f"Invalid characters in line: {', '.join(invalid_chars)}")
        return False

def process_line(line, strip_seconds):
    if not check_valid_characters(line.strip()):
        return None  # Skip this line if invalid characters are found

    data = line.strip().split('|')
    date = data[0]

    if strip_seconds:
        date = date.rsplit(':', 1)[0]  # Remove the seconds part

    temp1 = float(data[1])
    temp2 = float(data[2])
    humidity = float(data[3])
    pressure = float(data[4])

    # Check temperature range
    if not check_range(temp1, 5, 40, f"Temperature 1 for date {date}"):
        return None

    if not check_range(temp2, 5, 40, f"Temperature 2 for date {date}"):
        return None

    # Check humidity range
    if not check_range(humidity, 0, 100, f"Humidity for date {date}"):
        return None

    # Check pressure range
    if not check_range(pressure, 930, 1080, f"Pressure for date {date}"):
        return None

    return f"{date}|{temp1}|{temp2}|{humidity}|{pressure}\n"

if len(sys.argv) < 2:
    print("Usage: python script.py <filename> [-r] [-s]")
    sys.exit(1)

filename = sys.argv[1]
remove_lines = "-r" in sys.argv
strip_seconds = "-s" in sys.argv

output_filename = "processed_" + os.path.basename(filename) if remove_lines else None

with open(filename, 'r') as file, (open(output_filename, 'w') if remove_lines else sys.stdout) as output_file:
    for line_number, line in enumerate(file, start=1):
        processed_line = process_line(line, strip_seconds)
        if remove_lines and processed_line is not None:
            output_file.write(processed_line)

if remove_lines:
    print(f"Processed data written to {output_filename}")
