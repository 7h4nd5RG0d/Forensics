# File:
https://github.com/7h4nd5RG0d/Forensics/blob/main/Firmware/Silicon%20Data(%20OpenWRT)/forensics_silicon_data_sleuthing.zip

# Solve:

  
# Something new:
1) OpenWRT( Open Wireless Router): for embedded OS based on linux to route network traffic.  
   It's main components are Linux,util-linux,busybox,musl( C library for linux OS).  
   It features a writeable root file system, enabling users to modify any file.  
   This is accomplished by overlaying a read only compressed SquashFS file system along with a writeable JFFS2 file system using overlayfs.  
   **SquashFS** is a compressed read only FS, while **JFFS2** is a writeable FS.  
   **OverlayFS** is a union-FS that combines 2 directories into 1 unified view.  
   It is used to configure common features like port-forwarding,DNS,DHCP,firewall,routing...
2) binwalk -e <firmware> will give the file system in the firmware.
3) The details of the connection related to the firmware is stored in the JFFS2 FS.
