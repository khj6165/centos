#!/usr/bin/env python
import sys
import os

flist = ['asset', 'config', 'doc', 'edit', 'in', 'out', 'shot']
list2 = ['char', 'shader']
list3 = ['ocio', 'thumbnail']

for i in flist:
	os.makedirs("/project/%s/%s" % (sys.argv[1], i))
for j in list2:
	os.makedirs("/project/%s/asset/%s" % (sys.argv[1], j))
for k in list3:
	os.makedirs("/project/%s/config/%s" % (sys.argv[1], k))
os.makedirs("/project/%s/doc/concept" % (sys.argv[1]))

