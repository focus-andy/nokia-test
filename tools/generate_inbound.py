#! /usr/bin/python

import json
print json.dumps( {"deviceid":"abc",
					"data":{"type":"load",
							"value":56}} )
print json.dumps( {"deviceid":"xyz",
					"data":{"type":"import",
							"value":30}} )
print json.dumps( {"deviceid":"abc",
					"data":{"type":"export",
							"value":56}} )
print json.dumps( {"deviceid":"abc",
					"data":{"type":"export",
							"value":78}} )
print json.dumps( {"deviceid":"abc",
					"data":{"type":"communicate",
							"value":93}} )
