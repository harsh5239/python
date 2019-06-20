import numpy as np
x=int(input("input 1st dim   "))
y=int(input("input 2nd dim   "))
g=np.random.random((x,y))
g
f=open('file.txt','w')
f.write(str(g))
f.close()
