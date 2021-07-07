#! /usr/bin/env python

a="read_sample.txt"
with open(a,'r') as handle:
    for line in handle:
        print(line.strip())
handle=open(a,'r')

