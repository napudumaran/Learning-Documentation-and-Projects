# NCAT Install, Breakdown, and Uses

NOTE: DO NOT USE NCAT ON MACHINES YOU DO NOT OWN OR CONTROL WITHOUT EXPLICIT PERMISSION. DOING SO IS ILLEGAL AND UNETHICAL!

---

# Brief Summary

Ncat is a tool packaged with `nmap` that can send packets to open ports or set up ports to receive packets. This makes it useful for listening for incoming connections, as well as testing and debugging raw TCP/UDP connections.

# Install Steps:

If `nmap` is installed, `ncat` is usually installed along with it. We can check to see if the `ncat` package is installed by using the "help" flag with the `ncat` tool:
```bash
ncat -h
```

We should get some output that lists the `ncat` version, and some help information.

On some Linux distributions; such as Debian/Ubuntu, Kali, and Fedora, `ncat` is not bundled with the `nmap` package, so we can install it separately:
```bash
sudo pacman -Syu
sudo pacman -S nmap
```

If you were on a machine using an `apt` installer, the install command would be:
```bash
sudo apt update
sudo apt install nmap
```

# How, What, and Why:

## How-to use, and the different uses explained:

There are three common uses for `ncat`, which are:
- Connecting to a service(Client Mode)
- Listening for incoming connections (opening a port)
- Transferring files over TCP

---
### Connecting to a service
---

Connecting to a service lets you send data to open ports, letting you see banners(open port information) or checking for basic connectivity. This can be done with the command:
```bash
ncat 127.0.0.1 22
```
You can replace the IP with a different target, as well as a different port. This command targets the loopback address of our machine, as well as checks to see if port 22 is open. This would display a "banner" which looks like: `SSH-2.0-OpenSSH_10.0.` if port 22 is open. That banner is important since it gives valuable information about available services, and possibly if it's outdated and vulnerable. 

---
### Listening for incoming connections
---

Ncat gives the ability to listen to incoming connections by opening ports, and allow for connections to be established. We can open ports with the command:
```bash
ncat -lvp PortNumberHere
```
The flag `-lvp` means:
- `-l` listen for connections
- `-v` writeout active details during the connection(verbose)
- `-p` the option to choose a port

Simply replace "`PortNumberHere`" with an actual port to fill in the option for `-p`.

This way of using `ncat` is useful for testing whether logging programs detect unexpected open ports, and for simulating services during honeypotting or red team exercises, such as setting up reverse shells — a method where shells are created on a listening machine by sending commands to their system. It's similar to throwing a fishing line, and waiting for something to bite.

---
### Transferring files over TCP
---

File transfer with `ncat` is not encrypted or authenticated, but it's so universal and practical that it can be used almost anywhere. This process starts by establishing a TCP connection between two systems, and pushing data through it. 

**Important Note:** *Files are NOT downloaded; it is sent to the listening device through a continuous data stream. This distinction is important because reverse shells exploit similar behavior by forcing connecting systems to run malicious code*

This can be done with the command:
```bash
ncat -lvp PortNumberHere > YourFileHere.txt
```

This sets `ncat` to listen for a connection and saves the incoming file data to "`YourFileHere.txt`". The sending device then connects and streams the file over the TCP connection.  The sending device can send the file by running:
```bash
ncat YourTargetIP PortNumberHere < YourFileHere.txt
```

- Replace "`YourTargetIP`" with the IP of the machine hosting the open port
- Replace "`PortNumberHere`" with the port that was opened by the listening device
- Replace "`YourFileHere.txt`" with a desired file to share

This tool allows the ability to test against data exfiltration, as well as quick movement of tools and data in a stealthy manner. The issue with using this tool; however, is the file transfer is unencrypted and unauthenticated, so for testing purposes, do not use this tool with sensitive information or outside of lab environments even for learning purposes.
