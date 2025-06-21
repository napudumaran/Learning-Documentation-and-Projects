sudo apt install virt-manager libvirt-daemon-system qemu-kvm qemu-system ovmf bridge-utils

When installing applications, Linux doesn't just install everything in one "package" like Windows. Instead, it lets you — and often requires you — to choose the specific packages needed to get an application working.

Virt-Manager is the GUI for managing virtual machines. Without this, everything would be terminal-only.

libvirt-daemon-system runs the libvirtd service, which allows VM configuration and interaction through the Virt-Manager GUI.

qemu-kvm enables hardware virtualization so VMs can run fast, and also installs the QEMU runtime.

qemu-system installs the QEMU engine that runs the VMs. It emulates the CPU, memory, and storage needed for a virtual machine.

bridge-utils provides bridged networking, making it possible for the VM to get an IP from my router using DHCP — just like a real machine.

ovmf provides UEFI firmware, making it possible to boot using UEFI instead of being stuck with legacy BIOS booting.

