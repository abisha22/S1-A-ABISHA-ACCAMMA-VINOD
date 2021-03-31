Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Enter year")
Enter year
>>> endYear=int(input())
2060
>>> startYear=2020
>>> print("leap year's")
leap year's
>>> for year in range(startYear,endYear):
	if(0==year%4)and(0!=year%100)or(0==year%400):
		print(year)

		
2020
2024
2028
2032
2036
2040
2044
2048
2052
2056
>>> 