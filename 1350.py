a=int(input())
b=list(map(int,input().split()))
c=int(input())
k=0

for i in range(a):
    if b[i]>c and b[i]%c==0:
        k+=(b[i]//c)*c
    elif b[i]>c and b[i]%c!=0:
        k+=((b[i]//c)+1)*c
    elif b[i]<c and b[i]!=0:
        k+=c
    elif b[i]==c:
        k+=c
    elif b[i]==0:
        pass
        
    
print(k)
    
            
            
    
