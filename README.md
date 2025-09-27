# pwlab — Password Hashing & Controlled Dictionary Crack

Short lab to demonstrate hashing, salting, and dictionary attacks in a controlled classroom environment.

## Files
- hash_passwords.py — create salted SHA-256 hashes from plaintext.
- crack_dict.py — attempt to recover passwords using a small wordlist.
- sample_passwords.txt — example plaintext passwords (students can edit).
- wordlist.txt — small dictionary used for cracking (teacher-provided).

## Quick start (Kali/Termux)
1. Clone repo or copy files into a folder:
   ```bash
   mkdir -p ~/pwlab && cd ~/pwlab
   # place files here
2. Generate hashes:

python3 hash_passwords.py sample_passwords.txt hashes.txt
cat hashes.txt


3. Run dictionary crack:

python3 crack_dict.py hashes.txt wordlist.txt cracked_results.txt
cat cracked_results.txt



Learning tasks

Explain which accounts were cracked and why.

Describe how salt changes the hash and defends against rainbow tables.

Suggest defensive measures: strong passwords, password managers, bcrypt/argon2, rate limiting, 2FA.


Ethics

Only use these scripts on lab-created files and equipment you own or have permission to use. Do not attack external systems or accounts.

License

MIT EOF

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
