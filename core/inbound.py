#!/usr/bin/python
import threading
import os
import sys
import json
import time
from tools import load_file
from event_handler import EventHandler
import gvar
from pyinotify import  WatchManager, Notifier, \
ProcessEvent, IN_CREATE,IN_MODIFY

class Inbound(threading.Thread): 
	def __init__(self, input_path, output_path):
		threading.Thread.__init__(self)  
		self.input_path = input_path  
		self.output_path = output_path  
		self.thread_stop = False 
		self.wm = WatchManager()
		self.notifier = Notifier(self.wm, EventHandler())

	def run(self): 
		self.wm.add_watch(self.input_path, IN_CREATE, rec=True)
		while not self.thread_stop:  
			sys.stdout.write( '[INFO]: thread inbound is running...\n' )
			time.sleep(1)
#			global profile_dict
			self.notifier.process_events()
			if self.notifier.check_events():
				self.notifier.read_events()

	def stop(self):  
		self.notifier.stop()
		self.thread_stop = True

	def detect_historical_anomaly(self):
		history_file_list = []
		new_file_list= os.listdir(self.input_path)
		ret = list( set(history_file_list) ^ set(new_file_list) )
		while len(ret) > 0:
			for item in ret:
				self.detect_anomaly( ''.join(item) )
			history_file_list = new_file_list
			new_file_list= os.listdir(self.input_path)
			ret = list( set(history_file_list) ^ set(new_file_list) )
			
	def detect_anomaly( self, filename = '' ):
		sys.stdout.write( '[INFO]: start detecting file:%s\n' % (filename) )
		all_text = load_file( self.input_path+filename )
		if all_text == False:
			sys.stderr.write( "[ERROR]: load input file failed!" )
			return 

		input_list = []
		for line in all_text:
			inbound_data = json.loads( line.strip() ) 
			events_num = self.get_event_num( inbound_data )
			input_list.append(events_num)

		#sort
		input_list.sort(lambda x,y:cmp(x[1],y[1]), reverse=True)

		#write result to file
		f_write = open( self.output_path + filename, 'a' )
		for item in input_list:
			f_write.write('%s,%s\n' % (item[0], item[1]) )
		f_write.close()
		sys.stdout.write( '[INFO]: done. write result into file:%s\n' % (self.output_path + filename))

	def get_event_num( self, inbound_data ):
		profile_dict = gvar.profile_dict
		d_id = inbound_data['deviceid']
		d_type = inbound_data['data']['type']
		d_value = inbound_data['data']['value']
		ret = [d_id,-1]
		if profile_dict.has_key( d_type ):
			if d_value >= profile_dict[d_type]['thresholds']['lower'] \
				and d_value <= profile_dict[d_type]['thresholds']['upper']:
				ret[1] = (profile_dict[d_type]['thresholds']['upper'] - d_value) / profile_dict[d_type]['window'] \
							+ (d_value - profile_dict[d_type]['thresholds']['lower']) / profile_dict[d_type]['window']

		return ret


