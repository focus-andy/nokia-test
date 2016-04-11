#!/usr/bin/python
import unittest
import sys
sys.path.append('../core/')
import tools

class TestTools(unittest.TestCase):
	def setUp(self):  
		pass 

	def tearDown(self):
		pass
	
	def test_load_file_empty(self):
		self.assertEqual( tools.load_file('abc'), False, '#1 test load_file failed' )

	def test_load_file_normal(self):
		self.assertEqual( tools.load_file('test_load_file.txt'), ['abcd\n','ef\n'], '#2 test load_file failed' )

if __name__ == '__main__':
	unittest.main()


