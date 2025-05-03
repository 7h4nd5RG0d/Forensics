# File:
https://github.com/7h4nd5RG0d/Forensics/blob/main/Networking/Rerdp%20(%20RDP)/capture_output.pcap
# Solve:
https://0x90r00t.com/2024/09/30/defcamp-quals-2024-forensics-50-rerdp-write-up/
# Something new:
1) RDP is encapsulated and encrypted within the TCP.
2) RDP provides 64000 channels while other current tools provide a single channel.
3) The terminal service device driver coordinates and manages the RDP protocol activity.
4) It consists of 2 drivers a) **Wdtshare.sys** -> for UI transfer, encryption, framing and b) **Tdtcp.sys** -> package the protocol onto the underlying network protocol stack TCP/IP.
