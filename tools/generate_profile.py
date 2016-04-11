#! /usr/bin/python

import json
profile_dict = [
				{"type":"load",
				"thresholds":{"upper":80,"lower":20},
				"window":10},
				{"type":"type1",
				"thresholds":{"upper":81,"lower":21},
				"window":11},
				{"type":"type2",
				"thresholds":{"upper":82,"lower":22},
				"window":12},
				]
#print profile_dict
print json.dumps( {"type":"load",
					"thresholds":{"upper":80,"lower":20},
					"window":10} )
print json.dumps( {"type":"import",
					"thresholds":{"upper":40,"lower":10},
					"window":15} )
print json.dumps( {"type":"export",
					"thresholds":{"upper":90,"lower":50},
					"window":20} )
print json.dumps( {"type":"comuniate",
					"thresholds":{"upper":60,"lower":20},
					"window":7} )
'''
dic = json.loads(j_obj)
print dic
print dic[2]['type']
'''
