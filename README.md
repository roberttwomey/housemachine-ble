# housemachine-ble
Bluetooth Low Energy interface for minew E-8 beacons for housemachine project

## Setup
Runs on raspberry pi. Testing on raspberry pi 4. 

Install [bluepy](https://github.com/IanHarvey/bluepy) and sqlite.

```
sudo apt-get install python3-pip libglib2.0-dev
sudo pip3 install bluepy
sudo apt-get install sqlite
```

### Beacon Configuration
Disable unnecessary beacon slots (for instance iBeacon), according to this guide: [https://reelyactive.github.io/diy/minew-e8-config/](https://reelyactive.github.io/diy/minew-e8-config/)

Enable motion triggered event for ACCelerometer slot. I turn on triggering, with a duration of 1 second. This means that sensortag will broadcast accelerometer at 100ms for 1second after a qualifying motion event.

## Usage
To run one time type (bluepy has to be run as root):

`sudo python3 blescanner.py`

__To set Up Persistent Service__

1. Create a service file like the following, _blescanner.service_:
```
[Unit]
Description=Runs python based event logger after boot
After=syslog.target network.target

[Service]
Type=forking
ExecStart=/home/pi/housemachine-ble/textlog/launch_blescanner.sh

[Install]
WantedBy=multi-user.target
```

2. copy the service file to _/etc/init/_:

```console
sudo cp blescanner.service /lib/systemd/system
```

3. enable and start

```console
sudo systemctl enable blescanner.service
sudo systemctl start blescanner.service
```

4. stop
```console
sudo systemctl stop blescanner.service
```

## Info
See [this page](https://reelyactive.github.io/advlib/), and select __Minew I7 (Accelerometer)__, to see how the acceleration is packed into the advertising packet.

__E8 and i7 Accelerometer Beacon__

| Byte(s) | Hex String   | Description                         |
|--------:|:-------------|:------------------------------------|
| 0       | a1           | Frame type                          |
| 1       | 03           | Product model                       |
| 2       | 64           | Battery level in percent            |
| 3-4     | 00d7         | Acceleration in X-axis (signed 8.8) |
| 5-6     | 0087         | Acceleration in Y-axis (signed 8.8) |
| 7-8     | fffe         | Acceleration in Z-axis (signed 8.8) |
| 9-14    | 5705a03f23ac | MAC address                         |

from [https://github.com/reelyactive/advlib](https://github.com/reelyactive/advlib)
