# -*- coding: utf-8 -*-

import threading, time

class Threading_Test() :

	def __init__(self, interval = 1) :
		# type(interval) >> int
		# check interval, in seconds

		self.interval = interval

		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True # Daemonize thread
		thread.start()

	def run(self) :
		while  True :
			# Do something
			print("Doing something important in the background")

			time.sleep(self.interval)

temp =Threading_Test()
while True :
	time.sleep(1)