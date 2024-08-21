x=int(input())

n=list(map(int,input().split()))

n.sort()

k=n[0]
a=[n[0]]
for i in range(1,x):
    if k==n[i]:
        pass
    else:
        a.append(n[i])
        k=n[i]
for p in a:
    print(p,end=' ')
    
