# File: 

## Solve:  
Opening the pdf in the pdfstreamdumper we see that in the last stream there are bytes of jpg(JFIF) as well as zip(PK)  
Extracting them we see that we need a password for the zip file, also the jpg file does not open.  
Opening it in HxD we see that the bytes look like that of a PNG image rather than jpg(IHDR,IDAT,IEND), so correcting the header we get the PNG image. 
unnzipping using the password in png image we get a file not recognisable by linux.  
Viewing the file in a text editor we see that it is of the format of PDF but with some shift.  
So using bruteforce in ROT cipher we see that ROT13 gives the PDF file.  
Again going through the streams, one is of particualr interest, the one with FlatDecode Filter.  
Using 'qpdf' tool we can deocde this data to get the flag.  
