import hashlib
import os

def hash_file(path):
    try:
        hasher = hashlib.sha256()
        with open(path, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return "ERROR: File not found"
    except Exception as e:
        return f"ERROR: {e}"

def main():
    folder = "test_folder"
    print("=== FileWatch - Week 1 ===")
    for filename in sorted(os.listdir(folder)):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            print(f"{filename} : {hash_file(filepath)}")

main()