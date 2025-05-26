'''
num=input("name: ")
print(min(num))
print(max(num))
'''
'''
import math
x=float((input("sin number: ")))
print(math.sin(x))
'''
'''
import random
print (random.random())
print (random.randint(8,16))
'''
'''
def hi_bye () :
    print("1hi")
    print("2bye")
print("3")
hi_bye()
print("4")
'''
'''
num=input("name: ")

def hi_bye (name) :
    print("hi",name)
    print("bye",name)
hi_bye(num)#num ميره بجاي name
'''
'''
def jam(a,b):
    javab=a+b
    return javab

number_1=int(input("number_1: "))
number_2=int(input("number_2: "))
jam_2_adad=jam(number_1,number_2)
print(jam_2_adad)
'''
'''
def hoghogh (h,ph) :
    if h>8 :
        return "e"
    kol_daramad=h*ph
    return kol_daramad
x=int(input("number_1 h: "))
y=int(input("number_2 ph: "))
print (hoghogh(x,y))
'''
'''
n=5
while n>0:
    print(n)
    n=n-1
'''
'''
n=input("name: ")
while n != 'end':
    print ('hi',n)
    n=input("name: ")
'''
'''
n=3
while n>=0:
    print(n)
    n=n+1
    if n==100:
        print("oh")
        break
print("out")
'''
'''
for i in range(1,10):
    print(i)
'''
'''
for i in range(1,10):
    print(i,i*i)
    if i==5:
        print("I reched 5")
        break
'''
'''
frinds=[1,10,20]
for thisone in frinds:
    print(thisone)
'''
'''
frinds=['hasan','mirza','tahmine']
for thisone in frinds:
    print('hi',thisone)
'''
'''
frinds=['hasan','mirza','tahmine']
count=0
for thisone in frinds:
    print('hi',thisone)
    count=count+1
print('i said',count,'hi')
'''
'''
#تمرين
n=int(input("number: "))
jam=0
count=0
while n!=-1:
    print(n)
    jam=jam+n
    count=count+1
    miangin=jam/count
    n=int(input("number: "))
print(jam,"/",count,"=",miangin)
'''
'''
import random
javab=random.randint(1,99)
name=input("name: ")
hads=int(input("hads: "))
while hads !=javab:
    if hads >javab:
        print(">")
    else:
        print("<")
    hads=int(input("hads: "))
print("Wow",name,"you did it! you rock!")
'''

#تمزين
import random
a=1
b=99
hads=random.randint(a,b)
print(hads)
javab=input("b or k or d: ")
while javab!='d':
    if javab=='b':
        a=hads
    elif javab=='k':
        b=hads
    hads=random.randint(a,b)
    print(hads)
    javab=input("b or k or d: ")
    
print("True is",hads)

