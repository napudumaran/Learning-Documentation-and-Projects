NOTE: DO NOT REBOOT VM until getting to a part mentioned explicitely to reboot. If rebooting the VM, unless starting COMPLETELY OVER, things could happen like mount points being lost, or IP addresses being lost due to DHCP not being configured. There may be fixes made in case you did reboot. You could always start from the beginning as well. <br>
→ [View Notes — Rough Draft](/notes/Arch_Linux_Install.md)

Booted the Arch Linux ISO in my VM (Virt-Manager).

Checked that networking worked by pinging archlinux.org — DHCP came through fine.

Made sure I was booted in UEFI mode by looking for /sys/firmware/efi. It was there, so good.

Used lsblk to find my actual disk device → it was /dev/vda. Ignored the loop and rom devices since those are from the live ISO.

---
1. Partitioning for Boot, Root, and Home. <br>
→ [View Notes — Rough Draft](/notes/expanded/arch_build/Partitioning_Arch_Linux.md)
---
2. Installing the Base System <br>
→ [View Notes — Rough Draft](/notes/expanded/arch_build/Arch_Linux_Base.md)
---
3. Security Hardening <br>
→ [View Notes — Rough Draft](/notes/Arch_Security_Hardening.md)
---
4. Network Configuration <br>
→ [View Notes — Rough Draft](/notes/expanded/arch_build/Arch_Network_Config.md)
---
5. Setting up KDE for the desktop environment <br>
→ [View Notes — Rough Draft](/notes/expanded/arch_build/Arch_Linux_KDE_Setup.md)
---
