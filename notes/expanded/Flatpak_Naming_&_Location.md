# Flatpak Application Names and Install Locations explained

Flatpak names don't follow the traditional naming conventions like `apt` installs do. Instead, they follow a special order similar to reverse domain names. The order looks like this:

`org` or `com` . `vendor` . `AppName` 

Examples of applications I've installed are:

- `com.spotify.Client`
- `org.mozilla.firefox`
- `org.gnome.calculator` 

The reasoning behind the naming convention is the same as Android Apps, Java packages, and Gnome naming conventions. They ensure that each application name is unique to avoid naming conflicts.

For example, if multiple applications were named something generic like "calculator" or "editor", it would be unclear which developer or project they belong to. This convention solves that.

This naming conventions leads to:
- Unique IDs that are easier to parse and identify
- Isolated configuration directories (so apps don’t rely on shared paths or filenames)
- Better organization and categorization

You can find application IDs by either: 
- Searching on Flathub.org
- Using the terminal (Assuming flatpak and flathub are installed) → [See setup Instructions](/notes/expanded/Flatpak_Install_Expanded.md)

To search using the Terminal, you can run:

```bash
flatpak search AppNameHere
```

This would show something in the format of:

[Name]  [Description]  [Application ID]  [Version]  [Branch]  [Remotes]

If your terminal is too narrow, some columns will be cut off with ellipses (`…`). To prevent that, you can pipethe output through `less -S`:

```bash
flatpak search AppNameHere | less -S
```

This allows horizontal scrolling with the left/right arrow keys. Press `q` to exit.

Using the output from the `Application ID` field, we can insert that where `AppNameHere` would go and install our application via flatpak.

If you want to install the app system-wide (for all users), use `sudo`. For example:

```bash
sudo flatpak install com.spotify.Client
```

If you're only installing it for yourself, don't use `sudo`. For example:

```bash
flatpak install --user flathub com.spotify.Client
```
---

Flatpak install locations:
- System-level installs (`sudo`) typically go to: `/var/lib/flatpak/`
- User level installs typically go into: `~/.local/share/flatpak`

We can always check where flatpak installs are by running:

```bash
flatpak list --user
flatpak list --system
```

or 

```bash
flatpak list --all
```
