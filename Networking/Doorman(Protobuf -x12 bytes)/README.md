# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Networking/Doorman(Protobuf%20-x12%20bytes)/leaked.pcap  
  
# Solve:  
https://github.com/polycyber/24hCTF2024_challenges/tree/main/networking/doorman/solution  

# Something new:   
1) If in raw bytes in wireshark, we see a lot of /x12 bytes , we can assume it to be Protobuf protocol which can then be decoded using cyberchef.
2) Protobuf protocol is used to serialize structured data.
