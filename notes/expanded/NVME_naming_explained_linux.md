# NVME naming explained

- Linux has a unique naming scheme for devices unlike Windows. Linux names storage devices based on the actual device type, how many of them are present, and how many times they are partitioned. For example, my NVMe drives show as: `nvme0n1p1`.

  - `nvme` signals the type of device: Non-Volatile Memory Express.

  - The `0` portion represents how many of these drives are physically present on the system — this being the first one. If I had another, it would show up as nvme1n1p1, nvme2n1p1, and so on.

  - The `n1` portion shows the splitting of the physical drive into functionally separate drives, called namespaces. If I wanted to treat the same drive as multiple separate drives, I could split it and end up with `nvme0n2p1`, `nvme0n3p1`, etc., depending on how many times I split it. This could allow for things like dual booting, all from one physical device.

  - Finally, the `p1` portion represents the partitions — the separation of function within a single drive or namespace. If you partition your boot, recovery, and root file system, you'll see `p1`, `p2`, `p3`, and so on.
