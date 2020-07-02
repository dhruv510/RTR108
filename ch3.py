Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5 == 5
True
>>> 5 == 6
False
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> {}
{}
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> x != y               # x is not equal to y
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x != y               # x is not equal to y
NameError: name 'x' is not defined
>>> x > y                # x is greater than y
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x > y                # x is greater than y
NameError: name 'x' is not defined
>>> 17 and True
True
>>> if x > 0 :
	print('x is positive')
	if x < 0 :
		pass          # need to handle negative values!

	
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    if x > 0 :
NameError: name 'x' is not defined
>>> if x < 0 :
	pass          # need to handle negative values!
x = 3
SyntaxError: invalid syntax
>>> x = 3
>>> if x < 10print('Small')
SyntaxError: invalid syntax
>>> x = 3
>>> if x < 10:
	print('Small')

	
Small
>>> x = 3
>>> if x < 10:
	print('Small')
	print('Done')

	
Small
Done
>>> if x%2 == 0 :
	print('x is even')
	else :
		
SyntaxError: invalid syntax
>>> if x%2 == 0 :
	print('x is even')
else :
	print('x is odd')

	
x is odd
>>> if x < y:
	print('x is less than y')
elif x > y:
	print('x is greater than y')
else:
	print('x and y are equal')

	
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    if x < y:
NameError: name 'y' is not defined
>>> if x < y:
	print('x is less than y')
elif x > y:
	print('x is greater than y')
else:
print('x and y are equal')
SyntaxError: expected an indented block
>>> 
>>> if choice == 'a':
	print('Bad guess')
elif choice == 'b':
	print('Good guess')
elif choice == 'c':
	print('Close, but not correct')

	
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    if choice == 'a':
NameError: name 'choice' is not defined
>>> if x == y:
	print('x and y are equal')
else:
	if x < y:
		print('x is less than y')
		else:
			
SyntaxError: invalid syntax
>>> if x == y:
	print('x and y are equal')
else:
	if x < y:
	 	print('x is less than y')
	else:
		print('x is greater than y')

		
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    if x == y:
NameError: name 'y' is not defined
>>> inp = input('Enter Fahrenheit Temperature: ')
Enter Fahrenheit Temperature: fahr = float(inp)
>>> cel = (fahr - 32.0) * 5.0 / 9.0
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    cel = (fahr - 32.0) * 5.0 / 9.0
NameError: name 'fahr' is not defined
>>> cel = (fahr - 32.0) * 5.0 / 9.0
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    cel = (fahr - 32.0) * 5.0 / 9.0
NameError: name 'fahr' is not defined
>>> print(cel)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(cel)
NameError: name 'cel' is not defined
>>> # Code: http://www.py4e.com/code3/fahren.py
>>> python fahren.py
SyntaxError: invalid syntax
>>> Enter Fahrenheit Temperature:72
SyntaxError: invalid syntax
>>> Enter Fahrenheit Temperature:fred
SyntaxError: invalid syntax
>>> inp = input('Enter Fahrenheit Temperature:')
Enter Fahrenheit Temperature:
>>> try:

	fahr = float(inp)
	cel = (fahr - 32.0) * 5.0 / 9.0
	print(cel)
except:
	print('Please enter a number')
# Code: http://www.py4e.com/code3/fahren2.py

Please enter a number
>>> python fahren2.py
SyntaxError: invalid syntax
>>> Enter Fahrenheit Temperature:72
SyntaxError: invalid syntax
>>> 
>>> 
>>> x = 6
>>> y = 2
>>> x >= 2 and (x/y) > 2
True
>>> x = 1
>>> y = 0
>>> x >= 2 and (x/y) > 2
False
>>> x = 6
>>> y = 0
>>> x >= 2 and (x/y) > 2
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    x >= 2 and (x/y) > 2
ZeroDivisionError: division by zero
>>> x = 1
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2
False
>>> x = 6
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2
False
>>> x >= 2 and (x/y) > 2 and y != 0
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    x >= 2 and (x/y) > 2 and y != 0
ZeroDivisionError: division by zero
>>> x = 5
>>> y = 6
>>> Enter Hours: 45
SyntaxError: invalid syntax
>>> 