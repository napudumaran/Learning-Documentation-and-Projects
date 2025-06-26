# HTML & Torrent Downloads

This guide explains the difference between traditional direct downloads (HTML) and torrent-based downloads (peer-to-peer), including how to use qBittorrent on POP_OS!

---

## HTML (Direct) Downloads

- Downloads are initiated through a browser or terminal tools like `wget` or `curl`.
- The server sends the file directly to your device as a single continuous stream.
- If the stream breaks or the file is corrupted, you usually have to redownload the whole file.
- Download speed depends on:
  - Server bandwidth
  - Your internet speed
  - Server traffic and congestion
- If the URL or webpage is offline or removed, the download fails.

---

## Torrent (Peer-to-Peer) Downloads

- Torrent downloads use a `.torrent` file or a magnet link to start.
- Your client connects to other users (called peers) using:
  - Trackers (servers that coordinate peers)
  - DHT (Distributed Hash Table – decentralized discovery)
- You download parts of the file from multiple peers simultaneously.
  - More peers = faster download
  - Fewer peers = slower download
- While downloading, your client also uploads parts to others — this is called seeding.
- Torrents require a BitTorrent client — I recommend:

```bash
sudo apt install qbittorrent
```
---
# Using qBittorrent

1. Open qBittorrent.
```bash
qBittorrent
```
2. Click the "Open Torrent" tab.

3. Select your .torrent file or paste a magnet link.

4. Choose the download location and start.

5. The file will download in chunks from peers.

6. Once the download is complete, qBittorrent will switch to "Seeding" mode — sharing your completed file with others.
