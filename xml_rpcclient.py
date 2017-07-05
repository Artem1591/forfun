import xmlrpclib

s = xmlrpclib.ServerProxy('http://127.0.0.1:8000')
print s.selectAll()
print s.insert(3,'Vazgen')
print s.selectAll()
print s.deleteID(3)
print s.selectAll()