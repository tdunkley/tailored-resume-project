import sys
import os
import json
from docx import Document
from docx.shared import Pt, RGBColor

# Add the 's3_operations' folder to the system path so Python can find 'load_resume_from_s3'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 's3_operations')))

# Debugging: Print the current sys.path to verify the path is correct
print("Current sys.path:", sys.path)

# Now try importing the module after updating sys.path
try:
    from load_resume_from_s3 import load_resume_data_from_s3  # Now Python can find the module
except ModuleNotFoundError as e:
    print(f"Error importing module: {e}")
