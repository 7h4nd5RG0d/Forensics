# File:
https://drive.google.com/file/d/1P9uLCpvN__fN4MIP_lRxmc9hRdMVPJ85/view?usp=drive_web 

# Solve:
1) Find version of linux(using grep linux)  
2) For volatility 2 --> https://github.com/Abyss-W4tcher/volatility2-profiles/tree/master and for volatility3 --> https://github.com/leludo84/vol3-linux-profiles/tree/main.  
3) See the bash history using **python2 vol.py -f <lime_file> --profile=LinuxUbuntu_4_15_0-212-generic_4_15_0-212_223_amd64x64 linux_bash** to see there is a kernel module downloaded.  
4) Get the kernel module using this --> **python2 vol.py -f <lime_file> --profile=LinuxUbuntu_4_15_0-212-generic_4_15_0-212_223_amd64x64 linux_find_file -i  0xffff9fc2c580df18 -O moreram.ko**  
5) 

# Something new: 
1) Use this to load volatility profiles--> https://raksec.blogspot.com/2017/02/forensics-ctf-challenge-ramdisk-writeup.html  
2) Linux Forensics + Kernel Reversing ==> https://stuxnet999.github.io/dfir/insomnihack-teaser-2020-getdents/  
3) To create own profile in volatiltiy -> https://github.com/volatilityfoundation/volatility/wiki/Linux#creating-a-new-profile  
4) Kernel Module Reversing
