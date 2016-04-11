#! /usr/bin/python

import json
print json.dumps( {"deviceId":"abc",
					"data":{"type":"load",
							"value":56}} )
print json.dumps( {"deviceId":"xyz",
					"data":{"type":"import",
							"value":30}} )
print json.dumps( {"deviceId":"abc",
					"data":{"type":"export",
							"value":56}} )
print json.dumps( {"deviceId":"abc",
					"data":{"type":"export",
							"value":78}} )
print json.dumps( {"deviceId":"abc",
					"data":{"type":"communicate",
							"value":93}} )
'''
dic = json.loads(j_obj)
print dic
print dic[2]['type']
'''
