Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import collections
>>> collections
<module 'collections' from 'C:\\Users\\Sneha.Rajkumar\\AppData\\Local\\Programs\\Python\\Python39\\lib\\collections\\__init__.py'>
>>> collections.ordereddict()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    collections.ordereddict()
  File "C:\Users\Sneha.Rajkumar\AppData\Local\Programs\Python\Python39\lib\collections\__init__.py", line 68, in __getattr__
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
AttributeError: module 'collections' has no attribute 'ordereddict'
>>> collections.OrderedDict()
OrderedDict()
>>> dictob = collections.OrderedDict
>>> dictob
<class 'collections.OrderedDict'>
>>> def coder():
	print("coder")

	
>>> coder()
coder
>>> lambda:
	
SyntaxError: invalid syntax
>>> lambda x:print("coder")
<function <lambda> at 0x0000021CD17563A0>
>>> def coder(loc):
	print("error")

	
>>> lambda loc:print("error")
<function <lambda> at 0x0000021CD17564C0>
>>> coder("jvt")
error
>>> fn =lambda loc:print ("error")
>>> fn("code")
error
>>> 