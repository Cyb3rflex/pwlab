# pwlab — Password Hashing & Controlled Dictionary Crack

Short lab to demonstrate hashing, salting, and dictionary attacks in a controlled classroom environment.

## Files
- `hash_passwords.py` — create salted SHA-256 hashes from plaintext.
a. hash_passwkrds.py example to use

  ```bash
#!/usr/bin/env python3
# hash_passwords.py
# Usage: python3 hash_passwords.py sample_passwords.txt hashes.txt
# Produces file with lines: username:salt:hex_sha256(salt+password)

import sys
import hashlib
import secrets

if len(sys.argv) != 3:
    print("Usage: python3 hash_passwords.py sample_passwords.txt hashes.txt")
    sys.exit(1)

infile, outfile = sys.argv[1], sys.argv[2]

with open(infile, 'rt', encoding='utf-8') as f_in, open(outfile, 'wt', encoding='utf-8') as f_out:
    for i, line in enumerate(f_in):
        pw = line.strip()
        if not pw:
            continue
        username = f"user{i+1:02d}"           # fixed f-string formatting
        salt = secrets.token_hex(8)           # 8 bytes -> 16 hex chars
        h = hashlib.sha256((salt + pw).encode('utf-8')).hexdigest()
        f_out.write(f"{username}:{salt}:{h}\n")

print(f"Created hashes in {outfile}")```

- `crack_dict.py` — attempt to recover passwords using a small wordlist.
- `sample_passwords.txt` — example plaintext passwords (students can edit).
- `wordlist.txt` — small dictionary used for cracking (teacher-provided).

## Quick start (Kali/Termux)

1. Clone repo or copy files into a folder:
   ```bash
   mkdir -p ~/pwlab && cd ~/pwlab
   ```
   
2. Generate hashes:
```bash
python3 hash_passwords.py sample_passwords.txt hashes.txt
cat hashes.txt
```

3. Run dictionary crack:
```bash
python3 crack_dict.py hashes.txt wordlist.txt cracked_results.txt
cat cracked_results.txt
```


## Learning tasks

Explain which accounts were cracked and why.

Describe how salt changes the hash and defends against rainbow tables.

Suggest defensive measures: strong passwords, password managers, bcrypt/argon2, rate limiting, 2FA.


## Ethics

Only use these scripts on lab-created files and equipment you own or have permission to use. Do not attack external systems or accounts.

## MIT Licence 

MIT License

Copyright (c) 2025 Cyberflex

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### `.gitignore`
```bash
cat > .gitignore <<'EOF'
# Byte-compiled / caches
__pycache__/
*.py[cod]
*.pyo

# OS files
.DS_Store
Thumbs.db

# Local files
hashes.txt
cracked_results.txt
```
