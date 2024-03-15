#### Input file: https://cyberheroines.ctfd.io/files/28d8d5f5890e833f41af9cd6b439ec73/BarbaraLiskov.pyc?token=eyJ1c2VyX2lkIjo3MTcsInRlYW1faWQiOm51bGwsImZpbGVfaWQiOjEwfQ.ZXE3aQ.jxGu_6PWMG8UPXTrjKX1s5arYhY  
 Approach: We are given a .pyc file for download, where pyc stands for python compiled file.  
So using linux we can just "cat" out the commnads in the .pyc file and get a base64 encoded string which when decoded gives us the flag.  

#### Flag: chctf{u_n3v3r_n33d_0pt1m4l_p3rf0rm4nc3,_u_n33d_g00d-3n0ugh_p3rf0rm4nc3} 
