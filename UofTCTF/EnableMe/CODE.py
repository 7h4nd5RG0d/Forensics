def xor_decrypt(data, key):
    return ''.join(chr(d ^ ord(key[i % len(key)])) for i, d in enumerate(data))

def auto_open():
    v6 = [98, 120, 113, 99, 116, 99, 113, 108, 115, 39, 116, 111, 72, 113, 38, 123, 36, 34, 72, 116, 35, 121, 72, 101, 98, 121, 72, 116, 39, 115, 114, 72, 99, 39, 39, 39, 106]
    v7 = [44, 32, 51, 84, 43, 53, 48, 62, 68, 114, 38, 61, 17, 70, 121, 45, 112, 126, 26, 39, 21, 78, 21, 7, 6, 26, 127, 8, 89, 0, 1, 54, 26, 87, 16, 10, 84]

    v8 = 23

    v9 = ''.join(chr(d ^ ord(chr(v8)[i % len(chr(v8))])) for i, d in enumerate(v6))
    v10 = xor_decrypt(v7, v9)
    print(v9)
    print(v10)
# Run the auto_open function
auto_open()
