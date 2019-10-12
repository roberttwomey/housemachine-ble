from bluepy import btle
 
print("Connecting...")
dev = btle.Peripheral("AC:23:3F:A2:2B:16")
 
print("Services...")
for svc in dev.services:
    print(str(svc))


uuids = ["7f280001-8204-f393-e0a9-e50e24dcca9e",
         "a3c87500-8ed3-4bdf-8a39-a01bebede295"]

for uuid in uuids:
    serviceUUID = btle.UUID(uuid)
    service1 = dev.getServiceByUUID(serviceUUID)
    for ch in service1.getCharacteristics():
        print(str(ch))
        val = ch[0].read()
        print(val)


