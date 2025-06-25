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
- Using the terminal (Assuming flatpak and flathub are installed) → [Instructions Provided Here](/notes/expanded/Flatpak_Install_Expanded.md)

To search using the Terminal, you can run:

<code>flatpak search AppNameHere</code>

This would show something in the format of:

[Name]  [Description]  [Application ID]  [Version]  [Branch]  [Remotes]

If your terminal is too narrow, some columns will be cut off with ellipses (`…`). To prevent that, you can pipethe output through `less -S`:

<code>flatpak search AppNameHere | less -S</code>

This allows horizontal scrolling with the left/right arrow keys. Press `q` to exit.

Using the output from the `Application ID` field, we can insert that where `AppNameHere` would go and install our application via flatpak.

If you want to install the app system-wide (for all users), use `sudo`. For example:

<code>sudo flatpak install com.spotify.Client</code>

If you're only installing it for yourself, don't use `sudo`. For example:

System level installs (sudo level installs for the system) typically install into: `/var/lib/flatpak/`

User level installs typically install into: `~/.local/share/flatpak`

We can always check where flatpak installs are by running:

<code>flatpak list --user<br>
flatpak list --system</code>

or 

<code>flatpak list --all</code>
