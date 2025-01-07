# File:

# Solve:
https://infern0o.medium.com/icmtc-ctf-2023-final-forensics-writeup-b4292e7e1db0  

# Something new:
1) Perisistance keys ->  
a) **HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run** (Progrmas starts automatically when users log in)  
b) **HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce** (Execute only once and then removed from registry)  
c) **%AppData%\Microsoft\Windows\Start Menu\Programs\Startup** (Any file/folder runs on login)  
d) **HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnceEx**  
e) **HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices** (services start before user login)  
f) **HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce**  
g) **%SystemRoot%\System32\Tasks** (tasks are executed based on specific triggers)  
h) **HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run** (OR) **HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run** (scripts to run on user login/logout)  
i) **HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System\Scripts\Startup** (OR) **HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System\Scripts\Shutdown** (runs scripts during startup or shutdown)  
j) **HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Windows\AppInit_DLLs** (specifies DLL's to be loaded into every process)  
k) **HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell** (specifies the shell program)  
l) **HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit** ( program to run at user login)  
m) **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\BootExecute** (specifies the commands to be executed during boot process)  
n) **%ProgramData%\Microsoft\Windows\Start Menu\Programs\Startup** ( run at startup for all users)  
