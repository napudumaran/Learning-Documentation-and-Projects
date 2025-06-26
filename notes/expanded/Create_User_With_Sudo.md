Need to create user and add to "wheel" group (Supposedly its some old Unix naming for admin group)

`useradd -m -G wheel -s /bin/bash AddYourUsernameHere`

Give your login a password

passwd YourUsernameHere

Change the password for root in case your using the same password by running

`passwd`

We need to give sudo access to our created user account, but we have no text editor currently. We need to install one.

`pacman -Syu nano`

---
IF YOU RESTARTED BEFORE SETTING UP NETWORK CONFIG, YOU WILL HAVE MY PROBLEM HERE! Ignore this if you didnt restart your VM or power off for whatever reason

Edit: I have no network config. I assumed i did because the live IOS was able to ping, but this means we can't do anything until this is fixed → [Network Config Install Notes](/notes/Arch_Network_Config.md)

---

-S means to install
-y means refresh package list
-u means to upgrade outdated packages

We will also need to install the program `sudo` since it doesnt come with arch. 

`pacman -S sudo`

To edit sudo using our text editor, we can run

`EDITOR=nano visudo`

- `visudo` is the name of the helper tool in the sudo package we installed. 

Opening visudo using our text editoor will also give us its own explanation on why we call on visudo, rather than just sudo alone to edit.

We need to uncomment (delete the hastag#) the portion that says 

`## Uncomment to allow members of group wheel to execute any command`

`# %wheel ALL=(ALL:ALL) ALL`

Delet the comment from the wheel section so it looks like this

`%wheel ALL=(ALL:ALL) ALL`

We need to save(ctrl+O), Enter Key to confirm, then exit(ctrl+X)

We will then append our username to the wheel group

`usermod -aG wheel YourUsernameHere`

Test by logging into user profile

`su - YourUsernameHere`

- `su` means to switch user

and then running a sudo command like:

`sudo echo "sudo works"`
