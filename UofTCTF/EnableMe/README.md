### File: https://play.uoftctf.org/files/0e668b259a7d8e2030859f171bcded20/invoice.docm?token=eyJ1c2VyX2lkIjoxODMxLCJ0ZWFtX2lkIjoxMTI0LCJmaWxlX2lkIjo3MH0.ZaU_1g.i3Vb611reQW9AYM1muSjWkx__Ww

#### Approach:
Using oledump we get ![image](https://github.com/7h4nd5RG0d/UoftCTF-2024-/assets/128285431/1256e256-bd24-46bd-8386-b9ff5a1c040c) 
This shows that we have macros in ThisDocument
We can get the macros code using olevba
![image](https://github.com/7h4nd5RG0d/UoftCTF-2024-/assets/128285431/158d02f3-a5a4-493b-b0e3-236055b21f9a)  
Converting the VBA code to python we can get the flag by printing v9.  

##### CODE:
https://github.com/7h4nd5RG0d/UoftCTF-2024-/blob/main/CODE.py  


##### FLAG: 
![image](https://github.com/7h4nd5RG0d/UoftCTF-2024-/assets/128285431/c9d6a8cd-60de-453c-84ff-a6b0dd1f3456)  
