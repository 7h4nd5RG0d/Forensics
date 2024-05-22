# FIle: 

# Solve: 
https://github.com/PWrWhiteHats/BtS-2024-Writeups/tree/master/forensics/free_flag/writeup
  
1) Open the word in kali and using olevba you can get the macros.
2) Using libreoffice(**Right Click on first image-->Properties-->Options-->Description**) you can get the alternate text for the image.
3) Using this we can get the output of the VBA code as Shell code which on decompiling we get a C# code which gives the flag.
