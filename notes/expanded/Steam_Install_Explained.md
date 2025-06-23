On most systems, installing Steam is as simple as:
<code>sudo apt install steam</code>

But if Pop!_OS’s default method fails, we can add Steam’s repository directly and install it through APT ourselves.

---

If the default method fails, we can install Steam by adding Valve’s repository manually. We will need to get their repository key to download from Valve (the company that made Steam) directly.
What is a repository key, and why can't we just <code>sudo apt install</code> right now and call it a day?

Repositories are centralized storage locations for software packages and metadata. Think of them like software storefronts — similar to Walmart or an app store.

The issue is that repositories aren't always updated for all packages, and things like Steam aren't always up to date. The good news is, in this case we can just go to Steam's hosted repository for their software.
To do so we will need a repository key, which is given by steam for users to access. Think of the key like a membership card — it gives your system permission to “shop” from that repository, just like getting into Costco or Sam’s Club.

The official instructions for adding Valve’s repository are located here: https://repo.steampowered.com/steam/
But again, the command below currently fails...
This is the breakdown of the command I had mentioned under the "NOTE:" in the beginning.
- `cd` means to change directory, or to change the folder we are in.
- `~` is the shorthand for our home directory. Typically this is home/YourUsernameHere. This is the default home directory for linux users.
- `&&` runs two commands in sequence — only running the second command `wget` if the first command `cd` succeeds
- `wget` is a command-line tool used to download files from the web. People often think of it as “web get” — not its official name, but a helpful memory trick.
- `https://repo.steampowered.com/steam/archive/stable/steam.gpg` is the official GPG key file that valve provides to download their repository key.

All of this will change current directory to your downloads file on your user account, and then download that key into it.

Once the keyring is in our Downloads folder, we can then transfer that GPG key into our repository keyrings folder. The command to do so is:
<code>sudo mv ~/Downloads/NameOfFileHere /usr/share/keyrings/NameOfFileHere</code>

This is the breakdown of the command:
- `sudo` means super user do. Its the equivalent of doing something with administrative controls.
- `mv` means to move. This can also we used to rewrite the name of files by just taking the orignal name of the file and its path, into the same or different folder, with a different file name.
- `/usr/share/keyrings/` is the file path where GPG keys are stored for use.

We will then run:
<code>sudo apt update</code> and
<code>sudo apt install steam</code>

That’s it — Steam should now be installed and working from Valve’s own repository.

