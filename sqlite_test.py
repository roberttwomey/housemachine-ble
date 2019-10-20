#!/usr/bin/python
from __future__ import print_function

from time import gmtime, strftime, sleep, time
from bluepy.btle import Scanner, DefaultDelegate, BTLEException
import sys

import sqlite3

def write():
	conn = sqlite3.connect('example.db')
	c = conn.cursor()

	# Create table
	c.execute('''CREATE TABLE stocks
	             (date text, trans text, symbol text, qty real, price real)''')

	# Insert a row of data
	c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()


def add():
	conn = sqlite3.connect('example.db')
	c = conn.cursor()

	# Never do this -- insecure!
	symbol = 'RHAT'
	c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

	# Do this instead
	t = ('RHAT',)
	c.execute('SELECT * FROM stocks WHERE symbol=?', t)
	print(c.fetchone())

	# Larger example that inserts many records at a time
	purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
	             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
	             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
	            ]
	c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
	conn.close()


conn = sqlite3.connect('example.db')
c = conn.cursor()


for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

conn.close()
