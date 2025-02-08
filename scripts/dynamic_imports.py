import sys
import os

# Dynamically add the base scripts directory to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "scripts"))
sys.path.insert(0, scripts_dir)

try:
    from dynamic_imports import get_base_dir, get_sections_dir, get_s3_operations_dir, get_output_dir, get_resume_json_path
    print("dynamic_imports.py loaded successfully.")
except ModuleNotFoundError as e:
    print(f"Error: {e}")
