import logging
from job_description_fetcher import process_huntr_csv, save_job_descriptions

def test_process_huntr_csv():
    logging.basicConfig(level=logging.INFO)
    csv_file_path = "c:/Users/troy_/Downloads/Tailored Resume Process/S3/huntr_job_applications.csv"
    output_file_path = "c:/Users/troy_/Downloads/Tailored Resume Process/S3/test_huntr_job_descriptions.json"
    
    try:
        logging.info("Starting test_process_huntr_csv")
        print("Starting test_process_huntr_csv")
        job_descriptions = process_huntr_csv(csv_file_path)
        logging.info(f"Extracted {len(job_descriptions)} job descriptions.")
        print(f"Extracted {len(job_descriptions)} job descriptions.")
        save_job_descriptions(job_descriptions, output_file_path)
        logging.info(f"Job descriptions saved to {output_file_path}")
        print(f"Job descriptions saved to {output_file_path}")
    except Exception as e:
        logging.error(f"Error during test: {e}", exc_info=True)
        print(f"Error during test: {e}")

if __name__ == "__main__":
    test_process_huntr_csv()
