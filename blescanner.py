#!/usr/bin/python
from __future__ import print_function

from time import gmtime, strftime, sleep, time
from bluepy.btle import Scanner, DefaultDelegate, BTLEException
import sys

valid_addr = [
				"ac:23:3f:a2:2b:16",
				"ac:23:3f:a2:2b:0e",
				"ac:23:3f:a2:2b:0f",
				"ac:23:3f:a2:2b:11",
				"ac:23:3f:a2:2b:12",
				"ac:23:3f:ab:e7:49"
				]


# function toDecimal(word) {
#   var integer = parseInt(word.substr(0,2),16);
#   var decimal = parseInt(word.substr(2,2),16) / 256;

#   if(integer > 127) {
#     return (integer - 256) + decimal;
#   }
#   return integer + decimal;
# }

def toDecimal(word):
	integer = int(word[:2], 16)
	decimal = int(word[2:], 16)/256.0
	if integer >= 127:
		return (integer-256)+decimal
	return integer+decimal

def parse_accel(data, addr):
	addr_reversed = "".join(addr.split(":")[::-1])

	# check that we are getting a minew E-8 acceleration broadcast
	if data.startswith('e1ff') and data.endswith(addr_reversed):
		# print(data, addr_reversed)
		uuid = data[2:4]+data[0:2]
		frameType = data[4:6]
		productModel = data[6:8]
		batteryLevel = int(data[8:10], 16)
		accel_x = toDecimal(data[10:14])#float.fromhex(data[10:14])
		accel_y = toDecimal(data[14:18])#float.fromhex(data[10:14])
		accel_z = toDecimal(data[18:22])#float.fromhex(data[10:14])
		addr = "".join([data[22+i:22+i+2] for i in range(0, len(data[22:]), 2)][::-1])
		# print(uuid, frameType, productModel, batteryLevel, accel_x, accel_y, accel_z, addr)
		return (addr, accel_x, accel_y, accel_z, batteryLevel)

	return None

class ScanDelegate(DefaultDelegate):

	def handleDiscovery(self, dev, isNewDev, isNewData):
		# filtering by address
		if dev.addr in valid_addr:
			# print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dev.addr, dev.getScanData())
			for (adtype, desc, value) in dev.getScanData():
				# print("  %s = %s" % (desc, value))
				# print(value)
				accel_data = parse_accel(value, dev.addr)
				if accel_data is not None:
					# addr, accel_x, accel_y, accel_z, battery = accel_data
					print("%s:\t%f\t%f\t%f\t%f" % accel_data)
				sys.stdout.flush()

		# no filtering
		# print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dev.addr, dev.getScanData())
		# sys.stdout.flush()

def main():

	scanner = Scanner().withDelegate(ScanDelegate())

	# listen for ADV_IND packages for 10s, then exit
	# scanner.scan(10.0, passive=True)
	try:
		# scanner.start(passive=True)
		# lasttime = time()
		# scanner.process(1.0)
		while True:
			# do nothing
			# if(time()-lasttime > 1.0):
			scanner.scan(10.0, passive=True)
			print(".", end=" ")
			sys.stdout.flush()
				# lasttime =time()
	except KeyboardInterrupt:
		scanner.stop()
	print("exiting...")


if __name__ == "__main__":
    main()


