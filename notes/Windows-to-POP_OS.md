# Switching from Windows 11 to Pop!_OS

Edit: I originally listed out everything I did and didn’t do, but I realized that kind of post is boring and unhelpful. So instead of dumping a log, I’m going to document everything I actually did in detail—focusing on what might help others making the same switch.

## How I made POP_OS! My new daily driver
- Installed Steam via an `apt` install. — [Notes Here](/notes/expanded/Steam_Install_Explained.md)
- Installed `flatpak` and then installed Spotify — [Notes Here](/notes/expanded/Flatpak_Install_Expanded.md)
- Deleted the login with password prompt via `seahorse`
- How to set a wallpaper for multiple monitors since I can't get Wallpaper Engine on Steam to work — [Notes to come soon]

## What I Learned
- Linux has a unique naming scheme for devices unlike Windows. Linux names storage devices are based on the actual hardware device type, how many of them are present, and how many times they are partitioned. I use NVME, so my storage shows up as nvme0n1p1. My fullwriteup about nvme naming can be seen in this → [Deeper Breakdown](/notes/expanded/NVME_naming_explained_linux.md)
- `flatpak` installations and `apt` (Advanced Package Tool) installations are both very different, and very useful to use. I have incorporated both installation methods as some applications are better sandboxed, and some better installed with system-level access. My full explanation on both `apt` and `flatpak` tools can be found here. → [Deeper Breakdown](/notes/expanded/Flatpak_and_Apt.md)
- `flatpak` applications use a different naming convention compared to apt installs, and they also follow different directory paths when installed. I’ve written a short explanation of how Flatpak names its apps and where they get installed. → [Deeper Breakdown Coming Soon]
