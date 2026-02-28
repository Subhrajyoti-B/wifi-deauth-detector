from scapy.all import *
from collections import defaultdict
import time
import os

INTERFACE = "wlan0mon"
THRESHOLD = 15
TIME_WINDOW = 10

deauth_counter = defaultdict(list)

def log_attack(src, count):
    with open("logs/attacks.log", "a") as f:
        f.write(f"{time.ctime()} | Source: {src} | Frames: {count}\n")

def detect_deauth(packet):
    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype == 12:
            src = packet.addr2
            current_time = time.time()

            deauth_counter[src].append(current_time)

            deauth_counter[src] = [
                t for t in deauth_counter[src]
                if current_time - t <= TIME_WINDOW
            ]

            if len(deauth_counter[src]) >= THRESHOLD:
                print("\nDeauthentication Attack Detected!")
                print(f"Attacker MAC: {src}")
                print(f"Frames: {len(deauth_counter[src])}\n")
                log_attack(src, len(deauth_counter[src]))
                deauth_counter[src].clear()

print("[*] Starting WiFi Deauth Detector...")
sniff(iface=INTERFACE, prn=detect_deauth, store=0)
