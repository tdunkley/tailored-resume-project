import os
import sys

# Dynamically add the core module path
current_dir = os.path.dirname(os.path.abspath(__file__))
core_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "scripts"))
print(f"Core module path added: {core_dir}")
sys.path.append(core_dir)

try:
    from core import get_paths, load_resume_data, setup_logging
    print("Core module imported successfully!")
except ImportError as e:
    print(f"Failed to import core module: {e}")
    sys.exit(1)
