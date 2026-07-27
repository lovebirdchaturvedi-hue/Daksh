import os
import sys
import hashlib
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

target_dir = r"C:\Users\DELL\Downloads\Daksh\Buyers Doanloaded pdf"

def get_file_hash(filepath):
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as afile:
            buf = afile.read(65536)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(65536)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None
    return hasher.hexdigest()

def deduplicate():
    print(f"Starting deduplication in {target_dir}")
    hashes = defaultdict(list)
    total_files = 0
    total_size = 0
    
    # Gather hashes
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            filepath = os.path.join(root, file)
            # Prefix for Windows long paths
            if os.name == 'nt' and not filepath.startswith('\\\\?\\\\'):
                filepath = '\\\\?\\\\' + os.path.abspath(filepath)
                
            total_files += 1
            total_size += os.path.getsize(filepath)
            
            file_hash = get_file_hash(filepath)
            if file_hash:
                hashes[file_hash].append(filepath)

    deleted_count = 0
    deleted_size = 0
    
    # Delete duplicates
    for file_hash, filepaths in hashes.items():
        if len(filepaths) > 1:
            # Keep the first one (or shortest name), delete the rest
            # Sort by length of filename so we keep the original (e.g. keep "file.pdf", delete "file (1).pdf")
            filepaths.sort(key=lambda x: len(x))
            original = filepaths[0]
            duplicates = filepaths[1:]
            
            for duplicate in duplicates:
                size = os.path.getsize(duplicate)
                try:
                    os.remove(duplicate)
                    deleted_count += 1
                    deleted_size += size
                    print(f"Deleted: {duplicate} (Duplicate of {original})")
                except Exception as e:
                    print(f"Failed to delete {duplicate}: {e}")
                    
    print("\n--- Deduplication Summary ---")
    print(f"Scanned {total_files} files ({(total_size / 1024 / 1024):.2f} MB)")
    print(f"Deleted {deleted_count} duplicate files ({(deleted_size / 1024 / 1024):.2f} MB saved)")

if __name__ == '__main__':
    deduplicate()
