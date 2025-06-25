# Switching from Windows 11 to Pop!_OS: Making my new Daily Driver

- Installed Steam via an `apt` install. — [Notes Here](/notes/expanded/Steam_Install_Explained.md)
- IInstalled `flatpak` and used it to install Spotify — [Notes Here](/notes/expanded/Flatpak_Install_Expanded.md)
- emoved the GNOME Keyring login prompt using `seahorse`
- Configured wallpaper to span across multiple monitors (Wallpaper Engine wasn’t working) — [Notes Here](/notes/expanded/Setting_Wallpapers.md)

## What I Learned
- Linux has a unique naming scheme for devices unlike Windows. Linux names storage devices are based on the actual hardware device type, how many of them are present, and how many times they are partitioned. I use NVME, so my storage shows up as nvme0n1p1. My fullwriteup about nvme naming can be seen in this → [Deeper Breakdown](/notes/expanded/NVME_naming_explained_linux.md)
- `flatpak` installations and `apt` (Advanced Package Tool) installations are both very different, and very useful to use. I have incorporated both installation methods as some applications are better sandboxed, and some better installed with system-level access. My full explanation on both `apt` and `flatpak` tools can be found here. → [Deeper Breakdown](/notes/expanded/Flatpak_and_Apt.md)
- `flatpak` applications use a different naming convention compared to apt installs, and they also follow different directory paths when installed. I’ve written a short explanation of how Flatpak names its apps and where they get installed. → [Deeper Breakdown](/notes/expanded/Flatpak_Naming_&_Location.md)
- Shift + Ctrl + U (Unicode) lets me do things like insert arrows `→(u2192)`, em dashes `—(u2014)`, bullet points `•(u2022)` and more for typographic styling and readability on Github, webpages, and Linux OSs.
- How torrents differ from HTML downloads, what torrent I downloaded, and how I used → [Deeper Breakdown coming Soon]
- Using the terminal to manage my audio devices, and ensure they're using the correct quality mode — [Deeper Breakdown coming Soon]
