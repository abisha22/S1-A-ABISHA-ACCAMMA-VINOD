Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def findarea(r):
	pi=3.142
	return pi*(r*r);

>>> a=float(input("Enter the radius: "))
Enter the radius: 5
>>> print("Area is %.6f" %findarea(a));
Area is 78.550000
>>> 