Booted the Arch Linux ISO in my VM (Virt-Manager).

Checked that networking worked by pinging archlinux.org — DHCP came through fine.

Made sure I was booted in UEFI mode by looking for /sys/firmware/efi. It was there, so good.

Used lsblk to find my actual disk device — it was /dev/vda. Ignored the loop and rom devices since those are from the live ISO.

- Partitioning for Boot, Root, and Home. — [View Notes — Rough Draft](/notes/expanded/Partitioning_Arch_Linux.md)

- Installing the Base System — [View Notes — Rough Draft](/notes/expanded/Arch_Linux_Base.md)

- Security Hardening — [View Notes — Rough Draft](/notes/Arch_Security_Hardening.md)

- Network Configuration — [View Notes — Rough Draft](/notes/Arch_Network_Config.md)
