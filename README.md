# pwlab — Password Hashing & Controlled Dictionary Crack

Short lab to demonstrate hashing, salting, and dictionary attacks in a controlled classroom environment.

## Files
- `hash_passwords.py` — create salted SHA-256 hashes from plaintext.
  
a. hash_passwords.py example to use

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

print(f"Created hashes in {outfile}")
```

- `crack_dict.py` — attempt to recover passwords using a small wordlist.
  
b - crack_dict.py codes example to use
```bash
#!/usr/bin/env python3
# crack_dict.py
# Usage: python3 crack_dict.py hashes.txt wordlist.txt cracked_output.txt
# This only tries entries in wordlist.txt and only against the provided hashes.

import sys
import hashlib

if len(sys.argv) != 4:
    print("Usage: python3 crack_dict.py hashes.txt wordlist.txt cracked_output.txt")
    sys.exit(1)

hashes_file, wordlist_file, out_file = sys.argv[1], sys.argv[2], sys.argv[3]

# Load hashed entries
targets = []
with open(hashes_file, 'rt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(':')
        if len(parts) != 3:
            print(f"Skipping malformed line: {line}")
            continue
        user, salt, h = parts
        targets.append((user, salt, h))

# Load candidate words
with open(wordlist_file, 'rt', encoding='utf-8') as f:
    candidates = [w.strip() for w in f if w.strip()]

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

with open(out_file, 'wt', encoding='utf-8') as f:
    for user, pw in cracked:
        if pw:
            f.write(f"{user}:CRACKED:{pw}\n")
        else:
            f.write(f"{user}:NOT_FOUND\n")

print(f"Cracking finished. Results in {out_file}")
```
  
- `sample_passwords.txt` — example plaintext passwords (students can edit).
c - example sample_passwords.txt
 ```bash
password
secret
mypassword
uniqueStrong#1
teacher123
```
- `wordlist.txt` — small dictionary used for cracking (teacher-provided).
  
d - example wordlist by teacher
 ```bash
password
123456
qwerty
letmein
football
welcome
admin
secret
sunshine
iloveyou
mypassword
teacher123
student123
```
e - make script executable 
```bash
chmod +x hash_passwords.py crack_dict.py
```
f - test locally
 - Run
```bash
python3 hash_passwords.py sample_passwords.txt hashes.txt
cat hashes.txt
python3 crack_dict.py hashes.txt wordlist.txt cracked_results.txt
cat cracked_results.txt
```
g - Confirm `cracked_results.txt` lists CRACKED for weak ones and NOT_FOUND for strong ones.

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

# How salt changes the hash and defends against rainbow tables

A salt is a random value added to a password before hashing. Instead of hashing just the password (e.g., hash("mypassword")), the system hashes hash("randomSalt" + "mypassword").

This changes the output in two important ways:

1. Uniqueness: Two users with the same password will have different hashes, because each salt is different.


2. Rainbow table defense: A rainbow table is a large precomputed list of hashes for common passwords. Since the salt is random and unique per user, attackers would need to compute a new rainbow table for every possible salt — which is computationally infeasible.



So, salting ensures that precomputed attacks become useless and forces attackers to brute force each password individually.


---
# Suggest defensive measures: strong passwords, password managers, bcrypt/argon2, rate limiting, 2FA.


# Defensive measures

1. Strong passwords: Encourage long, unpredictable passwords to increase brute-force difficulty.


2. Password managers: Let users generate and store complex passwords without needing to remember them.


3. Modern hashing algorithms: Use adaptive functions like bcrypt, scrypt, or Argon2. They are deliberately slow and memory-hard, making brute-force attacks more expensive.


4. Rate limiting: Limit login attempts (e.g., 5 tries per minute per IP). This slows down online brute-force attacks.


5. Two-Factor Authentication (2FA): Require an additional factor (like an OTP or authenticator app code). Even if a password is compromised, the account remains protected.




---

Put simply: Salt defeats rainbow tables, bcrypt/Argon2 defeats brute force, strong passwords defeat guessing, and 2FA defeats password theft.


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
