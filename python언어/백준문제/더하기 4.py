n=int(input())
a=0
k=0
p=list(range(int(n)))
for i in range(n):
    x=list(map(int, input().split()))
    while k<int(len(x)):
        a+=int(x[k])
        k+=1
    p[i]=a
    k=0
    a=0
k=0
while k<int(n):
    print(p[k])
    k+=1
