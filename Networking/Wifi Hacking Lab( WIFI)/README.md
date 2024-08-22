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
        iwconfig wlan0mon channel 11
        sudo mdk4 wlan0mon p -t <MAC> -f <wordlist>
   
                              
