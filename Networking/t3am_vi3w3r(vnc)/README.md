# Link: 
https://app.cyber-edu.co/challenges/24de0e00-355b-11eb-ac70-bbefff011eae  

## Solve:  
Seeing the protocol hierarchy we can see lots of protocols.  
The one we are iterested in is vnc(Virtual Network Computing) protocol as it might contain useful information since it transfers mouse and keyboard input from one computer to another.  
Filtering out the vnc packets we see that the traffic is majorly in 2 ports--- 5900 and 33540  
Following the tcp stream of these we get the flag after removing the null bytes .  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/8b2b6fdc-1d76-4672-ba65-46ca1397ef35)
