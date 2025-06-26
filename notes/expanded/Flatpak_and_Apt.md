# APT and Flatpak Explained

The tool `apt` is called a system-level package manager. That’s just technical speak for saying that the software is installed directly into your operating system, not just your user account. This means the program can interact with your computer’s files, access shared system resources, and is available to all users on the system. 

For example, if I install Google Chrome using APT, it’s not just for me—any user who logs into the computer can also use it. Chrome will also install any extra system files it needs to run properly (called dependencies), and it will be able to access files across the system just like any other trusted application.

`apt` is also the default package manager (installation tool). Updates and patches on most Linux operating systems depend on the `apt` tool. 

The installation tool `flatpak` is not built into most Linux distros by default. It usually has to be installed separately, often using `apt`.

`flatpak` can be described as an application-level sandboxed package system. That just means:
- It's application-level because the software installs in your user directory, not system-wide. This keeps it isolated and safer.
- It's sandboxed, meaning the app can’t freely access the rest of your system unless you explicitly allow it.
- It’s a package system because it still pulls the software along with everything it needs, including its dependencies (these are bundled in with the insallation, unlike `apt` installs which share them system wide). 

For example, if I install Spotify using flatpak, it only installs for my user. Spotify won’t be able to touch system files or other folders on my computer unless I give it permission. It lives in its own contained space.

Keep in mind: apps on Flathub—the main Flatpak repo—are audited and reviewed before being published. So while the apps are sandboxed, there’s still a layer of trust and moderation behind what you’re installing.

---

So why do I personally use both instead of just relying on one installation method? 
- On Pop!_OS, Spotify is no longer available through `apt`. As of June 24, 2025, I can install it using `flatpak`, but not through the system’s default APT repositories. If I really want the app, I don’t have a choice—I have to use Flatpak.
- Sometimes I want apps to stay completely separate from the rest of my system. I don’t want them installing dependencies globally or scattering config files across my home directory. For example, Steam on Linux often needs compatibility tools like Proton and Wine to run Windows games. But I don’t want those tools touching anything outside of gaming. They’re not part of my everyday setup, and I don’t want leftover files once I’m done. `flatpak` lets me install them in a contained way—no mess, no lingering configurations after I uninstall.
- `flatpak` apps also come with their own pre-defined dependencies, so what I install is known to work out of the box. It won’t break unless I update it manually. That kind of stability is nice when I just want things to work and don’t care about running the latest version.
- `apt`, on the other hand, is easier to live with for core apps I never plan to uninstall—like my web browser. I use Brave, and I want it fully integrated into my system. I don’t want to think about sandbox permissions or updates. `apt` just keeps it up to date with the rest of my system, and that’s exactly what I want for something I use every day.

