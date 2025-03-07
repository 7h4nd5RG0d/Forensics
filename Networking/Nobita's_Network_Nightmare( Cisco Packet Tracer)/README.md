# File:
https://github.com/7h4nd5RG0d/Forensics/blob/main/Networking/Nobita's_Network_Nightmare(%20Cisco%20Packet%20Tracer)/map.pkt
# Solve:
https://abuctf.github.io/posts/ApoorvCTF/
# Something new:
1) Interface is a connection point in a network device( router,switch,firewall) that allows communication between devices. (**Physical-> Wifi,Fibre** and **Virtual--> VLAN,Loopback,tunnel**)
2) **Loopback Interface** --> always up. Used for testing,routing stability(router id's in OSPF,BGP), remote managaement.
3) **OSPF** --> Open Shortest Path First --> Interior protocol, uses Djkstra.
4) **BGP** -> Exterior, Path Vector Protocol
5) **Tunnel** --> encapsulates one protocol inside another. Used to encrypt data,bypass restrictions.  
       a) GRE Tunnel -->   encapsulates multicast traffic inside normal IPv4 packets.  
                           IPS's do not route multicast packets over the internet to prevent congestion.  
                           A multicast packet is sent from one source to multiple recipients simultaneously. Reduced Bandwidth, used in video streaming,online gaming.  
       b) L2TP tunnel --> combined with IPSec for security
6) Switches(same network) operate in layer 2, while routers(different networks) operate in layer 3. 
