
NOTE: DO NOT USE NMAP ON MACHINES YOU DO NOT OWN OR CONTROL WITHOUT EXPLICIT PERMISSION. DOING SO IS ILLEGAL AND UNETHICAL!

---

To install `nmap` on a Linux Machine with the `pacman` (Package manager) tool, we can use the command:
```bash
sudo pacman -S nmap
```
We can then check to see if `nmap` installed successfully, by using the `nmap` tool with the flag `-V` to get its version. This is the command:
```bash
nmap -V
```
To do our scans safely and legally for our learning, we can simply just scan our loopback address. An explanation of what loopback addresses are can be found here → [Deeper Breakdown Coming Soon]

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
- `sT` -TCP Scan (Testing for TCP services with open ports)
- `sU` -UDP Scan (Testing for UDP services with open ports)
- `SA` -ACK Scan (Testing for firewall behavior)
