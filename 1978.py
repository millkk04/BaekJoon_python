x=int(input())

y=list(map(int,input().split()))

k=0

z=0 
for i in y:
    for p in range(i):
        if i%(p+1)==0:
            k+=1
    if i!=1 and k<3:
        z+=1
    k=0
        
print(z)
