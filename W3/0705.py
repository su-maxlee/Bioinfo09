#! /usr/bin/env python

''' 
#나중에 한번봐보자
a= 11
if (b:=a)>10:
    print(f'the value of b is {b} and is greater than 10.')
'''
'''
#2 Variable my answer
import math
r=float(input('insert radius: '))

area= (r**2)*math.pi

print(f'The area of a circle with a radius of {r} is:',area)
'''
'''
#2 Variable t.answer
import math
import sys

#설명서 
if len(sys.argv) != 2: 
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

r=int(sys.argv[1])
pi=math.pi
result = round(r**2*pi, 2)

print(result)
'''
'''
#3 Operator my answer
num1 = 3
num2 = 5 
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1**num2)
'''
'''
#4 if-else
 
import sys 

if len(sys.argv)!=2:
    print(f'#usage: python {sys.argv[0]} [num]')
    sys.exit()


 46 #4 if-else
num = int(sys.argv[1])

if num%2==0:
    print(f'{num} is an even number')
else:   
    print(f'{num} is an odd number')
'''
'''
#5 if-elif-else
import sys
if len(sys.argv)!=2:
    print(f'#usage: python {sys.argv[0]} [num]')
    sys.exit()

num=int(sys.argv[1])

if num%3==0 and num%7==0:
    print(f'{num} is a multiple of 21')    
elif num%3==0:
    print(f'{num} is a multiple of 3')
elif num%7==0:
    print(f'{num} is a multiple of 7')
else:
    print(f'{num} is not a multiple of 3 or 7')
'''
'''
#6 for 
a=1
for i in range(1,11,1):
    a*=i
print(a)    
'''

'''
#7 multiple for 
'''

'''
#8 While t.answer

import sys

n=int(sys.argv[1])
val = 1

while n>0:
    val*=n
    n-=1
print(val)
'''

#9 Function t.answer

def greet():
    print('Hello, Bioinformatics')

def greet1(name):
    print(f"Hello, {name}")

def greet2(num):
    return num*2


greet()
greet1('max')
ret=greet2(3)
print(ret)

