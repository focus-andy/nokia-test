#!/usr/bin/python
import threading
import os
import sys
import json
from tools import load_file
from event_handler import EventHandler
from pyinotify import WatchManager, Notifier, \
ProcessEvent, IN_CREATE,IN_MODIFY

class Profile(threading.Thread): 
	def __init__(self, path):
		threading.Thread.__init__(self)  
		self.path = path
		self.thread_stop = False 
		self.wm = WatchManager()
		self.notifier = Notifier(self.wm, EventHandler())

	def run(self): 
		self.wm.add_watch(self.path, IN_MODIFY, rec=True)
		while not self.thread_stop:  
			sys.stdout.write( '[INFO]: thread profile is running...\n' )
			self.notifier.process_events()
			if self.notifier.check_events():
				self.notifier.read_events()

	def stop(self):  
		self.notifier.stop()
		self.thread_stop = True

	def load_profile(self):
		all_text = load_file( self.path )
		if all_text == False:
			sys.stderr.write( "[ERROR]: load profile failed!" )
			return False
		#load all the contents into tempory dictionary
		profile_dict = {}
		for line in all_text:
			profile = json.loads( line.strip() )
			profile_dict[profile['type']] = {'thresholds': profile['thresholds'],
											'window':profile['window']}
		sys.stdout.write( '[INFO]: load the device profile successfully!\n')
		return profile_dict


