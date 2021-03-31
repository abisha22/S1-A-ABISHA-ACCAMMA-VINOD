Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=[2,6,98,5,9]
>>> for n in list1:
	square=n**2
	print(n,'square is',square)

	
2 square is 4
6 square is 36
98 square is 9604
5 square is 25
9 square is 81
>>> stringA="I like To hEar music"
>>> print("given string:\n",stringA)
given string:
 I like To hEar music
>>> vowels="AaEeIiOoUu"
>>> res=set([each for each in stringA if each in vowels])
>>> print("the vowels present in string:\n",res)
the vowels present in string:
 {'i', 'e', 'E', 'I', 'o', 'u', 'a'}
>>> 