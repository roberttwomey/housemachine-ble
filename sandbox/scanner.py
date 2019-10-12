#!/usr/bin/python
from __future__ import print_function

from time import gmtime, strftime, sleep
from bluepy.btle import Scanner, DefaultDelegate, BTLEException
import sys

valid_addr = ["ac:23:3f:a2:2b:16"]


def parse_accel(data, addr):
	addr_reversed = "".join(addr.split(":")[::-1])
	if data.startswith('e1ff') and data.endswith(addr_reversed):
		# print(data, addr_reversed)
		return data[4:-11]
	return None

class ScanDelegate(DefaultDelegate):

	def handleDiscovery(self, dev, isNewDev, isNewData):
		# filtering by address
		if dev.addr in valid_addr:
			# print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dev.addr, dev.getScanData())
			for (adtype, desc, value) in dev.getScanData():
				# print("  %s = %s" % (desc, value))
				# print(value)
				accel = parse_accel(value, dev.addr)
				if accel is not None:
					print(accel)
				sys.stdout.flush()

		# no filtering
		# print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dev.addr, dev.getScanData())
		# sys.stdout.flush()


scanner = Scanner().withDelegate(ScanDelegate())

# listen for ADV_IND packages for 10s, then exit
scanner.scan(10.0, passive=True)
