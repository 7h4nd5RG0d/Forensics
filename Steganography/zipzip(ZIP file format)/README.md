# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Steganography/zipzip(ZIP%20file%20format)/archive%20(2).zip
# Solve:
1) Understanding the zip format using this --> https://en.wikipedia.org/wiki/ZIP_(file_format)#Extra_field we see that there are 2 files in the zip as opposed to only 1 file getting extracted.
![1](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/5de8f60f-075d-4e25-b72e-130a4ed6fd08)
![2](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/8d3ba9ba-4b54-4fac-bae0-4189a0efaa98)
2) So, yeah the flag has to be in the second file but how do we get it.
3) Here comes the need for understanding the zip file format.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/c56ef996-d2c3-406a-ab36-ac3ad311b5e7)
4) So lets use this for the first file, present at offset 0x00.
5) **Header**= 50 4B 03 04  
   **Version needed to extract** = "14 00" (20 in decimal--> version 2.0)  
   **Special bits** = "00 00"(no special flags)   
   **Compresssion method** = "08 00"(Deflation)  
   **Last modified time**= "4A 37 " 
   **Last modified date**= "84 58"  
   **CRC 32** = "C4 29 B0 39"  
   **Compressed size**= "01 B0 00 00" (--> this is in fact B001 bytes since we take it in big endian format)  
   **File name size**= "20 00"(32 bytes)    
   **File name** = "34 61 64 39 65 64 64 65 38 31 62 35 35 32 36 64 63 64 39 35 37 34 37 61 39 36 61 39 30 35 38 33"  
   **Only this much is required**

6)So the data of 1st file ends at (B001 + 3D(Header bytes) =B03E byte)   
7)Now I tried recovering the entire zip from here , like adding the header for the second file , but failed.  
8)But then, again we have the compressed data format right.  
![3](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/57ad3a63-63eb-4c29-8da7-cb990ba66187)  
9) So doing the above steps for file2 we see that the file name is **33 36 64 66 38 66 33 61 39 39 30 33 35 36 66 38 62 39 37 38 31 35 61 61 39 30 38 33 62 38 34 39** and the compressed data is 13 bytes.  
**Here I did backtracking, so the file name is as above, length is 32 bytes and so on we go back and get that the compressed data is 13 bytes long**  
10) So taking the next 13 bytes after the name we get the compressed data bytes as **F3 33 08 08 AE AE 32 2C 88 47 C2 B5 00**  
11) And we know that is deflate method from above so just using zlib.deflate gives us the flag.   
This is the code for deflating -->  https://github.com/7h4nd5RG0d/Forensics/blob/main/Steganography/zipzip(ZIP%20file%20format)/code2.py  

    
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/c5879be5-59e2-4d9b-a898-a0b0c0b01ce9)


# Something new :
1) https://en.wikipedia.org/wiki/ZIP_(file_format)#Extra_field  
