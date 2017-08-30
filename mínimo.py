Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> cnt=0
>>> def minimo(arr):
	x=arr[0]
	global cnt
	for y in arr:
		cnt+=1
		if(y<x):
			x=y
	return x

>>> def acomodar(arr)::
	
SyntaxError: invalid syntax
>>> def acomodar(arr):
	aux=arr[:]
	arrsort=[]
	for x in range(len(aux)):
		y=minimo(aux)
		aux.remove(y)
		arrsort.append(y)
	return arrsort

>>> import random
>>> p=random.sample(range(0,100),100)
>>> print(p)
[46, 85, 14, 63, 43, 62, 93, 15, 5, 23, 19, 41, 51, 26, 34, 69, 98, 52, 31, 57, 64, 28, 8, 76, 91, 96, 35, 81, 39, 83, 22, 55, 17, 27, 3, 80, 66, 44, 72, 78, 9, 89, 70, 56, 2, 18, 86, 42, 75, 65, 88, 99, 95, 77, 10, 24, 68, 36, 94, 71, 11, 49, 4, 59, 87, 47, 53, 50, 7, 32, 13, 16, 97, 33, 6, 84, 73, 90, 20, 58, 30, 25, 82, 92, 60, 29, 40, 21, 67, 37, 0, 74, 79, 48, 12, 38, 1, 54, 61, 45]
>>> psort=acomodar(p)
>>> print(cnt)
5050
>>> print(psort)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
