# FIle: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Steganography/freeflag(WORD)--Macros%2BAlternate%20Text/9f982b056b326e26bf78bca33bd2fe65.pcapng  
# Solve: 
https://github.com/PWrWhiteHats/BtS-2024-Writeups/tree/master/forensics/free_flag/writeup  



1)We can get the freeflag.docm by exporting objects from HTTP.  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/e57208d7-d871-4c00-971b-fce4fdedad88)  
2) Open the word in kali and using olevba you can get the macros.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/11bb769f-b240-434d-b746-e1c101b51837)  
3) Using libreoffice(**Right Click on first image-->Properties-->Options-->Description**) you can get the alternate text for the image.  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/b170f6bd-42bc-42e2-b077-78d02fc243c9)  
4) Converting the VBA code to python we get the output as a powershell script.  
https://github.com/7h4nd5RG0d/Forensics/blob/main/Steganography/freeflag(WORD)--Macros%2BAlternate%20Text/code.py  
5)Time to decode the powershell script.  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/7632494b-a186-44bd-b865-9101ba449fda)  
6)Identating the shell script we get it as: 
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/1a251011-df52-4797-9594-36de8c0d3e73)  
7) We can get the required file by : **curl http://192.168.56.1:1337/d9d9dec9d5d2**  
8) After that following the decryption we get the C# code.
9) Running the C# code on https://dotnetfiddle.net/ we get the flag.  
## Something new:  
1) Images may contain alternate text for helping visually impaired images which comes under macros.
2) Look out for the hexadecimal pattern **fc e8 82 00 00 00 ...** to identify shellcode.
3) Shellcode Analysis:- https://medium.com/ce-digital-forensics/analysing-metasploit-framework-shellcode-e66b89411000  
