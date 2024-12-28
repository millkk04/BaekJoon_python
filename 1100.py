outlist=[]
cnt=0
for i in range(8):
    x=list(input())
    outlist.append(x)
for p in range(8):
    for q in range(8):
        if (p+q)%2==0:
            if outlist[p][q]=='F':
                cnt+=1
print(cnt)
