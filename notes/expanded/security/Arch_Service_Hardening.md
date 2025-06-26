List all enabled services:

`systemctl list-unit-files --state=enabled`

On base Arch Linux Install, we should only have 8 (9 if you enabled sshd.service for ssh login)

For example:

| Unit File                          | State   | Preset   | Description                       |
|------------------------------------|---------|----------|-----------------------------------|
| auditd.service                     | enabled | disabled | Audit Logging                     |
| getty@.service                     | enabled | enabled  | Gives login on the console        |
| NetworkManager-dispatcher.service  | enabled | disabled | Run scripts on network events     |
| NetworkManager-wait-online.service | enabled | disabled | For networking service on boot    |
| NetworkManager.service             | enabled | disabled | Provided networking (DHCP)        |
| sshd.service                       | enabled | disabled | For VM                            |
| ufw.service                        | enabled | disabled | Firewall                          |
| systemd-userdbd.socket             | enabled | enabled  | Needed for systemd service        |
| remote-fs.target                   | enabled | enabled  | Used for mounting drives          |

Currently knowing how to see running services is good knowledge, but everything is currently safe for a bare bones arch setup.
