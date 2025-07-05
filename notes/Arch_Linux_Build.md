NOTE: DO NOT REBOOT VM until getting to a part mentioned explicitely to reboot. If rebooting the VM, unless starting COMPLETELY OVER, things could happen like mount points being lost, or IP addresses being lost due to DHCP not being configured. There may be fixes made in case you did reboot. You could always start from the beginning as well. → [View Notes — Rough Draft](/notes/Arch_Linux_Install.md)

Booted the Arch Linux ISO in my VM (Virt-Manager).

Checked that networking worked by pinging archlinux.org — DHCP came through fine.

Made sure I was booted in UEFI mode by looking for /sys/firmware/efi. It was there, so good.

Used lsblk to find my actual disk device → it was /dev/vda. Ignored the loop and rom devices since those are from the live ISO.

- Partitioning for Boot, Root, and Home. → [View Notes — Rough Draft](/notes/expanded/Partitioning_Arch_Linux.md)

- Installing the Base System → [View Notes — Rough Draft](/notes/expanded/Arch_Linux_Base.md)

- Security Hardening → [View Notes — Rough Draft](/notes/Arch_Security_Hardening.md)

- Network Configuration → [View Notes — Rough Draft](/notes/Arch_Network_Config.md)

- Setting up KDE for the desktop environment → [View Notes — In progress](/notes/Arch_Linux_KDE_Setup.md)
