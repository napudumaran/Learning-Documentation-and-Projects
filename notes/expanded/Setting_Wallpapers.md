To set a wallpaper, you can use GNOME's settings.
Open a terminal and run:

`gnome-control-center`

This will open a GUI, where we can navigate to Desktop > Background, and then either choose a new background or click "Add Picture" in the top right to open the file manager and select our own image.

---

If you have multiple monitors, there's another way to set a wallpaper so that it spans across all monitors, rather than just duplicating on each screen. It's not perfect, but it usually looks better than having the same wallpaper mirrored.

I suggest creating a directory (folder) inside your `Pictures` folder called `Wallpapers`, to store your wallpapers.
Run this in your terminal:

```bash
mkdir ~/Pictures/Wallpapers
```
- `mkdir` means "make directory," or create a new folder. If the directory does not already exist, this will create a folder named `Wallpapers`.

Once we have our picture(s) stored in the `Wallpapers` directory, we can then point to that picture when setting it for our wallpaper.

Running the following in the terminal will set the wallpaper to span:

NOTE: *You will need to set your wallpaper path manually before running the commands provided*

```bash
gsettings set org.gnome.desktop.background picture-uri "file://$HOME/Pictures/Wallpapers/YourWallpaperHere.jpg"
gsettings set org.gnome.desktop.background picture-uri-dark "file://$HOME/Pictures/Wallpapers/YourWallpaperHere.jpg"
gsettings set org.gnome.desktop.background picture-options "spanned"
```

Here's a breakdown of everything we ran in the terminal:
- `gsettings` is a command-line tool that lets us read and write application settings in GNOME's configuration system. This is the non-GUI way of configuring settings.
- `set` is a subcommand that updates or overwrites a setting with a new value.
- `org.gnome.desktop.background` is called a schema — a namespace that groups related settings, kind of like a config section in a file.
- `picture-uri` is the file path to our wallpaper (used in light mode).
- `picture-uri-dark` is the path to the wallpaper used in dark mode.
- `picture-options` is the setting for how the wallpaper is displayed.
- `spanned` is a personal choice that tells GNOME to stretch one wallpaper across all monitors. You can also use other values like `zoom`, `scaled`, or `centered`.

---

If you ever want to revert back to GNOME’s default wallpaper behavior, run this:

```bash
gsettings reset org.gnome.desktop.background picture-uri
gsettings reset org.gnome.desktop.background picture-uri-dark
gsettings reset org.gnome.desktop.background picture-options
```

The new command here — `reset` — just returns a setting back to its default value, like how it was when the OS was first installed.

And thats it.
