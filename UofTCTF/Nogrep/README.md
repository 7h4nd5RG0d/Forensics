### File: https://storage.googleapis.com/hourglass-uoftctf/ctf_vm.zip  
#### Approach: 
Downloading the VM and setting it up in virtualbox we can start looking for the flag.  
Took some time of exploring until I found something interesting, THE POWERSHELL CONSOLE HISTORY!!  
This is usually the jackpot file as it contains a hell lot of information.  
It was under C:\Users\analyst\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine
![image](https://github.com/7h4nd5RG0d/UoftCTF-2024-/assets/128285431/76725008-1763-48c0-af07-873124727526)  
This line looks suspicious Set-Alias -Name UpdateSystem -Value "C:\Windows\Web\Wallpaper\Theme2\update.ps1"  
So going to the location C:\Windows\Web\Wallpaper we see that there is no theme2 folder(!!!)  
But if you see under the Flowers directory we see an update file.  
Opening it we get a code.  
![image](https://github.com/7h4nd5RG0d/UoftCTF-2024-/assets/128285431/260610f0-45e7-43a0-a949-f1261f1d5803)    
Converting it to python we get the flag..##  

##### CODE:   
https://github.com/7h4nd5RG0d/Forensics/blob/main/UofTCTF/Nogrep/CODE.py  
##### FLAG: uoftctf{0dd_w4y_t0_run_pw5h}
