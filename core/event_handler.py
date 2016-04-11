#!/usr/bin/python
import sys
import os
import gvar 
from pyinotify import  WatchManager, Notifier, \
ProcessEvent, IN_CREATE,IN_MODIFY

'''
Class EventHandler defines the functions to deal with different file behaviours
'''
class EventHandler(ProcessEvent):
	def process_IN_CREATE(self, event):
		sys.stdout.write( "[INFO]: find new file: %s\n" % os.path.join(event.path,event.name) )
		gvar.thread_inbound.detect_anomaly(event.name)
	def process_IN_MODIFY(self, event):
		sys.stdout.write( "[INFO]: find modified file: %s\n" % os.path.join(event.path,event.name) )
#		global profile_dict 
		gvar.profile_dict = gvar.thread_profile.load_profile()
	
