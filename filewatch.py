import hashlib
import json
import os
import sys
from pathlib import Path

def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def scan_folder(folder):
    result = {}
    for root, dirs, files in os.walk(folder):
        for name in files:
            full = Path(root) / name
            rel = str(full.relative_to(folder))
            result[rel] = hash_file(full)
    return result

def check_changes(folder):
    with open("baseline.json") as f:
        old = json.load(f)
    new = scan_folder(folder)
    added = [f for f in new if f not in old]
    deleted = [f for f in old if f not in new]
    modified = [f for f in new if f in old and new[f] != old[f]]
    return added, modified, deleted

if __name__ == "__main__":
    folder = "test_folder"
    cmd = sys.argv[1]
    if cmd == "baseline":
        data = scan_folder(folder)
        with open("baseline.json", "w") as f:
            json.dump(data, f, indent=2)
        print("Baseline saved!")
    elif cmd == "check":
        added, modified, deleted = check_changes(folder)
        print("Added:", added)
        print("Modified:", modified)
        print("Deleted:", deleted)
        if not added and not modified and not deleted:
            print("No changes detected.")