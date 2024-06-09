# Files: 
https://drive.google.com/file/d/1-pDyle734PztiK5_6VMiQ1EzG7IGGsmc/view?usp=drive_web  

# Solve: 
1) Opening the pcap file in wireshark and going to **tcp stream 3** we get some base64 encoded data.
2) Baes64 decoding it we get a exe file -->
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/0c5dc1a2-5240-49dd-b845-9a4f4d5c4026)
3) We see that it is a .NET assembly so opening it in dnSpy to decompile it -->
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/1244d148-12b1-4076-af8c-6e3238617c3a)
5) We see that the data of port 1337 is being encrypted,using AES.
![4](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/584390df-cced-49be-8a7b-5187ab3be3a9)
![5](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/12bfb504-f098-4020-b817-8bd39d77c34b)
![6](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/c3cdabe3-e86c-45f4-a6f8-1b905b63a5a5)
6) So we need to decrypt the data sent and received on port 1337.
7) We first export the needed packets to make it easier for decryption.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/cf39433e-799a-49f8-b027-0f375333d8f8)
8) Then running this script for decryption we get something .. --> 
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/f80272a0-a57b-4a7b-be1b-861f6ea8bd2e)    
9) Some password for pastecode --> pastecode=pastebin --> there must be some pastecode link in the dump that need this password.  
10) Going to the dump,we see there is notepad.exe running which is suspicious. ![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/ad235a8e-a576-4d20-901d-d2546575344c)
11) So dumping the process using **python3 vol.py -f ../../memdump.mem -o c windows.memmap --pid 3608 --dump** and then going to the directory and running **strings * -e l** we get a pastebin link.(The dump is always little endian so we use **-e l** for that)/(We run strings since notes in notepad are stored in the file format itself so when we run strings notepad data is visible).  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/ff92fc25-fc04-486f-8f36-3761b7fce933)
12) So going to the link and entering the password we get base64 data.
13) Popping it in cyberchef we get a **zip file**. (PK header) ![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/e9087936-b4c0-45a0-819f-155dffd96bad)
14) So we try to unzip it but gives an error in kali so I just used 7-zip file manager to navigate till flag.jpg.![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/9302c30b-41cc-4212-a2d0-beee99317de1)
15) But it is password protected so I again went back and did **strings * -e l | grep -i 'password** and we get the password for the file.![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/69f9b25d-626e-4218-9d80-c0a2e861b150)
16) Extracting flag.jpg and using stegseek we get the flag FINALLYYYYYYYYYYYYYYYY.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/36a3ff48-e979-4975-8004-85c54b449783)

 


