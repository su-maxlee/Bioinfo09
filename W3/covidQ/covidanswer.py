#! /usr/bin/env python
#import sys
file_name='covid19.fasta'
#file name = sys.argv[1] 이렇게하면 파일명을 입력하면 결과 나올수있다

data=dict()

with open(file_name,'r') as handle:
    for line in handle:
        if line.startswith(">"): # 맨윗줄 필요없는 라인을 제거하기 
            continue
        for base in line.strip():
            if base not in data:
                data[base]=0
            data[base]+=1

print(data)
