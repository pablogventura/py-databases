from pyDB import *

f=CDF()
f.from_parse("A->B C, E->F A","A,B,C,D,E,F")
print str(f)
c=f.fnbc()

print "Forma Normal de Boyce Codd= "
c=[str(x) for x in c]
c.sort()
for i in c:
    print i
print len(c)
