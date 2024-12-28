a,b=input().split()
x=''
for i in range(len(a)):
    x+=a[len(a)-1-i]
a=x
k=''

for p in range(len(b)):
    k+=b[len(b)-1-p] 
b=k

a=int(a)
b=int(b)

if a>b:
    print(a)
else:
    print(b)
