from Crypto.Cipher import DES3
import os

def decrypt_file(input_file, output_file, key, iv):
    # Create a TripleDES cipher object
    cipher = DES3.new(key, DES3.MODE_CBC, iv)

    # Open the input file for reading binary data
    with open(input_file, 'rb') as f:
        ciphertext = f.read()

    # Decrypt the ciphertext
    decrypted_data = cipher.decrypt(ciphertext)

    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Input file to be decrypted
input_file = 'image.png'  # Change this to your encrypted file name

# Output file where decrypted data will be written
output_file = 'decrypted_file.png'  # Change this to your desired output file name

# Key and IV used for decryption
key = b'Lp3jXluuW799rnu4'
iv = bytes([0, 1, 2, 3, 4, 5, 6, 7])

# Decrypt the file
decrypt_file(input_file, output_file, key, iv)

print("Decryption complete.")
