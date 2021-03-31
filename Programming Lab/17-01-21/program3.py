Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=float(input("Enter fist number: "))
Enter fist number: 7
>>> b=float(input("Enter 2nd number: "))
Enter 2nd number: 4
>>> c=float(input("Enter 3rd number: "))
Enter 3rd number: 6
>>> if(a>b)and(a>c):
	largest=a
elif(b>a)and(b>c):
	largest=b
else:
	largest=c

	
>>> print("The largest number is",largest)
The largest number is 7.0
>>> 