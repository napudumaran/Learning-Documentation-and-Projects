Booted the Arch Linux ISO in my VM (Virt-Manager).

Checked that networking worked by pinging archlinux.org — DHCP came through fine.

Made sure I was booted in UEFI mode by looking for /sys/firmware/efi. It was there, so good.

Used lsblk to find my actual disk device — it was /dev/vda. Ignored the loop and rom devices since those are from the live ISO.

Started fdisk on /dev/vda to begin partitioning.

Took a moment to understand:

What sectors are (tiny chunks of disk, usually 512 bytes).

Why partitions start at sector 2048 (to avoid reserved disk areas and for better performance).

The difference between MB (marketing) and MiB (what Linux actually uses).

The purpose of my partitions — EFI for boot, swap for memory overflow, and root for everything else.

Created the first partition for EFI, accepted the default start sector (2048), and set the size to 512M.


