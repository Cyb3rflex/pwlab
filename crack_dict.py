#!/usr/bin/env python3
# crack_dict.py
# Usage: python3 crack_dict.py hashes.txt wordlist.txt cracked_output.txt
# This only tries entries in wordlist.txt and only against the provided hashes.

import sys, hashlib

if len(sys.argv) != 4:
    print("Usage: python3 crack_dict.py hashes.txt wordlist.txt cracked_output.txt")
    sys.exit(1)

hashes_file, wordlist_file, out_file = sys.argv[1], sys.argv[2], sys.argv[3]

# Load hashed entries
targets = []
with open(hashes_file, 'rt') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        user, salt, h = line.split(':')
        targets.append((user, salt, h))

# Load candidate words
candidates = [w.strip() for w in open(wordlist_file, 'rt') if w.strip()]

cracked = []

for user, salt, target_hash in targets:
    found = False
    for cand in candidates:
        cand_hash = hashlib.sha256((salt + cand).encode('utf-8')).hexdigest()
        if cand_hash == target_hash:
            cracked.append((user, cand))
            found = True
            break
    if not found:
        cracked.append((user, None))

with open(out_file, 'wt') as f:
    for user, pw in cracked:
        if pw:
            f.write(f"{user}:CRACKED:{pw}\n")
        else:
            f.write(f"{user}:NOT_FOUND\n")

print(f"Cracking finished. Results in {out_file}")
