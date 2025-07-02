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

We should get some output that lists the `ncat` version, and some help informtion.

On some linux distrobutions; such as Debian/Ubuntu, Kali, and Fedora, `ncat` is not bundled with the `nmap` package, so we can install it seperately:
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

## How-to scan, and additional types of scanning options:

## Interpreting Output
