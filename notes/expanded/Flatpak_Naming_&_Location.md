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

You can find the names of application packages by either using https://flathub.org/ or using the terminal to search(assuming flatpak and flathub are installed)
