# Arch Linux Virtual Machine Install 

NOTE: This documentation assumes you've already downloaded the ISO — whether by torrent or direct HTML. (If not, you can grab it from the official Arch Linux website.)
A quick write-up for downloading the ISO can be found here → [Full Breakdown](/notes/expanded/HTML&Torrents_HowTo.md)

Click edit tab top left > preferences > enable XML editiing for UEFI boot setup stuff cause of NVRAM emulation
File tab > New Virtual Machine > Local install media > browse for iso location and choose
best place to store ISOs is /var/lib/libvirt/images

forward > set memory and cpu settings > dont worry about changing default settings unless need more virt disk image space > click customize config then click finish. Network selection is good default.

---

I did UEFI boot so, this portion is for UEFI. 
Chipset needs to be Q35
Firmware needs to be UEFIx86_64 with OVMF_CODE_4M.fd
Should have came with OVMF install from notes in virt manager install in directory `usr/share/OVMF/`

Click apply

virt-manager doesnt have gui for NVRAM file location to emulate that NVRAM chip, need to add via XML, which is on the right side of details tab.
About 14 lines down in XML file should be <loader> entry. Need to put <nvram> entry. Virt-manager install should have covered what file and where the file is for that for the UEFI boot.
Mine looks like this:
   <loader readonly="yes" type="pflash">/usr/share/OVMF/OVMF_CODE_4M.fd</loader>
    <nvram>/var/lib/libvirt/qemu/nvram/OVMF.md</nvram>

Click apply 
    
 UEFI boot instructions end here

 ---

Go to SATA CDROM and go to xml again. Click in and press space somewhere and then put delete or revert the xml exactly how it was found. This just makes the SATA CDROM path persistent so when the VM is created and you decide to take a break and walk away and restart, the VM still boots off the CDROM since virt-manager likes to disassociate the file path after the first bootup everytime.

Click apply

Click begin installation

VM works, and should boot, even when restarting the vm for whatever reason. Also should save UEFI boot settings too
