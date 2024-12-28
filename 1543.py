stc=input()
cpn=input()
i=0
cnt=0
while True:
    if i==len(stc) or i+len(cpn)-1 > len(stc)-1:
        break
    else:
        if stc[i:i+len(cpn)]==cpn:
            cnt+=1
            i+=len(cpn)
        else:
            i+=1
    
print(cnt)
