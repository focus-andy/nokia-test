#!/usr/bin/python
import os

def load_file( filename = '' ):
	if not os.path.isfile( filename ):
		sys.stderr.write( "[ERROR]: file '%s' does not exist!\n" % (filename) )
		return False
	
	#read all the contents of a file
	f_read = open( filename, 'r' )
	all_text = f_read.readlines()
	f_read.close()

	return all_text


