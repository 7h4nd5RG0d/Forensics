# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Networking/sums-up(DNS)/malicious_sums.pcap  

# Solve: 
tshark -r malicious_sums.pcap -T fields -Y 'ip.src==192.168.0.110 && ip.dst==210.48.231.182' -e 'udp.checksum' ls  
DNS Exfiltration..
