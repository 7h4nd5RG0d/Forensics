### File: https://play.uoftctf.org/files/c1a0ac9cb4002be01190ed6864d7d5de/secret.pdf?token=eyJ1c2VyX2lkIjoxODMxLCJ0ZWFtX2lkIjoxMTI0LCJmaWxlX2lkIjo1OX0.ZaU-dg.3PcX7QyU6qQp3dL6KQLxreC_URE

#### Approach:   
##### 1)Method Using pdftotext-->   
pdftotext a.pdf  
cat a.txt
##### 2)Mathod Using pdfextract-->
pdfextract a.pdf  
cd a.dump  
cd streams  
cat *.dmp |grep -i 'ctf'  

##### FLAG: uoftctf{fired_for_leaking_secrets_in_a_pdf}
