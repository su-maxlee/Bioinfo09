#! /usr/bin/env python
'''
#111
i_111=input('Input String: ')
print(i_111 *2)

#112
i_112=int(input('숫자를 입력하세요: '))
print(i_112 + 10)

#113
i_113=int(input('input a number: '))
if i_113 %2==0:
    print('짝수')
else:
    print('홀수')
'''
'''
#114
i_114=int(input('입력값: '))
if (i_114+20)<255:
    print(i_114+20)
else:
    print(255)
'''
'''
#115
i_115=int(input('입력값: '))
if (i_115-20)>255:
    print(255)
elif (i_115-20)<0:
    print(0)
else:
    print(i_115-20)
'''
'''
#116
time=input('현재시간: ')
l_time=time.split(':')

if l_time[1] == '00':
    print('정각입니다')
else:
    print('정각이 아닙니다')
'''
'''
#117
fruit=['apple','grape','per']
user=input('Do you like that fruit? ')
if user in fruit:
    print('That is correct!')
else: 
    print('That is incorrect :(')
'''
'''
#119
fruit ={'spring':'strawberry','summer':'tomato','fall':'apple'}
user=input('What season do I like? ')
if user in fruit:
    print('Thats correct')
else:
    print('That is incorrect')
'''
'''
#120
fruit ={'spring':'strawberry','summer':'tomato','fall':'apple'}
user=input('What fruit do I like? ')
if user in fruit.values():
    print('Thats correct')
else:
    print('That is incorrect')
'''
'''
#121
user= input('>>')
if user.islower() == True:
    u_User=user.upper()
    print(u_User)
else:
    l_User=user.lower()
    print(l_User)
'''
'''
#122
a=int(input('Score? '))
if 80<a<101:
    print('A')
elif 60<a<81:
    print('B')
elif 40<a<61:
    print('C')
elif 20<a<41:
    print('D')
else:
    print('E')
'''
'''
#124
i1=int(input('Input number 1 : '))
i2=int(input('Input number 2 : '))
i3=int(input('Input number 3 : '))

i_list=[i1,i2,i3]

print(max(i_list))
'''
'''
#126
user=input('우편번호: ')
print(user[2])
if user[2]== '1' or '2' or '3':
    print('강북구')
elif user[2]== '4' or '5' or '6':
    print('도봉구')
else:
    print('노원구')
'''


