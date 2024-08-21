x=input()
x=int(x)
i=0
b=list(range(x))
while i<x:
    a=input()
    b[i]=a[0]+(a[int(len(a))-1])
    i+=1
i=0
while i<x:
    print(b[i])
    i+=1

