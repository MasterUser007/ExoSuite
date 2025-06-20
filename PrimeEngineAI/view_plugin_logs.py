# view_plugin_logs.py

import json
from pathlib import Path


def view_logs(file_path="logs/plugin_usage.log", plugin_filter=None):
    path = Path(file_path)
    if not path.exists():
        print("No log file found.")
        return
    with open(path) as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                if plugin_filter and entry["plugin"] != plugin_filter:
                    continue
                print(
                    f"[{entry['timestamp']}] {entry['plugin']} => Score: {entry['score']} (Input: {entry['input']})"
                )
            except json.JSONDecodeError:
                continue


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--plugin", type=str, help="Filter by plugin name")
    args = parser.parse_args()
    view_logs(plugin_filter=args.plugin)
