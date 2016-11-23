#!/bin/python

import shapefile

sf = shapefile.Reader("D:/Politeknik Pos Indonesia/Semester 5/Sistem Informasi Geografis/sig/negara.shp")
print sf
shapes = sf.shapes()
print len(shapes)

#for name in dir(shapes[3]):
#		if not name.startswitch('__'):
#				print name