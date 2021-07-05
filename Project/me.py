#! /usr/bin/env python

FILE = open('./write_file.txt','r')

for i in ['I ','like ','apple ']:
    FILE.write(i)

FILE.close

