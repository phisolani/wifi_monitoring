# WiFi Monitoring Framework

This project is designed to perform monitoring on WiFi enabled wireless devices. The setup comprises several Wireless Termination Points (WTPs) and a single Access Controller (AC).

The installation procedure is written below:

## On the WTPs:

Clone the git repository:
```
git clone https://github.com/phisolani/wifi_monitoring.git
```

Go to the folder:
```
cd wifi_monitoring
```

Run the installation bash script:
```
sudo ./install.sh
```

Edit configs/wtp_settings.ini to configure your wireless interface to be monitored and other parameters. 
Also, check if your interface is up with:
```
sudo ifconfig
```

Then, run the live capture application and start collecting WiFi statistics:
```
run sudo python capture/live_capture.py
```