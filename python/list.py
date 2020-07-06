Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> [10, 20, 30, 40]
[10, 20, 30, 40]
>>> ['crunchy frog', 'ram bladder', 'lark vomit']
['crunchy frog', 'ram bladder', 'lark vomit']
>>> ['spam', 2.0, 5, [10, 20]]
['spam', 2.0, 5, [10, 20]]
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> numbers = [17, 123]
>>> empty = []
>>> print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [17, 123] []
>>> print(cheeses[0])
Cheddar
>>> numbers = [17, 123]
>>> numbers[1] = 5
>>> print(numbers)
[17, 5]
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> 'Edam' in cheeses
True
>>> 'Brie' in cheeses
False
>>> for cheese in cheeses:
	print(cheese)

	
Cheddar
Edam
Gouda
>>> for i in range(len(numbers)):
	numbers[i] = numbers[i] * 2

	
>>> for x in empty:
	print('This never happens.')

	
>>> ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
>>> [0] * 4
[0, 0, 0, 0]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[3:]
['d', 'e', 'f']
>>> t[:]
['a', 'b', 'c', 'd', 'e', 'f']
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3] = ['x', 'y']
>>> print(t)
['a', 'x', 'y', 'd', 'e', 'f']
>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> print(t)
['a', 'b', 'c', 'd']
>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> print(t1)
['a', 'b', 'c', 'd', 'e']
>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> print(t)
['a', 'b', 'c', 'd', 'e']
>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> print(t)
['a', 'c']
>>> print(x)
b
>>> t = ['a', 'b', 'c']
>>> del t[1]
>>> print(t)
['a', 'c']
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> print(t)
['a', 'c']
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del t[1:5]
>>> print(t)
['a', 'f']
>>> nums = [3, 41, 12, 9, 74, 15]
>>> print(len(nums))
6
>>> print(max(nums))
74
>>> print(min(nums))
3
>>> print(sum(nums))
154
>>> print(sum(nums)/len(nums))
25.666666666666668
>>> total = 0
>>> count = 0
>>> while (True):
	inp = input('Enter a number: ')
	if inp == 'done': break
	value = float(inp)
	total = total + value
	count = count + 1

	
Enter a number: 5
Enter a number: 1
Enter a number: 3
Enter a number: 1
Enter a number: 2
Enter a number: 
Traceback (most recent call last):
  File "<pyshell#75>", line 4, in <module>
    value = float(inp)
ValueError: could not convert string to float: 
>>> while (True):
	inp = input('Enter a number: ')
	if inp == 'done': break
	value = float(inp)
	total = total + value
	count = count + 1
average = total / count
SyntaxError: invalid syntax
>>> while (True):
	inp = input('Enter a number: ')
	if inp == 'done': break
	value = float(inp)
	total = total + value
	count = count + 1
	average = total / count
	
       print('Average:', average)
       
SyntaxError: unindent does not match any outer indentation level
>>> # Code: http://www.py4e.com/code3/avenum.py

>>> numlist = list()
>>> while (True):
	inp = input('Enter a number: ')
	if inp == 'done': break
	value = float(inp)
	numlist.append(value)
	average = sum(numlist) / len(numlist)
	print('Average:', average)

	
Enter a number: 2
Average: 2.0
Enter a number: 4
Average: 3.0
Enter a number: 1
Average: 2.3333333333333335
Enter a number: 0
Average: 1.75
Enter a number: exit
Traceback (most recent call last):
  File "<pyshell#99>", line 4, in <module>
    value = float(inp)
ValueError: could not convert string to float: 'exit'
>>> # Code: http://www.py4e.com/code3/avelist.py
>>> s = 'spam'
>>> t = list(s)
>>> print(t)
['s', 'p', 'a', 'm']
>>> s = 'pining for the fjords'
>>> t = s.split()
>>> print(t)
['pining', 'for', 'the', 'fjords']
>>> print(t[2])
the
>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> s.split(delimiter)
['spam', 'spam', 'spam']
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> delimiter.join(t)
'pining for the fjords'
>>> From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
SyntaxError: invalid syntax
>>> fhand = open('mbox-short.txt')
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    fhand = open('mbox-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> a = 'banana'
>>> b = 'banana'
>>> a = 'banana'
>>> b = 'banana'
>>> a is b
True
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False
>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True
>>> b[0] = 17
>>> print(a)
[17, 2, 3]
>>> def delete_head(t):
	del t[0]

	
>>> letters = ['a', 'b', 'c']
>>> delete_head(letters)
>>> print(letters)
['b', 'c']
>>> t1 = [1, 2]
>>> t2 = t1.append(3)
>>> print(t1)
[1, 2, 3]
>>> print(t2)
None
>>> t3 = t1 + [3]
>>> print(t3)
[1, 2, 3, 3]
>>> t2 is t3
False
>>> def bad_delete_head(t):
	t = t[1:]              # WRONG!

	
>>> def tail(t):
	return t[1:]

>>> letters = ['a', 'b', 'c']
>>> rest = tail(letters)
>>> print(rest)
['b', 'c']
>>> 