Open sudo file safely

`sudo EDITOR=nano visudo`

Add two lines to bottom of the file:

- `Defaults timestamp_timeout=0`
- `Default logfiles="/var/log/sudo.log"`

This will remove password grace period for sudo users. Basically, type in password everytime sudo is used. It will also log everytime sudo is used at `/var/log/sudo.log`
