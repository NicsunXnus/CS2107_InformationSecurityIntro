import hashlib
import string
def getAll():
    for char in range(ord('a'), ord('z') + 1):
        s = str(chr(char))
        print(s)
        hsh = hashlib.sha1(s.encode())
        print(hsh.hexdigest())
    for char in range(ord('0'),ord('9') + 1):
        s = str(chr(char))
        print(s)
        hsh = hashlib.sha1(s.encode())
        print(hsh.hexdigest())
    for char in range(ord('A'),ord('Z') + 1):
        s = str(chr(char))
        print(s)
        hsh = hashlib.sha1(s.encode())
        print(hsh.hexdigest())
getAll()
punctuation = list(string.punctuation)
for p in punctuation:
    print(p)
    hsh = hashlib.sha1(p.encode())
    print(hsh.hexdigest())
        
