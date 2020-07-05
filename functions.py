Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(32)
<class 'int'>
>>> max('Hello world')
'w'
>>> min('Hello world')
' '
>>> len('Hello world')
11
>>> int('32')
32
>>> int('Hello')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int('Hello')
ValueError: invalid literal for int() with base 10: 'Hello'
>>> int(3.99999)
3
>>> int(-2.3)
-2
>>> float(32)
32.0
>>> float('3.14159')
3.14159
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'
>>> import math
>>> print(math)
<module 'math' (built-in)>
>>> ratio = signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    ratio = signal_power / noise_power
NameError: name 'signal_power' is not defined
>>> decibels = 10 * math.log10(ratio)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    decibels = 10 * math.log10(ratio)
NameError: name 'ratio' is not defined
>>> radians = 0.7
>>> height = math.sin(radians)
>>> degrees = 45
>>> radians = degrees / 360.0 * 2 * math.pi
>>> math.sin(radians)
0.7071067811865476
>>> math.sqrt(2) / 2.0
0.7071067811865476
>>> import random
>>> for i in range(10):
	x = random.random()
	print(x)

	
0.2945648390365898
0.5432192092625199
0.623399468331046
0.48986714994081826
0.08925559871475841
0.46034185540023076
0.973792164368709
0.7128003045227458
0.05357967678157616
0.1961540753788551
>>> t = [1, 2, 3]
>>> random.choice(t)
1
>>> random.choice(t)
2
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')

	
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')

	
>>> print(print_lyrics)
<function print_lyrics at 0x000000000302E9D8>
>>> print(type(print_lyrics))
<class 'function'>
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> def repeat_lyrics():
	print_lyrics()
	print_lyrics()

	
>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')

	
>>> def repeat_lyrics():
	print_lyrics()
	print_lyrics()

	
>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> # Code: http://www.py4e.com/code3/lyrics.py
>>> def print_twice(bruce):
	print(bruce)
	print(bruce)

	
>>> print_twice('Spam')
Spam
Spam
>>> print_twice(17)
17
17
>>> import math
>>> print_twice(math.pi)
3.141592653589793
3.141592653589793
>>> print_twice('Spam '*4)
Spam Spam Spam Spam 
Spam Spam Spam Spam 
>>> print_twice(math.cos(math.pi))
-1.0
-1.0
>>> michael = 'Eric, the half a bee.'
>>> print_twice(michael)
Eric, the half a bee.
Eric, the half a bee.
>>> x = math.cos(radians)
>>> golden = (math.sqrt(5) + 1) / 2
>>> math.sqrt(5)
2.23606797749979
>>> math.sqrt(5)
2.23606797749979
>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None
>>> print(type(None))
<class 'NoneType'>
>>> def addtwo(a, b):
	added = a + b
	return added

>>> x = addtwo(3, 5)
>>> print(x)
8
>>> # Code: http://www.py4e.com/code3/addtwo.py
>>> def fred():
	print("Zap")

	
>>> def jane():
	print("ABC")

	
>>> jane()
ABC
>>> fred()
Zap
>>> jane()
ABC
>>> Enter Hours: 45
SyntaxError: invalid syntax
>>> Enter Hours:
	
SyntaxError: invalid syntax
>>> computegrade
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    computegrade
NameError: name 'computegrade' is not defined
>>> score Grade
SyntaxError: invalid syntax
>>> 