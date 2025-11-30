"""
Task 2: SHA3-256 Hash Calculator with Self-Verification
"""

import hashlib
import os
import sys
from pathlib import Path
from typing import List

# --- Configuration ---
INPUT_DIRECTORY = Path(os.path.dirname(os.path.abspath(__file__))) / "Input"
EMAIL = "abdulkhay.payziev@gmail.com"

# Protocol constants
EXPECTED_FILE_COUNT = 256
SHA3_EMPTY_STRING_HASH = "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a"

# Test vector for sorting algorithm verification
TEST_HASH = "63a6ba9e5de66b11ad6c6d3d1b39a5456f65f918fde6250565e365d89a5196c6"
TEST_KEY = 71365623100112242680609229940949951316513259520000000000


def verify_sha3_implementation() -> None:
    """Verify SHA3-256 algorithm (not Keccak) using standard test vector."""
    test_hash = hashlib.sha3_256(b'').hexdigest()
    if test_hash != SHA3_EMPTY_STRING_HASH:
        raise RuntimeError(f"SHA3-256 mismatch! Got '{test_hash}'")
    print("✓ SHA3-256 algorithm verified")


def calculate_sorting_key(hash_str: str) -> int:
    """Calculate product of (hex_digit + 1) for each digit in hash."""
    product = 1
    for char in hash_str:
        product *= int(char, 16) + 1
    return product


def verify_sorting_logic() -> None:
    """Verify sorting key calculation against example from instructions."""
    if calculate_sorting_key(TEST_HASH) != TEST_KEY:
        raise RuntimeError("Sorting logic verification failed!")
    print("✓ Sorting logic verified")


def get_binary_files(directory: Path) -> List[Path]:
    """Get sorted list of non-hidden files from directory."""
    if not directory.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    files = sorted([
        f for f in directory.iterdir()
        if f.is_file() and not f.name.startswith('.')
    ])
    
    if len(files) != EXPECTED_FILE_COUNT:
        print(f"⚠ WARNING: Found {len(files)} files, expected {EXPECTED_FILE_COUNT}")
    
    return files


def compute_file_hash(file_path: Path) -> str:
    """Read file as binary and return SHA3-256 hash in lowercase hex."""
    with open(file_path, 'rb') as f:
        return hashlib.sha3_256(f.read()).hexdigest().lower()


def main():
    # 1. Verify environment
    try:
        verify_sha3_implementation()
        verify_sorting_logic()
    except RuntimeError as e:
        print(f"FATAL: {e}")
        sys.exit(1)
    
    # 2. Hash all files
    files = get_binary_files(INPUT_DIRECTORY)
    print(f"✓ Processing {len(files)} files")
    hashes = [compute_file_hash(f) for f in files]
    
    # 3. Sort by product of (digit + 1)
    sorted_hashes = sorted(hashes, key=calculate_sorting_key)
    
    # 4. Join hashes and append email
    result_string = ''.join(sorted_hashes) + EMAIL.lower()
    
    # 5. Calculate final hash
    final_hash = hashlib.sha3_256(result_string.encode()).hexdigest().lower()
    
    # 6. Output submission command
    print(f"\n!task2 {EMAIL.lower()} {final_hash}")


if __name__ == "__main__":
    main()
