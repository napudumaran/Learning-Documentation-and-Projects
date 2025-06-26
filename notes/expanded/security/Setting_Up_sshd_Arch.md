-Check to see if `sshd` is running:

`sudo systemctl status sshd`

-If inactive, set to active and turn on now:

`sudo systemctl enable sshd --now`

The `ufw` we set earlier denied all incoming traffic, so we need to open port 22(SSH) to connect from host terminal

`sudo ufw allow ssh`

Make sure its showing as running:

`sudo ufw status`

22/tcp should be set to [Allow | Anywhere]

find VM Ip using:

`ip a` 

use enp1s0 IP from inet.

On host terminal, connect to VM using:

`ssh YourUsernameHere@YourIPHere`

For example: `Josh@192.168.1.1`

Until we get a static IP, we will have to repeat the process of getting the current inet IP on every reboot of the VM.
