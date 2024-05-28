# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Steganography/vobla(PDF-TrueType%20Font(Glyphs)/vobla_tales.pdf
  
# Solve: 
https://github.com/Team-Drovosec/sasctf-quals-2024/tree/main/tasks/stego-vobla
1) The font of the pdf is strange.
2) To extract the font, we can use foremost on the pdf.
3) This gives us the font **AAAAAA+PASECA-Regular** which we can load in fontforge.
4) In fontforge, Encoding-->Compact , we see the UNI26F3 glyph.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/13612745-d7d9-4e10-9fab-88a037fadea7)
5) Double clicking on the glyph and zooming in we get the flag.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/c316545e-b722-42e8-96a5-fbe829c5d555)

# Something new: 
1) otf,ttf can be converted to ttx formats,which is XML format using **ttx** command.
  https://fonttools.readthedocs.io/en/latest/ttx.html
