import sys
import os

scripts_path = os.path.join(os.path.dirname(__file__), 'scripts')
sys.path.append(scripts_path)
print(sys.path)
