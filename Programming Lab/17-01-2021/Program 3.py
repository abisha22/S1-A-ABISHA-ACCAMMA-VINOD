Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = int(input("Enter the first number : "))
Enter the first number : 2
>>> num2 = int(input("Enter the Second number : "))
Enter the Second number : 4
>>> num3 = int(input("Enter the Third number : "))
Enter the Third number : 9
>>> if(num1>num2) and (num1>num3):
	largest=num1
elif(num2>num1)and(num2>num3):
	largest=num2
else:
	largest=num3

	
>>> print("The largest number is",largest)
The largest number is 9
>>> 