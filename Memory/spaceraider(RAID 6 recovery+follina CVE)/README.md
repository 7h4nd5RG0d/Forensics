# File: 
https://github.com/7h4nd5RG0d/Forensics/blob/main/Memory/spaceraider(RAID%206%20recovery%2Bfalloni%20CVE)/spaceraider.zip  

# Solve:  
https://github.com/Social-Engineering-Experts/SEETF-2022-Public/blob/main/forensics/spaceraider/solve/solution.md  
## Steps:  
1) Since the given 3 disk images were of same size it hinted towards RAID.
2) Recognition of RAID6-->  
    a) Since block starts from 0x1000 we find that 0x1048 bytes has value=0x06
   ![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/e8cba6e6-a75c-4a57-963b-35d309dce6ca)
    b)0x104C = 0x02 ---> Left symmetric
   ![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/457a9d25-48e9-4e36-bc7c-b42b0bbacdd3)
   c)0x105c = 0x04 ---> Number of disks=4
   ![image](https://github.com/7h4nd5RG0d/Forensics/assets/128285431/06cb860c-c00e-4373-b231-d8b671f47bb4)
3) Repopulating ox1000-0x1003 we get 3 RAID images.
4) Using losetup, allows the system to treat each image file as a physical disk.
   **Commands** --> sudo losetup /dev/loop0 sda1.img  
                --> sudo losetup /dev/loop1 sdb1.img  
                --> sudo losetup /dev/loop2 sdc1.img
5) Test it using sudo losetup -l
6) Then assemble the disk using mdadm command --> **sudo mdadm --assemble --force --run /dev/md0 /dev/loop0 /dev/loop1 /dev/loop2**
7) Check status using --> **cat /proc/mdstat**
8) Mount the disk --> **sudo mount /dev/md0 /mnt**
9) **cd /mnt**
10) You get the MoM.docx, which using command **rg** we can get the link.


## Something new:  
1) RAID recognition --> https://raid.wiki.kernel.org/index.php/RAID_superblock_formats
2) Why and how RAID is used --> https://www.geeksforgeeks.org/raid-redundant-arrays-of-independent-disks/
3) Follina (CVE-2022-30190) --> https://www.kaspersky.com/blog/follina-cve-2022-30190-msdt/44461/
4) mdadm command --> https://www.golinuxcloud.com/mdadm-command-in-linux/  
    
