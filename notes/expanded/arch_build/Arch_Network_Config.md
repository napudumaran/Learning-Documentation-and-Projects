Network manager should have been installed via the live ISO. If not, then the troubleshooting steps are below. General install instructions are provided anyways.

install the networkmanager app package:
```bash
sudo pacman -S networkmanager
```

Install GUI interface for network manager(optional):

```bash
sudo pacman -S networkmanager network-manager-applet
```

enable our network manager service:

```bash
sudo systemctl enable NetworkManager --now
```

reboot, login, and ping archlinux.org to confirm:

```bash
ping archlinux.org
```
---

# Troubleshooting

This section is for in case we dont have network manager working for some reason when we installed it during the `chroot` in our Arch-Linux desktop environment before restart.

After confirming that we lost our internet connection by pinging archlinux.org
`ping archlinux.org` and getting Temporary failure in name resolution, we can now setup DHCP completely manually.

We need to make a DHCP config file completely by scratch

Make the directory

```bash
mkdir -p /etc/systemd/network
```

Find your NIC name with:

```bash
ip link
```

Do not use the `lo` device. Your typically looking for another NIC device name, such as `enp1s0`. These device names are marked with numbers like: `1: lo: <LOOPBACK.....>` or `2. enp1s0: <BROADCAST.....>`.

Manually create the config file for your NIC. We will write using echo, since we dont have any text editors if we never installed them prior to rebooting.

```bash
echo '[Match]' > /etc/systemd/network/20-wired.network
echo 'Name=YourNICDeviceNameHere' >> /etc/systemd/network/20-wired.network
echo '' >> /etc/systemd/network/20-wired.network
echo '[Network]' >> /etc/systemd/network/20-wired.network
echo 'DHCP=yes' >> /etc/systemd/network/20-wired.network
 ```

If your typing it all by hand, just up arrow key and edit the previously used command to make this process quicker.

Enable and restart the needed services.

```bash
systemctl enable systemd-networkd --now
systemctl enable systemd-resolved --now
```

reboot your vm, and then acquire an IP

```bash
ip a
```

try to ping archlinux.org again.

```bash
ping archlinux.org
```

install the networkmanager app package:

```bash
sudo pacman -S networkmanager
```

OR

the GUI-supported network manager(optional):

```bash
sudo pacman -S networkmanager network-manager-applet
```

disable the services that we had to use to get our internet connection temporarily, or it will cause conflicts upon reboot

```bash
sudo systemctl disable systemd-networkd --now
sudo systemctl disable systemd-resolved --now
```

enable our network manager service to take over instead:

```bash
sudo systemctl enable NetworkManager --now
```

Take out our resolv.conf file, and replace it with Network Manager's

```bash
rm /etc/resolv.conf
ln -sf /run/NetworkManager/resolv.conf /etc/resolv.conf
```

reboot, login, and ping archlinux.org to confirm

```bash
ping archlinux.org
```

---

