N,K=map(int,input().split())
x=list(map(int,input().split(',')))
y=[]
for i in range(N):
    y.append(x[i])
for i in range(K):
    for j in range(N-1):
        y[j]=y[j+1]-x[j]
    y.pop()
    N-=1
    x.pop()
    for k in range(N):
        x[k]=y[k]
if len(y)==1:
    print(y[0])
else:
    for i in range(len(y)-1):
        print(y[i],end=',')
    print(y[i+1],end='')
    
    
