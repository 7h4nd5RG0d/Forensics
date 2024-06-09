# Files: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Networking/Sharing%20is%20not%20Caring/network.pcapng  
https://drive.google.com/file/d/1mTV9RZKhE8AyYRwGzlT0Glm9YsQ5Xlzl/view?usp=drive_web  

# Solve: 
1) The description hints towards a shared folder.
2) This is usually the Public folder that is accessible to all the users in the computer.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/6e7d0fd0-cc41-43ad-90f5-fc3af8d1d661)
3) So going straight to the Public folder in the.ad1 file using FTK we see lots of files in Documents section.
4) In that one looks of interest -> **GUYS download free RAM here!!!.txt**
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/ec1fe4c6-7e0a-4b2c-bc15-4257a169a28f)
5) Doing ** curl http://freerambooster.000webhostapp.com/** we see a link to download the executable.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/14eb04d8-a711-4eba-a969-658289b25900)
6) Going to the discordapp link we get the exe file and running strings on it, we see an interesting thing.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/190d2d93-e500-445d-b122-f1e050467445)
7) First reversing the string and then base64 decoding the string we get -->![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/b6e194b7-1733-44c1-a5f7-ee7bdcb987a4)
8) So we see get info on where the sslkeylog file is--> **C:\Users\Public\Documents\Internet Explorer\SIGNUP\ink\sslkey.log**. ![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/1b0e2906-f5a2-406b-ba02-50f8ff814446)
9) Going to that location in ad1 file and then extracting it we see that they are in fact ssl keys in the txt file.
10) Now we can decrypt the TLS traffic of wireshark using this file.(Edit-->Preferences-->TLS)
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/191525f1-8b2b-4555-8ee5-7eb7d5f413f3)
11) We see lots of HTTP and HTTP2 packets now.
12) Exporting all objects of HTTP and running strings we get the flag.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/532996bc-7696-4885-95e9-18348d8eecc1)







