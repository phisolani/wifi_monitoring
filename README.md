# WiFi Monitoring Framework

This project is designed to perform monitoring on WiFi enabled wireless devices. The setup comprises several Wireless Termination Points (WTPs) and a single Access Controller (AC).

The installation procedure is written below:

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

## On the WTPs:

Edit configs/wtp_settings.ini to configure your wireless interface to be monitored and other parameters. 
Then, run the live capture application and start collecting WiFi statistics:
```
run sudo python capture/live_capture.py
```

## On the ACs

Install the necessary libraries for the visualization app:
```
pip install dash==0.22.0  # The core dash backend
pip install dash-renderer==0.13.0  # The dash front-end
pip install dash-html-components==0.11.0  # HTML components
pip install dash-core-components==0.26.0  # Supercharged components
pip install plotly --upgrade  # Plotly graphing library used in examples
```