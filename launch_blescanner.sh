#!/bin/bash
sleep 5
cd /home/pi/housemachine-ble
/usr/bin/screen -dmS blescanner sudo /usr/bin/python3 /home/pi/housemachine-ble/blescanner.py