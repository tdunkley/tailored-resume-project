import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESUME_FILE = os.path.join(ROOT_DIR, 'resume.json')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'output')

if not os.path.exists(RESUME_FILE):
    raise FileNotFoundError(f"Resume file not found at {RESUME_FILE}")
os.makedirs(OUTPUT_DIR, exist_ok=True)

print(f"ROOT_DIR: {ROOT_DIR}")
print(f"RESUME_FILE: {RESUME_FILE}")
print(f"OUTPUT_DIR: {OUTPUT_DIR}")
