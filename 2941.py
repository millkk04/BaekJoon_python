eng=input()
cnt=0
i=0
while i<len(eng):
    if i < len(eng)-1 and (eng[i:i+2] in ['c=','c-','d-','lj','nj','s=','z=']):
        cnt+=1
        i+=2
    elif i< len(eng)-2 and eng[i:i+3]=='dz=':
        cnt+=1
        i+=3
    else:
        cnt+=1
        i+=1
print(cnt)
        
