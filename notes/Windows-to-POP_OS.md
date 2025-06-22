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
- Linux has a unique naming scheme for devices unlike Windows. Linux names storage devices based on the actual device type, how many of them are present, and how many times they are partitioned. For example, my NVMe drives show as: nvme0n1p1.

  - nvme signals the type of device: Non-Volatile Memory Express.

  - The 0 portion represents how many of these drives are physically present on the system — this being the first one. If I had another, it would show up as nvme1n1p1, nvme2n1p1, and so on.

  - The n1 portion shows the splitting of the physical drive into functionally separate drives, called namespaces. If I wanted to treat the same drive as multiple separate drives, I could split it and end up with nvme0n2p1, nvme0n3p1, etc., depending on how many times I split it. This could allow for things like dual booting, all from one physical device.

  - Finally, the p1 portion represents the partitions — the separation of function within a single drive or namespace. If you partition your boot, recovery, and root file system, you'll see p1, p2, p3, and so on.
