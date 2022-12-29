from hashlib import sha1

text = 'admin123'

my_hash = sha1(text.encode('UTF-8'))
print(my_hash.hexdigest())
