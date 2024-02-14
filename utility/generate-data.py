# for testing purposes, it is sometimes necessary to generate a text file with predictable data

import random, sys
from datetime import datetime, timedelta

def generate_sample_data(file_path, num_lines):
    date_format = "%d/%m/%Y %H:%M"

    with open(file_path, 'w') as file:
        start_date = datetime(2023, 1, 1, 0, 0)  # You can adjust the start date
        time_difference = timedelta(minutes=1)

        for i in range(num_lines):
            timestamp = start_date + i * time_difference
            temperature_sensor_1 = round(random.uniform(20.0, 30.0), 1)
            temperature_sensor_2 = round(random.uniform(20.0, 30.0), 1)
            humidity = round(random.uniform(30.0, 70.0), 1)
            pressure = round(random.uniform(950.0, 1050.0), 1)

            entry = f"{timestamp.strftime(date_format)}|{temperature_sensor_1}|{temperature_sensor_2}|{humidity}|{pressure}\n"
            file.write(entry)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_data.py output_file.csv num_lines")
        sys.exit(1)

    output_file_path = sys.argv[1]
    num_lines = int(sys.argv[2])

    generate_sample_data(output_file_path, num_lines)

    print(f"Sample data generated and saved to '{output_file_path}' with {num_lines} lines.")