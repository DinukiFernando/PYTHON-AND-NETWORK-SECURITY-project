# Add salting and iterations to your hashes.

import hashlib
import os

text_str = input("Enter your password: ")
password = text_str
password = password.encode()
salt = os.urandom(16)
password_hash1 = hashlib.pbkdf2_hmac("sha256", password, salt, 100000)
password_hash2 = hashlib.pbkdf2_hmac("sha384", password, salt, 100000)
password_hash3 = hashlib.pbkdf2_hmac("sha224", password, salt, 100000)

print(password_hash1)
print(password_hash2)
print(password_hash3)
