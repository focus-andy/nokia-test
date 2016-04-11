#!/usr/bin/python
import unittest
import sys
sys.path.insert( 0, '../core/')
import profile

class TestProfile(unittest.TestCase):
	def setUp(self):  
		pass

	def tearDown(self):
		pass
	
	def test_load_profile_empty(self):
		self.tclass = profile.Profile( 'abc' )
		self.assertEqual( self.tclass.load_profile(), False, '#1 test load_profile failed' )

	def test_load_profile_wrong_json(self):
		self.tclass = profile.Profile( './test_data/wrong_json.txt' )
		self.assertEqual( self.tclass.load_profile(), False, '#2 test load_profile failed' )

	def test_load_profile_wrong_key(self):
		self.tclass = profile.Profile( './test_data/wrong_profile_key.txt' )
		self.assertEqual( self.tclass.load_profile(), False, '#3 test load_profile failed' )
if __name__ == '__main__':
	unittest.main()


