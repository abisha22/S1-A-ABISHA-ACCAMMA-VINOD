Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=[12,3,4,56,7,8,9,19,34,87]
>>> list2=[10,4,67,89,4,77,29,5,7,8]
>>> len1=len(list1)
>>> len2=len(list2)
>>> if len1==len2:
	print('Both list have equal length')
else:
	print('Both list doesnot have equal length')

	
Both list have equal length
>>> list1=[12,3,4,56,7,8,9,19,34,87]
>>> list2=[10,4,67,89,4,77,29,5,7,8]
>>> total1=sum(list1)
>>> total2=sum(list2)
>>> if total1==total2:
	print('Both list have equal sum')
else:
	print('Both list doesnot have equal sum')

	
Both list doesnot have equal sum
>>> list1=[12,3,4,56,7,8,9,19,34,87]
>>> list2=[10,4,67,89,4,77,29,5,7,8]
>>> for value in list1:
	if value in list2:
		common=1

		
>>> if common==1:
	print("There are common element")
else:
	print("There is no common element")

	
There are common element
>>> 