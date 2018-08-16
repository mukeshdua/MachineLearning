print('Simple datatype examples as follows:')
multiply=3*7
print multiply
power=2**2
print power

print('String examples as follows:')
myname='Mukesh'
sonname='Hanshul'
print('My name is {}'.format(myname))
print('My name is {my},son name is {son}'.format(son=sonname,my=myname))
print(myname[2])
print(myname[1:])
print(myname[:3])
print(myname[1::3])

print('list examples as follows:')
intlist=[1,2,3]
stringlist=['mukesh','hanshul','dua']
print(intlist[2])
print(stringlist[1])
sublist=[1,2,[3,4,[5,6]]]
print(sublist[2][2][1])

print('Dictionary examples as follows:')
dict={'key1':'value1','key2':'value2'}
print('Simple dictionary:',dict['key1'])
innerdict={'key1':{'innerkey':[1,2,3]}}
print('Inner dictionary',innerdict['key1']['innerkey'][1])

print('Tuple examples as follows:')
tuple=(1,2,3)
print(tuple)
