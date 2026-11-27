import os
import sys
import json
import time
import hashlib
import logging
import fnmatch

# --- Colored Alert ---
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        RED = GREEN = YELLOW = CYAN = ""
    class Style:
        RESET_ALL = ""

# --- Log file me likhega ---
logging.basicConfig(
    filename="filewatch.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
logger = logging.getLogger("FileWatch")

def alert(msg, color=Fore.YELLOW):
    print(f"{color}[ALERT] {msg}{Style.RESET_ALL}")
    logger.info(msg)

def is_ignored(path, patterns):
    for pat in patterns:
        if fnmatch.fnmatch(path, pat) or fnmatch.fnmatch(os.path.basename(path), pat):
            return True
        if pat.replace("/*", "") in path:
            return True
    return False

def get_hash(filepath):
    try:
        h = hashlib.sha256()
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except (PermissionError, FileNotFoundError, OSError) as e:
        logger.warning(f"Cannot read {filepath}: {e}")
        return None

def scan_folder(folder, ignore_patterns):
    baseline = {}
    for root, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if not is_ignored(os.path.join(root, d), ignore_patterns)]
        for file in files:
            full_path = os.path.join(root, file)
            if is_ignored(full_path, ignore_patterns):
                continue
            file_hash = get_hash(full_path)
            if file_hash:
                baseline[full_path] = file_hash
    return baseline

def load_config():
    with open("config.json") as f:
        return json.load(f)

def main():
    config = load_config()
    watch_path = config["watch_path"]
    interval = config["interval_seconds"]
    ignore_patterns = config["ignore_patterns"]

    print(f"{Fore.CYAN}Watching: {watch_path} every {interval}s - Press Ctrl+C to stop")
    logger.info(f"Monitor started on {watch_path}")

    old_baseline = scan_folder(watch_path, ignore_patterns)
    print(f"Baseline loaded: {len(old_baseline)} files")

    try:
        while True:
            time.sleep(interval)
            new_baseline = scan_folder(watch_path, ignore_patterns)

            for file in new_baseline:
                if file not in old_baseline:
                    alert(f"NEW FILE: {file}", Fore.GREEN)
                elif new_baseline[file] != old_baseline[file]:
                    alert(f"MODIFIED: {file}", Fore.RED)

            for file in old_baseline:
                if file not in new_baseline:
                    alert(f"DELETED: {file}", Fore.YELLOW)

            old_baseline = new_baseline

    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}Monitor stopped cleanly. Bye!")
        logger.info("Stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    main()