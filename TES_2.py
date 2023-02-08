import hashlib
m = hashlib.sha256()
a = bytes("Hello12345", encoding='utf-8')
m.update(a)
print(m.hexdigest())
