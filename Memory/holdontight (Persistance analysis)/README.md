# FIle: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Memory/holdontight%20(Persistance%20analysis)/etc.zip  
# Solve: 
https://warlocksmurf.github.io/posts/l3akctf2024/  

# Something new:  
https://hadess.io/the-art-of-linux-persistence/  
1) **/etc/update-motd.d/** --> is used to send dynamic message of the day(MOTD) that is used to send messages to the users when they login.  
   If we can modify files listed in the directory, we can inject malicious script to escalate privileges.  
    https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/update-motd-privilege-escalation/#:~:text=Privilege%20Escalation%20%2Fetc%2Fupdate-motd.d%2F%20is%20used%20to%20generate%20the,we%20can%20inject%20malicious%20script%20to%20escalate%20privileges.
      
2) **/etc/logrotate.d/rsyslog/** --> it involves managing log files by creating new files and removing old ones.
   https://computingforgeeks.com/perform-proper-rsyslog-logs-rotation-using-logrotate/
  
3) **/etc/init.d/** --> while booting or logging in  
   https://pberba.github.io/security/2022/02/06/linux-threat-hunting-for-persistence-initialization-scripts-and-shell-configuration/  
   
4) **etc/crontab** --> cron is used for scheduling jobs.  
   https://dmfrsecurity.com/2021/08/23/cron-persistence/  
   
5) **/etc/systemd/system** --> systemd is a system and service manager for Linux distributions.  
   https://pberba.github.io/security/2022/01/30/linux-threat-hunting-for-persistence-systemd-timers-cron/
   https://redcanary.com/blog/threat-detection/attck-t1501-understanding-systemd-service-persistence/  

6) **/etc/rc.local** --> stores files that will run on boot.  
https://matheuzsecurity.github.io/hacking/linux-threat-hunting-persistence/  

7) **/etc/pam.d** --> configures Pluggable Authentification Modules(PAM) and stores files with the same name as the service they control access to.  
https://matheuzsecurity.github.io/hacking/linux-threat-hunting-persistence/  
https://pberba.github.io/security/2022/02/06/linux-threat-hunting-for-persistence-initialization-scripts-and-shell-configuration/  

8) **/etc/apt/apt.conf.d/** --> used for configuring APT(Advanced Package Tool) which allows you to manage software packages,install updates and handle dependancies.  
https://matheuzsecurity.github.io/hacking/linux-threat-hunting-persistence/  


  
