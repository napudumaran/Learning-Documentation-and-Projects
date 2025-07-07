# Wazuh Install, Breakdown, and How-to-use

NOTE: You will need both the Wuzah Manager, and the Wuzah Client. The Wuzah manager is not compatible as is with an Arch Linux distro, but is officially compatible with Debian/Ubuntu distros. The Wuzah clent is compatible with Arch Linux.

To begin installing the Wuzah Manager, we will start with getting the GPG key from Wuzahs web server. We can do this by running:
```bash
curl -sO https://packages.wazuh.com/key/GPG-KEY-WAZUH
```
- `-s` turns the download into a silent download
- `-O` keeps the original file name

Convert the GPG key into a useable format for `apt`, and store it:
```bash
gpg --dearmor < GPG-KEY-WAZUH | sudo tee /usr/share/keyrings/wazuh-archive-keyring.gpg >/dev/null
```
Here's a breakdown of the command:
- `gpg` is the GNU privacy guard tool, which handles encryption keys
- `--dearmor` converts keys from ASCII "armored" format into a binary form `apt` can use
- `< GPG-KEY-WAZUH` redirects the contents of the GPG key for `gpg` to use
- `|` take the output of the first command, and runs it through the next command
- `sudo tee` runs `tee`; a tool that writes to files, in "admin mode" 
- `/usr/share/keyrings/wazuh-archive-keyring.gpg` is the directory that holds the third-party `apt` keyrings for Debian/Ubuntu systems
- `>/dev/null` takes unneccesary output, and throws it in a garbage-bin equivalent

In summary: the command creates a keyring file in the right directory and format that `apt` can use from Wuzah's GPG key.

Add the Wuzah repository so `apt` uses packages signed by the key we downloaded previously"
```bash
echo "deb [signed-by=/usr/share/keyrings/wazuh-archive-keyring.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list
```
Here's a breakdown of the command:
- `echo` will print everything in quotes, so we can pipe(`|`) that into the next command
- `deb` indicates the input is a binary package repository
- `[signed-by=/usr/share/keyrings/wazuh-archive-keyring.gpg]` is the key we are refering to
- `signed-by=` indicates what `apt` should trust for this repository
- `https://packages.wazuh.com/4.x/apt/` is the web server of Wuzah's official repository
- `stable` is the release label
- `main` is the component name
- `sudo tee` writes the input from the pipe, into the directory `/etc/apt/sources.list.d/wazuh.list` with admin privileges

This creates a dedicate file for `apt` to securely pull Wuzah packages, which is trustworthy and ensured by the specific key we had downloaded.

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
Wuzah Manager should be showing as active and running, which means we're good to go.

If we want to enable the service on boot, we can run:
```bash
sudo systemctl enable wazuh-manager
```
This saves us having to remember to enable the service each time.
