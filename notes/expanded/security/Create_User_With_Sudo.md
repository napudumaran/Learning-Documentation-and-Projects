Need to create user and add to "wheel" group (Supposedly its some old Unix naming for admin group)
```bash
useradd -m -G wheel -s /bin/bash AddYourUsernameHere
```
Give your login a password
```bash
passwd YourUsernameHere
```
Change the password for root in case your using the same password by running
```bash
passwd
```
We need to give sudo access to our created user account. In case we don't have a text editor for some reason, we can install nano.
```bash
pacman -Syu nano
```
---

Edit: I have no network config. I assumed i did because the live IOS was able to ping, but this means we can't do anything until this is fixed → [Network Config Install Notes](/notes/Arch_Network_Config.md)

---

-S means to install
-y means refresh package list
-u means to upgrade outdated packages

We will also need to install the program `sudo` since it doesnt come with arch. 
```bash
pacman -S sudo
```
To edit sudo using our text editor, we can run
```bash
EDITOR=nano visudo
```
- `visudo` is the name of the helper tool in the sudo package we installed. 

Opening visudo using our text editoor will also give us its own explanation on why we call on visudo, rather than just sudo alone to edit.

We need to uncomment (delete the hastag#) the portion that says 
```bash
## Uncomment to allow members of group wheel to execute any command`
# %wheel ALL=(ALL:ALL) ALL`
```
Delete the comment from the wheel section so it looks like this
```bash
%wheel ALL=(ALL:ALL) ALL`
```
We need to save(ctrl+O), Enter Key to confirm, then exit(ctrl+X)

We will then append our username to the wheel group
```bash
usermod -aG wheel YourUsernameHere
```
Test by logging into user profile
```bash
su - YourUsernameHere
```
- `su` means to switch user

and then running a sudo command like:
```bash
sudo echo "sudo works"
```
You should get an initial message basically saying take great care and consideration when using sudo. That means, it works, along with your message of `sudo works`
