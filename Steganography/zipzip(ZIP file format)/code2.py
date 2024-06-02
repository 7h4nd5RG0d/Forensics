import zlib

# Hex string of the compressed data
compressed_hex_str = "F3330808AEAE322C8847C2B500"

# Convert the hex string to bytes
compressed_bytes = bytes.fromhex(compressed_hex_str)

# Decompress the data using raw DEFLATE compression
try:
    uncompressed_bytes = zlib.decompress(compressed_bytes, -zlib.MAX_WBITS)
    print(uncompressed_bytes)
except zlib.error as e:
    print(f"Decompression error: {e}")
