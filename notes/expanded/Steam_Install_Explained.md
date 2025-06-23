# NOTE: When I was creating this writeup on June23rd. 2025, the Valve repository was still online, but the GPG key ring was missing from their server, leading to issues with APT installs via POP_OS's repository, and getting the keyring to install from Steam's repository. I am listing multiple methods for install of Steam, and I may create a flatpak version of a Steam installer.

In order to install `steam`, we can typically just run:
<code>sudo apt install steam</code>
and we could but finished, but in case POP_OS's repository fails, we can try another way.

In order to install `Steam` through an `apt` install another way, we will need to get their repository key to download from Valve (the company that made Steam) directly.
What is a repository key, and why can't we just <code>sudo apt install</code> right now and call it a day?
Repositories are centralized storage locations for software packages and meta data. They operate like storefronts such as walmart or academy. They choose what is safe to install just like an app store. 
The issue is that repositories aren't always updated for all packages, and things like Steam aren't always up to date. The good news is, in this case we can just go to Steam's hosted repository for their software.
To do so we will need a repository key, which is given by steam for users to access. Think of this key as like a membership to be able to "shop" in their store, like Costco or Sams Club. 

These official instructions given by steam can be found at https://repo.steampowered.com/steam/

The command is:
<code>cd ~/Downloads && wget 
This is the breakdown of the command.
- `cd` means to change directory, or to change the folder we are in.
- `~` is the shorthand for our home directory. Typically this is home/YourUsernameHere. This is the default home directory for linux users.
- `&&` treats our `cd` command `wget` as two different commands, so we can run this full line without errors for copy and paste ease
- `wget` is short for web get. This is a command telling our terminal to download something from the web.

  
