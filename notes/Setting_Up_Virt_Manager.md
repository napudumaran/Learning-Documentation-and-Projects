The command to install virt-manager and all necessary packages for our use is:

<code>sudo apt install virt-manager libvirt-daemon-system qemu-kvm qemu-system ovmf bridge-utils</code>

When installing applications, Linux doesn't just install everything in one "package" like Windows. Instead, it lets you — and often requires you — to choose the specific packages needed to get an application working.

`Virt-Manager` is the GUI for managing virtual machines. Without this, everything would be terminal-only.

`libvirt-daemon-system` runs the libvirtd service, which allows VM configuration and interaction through the Virt-Manager GUI.

`qemu-kvm` enables hardware virtualization so VMs can run fast, and also installs the QEMU runtime.

`qemu-system` installs the QEMU engine that runs the VMs. It emulates the CPU, memory, and storage needed for a virtual machine.

`bridge-utils` provides bridged networking, making it possible for the VM to get an IP from my router using DHCP — just like a real machine.

`ovmf` provides UEFI firmware, making it possible to boot using UEFI instead of being stuck with legacy BIOS booting.

After everything is installed, it's good practice to enable the `libvirtd` service to start automatically on boot. This is the service we installed earlier to get Virt-manager to function beyond just a GUI. If we don't do this, we might later get stuck wondering why Virt-Manager isn't working properly. We can do this by running this command.
<code>sudo systemctl enable libvirtd</code>

Here’s a breakdown on what each word means in this command line
- `sudo` means “super user do” — it gives admin-level permission.
- `systemctl` is the startup service manager, similar to Windows’ “Services” tool.
- `enable` is the command (verb) that tells systemctl to set `libvirtd` to launch at boot. 

Now that `libvirtd` is set to start automatically at boot, we still need to start it immediately so it works without needing a reboot. The command is:
<code>sudo systemctl start libvirtd</code>

Everything here is the same as before, except this time we’re telling `systemctl` to start the service right now instead of waiting until the next reboot.

Now, we can start grabbing operating systems and setting them up with virt-manager using legacy boot (BIOS). Note that we did install the `ovmf` package in order to emulate UEFI boot, so in order to emulate modern hardware rather than legacy boot, the instructions are as follows.

We need to create a folder (directory) for `QEMU` (the engine that emulates CPU, memory, and storage) to store and write the virtualized UEFI variables to. UEFI needs a writable location because it stores boot entries and settings — just like on a real motherboard. The typical path is as follows.
<code>/var/lib/libvirt/qemu/</code>
  
We're going to create a new folder there called "nvram", making the full path:
<code>/var/lib/libvurt/qemu/nvram</code>
  
NVRAM is a physical chip on real motherboards where UEFI variables are stored. In our case, we’re emulating that with a file using QEMU.

To create the directory using the terminal, use:
<code>sudo mkdir -p /var/lib/libvirt/qemu/nvram</code>
  
Now that we’ve made that empty directory, we need to place a UEFI template file into it so the VM can write to it — just like real UEFI does. Luckily, when we installed the OVMF package, it gave us a default writable UEFI template file:
<code>/usr/share/OVMF/OVMF_VARS.fd</code>
  
We’ll copy that into our new NVRAM directory:
<code>/var/lib/libvirt/qemu/nvram</code>
  
The command we can use to do this easily is:
<code>sudo cp /usr/share/OVMF/OVMF_VARS.fd /var/lib/libvirt/qemu/nvram/</code>
  
Make note of the copied file name — you’ll need it when setting up your VM’s firmware in Virt-Manager (it’ll ask for this when assigning the NVRAM file for UEFI boot).



