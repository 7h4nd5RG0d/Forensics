# File:
https://github.com/7h4nd5RG0d/Forensics/blob/main/Networking/pingpong(ICMP)/traffic.pcap  
# Solve:
tshark -r traffic.pcap -Y 'icmp' -T fields -e 'data.data' > a.txt  
Converting hex to ascii, base64 decoding it and then saving it into PNG image we get the flag.  
![a](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/bd41363f-f5b8-4007-acdc-05266812f134)

Based on ICMP tunneling.  


