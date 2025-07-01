# NMAP Install, Breakdown, and Uses

NOTE: DO NOT USE NMAP ON MACHINES YOU DO NOT OWN OR CONTROL WITHOUT EXPLICIT PERMISSION. DOING SO IS ILLEGAL AND UNETHICAL!

---

# Brief Summary

`nmap` is a tool that doubles as a network discovery tool (hence the name network map, or `nmap` for short) and security auditing tool. Created by Gordan Lyon, it helped network engineers and sysadmins find hosts, running services, and open ports. 

# Install Steps:

To install `nmap` on a Linux Machine with the `pacman` (Package manager) tool, we can use the command:
```bash
sudo pacman -S nmap
```
We can then check to see if `nmap` installed successfully, by using the `nmap` tool with the flag `-V` to get its version. This is the command:
```bash
nmap -V
```
To do our scans safely and legally for our learning, we can simply just scan our loopback address. An explanation of what loopback addresses are, can be found here → [Deeper Breakdown Coming Soon]

# How, What, and Why:

## How-to scan, and additional types of scanning options:

A simple command that sends out SYN packets is:
```bash
nmap -sS 127.0.0.1
```
Simply replace the IP in the field with your loopback address, which by default is the IP provided already. You can also use another IP for a MACHINE YOU OWN.

The breakdown of the command is:
- `-s` is the flag for choosing a scan type option.
- `S` is the option for a SYN scan.

Syn scans, aka "stealth scans" or "half-open scans" are well known scans because of their tendency to not finish the full SYN, SYN/ACK, and ACK handshake process. This sometimes bypasses security logging systems that only log fully established connections, and also comes off as "quieter" because of the unfinished handshake, hence the "half-open" and "stealth" naming attributes.

Other common scanning options include:
- `-sT` -TCP Scan (Testing for TCP services with open ports)
- `-sU` -UDP Scan (Testing for UDP services with open ports)
- `-sA` -ACK Scan (Testing for firewall behavior)

There are many other options which are less commonly used such as:
- `-sN` -Null Scan (Testing for misconfigured legacy firewalls)
- `-sX` -Xmas Scan (Testing for host reactions to abnormal flag combinations)
- `-sF` -FIN Scan (Testing for simple firewalls)

One flag worth noting is `-A`. This flag is the option for an "aggressive" scan, in which the command bundles very "loud" scanning options such as:
- `-O` - OS Detection
- `-sV` - Version Detectionn
- `--script=Default` -Script Scanning (allows nmap to run their built in scanning scripts)
- `--traceroute` -Traceroute (allow for tracing every router between you and a target network)

This scan is "loud" and "aggressive" because of how it sends many unusual packets, which allows for easy detection after use.

## Interpreting Output

When running a command such as: ```sudo nmap -A 127.0.0.1```. generally output will look similar to what is shown below. I will breakdown the output line by line for easy understandng. This will make other commands easier to also break down, since we're using the "aggressive" option.


| Line | Output                                                                                                  |
|------|---------------------------------------------------------------------------------------------------------|
| 1    | [Napu@GhettoKali ~]$ sudo nmap -A 127.0.0.1                                                             |
| 2    | [sudo] password for Napu:                                                                               |
| 3    | Starting Nmap 7.97 ( https://nmap.org ) at 2025-07-01 09:27 -0500                                       |
| 4    | Nmap scan report for localhost (127.0.0.1)                                                              |
| 5    | Host is up (0.000031s latency).                                                                         |
| 6    | Not shown: 999 closed tcp ports (reset)                                                                 |
| 7    | PORT   STATE SERVICE VERSION                                                                            |
| 8    | 22/tcp open  ssh     OpenSSH 10.0 (protocol 2.0)                                                        |
| 9    | Device type: general purpose                                                                            |
| 10   | Running: Linux 2.6.X\|5.X                                                                               |
| 11   | OS CPE: cpe:/o:linux:linux_kernel:2.6.32 cpe:/o:linux:linux_kernel:5 cpe:/o:linux:linux_kernel:6        |
| 12   | OS details: Linux 2.6.32, Linux 5.0 - 6.2                                                               |
| 13   | Network Distance: 0 hops                                                                                |
| 14   | OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/.    |
| 15   | Nmap done: 1 IP address (1 host up) scanned in 1.57 seconds                                             |

- Line 1-2: This is just name of the machine, the command used, and a prompt for my password since we're using a commmand that requires sudo
- Line 3: Nmap version, date, and time
- Line 4: Nmap is listing the scanned target, my loopback address
- Line 5: Latency response from outgoing machine to target machine
- Line 6: Number of ports that did not respond out of the first 1000
- Line 7: Setting up graph information for line 8
- Line 8: What port, state, service, and version was detected
- Line 9: Nmaps "guess" on what the target device is used for
- Line 10: Estimate on OS running, and kernel series
- Line 11: Esimation of OS and software names using CPE identifiers (special strings)
- Line 12: Re-affirmation of precise guesstimate
- Line 13: The number of routers crossed to reach target
- Line 14: Information to report bugs and issues if found during scan
- Line 15: Quick summary of the whole output

## Why not just use all the scans?

#### "*Theoretically, the action of deleting logs will always be recorded, and the action of deleting the log that logs the delete, will always be recorded*"

Every action made on or against a system leaves a trace, and leaving a trace is the equivalent of signalling a threat. The caveat is that some people dedicate time and effort to removing as many traces as possible, but when it comes to `nmap`, that’s a different conversation.

With `nmap`, the goal for an attacker is to gather as much information as possible without setting off alarms. This is why we have "stealthy" scans like `-sS` compared to louder scans such as `sT`. Some methods of evading detection even include methods such as the "low and slow" approach, where a single scan is stretched over days or weeks to avoid triggering alerts.

#### "*In the game of attack and defense, the best defense ends the attack before it begins, and the best attack meets no defense at all.*"



