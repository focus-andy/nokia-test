#! /usr/bin/python
# encoding:utf-8

import os
import sys
import json
import time
import threading
from tools import load_file
from event_handler import EventHandler
from profile import Profile
from inbound import Inbound
import gvar
from pyinotify import  WatchManager, Notifier, \
ProcessEvent, IN_CREATE,IN_MODIFY


if __name__ == "__main__":
	#STEP 1, initialise threads
	gvar.thread_profile = Profile( '../profile/device.profile' )
	gvar.thread_inbound = Inbound( '../data/input/', '../data/output/' )
	gvar.thread_profile.setDaemon(True)
	gvar.thread_inbound.setDaemon(True)

	#STEP 2, initialise profile dictiornay by loading the device profile
	gvar.profile_dict = gvar.thread_profile.load_profile()
	sys.stdout.write( '[TRACE]: load the device profile\n')

	try:
	#STEP 3, run profile thread for updating profile automatically
		gvar.thread_profile.start()
	#STEP 4, detect the historical input files
		gvar.thread_inbound.detect_historical_anomaly()
		sys.stdout.write( '[TRACE]: historical input files are done\n' )
	#STEP 5, detect new input files
		gvar.thread_inbound.start()
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		gvar.thread_profile.stop()
		gvar.thread_inbound.stop()
		sys.stdout.write( '[TRACE]: threads stop successfully\n' )

