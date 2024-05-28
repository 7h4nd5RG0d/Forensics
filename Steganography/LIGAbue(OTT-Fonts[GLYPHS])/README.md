# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Steganography/LIGAbue(OTT-Fonts%5BGLYPHS%5D)/chall.otf
# Solve:
https://github.com/TeamItaly/TeamItalyCTF-2023/blob/master/LIGAbue/README.md  

# Something new: 
1) OpenType Programming Language --> https://simoncozens.github.io/fonts-and-layout/features.html
2) otfinfo command for otf files.
3) Tables are present in fonts, of which CFF stores the font glyphs while GSUB is a table used to substitute glyphs with other glyphs following some rules.
4) Table info is stored in .fea format and otf can be converted using ot2fea command in kali.
