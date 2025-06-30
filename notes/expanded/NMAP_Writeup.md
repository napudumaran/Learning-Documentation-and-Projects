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
Simply replace the IP in the field with your loopback address, which by default is the IP provided already.

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

## Why not just use all the scans?

#### "Theoretically, the action of deleting logs will always be recorded, and the action of deleting the log that logs the delete, will always be recorded"

Every action made on or against a system leaves a trace, and leaving a trace is the equivalent of signalling a threat. The caveat is that some people dedicate time and effort to removing as many traces as possible, but when it comes to `nmap`, that’s a different conversation.

With `nmap`, the goal for an attacker is to gather as much information as possible without setting off alarms. This is why we have "stealthy" scans like `-sS` compared to louder scans such as `sT`. Some methods of evading detection even include methods such as the "low and slow" approach, where a single scan is stretched over days or weeks to avoid triggering alerts.

In the game of attack and defense, the best defense ends the attack before it begins, and the best attack meets no defense at all.



