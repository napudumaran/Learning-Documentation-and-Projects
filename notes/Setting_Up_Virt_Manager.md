sudo apt install virt-manager libvirt-daemon-system qemu-kvm qemu-system ovmf bridge-utils

When installing applications, Linux doesn't just install everything in one "package" like Windows. Instead, it lets you — and often requires you — to choose the specific packages needed to get an application working.

Virt-Manager is the GUI for managing virtual machines. Without this, everything would be terminal-only.

libvirt-daemon-system runs the libvirtd service, which allows VM configuration and interaction through the Virt-Manager GUI.

qemu-kvm enables hardware virtualization so VMs can run fast, and also installs the QEMU runtime.

qemu-system installs the QEMU engine that runs the VMs. It emulates the CPU, memory, and storage needed for a virtual machine.

bridge-utils provides bridged networking, making it possible for the VM to get an IP from my router using DHCP — just like a real machine.

ovmf provides UEFI firmware, making it possible to boot using UEFI instead of being stuck with legacy BIOS booting.

After everything is installed, it's good practice to enable the libvirtd service to start automatically on boot. This is the service we installed earlier to get Virt-manager to function beyond just a GUI. If we don't do this, we might later get stuck wondering why Virt-Manager isn't working properly. We can do this by running this command.
- sudo systemctl enable libvirtd

Here’s a breakdown on what each word means in this command line
- sudo means “super user do” — it gives admin-level permission.
- systemctl is the startup service manager, similar to Windows’ “Services” tool.
- enable is the command (verb) that tells systemctl to set libvirtd to launch at boot. 

Now that libvirtd is set to start automatically at boot, we still need to start it immediately so it works without needing a reboot. The command is:
- sudo systemctl start libvirtd

Everything here is the same as before, except this time we’re telling systemctl to start the service right now instead of waiting until the next reboot.

