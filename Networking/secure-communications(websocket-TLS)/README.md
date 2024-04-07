# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Networking/secure-communications(websocket-TLS)/chall.pcapng  

## Solve:  
Observing the websocket packets we get a packet with TLS/SSL keys(tcp frame 137)  
Decrypting the traffic we get extra websockets packets and in one of them theres is the flag( frame.len==158) in the data field
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/d53dd5c8-f65c-43cd-9202-529548d87faf)
