# File:
https://drive.google.com/file/d/1tdPBWDPuGtYGMdIrgYZTLUPaHJop_GXP/view?usp=drive_web  

# Solve: 
1) We see an unusually large number of DNS packets.  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/741a9a84-138f-4f31-b5a1-c876bb7afafc)
2) This hints towards DNS exfiltration. To confirm just checking the DNS packets and we are correct.
![1](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/782960db-ae6d-4f32-b04f-c3eac0b6cb14)
3) So we have to extract the hex values and concatenate them while making sure we get each hex string only once.
4) Using this **dns && frame.len==170 && dns.qry.type==A** we get each hex string only once. Exporting these packets using wireshark to a new pcapng makes it easy.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/2339dc3b-dfda-463d-a78b-fe045fa00a04)
5) Now using this script we can get the hex strings concatenated -> https://github.com/7h4nd5RG0d/Forensics/blob/main/Networking/Sussy(DNS%20Exfiltration)/1.py
6) After popping it in cyberchef and running "To Hex" we get something that looks like a 7z file format.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/e843d7e0-20d3-4964-b474-82eb2118441e)
7) So saving it as a file and then trying to extract we see an error, inavlid file.
8) Again going back, I saw that one packet was missed during this since it has a length of 160..
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/af03a12c-f09f-478b-8413-1e6debfaf819)
9) Concatenating the hex bytes of this to the end, we get a valid 7z file.
10) But it is password protected, so using **john** to crack the password using **7z2john 'download (1).7z' > hash.txt** and then **john --wordlist=/path/to/wordlist.txt --format=7z hash.txt** we get a password using which we can extract the 7z file to get a PDF file.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/10817bbf-d8d5-4ae1-adb8-29b41401457e)
11) But even the PDF is password protected,again using **john** to crack the password using **pdf2john flag.pdf > hash.txt** and then **john --wordlist==/path to wordlist hash.txt** we can open the PDF and get the flag.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/13f1eaf1-3a9b-4f4f-aca6-439928d8d286)
12) Finally the flag --> ![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/3f9dbc60-c88b-4a6f-a12d-92c179c6f023)







