NOTE: As of June 23rd, 2025, the official Steam GPG key is missing from Valve’s server. The command below is what should allow us to download it:
<code>cd ~/Downloads && wget https://repo.steampowered.com/steam/archive/stable/steam.gpg</code>

...but currently results in a 404 error. Valve has not updated their documentation, and this is causing installation failures for new users trying to set up Steam via APT. We will cover multiple ways to install Steam if this kind of issue occurs.

In order to install `steam`, we can typically just run:
<code>sudo apt install steam</code>

If Pop!_OS’s default method fails, we can add Steam’s repository directly and install it through APT ourselves.

In order to install `Steam` through an `apt` install another way, we will need to get their repository key to download from Valve (the company that made Steam) directly.
What is a repository key, and why can't we just <code>sudo apt install</code> right now and call it a day?

Repositories are centralized storage locations for software packages and meta data. They operate like storefronts such as walmart or academy. They choose what is safe to install just like an app store. 

The issue is that repositories aren't always updated for all packages, and things like Steam aren't always up to date. The good news is, in this case we can just go to Steam's hosted repository for their software.
To do so we will need a repository key, which is given by steam for users to access. Think of this key as like a membership to be able to "shop" in their store, like Costco or Sams Club. 

These official instructions given by steam can be found at https://repo.steampowered.com/steam/

The command is:
<code>cd ~/Downloads && wget https://repo.steampowered.com/steam/archive/stable/steam.gpg</code>
This is the breakdown of the command.
- `cd` means to change directory, or to change the folder we are in.
- `~` is the shorthand for our home directory. Typically this is home/YourUsernameHere. This is the default home directory for linux users.
- `&&` treats our `cd` command `wget` as two different commands, so we can run this full line without errors for copy and paste ease
- `wget` is a tool that downloads files from the web, and people often refer to it as web get. Thats not the name of the tool, but it does make it easier to remember what the command `wget` does.
- `https://repo.steampowered.com/steam/archive/stable/steam.gpg` is the official GPG key file that valve provides to download their repository key.

All of this will change directory to your downloads file on your user account, and then download that key into it.

  
