# Wuzah Client Install on Arch Linux

In order to install the Wuzah client on Arch, we need to install the `yay` tool, which allows us to install the Wazuh client from the AUR(Arch User Repository) with little issue.

We will need to grab up to date "mirrors" which is arch's way of getting servers with the most up to date packages:
```bash
sudo pacman -S reflector
sudo reflector --latest 10 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
```
This lets us get the 10 fastest HTTPS mirrors for our machine.

We will then update our package database, and install the needed dependecies for `yay`:
```bash
sudo pacman -Syyu
sudo pacman -S --needed base-devel git
```
We can clone the `yay` repository into our temp folder:
```bash
sudo cd /tmp
sudo git clone https://aur.archlinux.org/yay.git
```
From here, we can then build and install `yay`:
```bash
sudo cd yay
sudo makepkg -si
```
Install the Wazuh Client:
```bash
sudo yay -S wazuh-agent
```
Enable the Wuzah agent service:
```bash
sudo systemctl enable wazuh-agent
```
We will then grab the IP of our Wuzah Manager host, and input it into the agent's config file. Per the Arch Linux setup guide, I used `nano` as my text editor:
```bash
sudo nano /var/ossec/etc/ossec.conf
```
There will be a section that looks like:
```bash
<server>
  <address>MANAGER_IP</address>
  ...
</server>
```
We will alter the "Manager_IP" to be our Wuzah Manager host IP.

Start the Wazuh agent service:
```bash
sudo systemctl start wazuh-agent
```
Confirm the service is running and working:
```bash
sudo systemctl status wazuh-agent
```
Check to see if auto-enable on boot is on:
```bash
sudo systemctl is-enabled wazuh-agent
```
If not, we can enable it:
```bash
sudo systemctl enable wazuh-agent
```
