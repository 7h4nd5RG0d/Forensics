# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Steganography/Nathan%20on%20Osu!(PNG)/nathan_on_osu.png  
## Solve:  
1)Downlading the acropalypse tool we can find the flag.  
https://v0lk3n.github.io/writeup/Osu!CTF2024/Osu!CTF2024-WriteUp#Volatile-Map  

# Something new:  
acropalypse vulnerablility in Windows 11(Snipping tool),..

**CVE 2023-21036** -->> Some points.  
  a) Present in Snipping tool(Windows 11) , Markup(Google pixels phone) , Snip and Snetch(Windows 10)  
  b) " **Markup uses zlib, a compression library that utilizes deflate compression, itself based on the lossless data compression algorithms LZ77 and LZ78, where each bit of data references the last, and dynamic Huffman 
     coding, where a Huffman tree is defined at the start of the block. The Huffman tree in Markup screenshots are respecified every 16 kilobytes. The initial exploit for aCropalypse precomputed a list of 8 bytestrings and 
     passed them to zlib, in order to start from a specific bit offset. Additionally, the initial exploit prefixed the image stream with 32 KB of the ASCII character "X"** "
