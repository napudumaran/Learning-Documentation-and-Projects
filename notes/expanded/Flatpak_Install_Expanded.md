The packaging tool apt doesn’t include Spotify in Pop!_OS’s default repository. This means that we will have to look at another installer to get Spotify. Fortunately, `flatpak` is able to be installed via `apt`.
The command to install flatpak is
<code>sudo apt install flatpak</code>

After installing `flatpak`, we will then need to enable the `flathub` repository, which is basically the Flatpak version of an app store—just like how apt pulls from Ubuntu or Pop!_OS repos. 

`flathub` is disabled by default, so to enable we will run:

<code>flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo</code>

This is the breakdown for the line we are running:
- `flatpak` is the name of the tool we installed, so now we are commanding it to do something by calling on it
- `remote-add` is a sub-command of `flatpak` itself. We are giving `flatpak` the command to add a new remote (aka repository).
- `--if-not-exists` is a flag. This tells Flatpak to only add the remote if it hasn’t already been added. It’s like a safeguard.
- `flathub` is the actual name of the store that flatpak uses.
- `https://flathub.org/repo/flathub.flatpakrepo` is where the flatpak store is located on the web. It’s a link `flatpak` uses to find and download the app list for `flathub`.

After running the command above, we’ve enabled and downloaded the repository for the `flathub` store, which means we can now install Spotify.

One thing you’ll notice when installing apps with `flatpak` is that it’s not as intuitive as `apt`. For example, something like:

<code>sudo apt install Spotify</code>
could work, if Spotify existed in the `apt` repository. But `flatpak` uses a different naming convention for its packages.

To install Spotify with `flatpak`, use:

<code>flatpak install flathub com.spotify.Client</code>

To launch Spotify after installing it, use:

<code>flatpak run com.spotify.Client</code>

If you want to avoid typing the full name every time, you can create a shortcut (alias). This will let you launch Spotify just like an `apt` install would:
To assign the alias, we need to edit our `bashrc` file:

Typically, the file is located at ~/.bashrc, so we can edit it using:

<code>nano ~/.bashrc</code>

and then adding this line all the way at the bottom of the file:

<code>alias spotify='flatpak run com.spotify.Client'</code>

We will then save (`Ctrl+O`,`Enter`), exit (`Ctrl+X`), and then apply the change for our current terminal session using:

<code>source ~/.bashrc</code>

Heres a breakdown of everything we used and touched:
- `nano` is a text editor that runs in our terminal, letting us open and edit files in the terminal itself.
- `~` is shorthand(shortcut) for your home directory. By default, this means /home/YourUserName
- The period in front of the `/.bashrc` file marks that this is a hidden file. 
- `bashrc` stands for “Bash Runtime Configuration” and is a text file run by the Bash shell every time we open a terminal. That’s why our alias will now automatically load in every new terminal session.
- `source` is a command that reads a file line by line in the current terminal session. This lets the terminal apply the changes we just made to the `bashrc` file immediately. Technically, we didn’t need to run <code>source ~/.bashrc</code>; we could’ve just opened a new terminal session instead.

With all of these changes made, we can now open up Spotify just like an `apt` install, using the terminal.
