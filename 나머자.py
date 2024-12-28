x=list(range(10))
for i in range(10):
    x[i]=input()

for k in range(10):
    x[k]=int(x[k])%42
a=set(x)
b=list(a)
print(len(b))
 
