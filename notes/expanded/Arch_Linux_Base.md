```bash
pacstrap /mnt base linux linux-firmware
```
- Minimal Arch userland (base)
- The Linux kernel (linux)
- Firmware blobs for hardware support (linux-firmware)

Let finish installing Base System packages

```bash
genfstab -U /mnt >> /mnt/etc/fstab
```
- `genfstab` scans mounted partitions in `/mnt` and generates UUIDs (Uniserval Unique Identifiers)
- `-U` uses UUIDs (preferred, avoids device name shuffling)
- `>>` appends the generated output into `/mnt/etc/fstab`

*Note: UUIDs are important since they gave a filesystem a unique and stable ID, preventing partitions from pointing to the wrong one, and corrupting them.*

confirm works by:
```bash
cat /mnt/etc/fstab
```
Should see partitions and UUID data.

switch from live ISO into Arch System

```bash
arch-chroot /mnt
```

setting time to central time
```bash
ln -sf /usr/share/zoneinfo/US/Central /etc/localtime
```

write current time to hardware clock
```bash
hwclock --systohc
```

```bash
sed -i '/^#en_US.UTF-8 UTF-8/s/^#//' /etc/locale.gen
```
That tells sed to:
- Find the line that starts with #en_US.UTF-8 UTF-8
- Remove the #, which turns the line from a "note-line" to an "actionable line."

Generate the locales:
```bash
locale-gen
```

Create system-wide locale setting in `/etc/locale.conf`
```bash
echo "LANG=en_US.UTF-8" > /etc/locale.conf
```
- We are writing using echo, and writing to the `locale.conf` file.

Test for confirmation:

```bash
cat /etc/locale.conf
```
Should see our system wide local setting as the output

Create hostname for device:
```bash
echo "YourHostNameHere" > /etc/hostname
```
I named mine GhettoKali for reference

```
cat <<EOF > /etc/hosts
```

127.0.0.1   localhost
::1         localhost
127.0.1.1   GhettoKali.localdomain GhettoKali
EOF

```bash
bootctl install
```
- installs systemd-boot to your mounted /boot (which is your ESP)
- Registers a boot entry with the UEFI firmware

check: 
```bash
cat /boot/loader/loader.conf
```
check: 
```bash
ls /boot
```
Create arch.conf for boot.
```bash
mkdir -p /boot/loader/entries
cat <<EOF > /boot/loader/entries/arch.conf
title   Arch Linux
linux   /vmlinuz-linux
initrd  /initramfs-linux.img
options root=PARTUUID=$(blkid -s PARTUUID -o value /dev/vda2) rw
EOF
```
Create password:
```bash
passwd
```
-enter password

exit
```bash
umount -R /mnt
```
reboot

force power off, take SATA CDROM off from first boot device, put VirtIO Disk back on top.

test VM, turn back on
username is root
password is what was set
