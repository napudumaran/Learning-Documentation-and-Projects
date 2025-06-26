Install audit package

`sudo pacman -S audit`

Enable and start the audit service:

`sudo systemctl enable auditd --now`

Check to see if audit service is running (`auditd`)

`systemctl status auditd`

Audit logs can be located in:

`/var/log/audit/audit.log`

No need to configure ownership and properties of `audit.log` like `sudo.log`. . Audit packages automatically configure the log files.

To test if the audit program is running, we can use command:

`sudo tail -n 20 /var/log/audit/audit.log`

Recap of command is:
- `tail` means to show the end of a file
- -`n 20` lets us see the last 20 lines
