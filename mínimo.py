Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> cons=0
>>> def minimo(arr):
	x=arr[0]
	global cons
	for y in arr:
		cons+=1
		if(y<x):
			x=y
			return x

		
>>> def ordenar(arr):
	aux=arr[:]
	arrsort=[]
	for x in range(len(aux)):
		y=minimo(aux)
		aux.remove(y)
		arrsort.append(y)
		return arrsort

	
>>> import random
>>> p=random.sample(range(0,100),40)
>>> print(p)
[27, 0, 2, 40, 88, 5, 10, 94, 87, 44, 33, 46, 39, 75, 92, 84, 58, 53, 48, 96, 73, 17, 30, 50, 74, 4, 7, 67, 43, 32, 8, 55, 9, 26, 29, 42, 45, 82, 93, 6]
>>> psort=ordenar(p)
>>> print(cons)
2
>>> print(psort)
[0]
>>> 
