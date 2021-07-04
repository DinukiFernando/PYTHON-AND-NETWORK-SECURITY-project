# Write a program in python to generate MD5 of string data

import hashlib

text = input("Enter your name: ")

result = hashlib.md5(text.encode())

print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())



