import os

def check_files():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_dir = os.path.join(base_dir, "..")
    sections_dir = os.path.join(scripts_dir, "sections")
    s3_operations_dir = os.path.join(scripts_dir, "s3_operations")

    files_to_check = {
        "key_mapper.py": os.path.join(scripts_dir, "key_mapper.py"),
        "load_resume_from_s3.py": os.path.join(s3_operations_dir, "load_resume_from_s3.py"),
        "personal_info.py": os.path.join(sections_dir, "personal_info.py"),
    }

    print("Checking file locations...")
    for file_name, file_path in files_to_check.items():
        if os.path.exists(file_path):
            print(f"{file_name} is accessible at: {file_path}")
        else:
            print(f"Error: {file_name} not found at: {file_path}")

if __name__ == "__main__":
    check_files()
