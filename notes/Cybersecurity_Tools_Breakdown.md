- Used `nmap` to simulate different types of port scans (SYN, TCP, UDP, and Aggressive scans) against my Arch Linux VM. Broke down how each scan works, what kind of output it produces, and how that output can be interpreted by defenders. <br>
  → [Deeper Breadown](/notes/expanded/cyber_tools/NMAP_Writeup.md)

- Used `ncat` to simulate raw TCP connections, open listening ports, and basic file transfer behavior. Demonstrated how these behaviors are used in reverse shells and data exfiltration, and explained how defenders might detect this kind of traffic. <br>
  → [Deeper Breakdown](/notes/expanded/cyber_tools/NCAT_Writeup.md)

- Set up Wazuh Manager and Wazuh Agent across separate Arch Linux VMs to simulate a basic SIEM environment. Configured iptables to log incoming `nmap` scans, then validated that Wazuh would display the log events. Used this setup to understand how SIEMs detect recon activity and forward system-level events for triage. <br>
  → [Deeper Breakdown — Rough Draft](/notes/expanded/cyber_tools/Wazuh_Writeup.md)

