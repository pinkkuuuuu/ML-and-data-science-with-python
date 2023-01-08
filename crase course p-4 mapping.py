def time2(var):
    return var*2

time2(3)

#map()

seq=[1,2,3,4,5]

list(map(time2,seq))

t = lambda var:var*2

t(7)

list(map(lambda num:num+6,seq))

print (list(filter(lambda num:num%2 ==0,seq)))

#methods

s ='hello my name is pinku'

s.lower()

s.upper()

s.split()

tweet ='go sports! #link'

tweet.split('#')[1]

d ={'k1':1,'k2':2}

d

d.keys()

d.items()

d.values()

lst=[1,2,3]

lst.pop()

lst

lst = [1,2,3,4,5]

item = lst.pop()

lst

item

first = lst.pop(0)

first

lst

lst.append('new')

lst

'x' in [1,2,3]

'x' in ['x','y','z']

#truple unpacking

x =[(1,2),(3,4),(5,6)]

x

x[0]

x[1][1]

for item in x:
    print(item)

for (a,b) in x:
    print(a)

for (a,b) in x:
    print(b)

for a,b in x:
    print(a)
    print(b)

