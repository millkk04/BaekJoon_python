pi=input()
m=input()
c=0
k=0
for i in range(len(pi)):
    if pi[i]!=m[0]:
        pass
    else:
        for j in range(len(m)):
            if pi[i+j]==m[j] and (i+j)<=len(pi)-1:
                c+=1
            else:
                break
        if c==len(m):
            k+=1
            c=0
print(k)

            
        
