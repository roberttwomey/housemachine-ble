# housemachine-ble
Bluetooth Low Energy interface for minew E-8 beacons for housemachine project
## Requirements
Runs on raspberry pi. Testing on raspberry pi 4. 
- install bluepy [https://github.com/IanHarvey/bluepy](https://github.com/IanHarvey/bluepy)
## Info
See this page, and select __Minew I7 (Accelerometer)__, to see how the acceleration is packed into the advertising packet.

###### E8 and i7 Accelerometer Beacon

This is best illustrated with an example using the following input:

    advData: {
      serviceData: { 
        uuid: "ffe1",
        data: "a1036400d70087fffe5705a03f23ac" 
      }
    }

| Byte(s) | Hex String   | Description                         |
|--------:|:-------------|:------------------------------------|
| 0       | a1           | Frame type                          |
| 1       | 03           | Product model                       |
| 2       | 64           | Battery level in percent            |
| 3-4     | 00d7         | Acceleration in X-axis (signed 8.8) |
| 5-6     | 0087         | Acceleration in Y-axis (signed 8.8) |
| 7-8     | fffe         | Acceleration in Z-axis (signed 8.8) |
| 9-14    | 5705a03f23ac | MAC address                         |

Which would add the following property to advData:

    serviceData: {
      uuid: "ffe1",
      data: "a1036400d70087fffe5705a03f23ac",
      minew: {
        frameType: "a1",
        productModel: 3,
        batteryPercent: 100,
        accelerationX: 0.83984375,
        accelerationY: 0.52734375,
        accelerationZ: -0.0078125,
        macAddress: "ac:23:3f:a0:05:57"
      }
    }

from [https://github.com/reelyactive/advlib](https://github.com/reelyactive/advlib)
