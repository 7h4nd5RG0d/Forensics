# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Networking/pinpoint(%20USB%20interface%20card)/findMyPin.pcap
# Solve:
https://github.com/VuwCTF/writeups/blob/main/DawgCTF25/fwn/pinpoint_1.md

# Something new:
1) ISO 7816 - It is standard for communication with smartcards (SIM cards..)
2) CCID (Chip Card Interface Device) - lets USB devices communicate smartcard messages over USB.
3) The computer sends a Command APDU (C-APDU) and the smartcard repsonds with a (R-APDU)
4) **C-APDU** : ![image](https://github.com/user-attachments/assets/47edca41-a731-4d1e-a369-1c3ebf1540f7)
5) **R-APDU** : ![Screenshot 2025-04-27 025608](https://github.com/user-attachments/assets/94f3508f-f1c2-441a-b7d3-f2e32257a8ce)
   SW1 and SW2 together form the status word that indicates **success**,**error** or something else.

 
