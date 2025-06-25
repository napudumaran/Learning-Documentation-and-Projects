# HTML(Direct) Downloads
- The browser or terminal (through commands such as `wget` or `curl`) sends out a request to the webpage.
- The server sends file to you via a continuous stream, which if broken or corrupted leads to a redownload of the whole thing
- Download speeds depend on the web server bandwidth, your internet connection, and the traffic of the web server.
- No URL or webpage means no download

# Torrent (Peer to Peer) Downloads
- opens via a torrent file or magnet link
- connects to peers (other PCs) via trackers or DHT (Distrubuted hash table) to download their same file
- more peers means faster download, less means slower download.
- You also upload your file like how you download it, which is called seeding
- needs a bittorrent client (I use qBittorrent)
- ISPs sometimes don't like them and will block or slow traffic

Qbittorent is easy to install via:

sudo apt install qbittorrent

How to use:
Open torrent > click file > select/add torrent file (will be wherever bittorrent or magnet link was downloaded to) 

The download now starts from downloading via other peoples systems. When download is down, the status bar will switch to seeding, so you can give back what you downloaded as long as qbittorrent is open
