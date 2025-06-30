# Arch Linux Virtual Machine Install 

NOTE: This documentation assumes you've already downloaded the .iso file — whether by torrent or direct HTML. (If not, you can grab it from the [official Arch Linux website](https://archlinux.org/download/).
A quick write-up for downloading the ISO can be found here → [Full Breakdown](/notes/expanded/HTML&Torrents_HowTo.md)

Once the virt-manager GUI is open, the first step we want to do is click edit on the top left tab > preferences > and enable XML editiing since we will need to edit XMLs to be able to get UEFI working. (Virt-Manager doesn't currently support a GUI way of getting a file path to our NVRAM directory)

We will then start on the process of setting up the VM for creation. We will start by clicking the "File" tab in the top left corner > New Virtual Machine > Local install media > then browse for .iso file location wherever it was downloaded to, and choose.

I personally prefer to download .iso files to `/var/lib/libvirt/images`. The directory is made after the libvirt install, so no need to create the directory manually.

After selecting the .iso file, we will continue by clicking forward and setting the memory and cpu settings. The CPU and memory settings aren't too much of an issue at this stage, since its a bare metal arch install. The default values are fine, and we can always change them in the future. 

Once we finish the CPU and Memory settings, we can move on, click customize config, then click finish. 

The current Network configurtion is also good out of the box, but we will test once we finish with the first time .iso bootup.

---

I did UEFI boot so, this portion is for UEFI. I HIGHLY recommended setting up UEFI boot regardless, since BIOS is legacy technology.


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
