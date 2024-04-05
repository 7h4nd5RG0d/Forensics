# Link: 
https://cyberdefenders.org/blueteam-ctf-challenges/hireme/  

## Solve:  
https://forensicskween.com/ctf/cyberdefenders/hireme/  

### Something new-->
Command line "regripper" in kali  
For profile--> **"regripper -p winver -r SOFTWARE"**  (windows/system32/config)  
For hostname --> **"regripper -p compname -r SYSTEM"**  (windows/system32/config)  
For last access of documents(MFT present in root) --> MFTparser  
For partitions --> **"regripper -p mountdev2 -r SYSTEM"**  
For user password history --> **"regripper -p samparse -r SAM"** (windows/system32/config)  
For google chrome history --> History present in google/chrome/userdata/default  
For timezone --> regripper -p timezone -r SYSTEM  
For DHCP lease time --> regripper -p networklist -r SOFTWARE  
For ip of system --> regripper -p ips -r SYSTEM  


**Also files in outlook are stored as .ost or .pst files**   
Use **pffexport** commandline to export them and then use **html2text** to convert to readable form.  
