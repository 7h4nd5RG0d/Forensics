# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Steganography/saveme/saveme-chall.zip  

# Solve: 
1) Unzipping the file, we see lots of images which seem to be have corrupted--> hinting towards ransomware.  
2) Also a .docm file is given --> running olevba on it tells us no **macros** is present in the doc.  
3) Opening the docm file we see lots of blank pages while just clicking we see that there is actually something written there.  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/96b0ac94-1c1e-4639-b907-4c94177d3533)  
4) So changing the font color we can see what is written ->  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/2dfe91c9-c8a3-4b3f-98b1-29691da4f68c)  
5) Popping it in cyberchef we get a dll file.  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/940c515b-b926-4e99-8e84-1f207ef8dc97)

6) Popping it in virustotal and then going to the community -> we see this report.  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/ea301842-b09b-4be8-8469-80888c66c639)  
7) In this report it says that the dll executes this command. (We can do all this by just clicking the dll in a **VM not your windows otherwise your system will be corrupted**)  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/8bb59f6c-ddb0-4b15-be5c-17010d1f9a60)  
8) So running the command on a VM we get the ransomware.exe which is a .NET Assembly.  ![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/52ffa4ea-ede3-40aa-95b4-0800f0b42cbf)  
9) Using dnSpy to decompile it we see that it is using 3DES with a hardcoded "iv" and "key".
![2](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/43a9fa3c-5243-48e8-b1e8-93d03bbe7eef)
![3](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/1cd7ca1e-d3a4-4c90-901f-c6a505a9e76e)
10) So we have everything we need to decrypt the images --> using this script I decoded the only PNG among them and got the flag -->
11) Using this script --> 
![decrypted_file](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/2f2cec0a-cb18-4655-a098-e5298fc343e9)








