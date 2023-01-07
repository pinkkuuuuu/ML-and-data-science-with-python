d = {'key':'value','key2':123}

d['key']

d['key2']

d = {'k1':[1,2,3]}

my_list = d['k1']



d = {'k1':{'innerkey':[1,2,3]}}

d['k1']['innerkey'][1]

True


my_list =[1,2,3]

my_list[0]

t =(1,2,3)

t[0]

my_list[0] = 'new'

my_list

set([1,2,3,3,4,5,5,5,6,6,6,7,7])

s ={1,2,3}

s.add(4)

s

s.add(5)

s

#comparison operator

1 > 2

2 > 1

1 <= 1

1 == 1

1 == 2

1 != 3

'hi'!= 'bye'

#logic operator

(1 < 2) and (2 > 3)

(1<2) or (2>3) or (1==1)

True or False

#if else statements

if 1 < 2:
    
    print('hello')

if True:
    print('pinku')

if True:
    x = 2+2

x

if 1 == 2:
    print('first')
else:
    print('last')

if 1 == 2:
    print('first')
elif 4 ==4:
    print('second')
elif 3==3:
    print('middle')
else:
    print('last')

seq =[1,2,3,4,5]

 for num in seq:
        print(num)

for num in seq:
        print('pinku')

i = 1

while i <5:
    print('i is:{}'.format(i))
    i = i +1



i = 1

while i <5:
    print('i is:{}'.format(i))
    i = i +1

for x in range(0,5):
    print(x)

list(range(10))

#list comprehension

x = [1,2,3,4]

out =[]

for num in x:
    out.append(num**2)

print(out)

[num**2 for num in x]

out = [num**2 for num in x]

print(out)

#fuctions  

def myname(name=''):
    print('hello' +  name)

myname('pinku')

def myname(name='pinku'):
    print('hello' +  name)

myname()

def square(num):
    '''
    Hello mr. Pinku.
    how are you.
    what are you doing.
    '''
    return num**2

output = square(4)

output

square(num)

range
