require('python')
pg = python.globals()
d = {}
pg.d = d
python.execute("d['key'] = 'value'")
table.foreach(d, print)

