# Instructions for a KDE Desktop Install Environment

For an easy copy and paste-like install for KDE, we can run:
```bash
sudo pacman -S plasma sddm konsole dolphin alsa-utils pulseaudio pulseaudio-alsa ttf-dejavu ttf-liberation noto-fonts
```
Here's a break down of everything being installed in this command:
- `plasma` pulls in dozens of packages needed for a functioning desktop environment. This is the "meta-package."
- `sddm` is a GUI that provides the login screen, and manages our user(s) sessions.
- `konsole` This is KDE's official terminal emulator, which allows for customization as well
- `dolphin` This is KDE's default file manager
- `alsa-utils` gives the ability to control hardware volume through `alasmixer`
- `pulseaudio` is the most commonly used Linux sound server application
- `pulseaudio-alsa` allows for alsa apps to work with pulseaudio properly
- `ttf-dejavu` is a complete set of commonly used fonts
- `ttf-liberation` is a set of commonly used microsoft-like fonts (Times New Roman)
- `noto-fonts` allows for unicode abilities like symbols both unicode and non-latin scripts


Important Considerations:
If your using intel CPU, we should considering installing the microcode update package for that hardware:
```bash
sudo pacman -S intel-ucode
```

The AMD CPU package is:
```bash
sudo pacman -S amd-ucode
```
When we begin installing, it will prompt us to choose from a selection of choices. We can just choose the default ones by pressing the `Enter` key.

Once we finish with the installation, we can now enable and start sddm to get into our desktop environment. Run this:
```bash
systemctl enable sddm
systemctl start sddm
```
You should get a login screen, where we can input our password to sign in, and then get an introductory menu from the creators of KDE. 

NOTE: `Konsole` is the name of the terminal in KDE, in case we tried to find it.

To install my recommended browser, brave browser, we can find the console with the search menu (ALT+SPACE) and then typing in konsole and launching it.

We need to update our repositories and install the build tools for the repository.
```bash
sudo pacman -S git base-devel
```
We will then need to install `yay`, which is a Arch User Repository(AUR) helper tool.
```bash
cd /tmp
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

We can then install brave with the following command:
```bash
yay -S brave-bin
```
