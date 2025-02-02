from tracker import CentralizedTracker

tracker = CentralizedTracker()

# Start tracking a step
tracker.start_tracking("Test Step")

# Perform some actions here (e.g., time.sleep(2) to simulate work)

# Complete tracking
tracker.complete_tracking()

# Print the logs
print(tracker.get_logs())
