#! /usr/bin/env python
'''
def func(name:str)->str:  # 이렇게 입출력 데이터 형식을 적어두는게 좋다
    return f'{name} hi' 

v=func('max')

print(v)
'''
'''
#13 사용자로부터 값 받기 - 하드코딩 피하기 
name=input('Input name: ')

print(f'Hello {name}')
'''
'''
#14 사용자로부터 값 받기 활용
s = input('Input: ')

if s.isalpha():
    print(f'{s} is a letter')
else:
    print(f'{s} is a number')
'''
'''
#15 Command line argument input
import sys
sample=sys.argv[1]

if lne(sys.argv) != 2:
    print(f'Python {sys.argv[0]} [sample]')
    sys.exit()

print(f'processing :{sample}')
'''
'''
# Error Handling 
import sys
try:
    num = int(sys.argv[1])
except ValueError as err:
    print(f'{err}, your input : {sys.argv[1]}')
    sys.exit(3)
try:
    res = 10/num
except ZeroDivisionError:
    sys.exit(2)
print(res)
'''

#16 파일읽기 
'''
file_name="read_sample.txt"
with open(file_name, 'r') as handle:
    for line in handle:
        print(line.strip())
handle =open(file_name,'r')

for line in handle:
    print(line.strip())
handle.close()
handle =open(file_name,'r')
lines=handle.readlines()
for line in lines:
    print(line.strip())
handle.close()
with open(file_name,'r') as handle:
    lines=handle.readlines()
    for line in lines:
'''
'''
#17 Write in file 
file_name='write_sample.txt'
handle=open(file_name, 'w')
handle.write('Hello\n')
handle.write('Bioinformatics\n')

with open(file_name, 'a') as handle:
    handle.write('max\n')

s= 's1,s2,s3' #csv 
data=s.split(',')
print(data)

with open(file_name, 'a') as handle:
    handle.write('\t'.join(data)+'\n') #tsv
'''
#18
import sys
try:
    with open('noname.txt','r') as fr:
        read = fr.readlines()
except FileNotFoundError as err:
    print(err)
    # noname.txt 를 생성하는 과정을 입력해도 괜찮다 
    sys.exit()
print(read)











