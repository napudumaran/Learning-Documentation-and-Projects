pacstrap /mnt base linux linux-firmware

- Minimal Arch userland (base)
- The Linux kernel (linux)
- Firmware blobs for hardware support (linux-firmware)

Let finish installing Base System packages

genfstab -U /mnt >> /mnt/etc/fstab

- U uses UUIDs (preferred, avoids device name shuffling)
- `>>` appends the generated output into /mnt/etc/fstab
- confirm works by cat /mnt/etc/fstab

switch from live ISO into Arch System

arch-chroot /mnt

setting time to central time
ln -sf /usr/share/zoneinfo/US/Central /etc/localtime

write current time to hardware clock
hwclock --systohc

sed -i '/^#en_US.UTF-8 UTF-8/s/^#//' /etc/locale.gen
That tells sed to:
- Find the line that starts with #en_US.UTF-8 UTF-8
- Remove the #

cat /etc/locale.conf
confirmed

echo "GhettoKali" > /etc/hostname

cat <<EOF > /etc/hosts

127.0.0.1   localhost
::1         localhost
127.0.1.1   GhettoKali.localdomain GhettoKali
EOF

bootctl install
- installs systemd-boot to your mounted /boot (which is your ESP)
- Registers a boot entry with the UEFI firmware

check: cat /boot/loader/loader.conf

check: ls /boot

Create arch.conf for boot.
mkdir -p /boot/loader/entries
cat <<EOF > /boot/loader/entries/arch.conf
title   Arch Linux
linux   /vmlinuz-linux
initrd  /initramfs-linux.img
options root=PARTUUID=$(blkid -s PARTUUID -o value /dev/vda2) rw
EOF

Create password:
passwd
-enter password

exit

umount -R /mnt

reboot

force power off, take SATA CDROM off from first boot device, put VirtIO Disk back on top.

test VM, turn back on
username is root
password is what was set
