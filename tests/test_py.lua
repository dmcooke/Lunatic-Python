require('python')

assert(nil == python.eval("None"))
assert(true == python.eval("True"))
assert(false == python.eval("False"))

assert(1 == python.eval("1"))
assert(1.5 == python.eval("1.5"))

pg = python.globals()
d = {}
pg.d = d
--python.execute("d['key'] = 'value'")
--table.foreach(d, print)

