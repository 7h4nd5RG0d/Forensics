# FIle: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Steganography/freeflag(WORD)--Macros%2BAlternate%20Text/9f982b056b326e26bf78bca33bd2fe65.pcapng  
# Solve: 
https://github.com/PWrWhiteHats/BtS-2024-Writeups/tree/master/forensics/free_flag/writeup
We can get the freeflag.docm by exporting objects from HTTP.  
1) Open the word in kali and using olevba you can get the macros.
2) Using libreoffice(**Right Click on first image-->Properties-->Options-->Description**) you can get the alternate text for the image.
3) Using this we can get the output of the VBA code as Shell code which on decompiling we get a C# code which gives the flag.


## Something new:  
1) Images may contain alternate text for helping visually impaired images which comes under macros.
