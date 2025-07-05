
First steps are 
```bash
fdisk /dev/vda
```
- `g` -create new GPT
- `n` -new partition
- Enter Key - use default sector (2048)
- `+512M` - give extra 512MiB of space from default sector

First partition is created, setting type `t` for `1` (EFI System) so it can boot from here instead of VM SATA DISKROM

Need to create second partition, which is my Root

- `n` -new partition
- `2` -root partition
- Enter Key - use default sector
- Enter Key - use default sector again since this is my last partition
- `p` -print table to confirm
- `w` -write to quit

Need to format 1st partition by making boot file system fat type (File Allocation Table) and use 32-bit cluster addresses
```bash
mkfs.fat -F32 /dev/vda1
```

Need to format 2nd partition by making root file system Fourth Extended Filesystem type
```bash
mkfs.ext4 /dev/vda2
```
Need to mount root partition
```bash
mount dev/vda2 /mnt
```
root partition is now located in /mnt

Need to make directory to boot, and mount partition 1 to boot
```bash
mkdir /mnt/boot
mount /dev/vda1 /mnt/boot
```
---
I messed up. I want to have a seperate partition for the home directory. I need 3 partitions
---
Fixing my mistakes start here:
Unmounting all my mounted drives
```bash
umount /mnt/boot
umount /mnt
```
Deleting partition 2
```bash
fdisk /dev/vda
```
- `d` -delete partition
- `2` -delete root
- `n` -new partition
- `2` -root partition
- Enter Key - default sector
- `+10G` - Last Sector Value

3rd Partition Steps"
`n` -new partition
`3` -home partition
- Enter Key - default sector
- Enter Key - default sector since its the last one
- `p` -print table to confirm
- `w` -write to changes and save

Format both 2nd and 3rd partitions for file system ext4
```bash
mkfs.ext4 /dev/vda2
and mkfs.ext4 /dev/vda3
```
---

safe to save and reboot here, do not reboot until next checkpoint after this, which is technically not safe until setting up network, or we lose IP with no networking tools

---

Mount all 3 partitions and create directories as needed:
```bash
mount /dev/vda2 /mnt
mkdir /mnt/boot
mount /dev/vda1 /mnt/boot
mkdir /mnt/home
mount /dev/vda3 /mnt/home
```
Good to go now
