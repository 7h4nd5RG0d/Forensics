# File: 
https://drive.google.com/file/d/1ktun3sLsT7Hh-VmgCwu-AYFPM8DSeH-D/view?usp=drive_web  
We need to find the application vulnerable to privelage escalation,its version and its path.  

## Solve 
We are given lots of hives in this disk image.  
Opening the SYSTEM hive with the help of registry explorer and going to Available Bookmarks/Uninstall we see 2  apps, VMWare and openvpn.  
Surfing the internet we see that openvpn 3.0.0 has privelege escalation exploitation and from there we can find the required data.  

https://a1l4m.medium.com/cyctf-finals-2023-forensics-writeups-f73ef9caa0cb  
https://www.exploit-db.com/exploits/47575  
