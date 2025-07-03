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

## How-to use, and the different uses explained:

There are three common uses for `ncat`, which are:
- Connecting to a service(Client Mode)
- Listening for incoming connections (opening a port)
- Transfering files over TCP

Connecting to a service lets you send data to open ports, letting you see banners(open port information) or checking for basic connectivity. This can be done with the command:
```bash
ncat 127.0.0.1 22
```

You can replace the IP with a different target, as well as a different protocol. This command targets the loopback address of our machine, as well as checks to see if port 22 is open. This would display a "banner" which looks like: `SSH-2.0-OpenSSH_10.0.` if port 22 is open.

## Interpreting Output
