# Switching from Windows 11 to Pop!_OS

## 📅 Date
June 2025

## 🎯 Why I Did This
I wanted to move away from Windows 11 for good and make Linux my daily driver. The goal was to get comfortable with the terminal and understand how computers work underneath all the Microsoft control and hand holding.

## 💻 System Details
- Main desktop PC
- Used USB flash drive to install Pop!_OS NVIDIA (I am using NVIDIA hardware and need compatibility)
- Full disk encryption (LUKS)

## 🛠️ What I Did
1. Backed up key files from Windows
2. Flashed Pop!_OS ISO to USB using Balena Etcher
3. Installed Pop!_OS with default partition layout and LUKS encryption
4. Installed Nvidia-Driver-575 via Pop_Shop! Due to 40 series Nvidia card compatibility
6. Installed Steam via: sudo apt install steam
7. Mounted the second drive for Steam game installs
8. Uninstalled firefox and replaced default browser with Brave Browser. 
9. Deleted the keyring for login on Linux via seahorse application to get my desktop to stop prompting for password on login everytime

## 💥 What Broke / What I Fixed
- Installing the Nvidia-Driver-575 broke my display, and I had to connect a monitor into the motherboard, boot up a recovery terminal, wipe the corrupted Nvidia driver install from the main OS, reinstall, and reboot. I have to use commands such as chmod.
- Wallpaper engine in steam doesn't work for Linux, so I had to install photoshop software, download a png I liked from wallpaper sites, and use the photoshop software to stretch the png to span across both of my monitors seemlessly due to resolution issues.
-Installed compatibilty tools for Steam due to games not running well on Linux natively. I had to make a special directory via: mkdir -p ~/.steam/root/compatibilitytools.d, on my second driver for Steam games, and then install GE-Proton. I now force combatibility tools for all my games on Steam.

## 🧠 What I Learned
- Even GUI-first Linux like Pop!_OS teaches you a lot under the hood.
- Linux feels lighter, faster, and less bloated than Windows. I didn't get stuck at a login screen for Microsoft account, and it comes with less bloatware.
- Google is now my best friend because if I want an additional feature, I usually have to look and see whats available, unlike Windows which gives you the feature, but only that one.
