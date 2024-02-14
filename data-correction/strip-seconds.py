# the script is removing seconds from the timestamp, as it is not needed for processing

from datetime import datetime

def convert_timestamps(input_file, output_file):
    with open(input_file, 'r', errors='ignore') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            try:
                parts = line.strip().split('|')
                timestamp = datetime.strptime(parts[0], "%d/%m/%Y %H:%M:%S").strftime("%d/%m/%Y %H:%M")
                modified_line = f"{timestamp}|{parts[1]}|{parts[2]}|{parts[3]}|{parts[4]}\n"
                outfile.write(modified_line)
            except ValueError as e:
                print(f"Skipping line due to error: {e}")

# Specify the paths to your input and output files
input_file_path = "data.csv"
output_file_path = "data-sanitized.csv"

convert_timestamps(input_file_path, output_file_path)