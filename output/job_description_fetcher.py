import csv
import json
import os

def process_huntr_csv(csv_file):
    """Process a CSV file exported from Huntr, focusing on records where listName is 'Wishlist'."""
    job_descriptions = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get("listName") == "Wishlist":
                job_descriptions.append({
                    "id": row.get("id"),
                    "title": row.get("title"),
                    "location": row.get("location"),
                    "url": row.get("url"),
                    "company_name": row.get("companyName"),
                    "description": row.get("htmlDescription")
                })
    return job_descriptions

def save_job_descriptions(job_descriptions, output_file):
    """Save job descriptions to a JSON file."""
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(job_descriptions, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # Example usage
    huntr_csv_file = "huntr_job_applications.csv"  # Replace with the path to your exported CSV file

    try:
        job_descriptions = process_huntr_csv(huntr_csv_file)
        save_job_descriptions(job_descriptions, "huntr_job_descriptions.json")
        print("Huntr job descriptions saved to huntr_job_descriptions.json")
    except Exception as e:
        print(f"Error processing Huntr CSV file: {e}")
