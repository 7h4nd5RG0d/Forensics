# File:
https://github.com/7h4nd5RG0d/Forensics/blob/main/Steganography/Broken%20Converter(FONTS%20-%20odttf)/Assignment-broken.xps
# Solve: 
https://enscribe.dev/blog/sekaictf-2022/forensics-writeup-compilation

# Something new:
1) odttf --> obfuscated ttf files. It is obfuscated by XORing the first 32 bytes of the ttf file with the guid of the file. The rest of the file is normal opentype.  
https://somanchiu.github.io/odttf2ttf/js/demo  
https://en.wikipedia.org/wiki/ODTTF  
2) Open stylistic sets(ss)**[ctrl+shift+F --> lookup]** --> https://learn.microsoft.com/en-us/typography/opentype/spec/features_pt#ssxx
3) In fontforge you can see the rulesets of these ss fonts under their respective subtables.
4) https://fontdrop.info/#/?darkmode=true.
