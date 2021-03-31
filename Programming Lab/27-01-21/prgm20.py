Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list=[44,11,22,33,55,77,88,99,44]
>>> print(list)
[44, 11, 22, 33, 55, 77, 88, 99, 44]
>>> for i in list:
	if(i%2==0):
		list.remove(i)

		
>>> print("Listafter removing Even numbers:",(list))
Listafter removing Even numbers: [11, 33, 55, 77, 99]
>>> 