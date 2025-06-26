- Install basic firewall `ufw`(Universal Firewall)

`sudo pacman -S ufw`

- Enable and start firewall service after install

`sudo systemctl enable ufw --now`

- Set basic rules for firewall

- `sudo ufw default deny incoming`
- `sudo ufw default allow outgoing`

- Enable the firewall rules

`sudo ufw enable`

- Confirm status of firewall

`sudo ufw status verbose`
