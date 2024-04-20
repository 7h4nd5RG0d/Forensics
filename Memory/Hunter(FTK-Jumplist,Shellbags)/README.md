# File: 
https://cyberdefenders.org/blueteam-ctf-challenges/hunter/  

## Solve:  
https://medium.com/@m0_4de1/hunter-blue-team-challenge-writeup-cyberdefender-bd4227e1a368  
https://forensicskween.com/ctf/cyberdefenders/hunter/  

# Something new:  
1) Shellbag is present in usrclass.dat **(C:Users< user_name >AppData\Local\Microsoft\Window)** .  
   Directory traversal info is stored here.  
   A shellbag entry is created every time a new file is created.  
2) Jumplists are records of recently accessed files and folders grouped by applications basis **(%APPDATA%Microsoft\Windows\Recent)**  
   They have -ms extension.  
