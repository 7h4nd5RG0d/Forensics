# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Networking/Notoriously%20Tricky%20Login%20Mess(NTLMv2%20hash%20cracking%20Wireshark)/swampchall.pcap  
# Solve:  

The first task is to find the username.  
It can be found easily by following the packets("adamkadaban")  
Now we were asked to crack the password.  
In "tcp.stream eq 19" we can all the information needed( This might be just one hash that can be cracked, other packets can also be used to crack the password)  

NTLMv2 Hash Format for cracking using john/hashcat::  
**username::domain name:NTLM Challenge:NTLM ProofStr:Rest of NTLM Respnse**  


We have already found **username**=adamkadaban.  
**Domain name**=null from packets.  
**NTLM challenge** =1fed9e8e0ca470a3 (will be different for different tcp streams, the right packet can be identified by info parameter).  
**NTLM ProofStr** =98ebffae0b77865893846dfadb757cfb( first 16 bytes of NTLMv2 response, alternatively there is a field in wireshark inbuilt).  
**NTLM Response removing proofstr** = 0101000000000000801c50dbc266da0188d48d08eff230a80000000002001e0045004300320041004d0041005a002d00450033003300530047004c00380001001e0045004300320041004d0041005a002d00450033003300530047004c00380004001e0045004300320041004d0041005a002d00450033003300530047004c00380003001e0045004300320041004d0041005a002d00450033003300530047004c003800070008005783ebd6c266da010000000000000000  

Final Hash: **adamkadaban:::1fed9e8e0ca470a3:98ebffae0b77865893846dfadb757cfb:0101000000000000801c50dbc266da0188d48d08eff230a80000000002001e0045004300320041004d0041005a002d00450033003300530047004c00380001001e0045004300320041004d0041005a002d00450033003300530047004c00380004001e0045004300320041004d0041005a002d00450033003300530047004c00380003001e0045004300320041004d0041005a002d00450033003300530047004c003800070008005783ebd6c266da010000000000000000**  
  
Storing it in a.hash and then using john to crack we get the password.  
**john  a.hash --wordlist=/usr/share/wordlists/rockyou.txt**  
