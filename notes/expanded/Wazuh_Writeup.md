# Wazuh Install, Breakdown, and How-to-use

NOTE: You will need both the Wuzah Manager, and the Wuzah Client. The Wuzah manager is not compatible as is with an Arch Linux distro, but is officially compatible with Debian/Ubuntu distros. The Wuzah clent is compatible with Arch Linux.

To begin installing the Wuzah Manager, we will start with getting the GPG key from Wuzahs web server. We can do this by running:
```bash
curl -sO https://packages.wazuh.com/key/GPG-KEY-WAZUH
```
- `-s` turns the download into a silent download
- `-O` keeps the original file name

Add the Wuzah repository, after downloading the GPG key:
```bash
echo "deb https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list
```

- The first portion of this command, `echo "deb https://packages.wazuh.com/4.x/apt/ stable main"` is printing everything quotes, so we can pipe it into the next command.
- `|` is what we're using to take the input into the next command
- `tee` takes the input, and writes it out into our specified file
- `/etc/apt/sources.list.d/wuzah.list` is the directory to the file `wuzah.list` where we are writing the wuzah repository link to.

This command lets `apt` know where to get Wuzah packages from.

Update our package list using:
```bash
sudo apt update
```
Install Wuzah Manager from their app repistory:
```bash
sudo apt install wazuh-manager
```
Enable Wuzah Manager once the installation has finished:
```bash
sudo systemctl enable --now wazuh-manager
```
Check the status of Wuzah Manager:
```bash
sudo systemctl status wazuh-manager
```
