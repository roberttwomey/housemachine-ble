#!/bin/bash
sleep 10
cd /home/pi/housemachine-ble
/usr/bin/screen -dmS housemachine /usr/bin/python /home/pi/housemachine-ble/blescanner.py