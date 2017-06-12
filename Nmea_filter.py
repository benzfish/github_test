#!/usr/bin/python3

import sys

'''
author:yuguang
date:2017/6/9
'''
print sys.argv[0], 'is used to filter NMEA sentences from AP log file'
print 'your file is ', sys.argv[1], 'let\'s read & filter it.'
sourceFile = sys.argv[1]
targetFile = "NMEASentence.txt"
compareObject=['$GPGSV', '$GLGSV', '$GAGSV','$GPGSA','$GNGSA','$GPVTG','$GPRMC','$GPGGA','$GNVTG', '$GNRMC', '$GNGGA']
print 'parsing!!! please wait...'
for line in open(sourceFile, 'r'):
#	print (line)
	for s in compareObject:
		if s in line:
			index = line.find(s)
			#print line[index:]
			with open(targetFile, 'a') as writeFile:
				writeFile.write(line[index:])
print 'done, please check NMEASentence.txt at the current directory'
