# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Steganography/walls(BMP-Padding)/challenge.bmp
# Solve: 
https://github.com/PWrWhiteHats/BtS-2024-Writeups/tree/master/stegano/walls/writeup

# Something new:  
1) **In a 24-bit bitmap, each scanline (row of pixels) is aligned to a 4-byte boundary, meaning each row might include some padding bytes at the end to ensure this alignment** --> this can hide data as padding can be anything possible.
2) https://en.wikipedia.org/wiki/BMP_file_format#Pixel_storage  
