- Used `nmap` to simulate different types of port scans (SYN, TCP, UDP, and Aggressive scans) against my Arch Linux VM. Broke down how each scan works, what kind of output it produces, and how that output can be interpreted by defenders. This scan was later tied into a Wazuh lab to test detection of recon activity.<br>
  → [Deeper Breadown](/notes/expanded/cyber_tools/NMAP_Writeup.md)

- Used `ncat` to simulate raw TCP connections, open listening ports, and basic file transfer behavior. Demonstrated how these behaviors are used in reverse shells and data exfiltration, and explained how defenders might detect this kind of traffic. Used in coordination with tcpdump for visibility and logging tests. <br>
  → [Deeper Breakdown](/notes/expanded/cyber_tools/NCAT_Writeup.md)

- Set up Wazuh Manager and Wazuh Agent across separate Arch Linux VMs to simulate a basic SIEM environment. Configured iptables to log incoming Nmap scans, then validated that Wazuh could ingest and display the log events. Used this setup to understand how SIEMs detect recon activity and forward system-level events for triage. <br>
  → [Deeper Breakdown — In progress](/notes/expanded/cyber_tools/Wazuh_Writeup.md)

