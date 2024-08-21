x=int(input())
l=[]
s=0
for i in range(x):
    h=0
    c=1
    k=int(input())
    l.append(k)
    if l[i]==0 and i==0:
        continue
    elif l[i]==0:
        for p in range(x):
            if i-c<0 or h==1:
                break
            else:
                if l[i-c]==0:
                    c+=1
                else:
                    l[i-c]=0
                    h=1
for i in range(x):
    s+=l[i]
print(s)
    
            
        
