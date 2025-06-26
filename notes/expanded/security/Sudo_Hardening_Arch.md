Open sudo file safely

`sudo EDITOR=nano visudo`

Add line for time allowed between sudo password prompts, changing it to everytime:
- `## Change sudo prompt-time for needing password again`
- `Defaults timestamp_timeout=0`

Add line for logging for everytime sudo is used:
- `## Enable sudo logging for auditing`  
- `Defaults logfile=/var/log/sudo.log`

