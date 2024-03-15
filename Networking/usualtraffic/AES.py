import base64
from Crypto.Cipher import AES
from Crypto import Random

def decrypt(key,iv,secret):
    secret=base64.b64decode(secret)
    cipher=AES.new(key,AES.MODE_CBC,iv)
    return cipher.decrypt(secret)

key=bytes.fromhex("74c95604043427f0bee1d0e16bfa53afd537f736ad0073c4cc4e1ccb3a82b5dc")
iv=bytes.fromhex("8bf46c25d9bad98ed8eae6c1f7ad2d04")
secret="uWyYTCYqBTy9afI69to3eK0ScCA3SlPDEzBsWBnR9D8Ro7aIOqihGMPXwu/Z+HLn"
print(decrypt(key,iv,secret))
