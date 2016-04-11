#! /usr/bin/python

import json
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
