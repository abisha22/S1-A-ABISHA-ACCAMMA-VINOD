Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import operator
>>> d={1:2,4:3,3:4,5:6,7:8,9:7}
>>> print('Original dictionary:',d)
Original dictionary: {1: 2, 4: 3, 3: 4, 5: 6, 7: 8, 9: 7}
>>> sorted_d=sorted(d.items(),key=operator.itemgetter(1))
>>> print('Dictionary in asending order by value:',sorted_d)
Dictionary in asending order by value: [(1, 2), (4, 3), (3, 4), (5, 6), (9, 7), (7, 8)]
>>> print('Dictionary in descending order by value:',sorted_d)
Dictionary in descending order by value: [(1, 2), (4, 3), (3, 4), (5, 6), (9, 7), (7, 8)]
>>> 