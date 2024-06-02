# File:  
https://github.com/7h4nd5RG0d/Forensics/blob/main/Networking/HID(USB-Mouse%20Drawing)/capture.pcapng
# Solve:  
1) Recognising the relevant data , we see USB capture and USBHUB data --> We need to find the USB device connected to port 7.  
2) Going through the packets in wireshark using filter "frame.len==71" ( Why? since just by scrolling you can see that majority of packets have either length 64 or 71, and by experience the larger packet contains HID data, we need to filter the larger one).
 ![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/13dddca9-c56c-40ab-843c-f3dd5a0525e4)
3) We see in HID data,2 things of interest X(usbhid.data.axis.x) && Y(usbhid.data.axis.y) --> it has to be either a mouse/joystick..(who cares) --> basically an image is being formed.  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/93ce4cc6-d722-4cf8-a51f-41f4fdc88690)
4) Now we need to extract the data, we can use tshark for that.  
**tshark -r capture.pcapng -Y "frame.len==71" -T fields -e "usbhid.data.axis.x" -e "usbhid.data.axis.y" > a.txt**  
**-r** for reading the capture.  
**-Y** for filter used.  
**-T** to set the fields flag.  
**-e** for extracting the required info needed, in this case (usbhid.data.axis.x) && (usbhid.data.axis.y).  
5) Now we need to convert it into an image.
6) We can observe that the coordinates are very small and repetitive meaning we have the displacement and not the exact position of the mouse--> if X=1 and Y=0 then the mouse has moved +1 to X and 0 to Y.  
7) So just write a code for that and we get the flag.
8) Here is the code that I used --> 
9) Keep something in mind after seeing the inital image formed. -->  
a) Image is inverted so -->flip the y axis  
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/9441c8e6-a5f3-4e53-99ab-2c80237dae31)
b) Reading is difficult so scale it accordingly -->Here scale for both is 1.    
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/7da68677-7780-4a1c-b31f-c646fbdbff9b)
10) Also was a challenge to read the flag,but since the task was related to **mouse drawing** it was easy to figure it out.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/d7488dd3-cd59-4836-aec2-48b5c6cd2953)

# Similiar writeup.  
https://github.com/xXLeoXxOne/writeups/blob/main/CrewCTF%202022/Paint.md  
# Similiar USB-Capture but with leftover data dealing here:  
https://github.com/WangYihang/USB-Mouse-Pcap-Visualizer  
**In this packet lengths of 31 are used for transfer of data, adn the capture data can be decoded as (first byte==button state / second byte==X position / third byte==Y position / Fourth position==scroll wheel)**
