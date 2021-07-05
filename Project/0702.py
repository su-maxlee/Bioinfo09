#! /usr/bin/env python
'''
#계산기 
def calc(num0,num1,op):
    prnt('{} {} {}'.format(num0, num1, op))
    if op=='+':
        return  num0 + num1
    elif op=='-':
        return  num0 - num1
    elif op=='*':
        return  num0 * num1
    elif op=='/':
        return num0 /num1
cal1 = calc(5,2,'*')
cal2 = calc(5,2,'/')
print(cal1)
print(cal2)

#피보나치 수열 
n_pivo = int(input('n_th pivo: '))
l_pivo = [0,1]
print('len(l_pivo): ', len(l_pivo))
#list method
def pivo(n):
    #while len(l_pivo)<n:
    for i in range(n- len(l_pivo)):
        l_pivo.append(l_pivo[-1]+l_pivo[-2])
    print(l_pivo[-1])
    print(l_pivo)

#재귀함수 사용
def pivo_r(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return pivo_r(n-1)       
'''
'''
#Class
a='apple'
print(a.count('p')) #a 라는 객체의 count 함수를 쓴 꼴 
#속성: 클래스의 변수 attribute
#메소드: 클래스의 함수 method 

#Class 2 
class Person: 
    nation = 'A nation' 
    
    def greeting(self):
        print('Hi')

    def printNation(self):
        print(self.nation)
    
    def changeNation(self,country):
        self.nation = country

yune=Person()
yune.greeting()
yune.printNation()
yune.changeNation('Korea')
yune.printNation()
print("-"*40)
#Class 3
class Person:
    nation = 'A nation'
    def greeting(self):
        print('(method)greeting: ', 'Hi')

    def hi1(self):
        self.greeting()
    def hi2(self):  
        greeting()
def greeting():
    print('(function) greeting: ','Hello!')
yune = Person()
yune1= Person()
yune.greeting()
print()
yune.hi1()
yune.hi2()
print('-'*40)

#Class 4
class Person:
    nation = 'A nation'
    def greeting(self):
        print('(method)greeting: ','Hi')

yune=Person()
yune.greeting()

print(isinstance(yune, Person))
print('check1', isinstance("hello", (float,int,str,list,dict,tuple)))
print('check2', isinstance("hello", (float,int,str,list,dict,tuple)))

'''
'''
#init 생성자 initialization method 
print('-'*20,'__init1상속__','-'*20)
class Cat:
    def __init__(self):
        self.sleepy=True
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def snack(self):
        print("야옹~")

catcat=Cat()
catcat.snack()
print(catcat.sleepy, end='\n\n')

minyong = KoShort()
minyong.snack()
print(minyong.sleepy)


print('-'*20,'__init2__','-'*20)
class Person:
    def __init__(self,in_nation):
        self.nation=in_nation

    def showNation(self):
        print(self.nation)

yune=Person('Korea')
yune1=Person('AAA')

yune.showNation()
yune1.showNation()
'''

print('Try: ')
try:
    print('aaaaaa')
    print('aaaaaa')
    print(adfas)
    print('bbbbbb')
    print('bbbbbb')
except:
    print('error!')
print()
print()
print()
print('DONE!')





