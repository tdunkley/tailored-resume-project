<<<<<<< HEAD
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
=======
# tracker.py
import logging
from datetime import datetime

class CentralizedTracker:
    def __init__(self):
        self.steps = {}
        self.logger = logging.getLogger("CentralizedTracker")

    def start_tracking(self, step_name):
        if step_name in self.steps:
            self.logger.warning(f"Step '{step_name}' is already being tracked.")
        self.steps[step_name] = {
            "start_time": datetime.now(),
            "end_time": None,
            "duration": None,
            "status": "in_progress",
            "errors": []
        }
        self.logger.info(f"Started tracking step: {step_name} at {self.steps[step_name]['start_time']}")

    def end_tracking(self, step_name):
        if step_name not in self.steps:
            self.logger.error(f"Step '{step_name}' was not being tracked.")
            return
        self.steps[step_name]["end_time"] = datetime.now()
        self.steps[step_name]["duration"] = self.steps[step_name]["end_time"] - self.steps[step_name]["start_time"]
        self.steps[step_name]["status"] = "completed"
        self.logger.info(f"Ended tracking step: {step_name} at {self.steps[step_name]['end_time']} (Duration: {self.steps[step_name]['duration']})")

    def track_error(self, step_name, error_message):
        if step_name not in self.steps:
            self.logger.error(f"Cannot log error for untracked step '{step_name}'.")
            return
        self.steps[step_name]["errors"].append(error_message)
        self.steps[step_name]["status"] = "failed"
        self.logger.error(f"Error in step '{step_name}': {error_message}")

    def track_section_start(self, section_name):
        self.start_tracking(section_name)
        self.logger.info(f"Started tracking section: {section_name}")

    def track_section_success(self, section_name):
        self.end_tracking(section_name)
        self.logger.info(f"Section '{section_name}' processed successfully.")

    def track_failure(self, error_message):
        self.logger.error(f"Processing failure: {error_message}")

    def finalize(self):
        self.logger.info("Finalizing tracking process...")
        for step, details in self.steps.items():
            self.logger.info(f"Step: {step}, Details: {details}")
>>>>>>> 011eb20403b89d07c8ae11e5b4bc3094a262060f
