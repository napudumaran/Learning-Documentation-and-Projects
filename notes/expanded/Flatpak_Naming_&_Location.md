Flatpak names don't get the traditional naming conventions like `apt` installs do. Instead, they follow a special order similar to reverse domain names. The order looks like this:

`org` or `com` . `vendor` . `AppName` 

Examples of applications I've installed are:

- `com.spotify.Client`
- `org.mozilla.firefox`
- `org.gnome.calculator` 

Thes reasoning behind the naming convention is the same as Android Apps, Java packages, and Gnome naming conventions. They ensure that each application name is unique as to avoid naming conflicts.

For example, if multiple applications had the name "calculator", "gnome", or "editor" in them, there would be confusion on which app is owned by who, which then leads to confusions of what app is owned by who.

The naming conventions leads to:
- unique IDs that are much easier to parse through, and obtain the correct application.
- its own isolated configuration directory — meaning the system can identify apps without filenames or commmon pathing.
- easier organization and categorization

You can find the names of application packages by either using https://flathub.org/ or using the terminal to search. (Assuming flatpak and flathub are installed) → [Instructions Provided Here](/notes/expanded/Flatpak_Install_Expanded.md)

To search using the Terminal, you can run:

<code>flatpak search AppNameHere</code>

This would show something in the format of:

[Name]  [Description]  [Application ID]  [Version]  [Branch]  [Remotes]

In case your terminal is too small, or cannot be expanded further, information will be cut off when search with the terminal. You can force the terminal to display all output without chop lines by using:

<code>flatpak search AppNameHere | less -S</code>

This well let you see and cycle through the full output using the left and right arrow keys, uing the `q` key to exit.\

Using the output for the `Application ID`, we can insert that where `AppNameHere` would go and be able to install our application via flatpak.

If we wanted to install the application for all users on the system, we would have to run `sudo`. For example:

<code>sudo flatpak install com.spotify.Client</code>

If we wanted to install the application for us, the individual user, we can install it without `sudo`.

System level installs (sudo level installs for the system) typically install into: `var/lib/flatpak/`

User level installs typically install into: `/.local/share/flatpak`

We can always check where flatpak installs are by running:

<code>flatpak list --user<br>
flatpak list --system</code>

or 

<code>flatpak list --all</code>
