import sys
import os

# Determine the absolute path to the 'src' directory
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')

# Add 'src' to sys.path
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from PrimeEngineAI import pef

result = pef()
print(result)
