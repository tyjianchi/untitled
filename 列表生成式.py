import os

n=1
x={}
for d in os.listdir('.'):
   x[n]=d
   n=n+1
print(x[2])