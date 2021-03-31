Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> def gcd(a,b):
#Everything divides 0
	if (b==0):
		return a
	return gcd(b,a%b)

>>> a=45
>>> b=15
>>> if (gcd(a,b)):
	print('GCD of',a,'and',b,'is',gcd(a,b))
else:
	print('Not found')

	
GCD of 45 and 15 is 15
>>> 