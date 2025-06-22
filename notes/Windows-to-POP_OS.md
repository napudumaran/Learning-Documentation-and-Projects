# Switching from Windows 11 to Pop!_OS

## 📅 Date
June 2025

## 🎯 Why I Did This
I wanted to move away from Windows 11 for good and make Linux my daily driver. The goal was to get comfortable with the terminal and understand how computers work underneath all the Microsoft control and handholding.

## 💻 System Details
- Main desktop PC
- Used USB flash drive to install Pop!_OS NVIDIA (I am using NVIDIA hardware and need compatibility)
- Full disk encryption (LUKS)

## 🛠️ What I Did
1. Backed up key files from Windows
2. Flashed Pop!_OS ISO using Balena Etcher
3. Installed Pop!_OS with default partitions and LUKS
4. Installed nvidia-driver-575 via Pop!_Shop for my 40-series GPU
5. Installed Steam (via Flatpak)
6. Mounted a second drive for game installs
7. Uninstalled Firefox, installed Brave
8. Removed login keyring via seahorse to skip password prompt
9. Mounted my second NVME drive. 

## 💥 What Broke / What I Fixed
- nvidia-driver-575 broke my display; I had to connect a second monitor to the motherboard, boot into recovery, wipe and reinstall Nvidia drivers manually.
- Wallpaper Engine didn’t work, so I stretched a custom PNG across both monitors using photo editing tools
-Installed compatibilty tools for Steam due to some games not running well on Linux natively. I had to make a special directory via: mkdir -p ~/.steam/root/compatibilitytools.d, on my second driver for Steam games, and then install GE-Proton. I now force combatibility tools for all my games on Steam. I learned those native Windows games use Proton to emulate a Windows environment to work.

## 🧠 What I Learned
- Linux has a unique naming scheme for devices unlike Windows. Linux names storage devices based on the actual device type, how many of them are present, and how many times they are partitioned. My fullwriteup can be seen in this [Deeper Breakdown](/notes/expanded/NVME_naming_explained_linux.md)
