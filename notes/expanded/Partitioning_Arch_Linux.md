
Started fdisk on /dev/vda to begin partitioning.

Took a moment to understand:

What sectors are (tiny chunks of disk, usually 512 bytes).

Why partitions start at sector 2048 (to avoid reserved disk areas and for better performance).

The difference between MB (marketing) and MiB (what Linux actually uses).

The purpose of my partitions — EFI for boot, swap for memory overflow, and root for everything else.

Created the first partition for EFI, accepted the default start sector (2048), and set the size to 512M.

Steps are fdisk /dev/vda > g -create new GPT > n -new partition > use default sector (2048) > give extra 512MiB of space (+512M)

First partition is created, setting type `t` for `1` (EFI System) so it can boot from here instead of VM SATA DISKROM

Need to create second partition, which is my Root

n -new partition > 2 -root system > use default sector > use default sector again since this is my last partition > p -print table to confirm > w -write to quit

Need to format 1st partition by making boot file system fat type (File Allocation Table) and use 32-bit cluster addresses
mkfs.fat -F32 /dev/vda1

Need to format 2nd partition by making root file system Fourth Extended Filesystem type
mkfs.ext4 /dev/vda2

Need to mount root partition > mount dev/vda2/ /mnt
root partition is now located in /mnt

Need to make directory to boot, and mount partition 1 to boot
mkdir /mnt/boot
mount /dev/vda1 /mnt/boot

---
I messed up. I want to have a seperate partition for the home directory. I need 3 partitions
---
Fixing my mistakes start here:
Unmounting all my mounted drives
umount /mnt/boot
umount /mnt

Deleting partition 2
fdisk /dev/vda > d -delete partition > 2 -delete root > n -new partition > 2 -root partition > default sector > +10G

3rd Partition : n -new partition > 3 -home partition > default sector > default sector since its the last one > p -print table to confirm > w -write to changes and save

Format both 2nd and 3rd partitions for file system ext4
mkfs.ext4 /dev/vda2 and mkfs.ext4 /dev/vda3

---

safe to save and reboot here, do not reboot until next checkpoint after this, which is technically not safe until setting up network, or we lose IP with no networking tools

---

Mount all 3 partitions and create directories as needed:
- mount /dev/vda2 /mnt
- mkdir /mnt/boot
- mount /dev/vda1 /mnt/boot
- mkdir /mnt/home
- mount /dev/vda3 /mnt/home

Good to go now
