import os
import logging
from docx import Document

# Setup logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    """Main function to generate a basic Word document."""
    logging.info("Starting the basic document generation process")
    try:
        document = Document()
        logging.debug("Document object created")

        # Add a simple paragraph
        logging.debug("Adding a simple paragraph")
        document.add_paragraph("This is a test document.")
        logging.debug("Paragraph added")

        # Save the document
        output_dir = os.path.join("c:/Users/troy_/Downloads/Tailored Resume Process/S3", "output")
        if not os.path.exists(output_dir):
            logging.info(f"Creating output directory: {output_dir}")
            os.makedirs(output_dir)
        output_path = os.path.join(output_dir, "test_basic_document.docx")
        logging.info(f"Saving document to {output_path}")
        document.save(output_path)
        logging.info(f"Test document generated and saved to {output_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
