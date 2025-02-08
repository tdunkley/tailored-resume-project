import logging

def setup_logging(log_filename="tracker.log"):
    """Set up logging for the tracker."""
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def log_event(section_name, status, message, level=logging.INFO):
    """
    Logs an event related to a section during testing.

    Args:
        section_name (str): The name of the section (e.g., "experience").
        status (str): The status of the event (e.g., "APPROVED", "REJECTED", "ERROR").
        message (str): A detailed message about the event.
        level (int): The logging level (e.g., logging.INFO, logging.ERROR).
    """
    logging.log(level, f"Section: {section_name} | Status: {status} | Message: {message}")

def log_error(section_name, error_message):
    """Logs an error related to a section."""
    log_event(section_name, "ERROR", error_message, logging.ERROR)
