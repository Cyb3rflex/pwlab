#!/usr/bin/env python3
# hash_passwords.py
# Usage: python3 hash_passwords.py sample_passwords.txt hashes.txt
# Produces file with lines: username:salt:hex_sha256(salt+password)

import sys, os, hashlib, secrets

if len(sys.argv) != 3:
    print("Usage: python3 hash_passwords.py sample_passwords.txt hashes.txt")
    sys.exit(1)

infile, outfile = sys.argv[1], sys.argv[2]

with open(infile, 'rt') as f_in, open(outfile, 'wt') as f_out:
    for i, line in enumerate(f_in):
        pw = line.strip()
        if not pw:
            continue
        username = f"user{:02d}".format(i+1)
        salt = secrets.token_hex(8)          # 16 hex chars = 8 bytes
        h = hashlib.sha256((salt + pw).encode('utf-8')).hexdigest()
        f_out.write(f"{username}:{salt}:{h}\n")

print(f"Created hashes in {outfile}")
