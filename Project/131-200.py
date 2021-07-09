#! /usr/bin/env python
"""
for a in ['a','b','c']:
    print(a)
"""
"""
#140
for a in range(0,4,1):
    print('--------')
"""
"""
#141
a = [100,200,300]
for i in a:
    print(i+10)
"""
"""
#143
a=['asdfasdfsd','bbafbdbasdbsdbsd','asdfeqwewqewq']
for i in a:
    print(len(i))
"""
"""
#145
a=['asdfdasf','qweqweg','nafnfbsd']

for i in a:
    print(i[0])
"""
"""
#147
a=[1,2,3]
p=0
for i in a:
    print(i,'x',3, '=', i*3)
"""
"""
#148
a=['a','b','c','d']

for i in a[1:]:
    print(i)
#149
for i in a[::2]:
    print(i)
#150
for i in a[::-1]:
    print(i)

"""
"""
#151
a=[3,-20,-3,44]
b=[]
for i in a:
    if i<0:
        b.append(i)
    else:   
        continue
print(b)
"""
"""
#159
a=['max.p','asdf.d','kafd.qe']
for i in a:
    print(i.split('.')[::2])
"""
"""
#161
for i in range(0,100,1):
    print(i,end=" ")
"""
"""
#165
for i in range(0,10,1):
    print(i/10)
"""
"""
#168 
a=0
for i in range(1,11):
    a=a+i
print(a)
"""
"""
#169
a=0 
for i in range(1,11,2):
    a=a+i
print(a)
"""
"""
#170
a=1
for i in range(1,11):
    a*=i
print(a)
"""
"""
#171
l_price=[32100,32150,32000,32500]
for i in range(len(l_price)):
    print(l_price[i])
"""
"""
#172
l_price=[32100,32150,32000,32500]
for i in range(len(l_price)):
    print(i,l_price[i])
for i, data in enumerate(l_price):
    print(i,data)
"""
"""
#173
l_price=[32100,32150,32000,32500]
for i in range(len(l_price)):
    print(len(l_price)-i-1,l_price[i])
"""

# 174
l_price = [32100, 32150, 32000, 32500]
print(l_price)

