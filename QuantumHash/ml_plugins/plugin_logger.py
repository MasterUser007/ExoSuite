# ml_plugins/plugin_logger.py

import time
import json
import os
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "plugin_usage.log"


def log_plugin_usage(plugin_name, input_val, score):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    entry = {
        "plugin": plugin_name,
        "input": input_val,
        "score": score,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
