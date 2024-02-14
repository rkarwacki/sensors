# averages the data for each hour

import sys
from datetime import datetime

def average_data_by_hour(data):
    date_format = "%d/%m/%Y %H:%M"

    averaged_data = {}
    current_hour_data = []

    for line in data:
        line_data = line.strip().split('|')
        timestamp = datetime.strptime(line_data[0], date_format)
        current_hour = timestamp.replace(minute=0, second=0)

        if not current_hour_data:
            current_hour_data.append(line_data)
        elif current_hour == datetime.strptime(current_hour_data[0][0], date_format):
            current_hour_data.append(line_data)
        else:
            # Calculate the average for the current hour
            averaged_values = calculate_average(current_hour_data)
            averaged_data[current_hour] = averaged_values

            # Reset for the next hour
            current_hour_data = [line_data]

    # Calculate the average for the last hour
    if current_hour_data:
        averaged_values = calculate_average(current_hour_data)
        averaged_data[current_hour] = averaged_values

    return averaged_data

def calculate_average(hour_data):
    num_samples = len(hour_data)
    temp1_sum = temp2_sum = humidity_sum = pressure_sum = 0

    for data_point in hour_data:
        temp1_sum += float(data_point[1])
        temp2_sum += float(data_point[2])
        humidity_sum += float(data_point[3])
        pressure_sum += float(data_point[4])

    temp1_avg = temp1_sum / num_samples
    temp2_avg = temp2_sum / num_samples
    humidity_avg = humidity_sum / num_samples
    pressure_avg = pressure_sum / num_samples

    return temp1_avg, temp2_avg, humidity_avg, pressure_avg

def save_averaged_data(averaged_data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for timestamp, values in sorted(averaged_data.items()):
            output_file.write(f"{timestamp.strftime('%d/%m/%Y %H:%M')}|{values[0]:.2f}|{values[1]:.2f}|{values[2]:.2f}|{values[3]:.2f}\n")

if len(sys.argv) != 3:
    print("Usage: python script.py input_data.csv output_averaged_data.csv")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

try:
    with open(input_file_path, 'r') as file:
        your_data = file.readlines()

    averaged_data = average_data_by_hour(your_data)
    save_averaged_data(averaged_data, output_file_path)

    print(f"Averaged data saved to {output_file_path}")
except FileNotFoundError:
    print(f"Error: File not found at {input_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
