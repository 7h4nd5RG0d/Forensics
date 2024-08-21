# Resources: 
https://medium.com/@redfanatic7/car-hacking-the-ultimate-guide-part-i-148040f97d96  
https://medium.com/@redfanatic7/car-hacking-the-ultimate-guide-part-ii-445fe022a07c  
https://medium.com/@redfanatic7/car-hacking-the-ultimate-guide-part-iii-d7edb0630771  
# Tools: 
https://github.com/zombieCraig/ICSim

# Notes:
1) Controller Area Network(CAN):  
   a) allows communication of various ECU's(Engine Control Units).  
   b) The traffic is UDP not TCP.  
   c) It is a multi-master network, i.e, does not require a central controller.  
   d) Central locking system, Engine control module, infotainment system.  
   e) Messages with numericall ylower ID's are given higher preferance, called the priority-based bus arbitration.  
   f) CAN bus consists of 2 different cables(CAN HIGH and CAN LOW), and as it is a bus many devices can be connected to it.  
   g) CAN framework has 3 main parts--> Arbitration Identifier / Data Length Code / Data Field.  
   h) To access CAn bus you must have access to cab diagnostic port(OBD).  
   i) Controls of ICSim--> ![image](https://github.com/user-attachments/assets/4b63e348-5343-4ae6-be55-800635f91317)
   j) 

