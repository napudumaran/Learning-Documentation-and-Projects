Booted the Arch Linux ISO in my VM (Virt-Manager).

Checked that networking worked by pinging archlinux.org — DHCP came through fine.

Made sure I was booted in UEFI mode by looking for /sys/firmware/efi. It was there, so good.

Used lsblk to find my actual disk device — it was /dev/vda. Ignored the loop and rom devices since those are from the live ISO.

Began partitioning for boot, root, and home. — [Notes — Rough Draft](/notes/expanded/Partitioning_Arch_Linux.md)
