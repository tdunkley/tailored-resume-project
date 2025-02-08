import logging

# ...existing code...

def setup_logging(log_file, log_level=logging.INFO):
    """Setup logging configuration."""
    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger()
    return logger

# ...existing code...
