install the networkmanager app package, which is GUI based:
- `sudo pacman -S networkmanager`
- `sudo pacman -S networkmanager network-manager-applet`

enable our network manager service:

`sudo systemctl enable NetworkManager --now`

reboot, login, and ping archlinux.org to confirm

`ping archlinux.org`

---

This section is for people who rebooted after first root login, and realized networking wasnt setup, losing our IP upon shutdown, and then not getting a new one upon boot up.

After confirming that we lost our internet connection by pinging archlinux.org
`ping archlinux.org` and getting Temporary failure in name resolution, we can now setup DHCP completely manually.

We need to make a DHCP config file completely by scratch

Make the directory

mkdir -p /etc/systemd/network

Write using echo, since we dont have any text editors installed more than likely.

- `echo '[Match]' > /etc/systemd/network/20-wired.network`
- `echo 'Name=enp1s0' >> /etc/systemd/network/20-wired.network`
- `echo '' >> /etc/systemd/network/20-wired.network`
- `echo '[Network]' >> /etc/systemd/network/20-wired.network`
- `echo 'DHCP=yes' >> /etc/systemd/network/20-wired.network`
 
If your typing it all by hand, just up arrow key and edit the previously used command to make this process quicker.

Enable and restart the needed services.

- `systemctl enable systemd-networkd --now`

- `systemctl enable systemd-resolved --now`

reboot your vm, and then acquire an IP

`ip a`

try to ping archlinux.org again.

`ping archlinux.org`

install the networkmanager app package, which is GUI based:
- `sudo pacman -S networkmanager`
- `sudo pacman -S networkmanager network-manager-applet`

disable the services that we had to use to get our internet connection temporarily:

- `sudo systemctl disable systemd-networkd --now`
- `sudo systemctl disable systemd-resolved --now`

enable our network manager service to take over instead:

`sudo systemctl enable NetworkManager --now`

Take out our resolv.conf file, and replace it with Network Manager's

- `rm /etc/resolv.conf`
- `ln -sf /run/NetworkManager/resolv.conf /etc/resolv.conf`

reboot, login, and ping archlinux.org to confirm

`ping archlinux.org`

---

