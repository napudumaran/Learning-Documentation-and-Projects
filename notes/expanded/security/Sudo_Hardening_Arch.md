Open sudo file safely

`sudo EDITOR=nano visudo`

Add line for time allowed between sudo password prompts, changing it to everytime:
- `## Change sudo prompt-time for needing password`
- `Defaults timestamp_timeout=0`

Add line for logging for everytime sudo is used:
- `## Enable sudo logging for auditing`  
- `Defaults logfile=/var/log/sudo.log`

Create the log file for logging:

- `sudo touch /var/log/sudo.log`
- `sudo chown root:root /var/log/sudo.log`
- `sudo chmod 600 /var/log/sudo.log`

Breakdown:
-`touch` creates the file
- `chown` sets ownership, which we set for root
- `chmod` makes readable and writeable by root only

test by running a random sudo command:

-`sudo ls`

Open and read the file:

-`sudo cat /var/log/sudo.log`
