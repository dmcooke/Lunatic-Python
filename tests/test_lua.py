"""
>>> import lua
>>> lg = lua.globals()
>>> lg.string
<Lua table at 0x...>
>>> lg.string.lower
<Lua function at 0x...>
>>> lg.string.lower("Hello world!")
'hello world!'

>>> d = {}
>>> lg.d = d
>>> lua.execute("d['key'] = 'value'")
>>> d
{'key': 'value'}

>>> d2 = lua.eval("d")
>>> d is d2
True

>>> lua.eval("python")
<Lua table at 0x...>

>>> class MyClass:
...     def __repr__(self): return '<MyClass>'
... 
>>> obj = MyClass()
>>> obj
<MyClass>
>>> from pprint import pprint
>>> pprint(lua.eval('python.globals()'))
>>> lua.eval('python.eval("obj")')
<MyClass>
>>> lua.eval(\"\"\"python.eval([[lua.eval('python.eval("obj")')]])\"\"\")
<MyClass>

>>> lua.execute("pg = python.globals()")
>>> lua.eval("pg.obj")
<MyClass>

>>> table = lua.eval("table")
>>> def show(key, value):
...   print "key is %s and value is %s" % (`key`, `value`)
... 
>>> t = lua.eval("{a=1, b=2, c=3}")
>>> table.foreach(t, show)
key is 'a' and value is 1
key is 'c' and value is 3
key is 'b' and value is 2
>>> 

"""

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)


