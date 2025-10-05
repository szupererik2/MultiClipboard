import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

sys.path.append("D:/Erik/Projects/Self/Automation/MultiClipboard/src")
from src.Key_press import *

detect_key_press()