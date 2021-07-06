#! /usr/bin/env python
# gzip 으로 하면 처음에 import 해야하고 읽을때도 rt read text 로 설정해줘야한다
import gzip

data=dict()

covid_file='covid19.fasta.gz'


with gzip.open(covid_file, 'rt') as handle:
    for line in handle:
        if line.startswith('>'):
            continue
        for base in line.strip():
            if base not in data:
                data[base]=0
            data[base]+=1

print(data)












