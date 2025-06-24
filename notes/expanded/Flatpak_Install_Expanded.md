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
