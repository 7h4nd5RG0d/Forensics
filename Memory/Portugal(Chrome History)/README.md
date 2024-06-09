# File: 
https://drive.google.com/file/d/1NQA4UzliB4xhNNWipFHlbM58zv_hOpSs/view?usp=drive_web

# Solve:  
1) Since it is a memory dump, we first open it using volatility.
2) Using pslist we see a lot of chrome processes running,which even though not suspicious aids to the description of the question that there was something being searched.
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/1e21edf9-7a50-426c-a65a-55f01537c915)
3) So we get a hint that we need to find the history of chrome in order to get the flag.
4) Volatiltiy already has a plugin built for chrome history --> https://github.com/superponible/volatility-plugins/blob/master/chromehistory.py
5) So just install it(**Remember it is for volatility2 and not volatility3**).
6) Using **python2 vol.py -f ../memdump1.mem --profile=Win10x86 chromehistory --output=csv > chromehistory_output.csv** we get a CSV file of history.
7) Under the title section we see something interesting,and it is the flag......
![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/501953d8-18c9-45de-bcd5-31cfd33c81d9)
8) The flag is in parts--> Like 1-AK means first part is AK and so on..

