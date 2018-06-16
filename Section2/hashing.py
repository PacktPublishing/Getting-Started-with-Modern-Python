checksum=0
a_string = "12 32 15 25"
for letter in a_string:
    checksum = (checksum + (32*ord(letter)+12)) % 255

print(checksum)
import hashlib
with open(__file__,"rb") as f:
    print(hashlib.md5(f.read()).hexdigest())

password="test"
hashed_pw = hashlib.sha1(password.encode('utf8')).hexdigest()

print(hashed_pw)

print(hashlib.sha1(b"test").hexdigest() == hashed_pw)