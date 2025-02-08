import logging

def setup_logging(log_filename="tracker.log"):
    """Set up logging for the tracker."""
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def log_event(event_name, event_status, event_message, log_level=logging.INFO):
    """Log an event with the specified details."""
    logger = logging.getLogger("tracker")
    logger.log(log_level, f"{event_name} - {event_status}: {event_message}")

def log_error(section_name, error_message):
    """Logs an error related to a section."""
    log_event(section_name, "ERROR", error_message, logging.ERROR)
