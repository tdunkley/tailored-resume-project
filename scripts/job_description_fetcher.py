import csv
import json
import logging
import re
from bs4 import BeautifulSoup
import html
import requests

# Ensure s3_manager is imported correctly
try:
    from s3_manager import upload_to_s3
except ImportError as e:
    logging.error(f"Error importing s3_manager: {e}", exc_info=True)
    raise

def strip_html_tags(text):
    """Remove HTML tags from a string and decode HTML entities."""
    text = BeautifulSoup(text, "html.parser").get_text()
    text = html.unescape(text)
    text = re.sub(r'\u2019', "'", text)  # Replace right single quotation mark with apostrophe
    text = re.sub(r'\u2013', '-', text)  # Replace en dash with hyphen
    text = re.sub(r'\u2014', '-', text)  # Replace em dash with hyphen
    text = re.sub(r'\u2026', '...', text)  # Replace ellipsis with three dots
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'(?<=[.,!?])(?=[^\s])', r' ', text)  # Add space after punctuation if missing
    return text.strip()  # Remove leading and trailing whitespace

def fetch_job_description(job_id):
    """Fetch job description from API."""
    response = requests.get(f"https://api.example.com/jobs/{job_id}")
    if response.status_code == 200:
        logging.info(f"Fetched job description for job ID {job_id}")
        return response.json()
    else:
        logging.error(f"Failed to fetch job description for job ID {job_id}")
        return None

def process_huntr_csv(csv_file_path):
    """Process the Huntr CSV file and extract job descriptions."""
    logger = logging.getLogger("job_description_fetcher")
    job_descriptions = []
    
    try:
        logger.info(f"Opening CSV file: {csv_file_path}")
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                logger.info(f"Processing row: {row}")
                if row.get("listName", "").strip() == "Wishlist":
                    description = strip_html_tags(row.get("htmlDescription", "").strip())
                    if description.startswith("About the job"):
                        description = description.replace("About the job", "About the job: ", 1)
                        description = description[0:15] + description[15].upper() + description[16:]  # Capitalize first letter after "About the job: "
                    job_description = {
                        "companyName": strip_html_tags(row.get("companyName", "").strip()),
                        "title": strip_html_tags(row.get("title", "").strip()),
                        "location": strip_html_tags(row.get("location", "").strip()),
                        "description": description,
                        "requirements": strip_html_tags(row.get("requirements", "").strip())
                    }
                    job_descriptions.append(job_description)
                    logger.info(f"Processed job description: {job_description}")
        logger.info(f"Total job descriptions extracted: {len(job_descriptions)}")
    except Exception as e:
        logger.error(f"Error processing Huntr CSV file: {e}", exc_info=True)
        raise
    
    return job_descriptions

def save_job_descriptions(job_descriptions, output_file_path, s3_bucket_name=None, s3_key=None):
    """Save job descriptions to a JSON file and optionally upload to S3."""
    try:
        with open(output_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(job_descriptions, json_file, indent=4)
        logging.info(f"Job descriptions saved to {output_file_path}")
        
        if s3_bucket_name and s3_key:
            upload_to_s3(output_file_path, s3_bucket_name, s3_key)
            logging.info(f"Job descriptions uploaded to S3: s3://{s3_bucket_name}/{s3_key}")
    except Exception as e:
        logging.error(f"Error saving job descriptions: {e}", exc_info=True)
        raise
