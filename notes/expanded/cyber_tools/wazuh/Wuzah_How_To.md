## Wazuh Recon Scan Detection Lab (Abandoned)

After attempting to get Wazuh to log `nmap` reconnaissance scans out of the box, I explored alternative methods including `iptables` and `Suricata` to assist in generating or capturing relevant events. While the agent machine successfully logged scan activity locally, those logs never made it to the Wazuh Manager despite multiple configuration attempts.

After several days of troubleshooting — including log forwarding setups, rule tuning, and kernel-level monitoring, I abandoned the project. The goal was to observe and interpret logs, not to architect and maintain a full-scale SIEM. The overhead quickly took away valuable time from learning about logs and parsing them. 

## What I learned:

- Wazuh does not natively parse `nmap` recon scan output without other logging tools (e.g., `iptables`, `Suricata`, or `journald`).

- Setting up log forwarding is extremely difficult. Even when logs exist locally on an agent, forwarding them requires deep configuration and many edits to config and .xml files. 

- Syslog formats and pipelines are uniquely complex. The issue turns into a: `journald` vs. raw log files vs. firewall output configuration headache.

- Not every lab needs to have a polished professional finish. Some things truly are beyond the scope of self taught, without covering basic foundations first.

## Nmap logging and detection (Agent Side)
```bash
Jul 09 21:42:55 GhettoKali kernel: IPT-LOG: IN=enp1s0 OUT= MAC=52:54:00:df:37:26:52:54:00:7a:08:0a:08:00 SRC=192.168.122.40 DST=192.168.122.205 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=22384 DF PROTO=TCP SPT=45540 DPT=2004 WINDOW=64240 RES=0x00 SYN URGP=0
Jul 09 21:42:55 GhettoKali kernel: IPT-LOG: IN=enp1s0 OUT= MAC=52:54:00:df:37:26:52:54:00:7a:08:0a:08:00 SRC=192.168.122.40 DST=192.168.122.205 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=62655 DF PROTO=TCP SPT=57772 DPT=8701 WINDOW=64240 RES=0x00 SYN URGP=0
Jul 09 21:42:55 GhettoKali kernel: IPT-LOG: IN=enp1s0 OUT= MAC=52:54:00:df:37:26:52:54:00:7a:08:0a:08:00 SRC=192.168.122.40 DST=192.168.122.205 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=40385 DF PROTO=TCP SPT=36294 DPT=10616 WINDOW=64240 RES=0x00 SYN URGP=0
```
These logs were captured from an "Attack Machine" running "SYN" scans from nmap.

Here is a breakdown of the logs:

| Field                 | Meaning                             |
| --------------------- | ------------------------------------|
| `Jul 09 21:42:55`     | Date and time of long entry         |
| `GhettoKali`          | Hostname of the agent               |
| `kernel:`             | Source of the log                   |
| `IPT-LOG:`            | Custom prefix from iptables         |
| `IN=enp1s0`           | Interface the packet entered on     |
| `OUT=`                | Interface the packet exited(blank)  |
| `MAC=...`             | Ethernet MAC address info           |
| `SRC=192.168.122.40`  | "Attacking" machine IP              |
| `DST=192.168.122.205` | Scanned Machine IP (Agent System)   |
| `LEN=60`              | Length of the packet in bytes       |
| `TOS=0x00`            | Type of Service byte                |
| `PREC=0x00`           | Precedence bits                     |
| `TTL=64`              | Time To Live                        |
| `ID=22384`            | Packet ID assigned by sender        |
| `DF`                  | "Don't Fragment" flag               |
| `PROTO=TCP`           | Protocol, which was set for TCP     |
| `SPT=45540`           | Source port                         |
| `DPT=2004`            | Destination port                    |
| `WINDOW=64240`        | TCP window size                     |
| `RES=0x00`            | Reserved bits                       |
| `SYN`                 | Flag being sent to Agent from scan  |
| `URGP=0`              | Urgent pointer value(no value here) |

A short summary of this log can be: <br>
The agent system `GhettoKali` was scanned via its `enp1s0` interface by IP `192.168.122.40`. The scan attempted to connect to TCP port `2004` using a `SYN` packet(`nmap -sS` for stealth scan), likely as part of a probe. The traffic appears malicious due to the use of random high source ports and no ACK/RST flags, suggesting it wasn’t legitimate client activity but a recon attempt.
