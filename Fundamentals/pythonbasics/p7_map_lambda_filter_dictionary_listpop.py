#map()- is used to call function for all values of list
print('example map')
def times2(var):
	return var*2

seq=[1,2,3,4,5]
print(list(map(times2,seq)))

#lambda- convert times2 function to lambda. 
#how to convert from function to lambda-https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp/learn/v4/t/lecture/5733146?start=840
print('lambda')
print(list(map(lambda(var):var*2,seq)))

#filter
print('filter')
print(list(filter(lambda(var):var%2==0,seq)))

#dictionary
print('Dictionary')
d={'k1':1,'k2':2}
print(d.keys())

#list
print('list.append,list.pop')
lst=[1,2,3,4,5]
print(lst.pop())
print(lst.pop(1))
print('final list-',lst)
