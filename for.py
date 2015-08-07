Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for munum is [1,2,3,4,5]:
	
SyntaxError: invalid syntax
>>> for mynum in [1,2,3,4,5]:
...	print"Hello",mynum
...
  File "<pyshell#3>", line 3
    ...	print"Hello",mynum
    ^
IndentationError: expected an indented block
>>> for mynum in [1,2,3,4,5]:
	print"Hello",mynum
	
