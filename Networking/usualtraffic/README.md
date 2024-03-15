# Link: https://app.cyber-edu.co/challenges/4fbddad0-1430-11eb-83ee-554d4bde0f5d 
## Solve: 
We see that a connections is being made to localhost.localdomain using BGP(Border Gateway) protocol.  
Analyzing the BGP packets we see that the the bgp.nlri_prefix is holding some information so extracting it using tshark with the commands:  
tshark -r traffic.pcapng -Y "bgp && ip.src==10.10.10.251" -T fields -e bgp.nlri_prefix > b  
tshark -r traffic.pcapng -Y "bgp && ip.src==10.10.10.1" -T fields -e bgp.nlri_prefix > a 
(Since there are 2 ip's in conversaion sending different parts of the flag)  
So now we have to just script a code.

#### CODE: 
