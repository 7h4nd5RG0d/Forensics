# File: 
https://drive.google.com/file/d/1Um4nX3RpzsmyrrLbtYG9-gri3MC6AZQf/view  
# Solve: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Memory/keepa-si-safe(Keepass%2BThunderbird%2BPowershell---%3E%20Volatitltiy)/Author_WU_keepa-si-safe_.pdf  

## Somethinng new:  

1) Thunderbird stores all info in Profile folders.
2) Powershell was running -->> command line will be of help and it is stored in Console_History.txt.
3) Working of CVE-2023-32784 --> Some randome points.  
  a) The first character cannot be recovered.  
  b) Present in all versions before 2.54  
  c) "**The flaw exploited here is that for every character typed, a leftover string is created in memory. Because of how .NET works, it is nearly impossible to get rid of it once it gets created. For example, when 
     "Password" is typed, it will result in these leftover strings: •a, ••s, •••s, ••••w, •••••o, ••••••r, •••••••d. The POC application searches the dump for these patterns and offers a likely password character for each 
     position in the password.**"
   
