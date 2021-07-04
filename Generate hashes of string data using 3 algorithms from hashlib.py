import hashlib

# Write a program in python to generate hashes of string data using 3 algorithms from hashlib.


text_str = input("Enter your name: ")

result1 = hashlib.sha256(text_str .encode())
print(result1.hexdigest())

result2 = hashlib.sha384(text_str .encode())
print(result2.hexdigest())

result3 = hashlib.sha224(text_str .encode())
print(result3.hexdigest())


