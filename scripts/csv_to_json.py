import sys
import json
from datetime import datetime

def average_temperatures(data):
    averaged_data = []

    for line in data:
        line_data = line.strip().split('|')
        timestamp = datetime.strptime(line_data[0], "%d/%m/%Y %H:%M")

        temp1 = float(line_data[1])
        temp2 = float(line_data[2])
        averaged_temp = round((temp1 + temp2) / 2, 1)

        entry = {
            'timestamp': timestamp.strftime('%Y-%m-%d %H:%M'),
            'averaged_temp': averaged_temp,
            'humidity': float(line_data[3]),
        }

        averaged_data.append(entry)

    return averaged_data

if len(sys.argv) != 3:
    print("Usage: python script.py input_data.csv output_data.js")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

try:
    with open(input_file_path, 'r') as file:
        your_data = file.readlines()

    averaged_data = average_temperatures(your_data)

    with open(output_file_path, 'w') as js_file:
        js_file.write("let data = ")
        json.dump(averaged_data, js_file, indent=2)

    print(f"Averaged data saved to {output_file_path}")
except FileNotFoundError:
    print(f"Error: File not found at {input_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
