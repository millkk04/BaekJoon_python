n=int(input())
hk=[]
for i in range(n):
    x,y=map(int,input().split())
    hk.append([x,y])
z=[]
for i in range(n):
    p,q=hk[i][0],hk[i][1]
    c=0
    for j in range(n):
        if p<hk[j][0] and q<hk[j][1]:
            c+=1
    z.append(c+1)
for t in z:
    print(t,end=' ')

        
