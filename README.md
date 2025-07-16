# Wireless-Deauthentication-Attack
Simulated a wireless DoS attack by sending deauth frames to disconnect clients from Wi-Fi networks.  Captured and analyzed 802.11 traffic, identified WPA/WPA2 vulnerabilities, and explored mitigation techniques in a controlled lab environment. 
# Wireless Deauthentication Attack Simulation

This project simulates a **Wi-Fi deauthentication denial of service (DoS) attack** to demonstrate wireless security vulnerabilities and testing techniques in a controlled lab environment.

---

## 📝 Project Description

In this project, we:

- **Simulated a wireless DoS attack** by sending deauthentication frames to disconnect clients from a Wi-Fi network.
- **Captured and analyzed 802.11 traffic** to understand the behavior of management frames.
- **Identified WPA/WPA2 vulnerabilities** related to unprotected management frames.
- **Explored mitigation techniques** like 802.11w Management Frame Protection in a controlled lab setup.

---

## ⚙️ Tools & Technologies Used

| Tool/Tech | Purpose |
| --- | --- |
| Kali Linux | Penetration testing OS |
| Aireplay-ng | Injecting deauth frames |
| Airodump-ng | Capturing Wi-Fi traffic |
| Wireshark | Protocol analysis |
| Scapy (Python) | Crafting and sending custom deauth frames |
| Alfa Wi-Fi Adapter | Packet injection and monitoring |
| IEEE 802.11 Protocols | Wireless standards understanding |
| WPA2 | Encryption protocol tested |

---

## ⚠️ Legal Disclaimer

This script and methodology are intended **only for educational purposes or authorized penetration testing** on networks you own or have explicit written permission to test.  
**Unauthorized access or attacks on networks is illegal and unethical.** Use responsibly.

---

## 🚀 Setup & Installation

### 1. Enable Monitor Mode

Ensure your Wi-Fi adapter supports monitor mode. Activate it:

```bash
sudo airmon-ng start wlan0
