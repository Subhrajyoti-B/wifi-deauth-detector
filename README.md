# 📡 WiFi Deauthentication Attack Detector

A Python-based **Wireless Intrusion Detection System (WIDS)** that
detects WiFi Deauthentication attacks by analyzing raw 802.11 management
frames in monitor mode.

------------------------------------------------------------------------

## 🚀 Overview

WiFi deauthentication attacks are commonly used in:

-   Evil Twin attacks\
-   Man-in-the-Middle (MITM) setups\
-   WiFi disruption attacks\
-   Credential harvesting

This tool detects abnormal bursts of **Deauthentication (Subtype 12)
frames** in real time and alerts the user when a threshold is exceeded.

------------------------------------------------------------------------

## 🔥 Features

-   Real-time 802.11 packet monitoring\
-   Deauthentication frame detection\
-   MAC-based attack tracking\
-   Time-window threshold analysis\
-   Attack logging system\
-   Lightweight and fast

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python 3\
-   Scapy\
-   802.11 Protocol Analysis\
-   Monitor Mode Interface\
-   Linux Networking Tools\
-   Aircrack-ng (for lab simulation)

------------------------------------------------------------------------

## 🧠 Detection Logic

The detector:

1.  Sniffs raw 802.11 frames in monitor mode\
2.  Filters for:
    -   Frame Type = Management (0)
    -   Subtype = Deauthentication (12)\
3.  Tracks frequency per source MAC address\
4.  Raises alert if frame count exceeds threshold within a defined time
    window

------------------------------------------------------------------------

## 📂 Project Structure

    wifi-deauth-detector/
    │
    ├── main.py
    ├── requirements.txt
    ├── logs/
    │   └── attacks.log
    └── README.md

------------------------------------------------------------------------

## ⚙️ Installation

### 1️⃣ Clone Repository

``` bash
git clone https://github.com/yourusername/wifi-deauth-detector.git
cd wifi-deauth-detector
```

### 2️⃣ Create Virtual Environment (Recommended)

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 📡 Usage

### Step 1: Enable Monitor Mode

``` bash
sudo airmon-ng start wlan0
```

### Step 2: Run Detector

``` bash
sudo python3 main.py
```

### Step 3: Simulate Attack (Lab Only)

``` bash
sudo aireplay-ng --deauth 20 -a <BSSID> wlan0mon
```

If attack is detected:

    🚨 Deauthentication Attack Detected!
    Attacker MAC: XX:XX:XX:XX:XX:XX

------------------------------------------------------------------------

## 📝 Logs

Detected attacks are stored in:

    logs/attacks.log

Log Format:

    Timestamp | Source MAC | Frame Count

------------------------------------------------------------------------

## 🎯 Resume Description

Developed a Python-based Wireless Intrusion Detection System (WIDS)
capable of detecting WiFi deauthentication attacks through real-time
802.11 management frame analysis using Scapy in monitor mode.

------------------------------------------------------------------------

## ⚠️ Disclaimer

This project is intended for:

-   Educational purposes\
-   Authorized security testing\
-   Personal lab environments only

Unauthorized wireless testing is illegal.

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Channel hopping support\
-   Evil Twin detection\
-   Signal strength anomaly analysis\
-   JSON/CSV export\
-   Web dashboard\
-   Raspberry Pi portable IDS version

------------------------------------------------------------------------

## 👨‍💻 Author

Subhrajyoti Bhowmik\
Cybersecurity Enthusiast \| Ethical Hacking \| Wireless Security
