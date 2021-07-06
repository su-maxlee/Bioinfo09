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
'''
'''
#19 Debugging
import sys
try:
    num = int(input('Enter: '))
except ValueError as err:
    print(err)
    sys.exit()
try:
    print(10/num)
except ZeroDivisionError as err:
    print(err)
    sys.exit()
#한번에 합치기 가능 하지만 어디서 에러가 났는지 명확하게 알려면은 나눠서 하는것이 좋다 

try: 
    num=int(input('Enter: '))
    print(10 / num)
except ValueError:
    print('Enter a value')
    sys.exit()
except ZeroDivisionError:
    print('Cant divide by 0') 
    sys.exit
'''
'''
#20 문자열 더하기 
a='Bio'
b=' Informatics'
print(a+b)
'''
'''
# Extra class
class A:
    def __init__(self,val):
        self.val = val
    def __add__(self,other):            # __add__ 는 + 이 무엇을 하는지를 설정하는것!
        return self.val + other.val
    def __mul__(self,other):
        return "__mul__"

a1 = A('Bio')
a2 = A('Informatics')
print(a1.val + a2.val)
print(a1+a2)
print(a1*a2) #이렇듯 스트링은 곱하기가 안되지만 곱하기를 다른걸로 지정해줘서 에러가 안뜬다
'''

#21 문자열 n 번째 출력하기
'''
Seq1='AGTTTATAG'
print(Seq1[5])

#22 문자열 나누기 
print(Seq1[3:6])

#23 문자열 길이 구하기 
print(len(Seq1))

#24 대소문자 변환기 
Seq2='ATGttATaG'
print(Seq2.upper())
print(Seq2.lower())
'''
'''
#25 문자열 n 씩 건너뛰며 출력하기 
Seq1 = 'ATGTTATAG'
print(Seq1[::3])
print('-'*20)
#26 문자열 n씩 건너뛰며 출력하기
print(Seq1[:3])
print(Seq1[3:6])
print(Seq1[6::])
print('-'*20)
#27 문자열 순서 뒤집기 
print(Seq1[::-1])
print('-'*20)
#28 문자열 바꾸기 
d_DNA={'A':'T','T':'A','G':'C','C':'G'}
comp_seq=''
for s in Seq1:
    comp_seq += d_DNA[s]
print(Seq1)
print(comp_seq)

for i in range(len(Seq1)):
    s=Seq1[i]
    cs=comp_seq[i]
    bond ='≡'
    if s =='A' or s=='T':
        bond ='='
    print(f'{s}{bond}{cs}')
    
#29 특정 문자 확인하기 
#print('C' in Seq1)
'''
'''
#30 문자열 index 번호 출력하기 

seq= 'ATGTTTATAG'

for i in range(len(seq)):
    s=seq[i:i+2]
    print(i, s, s=='TT')
    #if s =='TT':
       # print(i)
'''
#31 문자열 리스트로 바꾸기 
a='AA,AC,AG,AT'
l_a=a.split(',')
print(l_a)
#32 리스트에 요소 추가하기 
l_a.append('CA')
print(l_a)
#33 reverse list
print(l_a[::-1])
#34 min max 
b=[3,1,1,2,0,0,2,3,3]
print(max(b))
print(min(b))
#35 count dict list 
l_q35=[3,1,1,2,0,0,2,3,3]
d_q35=dict()
for i in l_q35:
    if i not in d_q35:
        d_q35[i]=0
    d_q35[i]+=1
print(d_q35)




