import csv
import logging

# ...existing code...

def validate_huntr_csv(file_path):
    """Validate Huntr CSV file."""
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 5:
                logging.error(f"Invalid row: {row}")
                return False
    logging.info("Huntr CSV file validated successfully.")
    return True

# ...existing code...
