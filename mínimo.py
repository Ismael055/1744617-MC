Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> p=[]
>>> for i in range(100):
	p.append(i)

	
>>> def minimo(arr):
	aux=arr
	for n1 in arr:
		aux.pop(n1)
		for n2 in aux:
			if(n1>n2):
				break
			resultado=n1
			break
		return resultado
