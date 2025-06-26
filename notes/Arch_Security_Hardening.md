Need to create a user to stop using root user.
Need to create user and add to "wheel" group (Supposedly its some old Unix naming for admin group)

useradd -m -G wheel -s /bin/bash AddYourUsernameHere

Give your login a password

passwd YourUsernameHere

Change the password for root in case your using the same password

passwd

We need to give sudo access to our created user account, but we have no text editor currently. We need to install one.

pacman -S nano

---

I have no network config. I assumed i did because the live IOS was able to ping, but this means we can't do anything until this is fixed → [Network Config Install Notes](/notes/Arch_Network_Config.md)

---
