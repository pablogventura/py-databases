from pyDB import *

a=DF(["A"],["B","C"])
b=DF(["E"], ["F","A"])


f=CDF([a,b], ["A","B","C","D","E","F"])



c=f.fnbc()

print "clausura= "
c=[str(x) for x in c]
c.sort()
for i in c:
    print i
print len(c)
