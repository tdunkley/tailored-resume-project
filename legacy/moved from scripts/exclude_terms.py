import logging

logger = logging.getLogger("exclude_terms")

def exclude_terms_from_text(text, terms):
    """Exclude specified terms from the given text."""
    for term in terms:
        text = text.replace(term, "")
        logger.info(f"Excluded term: {term}")
    return text

def load_exclusion_terms(file_path):
    """Load exclusion terms from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            terms = file.read().splitlines()
        logger.info(f"Loaded exclusion terms from {file_path}")
        return terms
    except Exception as e:
        logger.error(f"Error loading exclusion terms: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    exclusion_terms_file = "path/to/exclusion_terms.txt"  # Replace with the actual path to your exclusion terms file
    text_to_process = "Sample text to process and exclude terms from."  # Replace with the actual text to process

    terms = load_exclusion_terms(exclusion_terms_file)
    processed_text = exclude_terms_from_text(text_to_process, terms)
    print(f"Processed text: {processed_text}")
